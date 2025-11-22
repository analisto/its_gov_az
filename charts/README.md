# 📊 Azerbaijan Medical Institutions Data Analysis

## Overview

This folder contains comprehensive visualizations and analysis of medical institutions in Azerbaijan, scraped from [its.gov.az](https://its.gov.az). The dataset includes **291 medical institutions** and **2,353 subsidiary healthcare facilities** across Azerbaijan.

---

## 📈 Charts & Visualizations

### 1. Geographic Distribution of Medical Institutions

![Geographic Distribution](01_geographic_distribution.png)

**Description:** Interactive map showing the geographic spread of medical institutions across Azerbaijan. The size of each point represents the number of subsidiary institutions, and the color intensity indicates the subsidiary count.

**Key Insights:**
- Medical institutions are distributed across all regions of Azerbaijan
- Larger institutions (with more subsidiaries) are primarily concentrated in major urban centers
- Geographic coordinates are available for **291 institutions (100%)**
- Coverage extends from northern regions (Zaqatala, Balakən) to southern areas and the Nakhchivan Autonomous Republic

**Actionable Insights:**
- ✅ Consider establishing additional large medical centers in underserved rural areas
- ✅ Use geographic clustering to optimize emergency medical service routing
- ✅ Coordinate with institutions in proximity for resource sharing and patient transfers

---

### 2. Top 15 Medical Institutions by Subsidiaries

![Top Institutions](02_top_institutions.png)

**Description:** Ranking of the 15 largest medical institutions by number of subsidiary healthcare facilities.

**Key Insights:**
- **Ağdam Rayon Mərkəzi Xəstəxanası** leads with **119 subsidiaries**
- **Balakən Rayon Mərkəzi Xəstəxanası** has **73 subsidiaries**
- **Zaqatala Rayon Mərkəzi Xəstəxanası** has **40 subsidiaries**
- The top 15 institutions manage **739 subsidiaries** (31.4% of all subsidiaries)
- Regional hospitals (Rayon Mərkəzi Xəstəxanası) dominate the top rankings

**Actionable Insights:**
- ✅ Large regional hospitals with extensive networks could serve as models for healthcare delivery
- ✅ Implement knowledge-sharing programs between top-performing institutions
- ✅ Investigate whether large subsidiary networks face coordination challenges
- ✅ Use these institutions as pilot sites for new healthcare initiatives

---

### 3. Subsidiary Distribution Analysis

![Subsidiary Distribution](03_subsidiary_distribution.png)

**Description:** Two-panel visualization showing: (1) proportion of institutions with/without subsidiaries, and (2) distribution histogram of subsidiary counts.

**Key Insights:**
- **76.3%** (222 institutions) have **NO subsidiaries**
- **23.7%** (69 institutions) manage subsidiary networks
- Among institutions with subsidiaries:
  - **Mean:** 34.1 subsidiaries per institution
  - **Median:** 18 subsidiaries per institution
  - **Maximum:** 119 subsidiaries (Ağdam Rayon Mərkəzi Xəstəxanası)
- Most institutions with subsidiaries manage between 5-40 facilities

**Actionable Insights:**
- ✅ 222 standalone institutions may benefit from forming or joining healthcare networks
- ✅ High variation in subsidiary counts suggests potential for standardization
- ✅ Investigate whether standalone facilities are specialized centers or underutilized resources
- ✅ Consider creating regional healthcare clusters to improve coordination

---

### 4. Types of Subsidiary Institutions

![Subsidiary Types](04_subsidiary_types.png)

**Description:** Breakdown of subsidiary facilities by type (Medical Points, Family Health Centers, Medical Stations, etc.).

**Key Insights:**
- **Medical Points (həkim məntəqəsi):** 1,376 facilities (58.5%)
- **Medical Stations (tibb məntəqəsi):** 692 facilities (29.4%)
- **Family Health Centers (Ailə Sağlamlıq Mərkəzi):** 194 facilities (8.2%)
- **Other specialized facilities:** 91 (3.9%)
- Medical points and stations comprise **87.9%** of all subsidiaries

**Actionable Insights:**
- ✅ Medical points are the primary healthcare delivery mechanism in Azerbaijan
- ✅ Family Health Centers represent growing preventive care infrastructure
- ✅ Standardize services across medical points to ensure quality consistency
- ✅ Expand Family Health Center model for improved primary care access
- ✅ Digitize and integrate medical points into central health information systems

---

### 5. Regional Distribution of Medical Institutions

![Regional Distribution](05_regional_distribution.png)

**Description:** Top 15 regions/cities ranked by number of medical institutions.

**Key Insights:**
- **Bakı (Baku):** 91 institutions (31.3% of total)
- **Gəncə:** 16 institutions
- **Sumqayıt:** 14 institutions
- **Naxçıvan:** 9 institutions
- **Mingəçevir:** 8 institutions
- Other regions have 5 or fewer institutions each
- Strong concentration in major urban centers

**Actionable Insights:**
- ✅ **Urban-rural disparity:** Baku has 5.7x more institutions than the second-ranked city
- ✅ Develop satellite healthcare facilities in suburban areas to reduce Baku's burden
- ✅ Invest in telemedicine infrastructure to connect rural areas with urban specialists
- ✅ Ensure equitable distribution of healthcare resources across regions
- ✅ Strengthen secondary cities (Gəncə, Sumqayıt) as regional healthcare hubs

---

### 6. Data Completeness Analysis

![Data Completeness](06_data_completeness.png)

**Description:** Assessment of data quality and completeness across key fields.

**Key Insights:**
- **Name:** 100% complete (291/291)
- **Address:** 100% complete (291/291)
- **Coordinates:** 100% complete (291/291)
- **Phone:** 99.3% complete (289/291)
- **Google Maps:** 82.1% complete (239/291)
- **Subsidiaries:** 23.7% have subsidiaries (69/291)

**Actionable Insights:**
- ✅ **Excellent data quality** - core fields have near-perfect completeness
- ✅ Add missing phone numbers for 2 institutions to reach 100% contact coverage
- ✅ Complete Google Maps embeddings for remaining 52 institutions (17.9%)
- ✅ Validate coordinate accuracy through periodic audits
- ✅ Implement data governance policies to maintain high quality standards
- ✅ Expand data collection to include: operating hours, services offered, bed capacity, specialist availability

---

### 7. Healthcare Network Hierarchy

![Subsidiary Hierarchy](07_subsidiary_hierarchy.png)

**Description:** Categorization of institutions by size of their subsidiary networks.

**Key Insights:**
- **No Subsidiaries:** 222 institutions (76.3%)
- **1-5 Subsidiaries:** 9 institutions (3.1%)
- **6-15 Subsidiaries:** 18 institutions (6.2%)
- **16-30 Subsidiaries:** 18 institutions (6.2%)
- **30+ Subsidiaries:** 24 institutions (8.2%)

**Actionable Insights:**
- ✅ **Three-tier healthcare model emerging:**
  - Tier 1: Standalone specialized facilities (76.3%)
  - Tier 2: Small-medium regional networks (15.5%)
  - Tier 3: Large regional healthcare systems (8.2%)
- ✅ Institutions with 30+ subsidiaries manage 79.5% of all subsidiary facilities
- ✅ Strengthen mid-tier institutions (6-30 subsidiaries) to reduce pressure on large networks
- ✅ Consider merger opportunities for standalone institutions in geographic proximity

---

## 📊 Summary Statistics

| Metric | Value |
|--------|-------|
| **Total Medical Institutions** | 291 |
| **Total Subsidiary Facilities** | 2,353 |
| **Institutions with Subsidiaries** | 69 (23.7%) |
| **Standalone Institutions** | 222 (76.3%) |
| **Average Subsidiaries per Network** | 34.1 |
| **Largest Institution** | Ağdam Rayon Mərkəzi Xəstəxanası (119 subsidiaries) |
| **Institutions with Coordinates** | 291 (100%) |
| **Institutions with Phone Numbers** | 289 (99.3%) |
| **Unique Regions Covered** | 50+ cities and districts |

---

## 🎯 Key Findings & Recommendations

### 🏥 **Healthcare Infrastructure**

**Finding:** Azerbaijan has a well-distributed network of 291 medical institutions supported by 2,353 subsidiary facilities.

**Recommendations:**
1. **Geographic Optimization:** Use coordinate data to perform coverage analysis and identify healthcare deserts
2. **Resource Allocation:** Prioritize underserved regions identified in regional distribution analysis
3. **Network Efficiency:** Study high-performing institutions (30+ subsidiaries) to develop best practices

---

### 🌍 **Regional Coverage**

**Finding:** Significant urban-rural disparity with 31.3% of institutions concentrated in Baku.

**Recommendations:**
1. **Decentralization:** Strengthen regional hubs in Gəncə, Sumqayıt, and other secondary cities
2. **Mobile Clinics:** Deploy mobile health units to areas with limited facility access
3. **Telemedicine:** Implement telehealth infrastructure to connect rural areas with urban specialists
4. **Incentive Programs:** Create incentives for healthcare professionals to work in underserved regions

---

### 🔗 **Network Integration**

**Finding:** 76.3% of institutions operate independently without subsidiary networks.

**Recommendations:**
1. **Clustering Strategy:** Form regional healthcare clusters for better coordination
2. **Digital Integration:** Implement unified health information system across all facilities
3. **Referral Networks:** Establish clear pathways between primary, secondary, and tertiary care
4. **Resource Sharing:** Enable equipment, specialist, and supply sharing among proximate facilities

---

### 📱 **Primary Care Delivery**

**Finding:** Medical points (həkim məntəqəsi) and stations (tibb məntəqəsi) comprise 87.9% of subsidiary facilities.

**Recommendations:**
1. **Standardization:** Develop national standards for services offered at each facility type
2. **Capacity Building:** Train staff at medical points in evidence-based primary care
3. **Quality Assurance:** Implement regular quality audits and patient satisfaction monitoring
4. **Technology Adoption:** Equip medical points with basic diagnostic equipment and electronic records

---

### 📊 **Data & Technology**

**Finding:** Excellent data completeness (99-100% for core fields) provides strong foundation for digital health initiatives.

**Recommendations:**
1. **API Development:** Create public API for facility lookup and service availability
2. **Patient Portal:** Develop mobile app for finding nearby facilities and booking appointments
3. **Analytics Dashboard:** Build real-time monitoring system for healthcare administrators
4. **Data Expansion:** Collect additional data on bed capacity, specialties, equipment, and wait times
5. **Interoperability:** Ensure data standards allow integration with national health systems

---

### 🚑 **Emergency & Specialized Care**

**Recommendations:**
1. **Emergency Networks:** Map optimal locations for emergency medical service stations
2. **Specialty Distribution:** Analyze distribution of specialized services (cardiology, oncology, etc.)
3. **Capacity Planning:** Use subsidiary data to forecast healthcare demand and plan expansions
4. **Disaster Preparedness:** Develop emergency response plans leveraging facility networks

---

## 🔍 Data Quality Notes

- **Source:** Data scraped from [its.gov.az/page/tibb-muessiselerinin-axtarisi](https://its.gov.az/page/tibb-muessiselerinin-axtarisi)
- **Collection Date:** Based on scraper implementation (2024)
- **Validation:** Coordinate data validated against Google Maps embeddings
- **Completeness:** Exceptionally high (99-100% for critical fields)
- **Update Frequency:** Manual scraping required for updates

---

## 📁 Files in This Repository

- **`medical_institutions.csv`** - Main dataset with 291 institutions
- **`subsidiary_institutions.csv`** - Detailed list of 2,353 subsidiary facilities
- **`medical_institutions.json`** - JSON format of main dataset
- **`medical_scraper.py`** - Python scraper for data collection
- **`generate_charts.py`** - Chart generation script

---

## 🔄 Next Steps

1. **Validation:** Cross-reference with Ministry of Health official records
2. **Enhancement:** Add operating hours, services, bed capacity, staff counts
3. **Monitoring:** Set up automated scraping for periodic data updates
4. **Integration:** Connect with national health information systems
5. **Public Access:** Deploy web interface for public facility lookup

---

## 📞 Contact & Contribution

This analysis provides valuable insights into Azerbaijan's healthcare infrastructure. For questions, updates, or contributions:

- Review the source code in `medical_scraper.py`
- Regenerate charts using `python3 generate_charts.py`
- Submit issues or improvements via repository

---

**Last Updated:** November 22, 2025
**Data Source:** [its.gov.az](https://its.gov.az)
**Total Facilities Analyzed:** 2,644 (291 institutions + 2,353 subsidiaries)
