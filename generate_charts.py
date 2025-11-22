#!/usr/bin/env python3
"""
Azerbaijan Medical Institutions Data Analysis and Visualization
Generates comprehensive charts for medical institutions data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from collections import Counter
import re
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking charts
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Configure matplotlib for better font handling
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

class MedicalDataAnalyzer:
    def __init__(self):
        self.institutions_df = None
        self.subsidiaries_df = None
        self.output_dir = 'charts'

    def load_data(self):
        """Load CSV data files"""
        print("Loading data files...")
        try:
            self.institutions_df = pd.read_csv('medical_institutions.csv')
            self.subsidiaries_df = pd.read_csv('subsidiary_institutions.csv')
            print(f"✓ Loaded {len(self.institutions_df)} medical institutions")
            print(f"✓ Loaded {len(self.subsidiaries_df)} subsidiary institutions")
        except Exception as e:
            print(f"Error loading data: {e}")
            raise

    def extract_location_info(self, address):
        """Extract city/region from address"""
        if pd.isna(address) or not address:
            return 'Unknown'

        # Common patterns in Azerbaijani addresses
        patterns = [
            r'(Bakı|Baki)',
            r'(Sumqayıt)',
            r'(Gəncə|Gence)',
            r'(Mingəçevir)',
            r'(Naxçıvan)',
            r'(\w+)\s+(şəhəri|şəhəri,)',
            r'(\w+)\s+(rayonu|rayon)',
            r'(\w+)\s+(qəsəbəsi|qəsəbəsi,)',
        ]

        for pattern in patterns:
            match = re.search(pattern, address, re.IGNORECASE)
            if match:
                location = match.group(1)
                # Clean up common variations
                if location.lower() in ['baki', 'bakı']:
                    return 'Bakı'
                return location.capitalize()

        return 'Other'

    def analyze_subsidiary_types(self):
        """Analyze types of subsidiary institutions"""
        type_keywords = {
            'Ailə Sağlamlıq Mərkəzi': 'Family Health Center',
            'həkim məntəqəsi': 'Medical Point',
            'tibb məntəqəsi': 'Medical Station',
            'Xəstəxana': 'Hospital',
            'poliklinika': 'Polyclinic',
            'Mərkəz': 'Center'
        }

        type_counts = {v: 0 for v in type_keywords.values()}
        type_counts['Other'] = 0

        for subsidiary_name in self.subsidiaries_df['subsidiary_name']:
            found = False
            for keyword, eng_name in type_keywords.items():
                if keyword in str(subsidiary_name):
                    type_counts[eng_name] += 1
                    found = True
                    break
            if not found:
                type_counts['Other'] += 1

        return type_counts

    def chart_1_geographic_distribution(self):
        """Chart 1: Geographic distribution map of medical institutions"""
        print("Generating Chart 1: Geographic Distribution...")

        # Filter institutions with valid coordinates
        valid_coords = self.institutions_df.dropna(subset=['latitude', 'longitude'])

        fig, ax = plt.subplots(figsize=(14, 10))

        # Create scatter plot with size based on subsidiary count
        sizes = valid_coords['subsidiary_count'].fillna(0) * 10 + 50

        scatter = ax.scatter(
            valid_coords['longitude'],
            valid_coords['latitude'],
            s=sizes,
            alpha=0.6,
            c=valid_coords['subsidiary_count'].fillna(0),
            cmap='YlOrRd',
            edgecolors='black',
            linewidth=0.5
        )

        # Add colorbar
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('Number of Subsidiaries', rotation=270, labelpad=20)

        ax.set_xlabel('Longitude', fontsize=12, fontweight='bold')
        ax.set_ylabel('Latitude', fontsize=12, fontweight='bold')
        ax.set_title('Geographic Distribution of Medical Institutions in Azerbaijan\n(Size represents number of subsidiaries)',
                     fontsize=14, fontweight='bold', pad=20)

        ax.grid(True, alpha=0.3)

        # Add statistics text box
        stats_text = f'Total Institutions: {len(valid_coords)}\nWith Subsidiaries: {len(valid_coords[valid_coords["subsidiary_count"] > 0])}'
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                verticalalignment='top', fontsize=10)

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/01_geographic_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Chart 1 saved")

    def chart_2_top_institutions(self):
        """Chart 2: Top 15 institutions by subsidiary count"""
        print("Generating Chart 2: Top Institutions by Subsidiaries...")

        # Get top 15 institutions
        top_institutions = self.institutions_df.nlargest(15, 'subsidiary_count')[['name', 'subsidiary_count']]

        fig, ax = plt.subplots(figsize=(14, 10))

        bars = ax.barh(range(len(top_institutions)), top_institutions['subsidiary_count'].values)

        # Color bars with gradient
        colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(bars)))
        for bar, color in zip(bars, colors):
            bar.set_color(color)

        # Customize labels
        ax.set_yticks(range(len(top_institutions)))
        ax.set_yticklabels([name[:50] + '...' if len(name) > 50 else name
                           for name in top_institutions['name'].values], fontsize=10)

        ax.set_xlabel('Number of Subsidiary Institutions', fontsize=12, fontweight='bold')
        ax.set_title('Top 15 Medical Institutions by Number of Subsidiaries',
                     fontsize=14, fontweight='bold', pad=20)

        # Add value labels on bars
        for i, (idx, row) in enumerate(top_institutions.iterrows()):
            ax.text(row['subsidiary_count'] + 0.5, i, f"{int(row['subsidiary_count'])}",
                   va='center', fontsize=10, fontweight='bold')

        ax.grid(True, axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/02_top_institutions.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Chart 2 saved")

    def chart_3_subsidiary_distribution(self):
        """Chart 3: Distribution of institutions by subsidiary count"""
        print("Generating Chart 3: Subsidiary Count Distribution...")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        # Pie chart: With vs Without subsidiaries
        has_subsidiaries = len(self.institutions_df[self.institutions_df['subsidiary_count'] > 0])
        no_subsidiaries = len(self.institutions_df[self.institutions_df['subsidiary_count'] == 0])

        sizes = [has_subsidiaries, no_subsidiaries]
        labels = [f'With Subsidiaries\n({has_subsidiaries})', f'Without Subsidiaries\n({no_subsidiaries})']
        colors = ['#ff9999', '#66b3ff']
        explode = (0.05, 0)

        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
                shadow=True, startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
        ax1.set_title('Institutions with vs without Subsidiaries', fontsize=14, fontweight='bold', pad=20)

        # Histogram: Distribution of subsidiary counts
        subsidiary_counts = self.institutions_df[self.institutions_df['subsidiary_count'] > 0]['subsidiary_count']

        ax2.hist(subsidiary_counts, bins=20, color='steelblue', edgecolor='black', alpha=0.7)
        ax2.set_xlabel('Number of Subsidiaries', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Number of Institutions', fontsize=12, fontweight='bold')
        ax2.set_title('Distribution of Subsidiary Counts\n(Institutions with Subsidiaries)',
                     fontsize=14, fontweight='bold', pad=20)
        ax2.grid(True, alpha=0.3)

        # Add statistics
        stats_text = f'Mean: {subsidiary_counts.mean():.1f}\nMedian: {subsidiary_counts.median():.0f}\nMax: {subsidiary_counts.max():.0f}'
        ax2.text(0.75, 0.95, stats_text, transform=ax2.transAxes,
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
                verticalalignment='top', fontsize=10)

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/03_subsidiary_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Chart 3 saved")

    def chart_4_subsidiary_types(self):
        """Chart 4: Types of subsidiary institutions"""
        print("Generating Chart 4: Subsidiary Types Analysis...")

        type_counts = self.analyze_subsidiary_types()

        # Remove 'Other' if it's 0
        type_counts = {k: v for k, v in type_counts.items() if v > 0}

        # Sort by count
        sorted_types = dict(sorted(type_counts.items(), key=lambda x: x[1], reverse=True))

        fig, ax = plt.subplots(figsize=(14, 8))

        bars = ax.bar(range(len(sorted_types)), list(sorted_types.values()))

        # Color bars with gradient
        colors = plt.cm.Set3(np.linspace(0, 1, len(bars)))
        for bar, color in zip(bars, colors):
            bar.set_color(color)

        ax.set_xticks(range(len(sorted_types)))
        ax.set_xticklabels(list(sorted_types.keys()), rotation=45, ha='right', fontsize=11)

        ax.set_ylabel('Number of Institutions', fontsize=12, fontweight='bold')
        ax.set_title('Distribution of Subsidiary Institution Types', fontsize=14, fontweight='bold', pad=20)

        # Add value labels on bars
        for i, (type_name, count) in enumerate(sorted_types.items()):
            ax.text(i, count + 20, f'{count}', ha='center', va='bottom',
                   fontsize=11, fontweight='bold')

        ax.grid(True, axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/04_subsidiary_types.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Chart 4 saved")

    def chart_5_regional_distribution(self):
        """Chart 5: Regional distribution of institutions"""
        print("Generating Chart 5: Regional Distribution...")

        # Extract regions from addresses
        self.institutions_df['region'] = self.institutions_df['address'].apply(self.extract_location_info)

        region_counts = self.institutions_df['region'].value_counts().head(15)

        fig, ax = plt.subplots(figsize=(14, 9))

        bars = ax.barh(range(len(region_counts)), region_counts.values)

        # Color bars with gradient
        colors = plt.cm.Spectral(np.linspace(0.2, 0.8, len(bars)))
        for bar, color in zip(bars, colors):
            bar.set_color(color)

        ax.set_yticks(range(len(region_counts)))
        ax.set_yticklabels(region_counts.index, fontsize=11)

        ax.set_xlabel('Number of Medical Institutions', fontsize=12, fontweight='bold')
        ax.set_title('Top 15 Regions by Number of Medical Institutions', fontsize=14, fontweight='bold', pad=20)

        # Add value labels
        for i, count in enumerate(region_counts.values):
            ax.text(count + 0.5, i, f'{count}', va='center', fontsize=11, fontweight='bold')

        ax.grid(True, axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/05_regional_distribution.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Chart 5 saved")

    def chart_6_data_completeness(self):
        """Chart 6: Data completeness analysis"""
        print("Generating Chart 6: Data Completeness...")

        # Calculate completeness for key fields
        total = len(self.institutions_df)

        completeness = {
            'Name': len(self.institutions_df.dropna(subset=['name'])),
            'Address': len(self.institutions_df.dropna(subset=['address'])),
            'Phone': len(self.institutions_df.dropna(subset=['phone'])),
            'Coordinates': len(self.institutions_df.dropna(subset=['latitude', 'longitude'])),
            'Google Maps': len(self.institutions_df.dropna(subset=['google_maps_embed'])),
            'Subsidiaries': len(self.institutions_df[self.institutions_df['subsidiary_count'] > 0])
        }

        # Convert to percentages
        completeness_pct = {k: (v/total)*100 for k, v in completeness.items()}

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

        # Bar chart - percentage
        bars = ax1.bar(range(len(completeness_pct)), list(completeness_pct.values()))
        colors = ['#2ecc71' if v > 80 else '#f39c12' if v > 50 else '#e74c3c'
                 for v in completeness_pct.values()]
        for bar, color in zip(bars, colors):
            bar.set_color(color)

        ax1.set_xticks(range(len(completeness_pct)))
        ax1.set_xticklabels(list(completeness_pct.keys()), rotation=45, ha='right', fontsize=11)
        ax1.set_ylabel('Completeness (%)', fontsize=12, fontweight='bold')
        ax1.set_title('Data Completeness by Field', fontsize=14, fontweight='bold', pad=20)
        ax1.set_ylim(0, 105)

        # Add percentage labels
        for i, (field, pct) in enumerate(completeness_pct.items()):
            ax1.text(i, pct + 2, f'{pct:.1f}%', ha='center', va='bottom',
                    fontsize=10, fontweight='bold')

        ax1.grid(True, axis='y', alpha=0.3)
        ax1.axhline(y=100, color='green', linestyle='--', alpha=0.5, label='100% Complete')
        ax1.legend()

        # Stacked bar - absolute numbers
        complete = list(completeness.values())
        incomplete = [total - v for v in complete]

        x = np.arange(len(completeness))
        width = 0.6

        ax2.bar(x, complete, width, label='Complete', color='#3498db')
        ax2.bar(x, incomplete, width, bottom=complete, label='Incomplete', color='#ecf0f1')

        ax2.set_xticks(x)
        ax2.set_xticklabels(list(completeness.keys()), rotation=45, ha='right', fontsize=11)
        ax2.set_ylabel('Number of Records', fontsize=12, fontweight='bold')
        ax2.set_title('Data Completeness (Absolute Numbers)', fontsize=14, fontweight='bold', pad=20)
        ax2.legend()
        ax2.grid(True, axis='y', alpha=0.3)

        # Add total line
        ax2.axhline(y=total, color='red', linestyle='--', alpha=0.5, label=f'Total: {total}')

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/06_data_completeness.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Chart 6 saved")

    def chart_7_subsidiary_hierarchy(self):
        """Chart 7: Institutions categorized by subsidiary count ranges"""
        print("Generating Chart 7: Subsidiary Hierarchy...")

        # Categorize institutions
        def categorize_subsidiaries(count):
            if count == 0:
                return 'No Subsidiaries'
            elif count <= 5:
                return '1-5 Subsidiaries'
            elif count <= 15:
                return '6-15 Subsidiaries'
            elif count <= 30:
                return '16-30 Subsidiaries'
            else:
                return '30+ Subsidiaries'

        self.institutions_df['subsidiary_category'] = self.institutions_df['subsidiary_count'].apply(categorize_subsidiaries)

        category_counts = self.institutions_df['subsidiary_category'].value_counts()

        # Define order
        category_order = ['No Subsidiaries', '1-5 Subsidiaries', '6-15 Subsidiaries',
                         '16-30 Subsidiaries', '30+ Subsidiaries']
        category_counts = category_counts.reindex(category_order, fill_value=0)

        fig, ax = plt.subplots(figsize=(12, 8))

        # Create pie chart
        colors = ['#e74c3c', '#f39c12', '#f1c40f', '#2ecc71', '#27ae60']
        explode = [0.05 if i == 0 else 0 for i in range(len(category_counts))]

        wedges, texts, autotexts = ax.pie(category_counts.values, labels=category_counts.index,
                                           autopct='%1.1f%%', colors=colors, explode=explode,
                                           shadow=True, startangle=90,
                                           textprops={'fontsize': 11, 'fontweight': 'bold'})

        # Add count to labels
        for i, (label, count) in enumerate(zip(category_counts.index, category_counts.values)):
            texts[i].set_text(f'{label}\n({count} institutions)')

        ax.set_title('Healthcare Network Hierarchy\nInstitutions by Subsidiary Count Range',
                    fontsize=14, fontweight='bold', pad=20)

        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/07_subsidiary_hierarchy.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Chart 7 saved")

    def generate_summary_statistics(self):
        """Generate summary statistics for README"""
        stats = {
            'total_institutions': len(self.institutions_df),
            'total_subsidiaries': len(self.subsidiaries_df),
            'institutions_with_subsidiaries': len(self.institutions_df[self.institutions_df['subsidiary_count'] > 0]),
            'institutions_with_coordinates': len(self.institutions_df.dropna(subset=['latitude', 'longitude'])),
            'institutions_with_phone': len(self.institutions_df.dropna(subset=['phone'])),
            'avg_subsidiaries': self.institutions_df[self.institutions_df['subsidiary_count'] > 0]['subsidiary_count'].mean(),
            'max_subsidiaries': self.institutions_df['subsidiary_count'].max(),
            'top_institution': self.institutions_df.nlargest(1, 'subsidiary_count')['name'].values[0],
            'regions_count': self.institutions_df['region'].nunique() if 'region' in self.institutions_df.columns else 0
        }
        return stats

    def generate_all_charts(self):
        """Generate all charts"""
        print("\n" + "="*60)
        print("Azerbaijan Medical Institutions - Data Visualization")
        print("="*60 + "\n")

        self.load_data()

        self.chart_1_geographic_distribution()
        self.chart_2_top_institutions()
        self.chart_3_subsidiary_distribution()
        self.chart_4_subsidiary_types()
        self.chart_5_regional_distribution()
        self.chart_6_data_completeness()
        self.chart_7_subsidiary_hierarchy()

        print("\n" + "="*60)
        print("✓ All charts generated successfully!")
        print(f"✓ Charts saved to: {self.output_dir}/")
        print("="*60)

        return self.generate_summary_statistics()

if __name__ == "__main__":
    analyzer = MedicalDataAnalyzer()
    stats = analyzer.generate_all_charts()

    print("\n📊 Summary Statistics:")
    print(f"  Total Institutions: {stats['total_institutions']}")
    print(f"  Total Subsidiaries: {stats['total_subsidiaries']}")
    print(f"  Institutions with Subsidiaries: {stats['institutions_with_subsidiaries']}")
    print(f"  Average Subsidiaries: {stats['avg_subsidiaries']:.1f}")
    print(f"  Top Institution: {stats['top_institution']}")
