# Advanced Threat Incident Analytics and Security Visualization Framework

## Overview

The **Advanced Threat Incident Analytics and Security Visualization Framework** is an end-to-end cybersecurity analytics project designed to transform incident-level cybersecurity data into structured, visual, and actionable security intelligence.

The project is developed across four milestones, progressing from **data preparation and data warehouse design** to **threat intelligence, temporal analytics, operational security analysis, risk assessment, predictive analytics, anomaly detection, and executive decision support**.

The complete solution is implemented primarily using **Python, Pandas, Power BI, DAX, and Star Schema dimensional modeling**.

---

## Project Objectives

The main objectives of the project are to:

- Prepare and clean cybersecurity incident data.
- Engineer analytical features for cybersecurity assessment.
- Develop a unified **Threat Severity Index (TSI)**.
- Design a dimensional **Star Schema** for analytical reporting.
- Analyze cybersecurity threats by attack type and severity.
- Identify temporal trends and unusual incident patterns.
- Analyze cybersecurity incident impact.
- Evaluate operational response performance.
- Analyze geographic cybersecurity hotspots.
- Classify incidents based on security risk.
- Apply forecasting and anomaly detection.
- Monitor response performance and SLA compliance.
- Develop executive-level cybersecurity dashboards.
- Generate analytical alerts and management recommendations.

---

# Project Workflow

```text
Raw Cybersecurity Incident Dataset
                │
                ▼
┌─────────────────────────────────────────┐
│ MILESTONE 1                            │
│ Data Preparation & Data Warehouse      │
│ Design                                 │
│                                         │
│ Python + Pandas + Star Schema          │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ MILESTONE 2                            │
│ Threat Intelligence & Temporal         │
│ Analytics                              │
│                                         │
│ Threat + Severity + Trends + Anomalies│
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ MILESTONE 3                            │
│ Operational Security Analytics         │
│                                         │
│ Geography + Response + Operations      │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ MILESTONE 4                            │
│ Risk Intelligence & Executive         │
│ Analytics                              │
│                                         │
│ Risk + Forecasting + SLA + Alerts      │
└──────────────────┬──────────────────────┘
                   │
                   ▼
        ACTIONABLE SECURITY
            INTELLIGENCE
```

---

# Milestone 1 — Data Preparation & Data Warehouse Design

## Objective

Milestone 1 establishes the data and modeling foundation for the cybersecurity analytics framework.

The raw cybersecurity incident dataset is processed using Python and Pandas and subsequently organized into a dimensional Star Schema for Power BI analytics.

## Data Preparation

The implemented preprocessing workflow includes:

- Dataset loading
- Basic data inspection
- Duplicate removal
- Missing-value handling
- Timestamp conversion
- Data type verification
- Feature normalization
- TSI calculation
- TSI rounding
- Clean dataset export

## Feature Engineering

The following analytical features are generated:

- `Severity_Norm`
- `Loss_Norm`
- `Data_Norm`
- `Users_Norm`
- `Response_Norm`
- `TSI_Score`

## Threat Severity Index

The project-defined TSI model combines five normalized components:

```text
TSI_Score =
    0.35 × Severity_Norm
  + 0.25 × Loss_Norm
  + 0.20 × Data_Norm
  + 0.10 × Users_Norm
  + 0.10 × Response_Norm
```

The TSI provides a unified analytical measure of incident severity and impact.

## Data Warehouse

A Star Schema is designed with:

- `fact_incident`
- `dim_time`
- `dim_location`
- `dim_threat`
- `dim_operational`

The fact table contains incident-level measures, while the dimension tables provide descriptive context for analytical filtering and aggregation.

## Milestone 1 Outcome

Milestone 1 produces a cleaned, analysis-ready cybersecurity dataset and a dimensional data warehouse foundation for Power BI reporting.

[View Milestone 1](./milestone-1/)

---

# Milestone 2 — Threat Intelligence & Temporal Analytics

## Objective

Milestone 2 focuses on understanding the cybersecurity threat landscape through threat classification, severity analysis, temporal analysis, anomaly detection, and incident impact analysis.

## Threat Intelligence Overview

The analysis provides:

- Total incident count
- Average Threat Severity Index
- Incidents by attack type
- Threat severity distribution

## Threat Classification & Severity

The analysis includes:

- Average TSI by attack type
- Threat severity by attack type
- Average TSI by threat severity

These visualizations provide insight into the distribution and severity of different cybersecurity attack categories.

## Temporal Threat Analysis

Temporal analysis includes:

- Monthly incident trends
- Monthly average TSI trends

This allows changes in incident volume and threat severity to be examined over time.

## Anomaly Detection

Power BI anomaly detection is applied to daily incident volume.

The analysis identifies unusual patterns in incident activity using expected ranges and anomaly detection.

An identified anomaly represents an unusual incident-volume pattern and does not by itself indicate a confirmed cyberattack.

## Threat Impact Analysis

Incident impact is analyzed using:

- Financial loss
- Data compromised
- Affected users
- Average attack duration

## Environmental Correlation

The broader milestone requirements include environmental correlation analysis.

The current implementation uses the cybersecurity incident dataset only. Since the available dataset does not contain environmental or weather variables, environmental correlation is not artificially introduced.

## Milestone 2 Outcome

Milestone 2 provides threat intelligence across attack classification, threat severity, temporal patterns, anomalies, and incident impact.

[View Milestone 2](./milestone-2/)

---

# Milestone 3 — Operational Security Analytics

## Objective

Milestone 3 focuses on operational cybersecurity analysis, including geographic hotspots, response performance, temporal incident activity, security-tool utilization, and city-level threat severity.

## Executive KPIs

The dashboard provides:

- Average Response Time
- Total Affected Users
- Total Incidents
- Total Financial Loss

## Geographic Hotspot Analysis

An interactive geographic visualization is used to examine the distribution of cybersecurity incidents and associated risk levels across locations.

## Response Performance

The dashboard analyzes response performance through:

- Top 10 Cities by Response Time
- Response Performance by State

These visualizations provide a comparative view of incident response across geographic areas.

## Temporal Analysis

Incident activity is analyzed across year and quarter to identify changes in cybersecurity incident volume over time.

## Security Tool Utilization

Security-tool utilization is analyzed to show the distribution of incidents associated with different security tools.

## Cyber-Risk Analysis

The dashboard includes:

- Top 10 Cities by Cyber Risk

Cyber risk is represented using average TSI at the city level.

## Interactive Filters

The dashboard provides filters for:

- Year
- Risk Level
- State

These filters allow users to explore the operational analysis dynamically.

## Milestone 3 Outcome

Milestone 3 provides an operational view of cybersecurity incidents by combining geographic analysis, response performance, temporal activity, security-tool utilization, and city-level cyber risk.

[View Milestone 3](./milestone-3/)

---

# Milestone 4 — Risk Intelligence & Executive Analytics

## Objective

Milestone 4 converts the analytical results into an executive-level cybersecurity intelligence framework.

The milestone covers:

- Security risk assessment
- Risk intelligence
- Predictive analytics
- Anomaly detection
- Executive KPIs
- SLA monitoring
- Security alerts
- Management recommendations

---

## Security Risk Assessment

The project extends the incident risk classification into four analytical levels using project-defined TSI thresholds:

| TSI Score | Risk Level |
|---|---|
| `< 0.40` | Low |
| `0.40 – 0.649` | Medium |
| `0.65 – 0.849` | High |
| `≥ 0.85` | Critical |

This four-level classification provides a more granular view of cybersecurity risk.

---

## Risk Intelligence Analysis

Risk is analyzed across:

- State
- Attack type
- Financial loss
- Risk level

The analysis provides a structured view of where higher-risk incidents and financial exposure occur.

## Executive Command Center

The executive dashboard provides key indicators including:

- Total Incidents
- Average TSI
- High/Critical Risks
- Total Financial Loss
- Average Response Time
- SLA Compliance

Current project results include approximately:

| KPI | Result |
|---|---:|
| Total Incidents | 10K |
| Average TSI | 0.52 |
| High/Critical Risks | ~2K |
| Total Financial Loss | ~₹50B |
| Average Response Time | 153.33 minutes |
| SLA Compliance | 88.29% |

---

## Risk-Based SLA Monitoring

Risk-based response targets are defined as:

| Risk Level | SLA Target |
|---|---:|
| Critical | ≤ 180 min |
| High | ≤ 240 min |
| Medium | ≤ 270 min |
| Low | ≤ 300 min |

The current overall SLA compliance is approximately **88.29%** under this project-defined SLA framework.

---

## Predictive Threat Analytics

Power BI forecasting is applied to monthly incident counts.

### Forecast Configuration

- Forecast horizon: Next 3 months
- Confidence interval: 95%
- Seasonality: Auto
- Input: Monthly incident count

The forecast provides an analytical view of expected incident workload for the upcoming period.

---

## Anomaly Detection & Threat Trend

Daily incident volume is analyzed using Power BI anomaly detection.

The project also monitors monthly average TSI to identify changes in overall threat severity.

The observed monthly average TSI remains approximately within the **0.50–0.53** range during the analyzed period, with periodic fluctuations.

---

## Security Alerts

Three analytical alert conditions are implemented.

### Risk Exposure Alert

Identifies elevated exposure when the proportion of High and Critical incidents exceeds the project-defined threshold.

### SLA Breach Alert

Identifies a potential response-performance issue when SLA compliance falls below the project-defined 90% threshold.

### Critical Response Alert

Identifies a potential critical-response issue when average Critical-risk response time exceeds the project-defined 180-minute target.

---

## Management Recommendations

The analytical framework supports the following management actions:

1. **Prioritize High/Critical Incidents**
   - Focus security investigation and response resources on higher-risk incidents.

2. **Improve Response Performance**
   - Review incident-response workflows, escalation processes, and resource allocation.

3. **Strengthen Critical Incident Escalation**
   - Prioritize Critical incidents and dedicated response resources to reduce response delays.

## Milestone 4 Outcome

Milestone 4 integrates risk classification, executive KPIs, predictive analytics, anomaly detection, SLA monitoring, analytical alerts, and management recommendations into an executive cybersecurity intelligence framework.

[View Milestone 4](./milestone-4/)

---

# Overall Project Architecture

```text
                  CYBERSECURITY INCIDENT DATA
                              │
                              ▼
                 ┌────────────────────────┐
                 │   DATA PREPARATION     │
                 │    Python + Pandas     │
                 └────────────┬───────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │ FEATURE ENGINEERING    │
                 │ Normalized Features    │
                 │ + TSI Score            │
                 └────────────┬───────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │      STAR SCHEMA       │
                 │ Fact + Dimensions      │
                 └────────────┬───────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │     POWER BI MODEL     │
                 │       + DAX            │
                 └────────────┬───────────┘
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
      THREAT INTEL.     OPERATIONAL       RISK INTEL.
      & TEMPORAL       SECURITY ANALYSIS   & EXECUTIVE
        ANALYTICS                          ANALYTICS
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │ PREDICTIVE ANALYTICS   │
                 │ Forecast + Anomalies   │
                 └────────────┬───────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │ EXECUTIVE DECISION     │
                 │ SUPPORT                │
                 └────────────────────────┘
```

---

# Key Analytical Components

| Component | Technology / Method |
|---|---|
| Data Preparation | Python, Pandas |
| Data Quality | Duplicate removal, missing-value handling |
| Feature Engineering | Normalization |
| Threat Severity | Weighted TSI |
| Data Warehouse | Star Schema |
| Data Modeling | Power BI |
| Analytical Calculations | DAX |
| Visualization | Power BI |
| Temporal Analysis | Daily, monthly, quarterly and yearly analysis |
| Anomaly Detection | Power BI Anomaly Detection |
| Forecasting | Power BI Forecast |
| Risk Classification | TSI-based project-defined thresholds |
| SLA Monitoring | Risk-based SLA framework |
| Decision Support | Analytical alerts and recommendations |

---

# Tools & Technologies

- **Python**
- **Pandas**
- **Power BI**
- **DAX**
- **CSV**
- **Star Schema**
- **Power BI Forecasting**
- **Power BI Anomaly Detection**

---

# Repository Structure

```text

Cyber_threat_analytics/
│
├── Risk_Intelligence_Executive_Analy...   ← Power BI .pbix file
│
├── milestone-1/
│   ├── Scripts/
│   │   ├── India_Cybersecurity_Incident_...
│   │   ├── clean_data.csv
│   │   └── data_processing.py
│   └── Readme.md
│
├── milestone-2/
│   ├── screenshots/
│   └── README.md
│
├── milestone-3/
│   ├── screenshots/
│   └── Readme.md
│
└── milestone-4/
    ├── screenshots/
    └── README.md

---

# Power BI Report

The complete Power BI report is provided as a `.pbix` file for interactive evaluation.

**Power BI Report:**

[M4 Risk Intelligence & Executive Analytics](./M4_Risk_Intelligence_Executive_Analytics.pbix)

The report contains the Power BI analysis developed across the project milestones.

---

# Project Outcomes

The completed project provides an end-to-end cybersecurity analytics framework covering the following stages:

### 1. Data Foundation

The raw cybersecurity incident data is cleaned, transformed, enriched with analytical features, and structured using a Star Schema.

### 2. Threat Intelligence

Cybersecurity incidents are analyzed by attack type, threat severity, TSI, temporal trends, anomalies, and impact.

### 3. Operational Intelligence

Geographic hotspots, response performance, temporal activity, security-tool utilization, and city-level cyber risk are analyzed.

### 4. Risk Intelligence

Incidents are classified into Low, Medium, High, and Critical analytical risk levels using project-defined TSI thresholds.

### 5. Predictive Analytics

Forecasting and anomaly detection are applied to provide additional analytical insight into incident activity.

### 6. Executive Decision Support

Executive KPIs, SLA monitoring, analytical alerts, and management recommendations provide a consolidated security intelligence view.

---

# Milestone Completion

| Milestone | Title | Status |
|---|---|---|
| **M1** | Data Preparation & Data Warehouse Design | ✅ Complete |
| **M2** | Threat Intelligence & Temporal Analytics | ✅ Complete |
| **M3** | Operational Security Analytics | ✅ Complete |
| **M4** | Risk Intelligence & Executive Analytics | ✅ Complete |

---

# Conclusion

The **Advanced Threat Incident Analytics and Security Visualization Framework** provides a complete cybersecurity analytics workflow, progressing from raw incident data to structured security intelligence.

The project combines data preparation, feature engineering, Threat Severity Index calculation, dimensional modeling, threat intelligence, operational analytics, risk assessment, predictive analytics, anomaly detection, SLA monitoring, and executive visualization.

The resulting Power BI framework provides multiple analytical perspectives for understanding cybersecurity incidents, their impact, response performance, and associated risk.

---

## Project Status

**Project Completed — Milestones 1 to 4**
