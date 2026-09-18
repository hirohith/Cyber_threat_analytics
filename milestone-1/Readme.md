# Milestone 1 — Data Preparation & Data Warehouse Design

## Overview

Milestone 1 establishes the data foundation for the **Advanced Threat Incident Analytics and Security Visualization Framework**.

This milestone focuses on preparing the cybersecurity incident dataset for analysis, performing data quality handling, engineering the **Threat Severity Index (TSI)**, and designing a dimensional **Star Schema** for analytical reporting.

The resulting cleaned dataset and data warehouse model provide the foundation for the subsequent cybersecurity analytics milestones.

---

## 1. Dataset

The project uses the **India Cybersecurity Incident Dataset** as the primary source dataset.

The dataset contains incident-level information related to cybersecurity attacks, including attack characteristics, affected entities, impact, response, mitigation, and reporting information.

### Main Dataset Attributes

| Category | Attributes |
|---|---|
| Identification | `Incident_ID` |
| Time | `Timestamp` |
| Geography | `State`, `City` |
| Organization | `Industry`, `Organization` |
| Threat | `Attack_Type`, `Attack_Severity`, `Threat_Severity` |
| Target | `Target_System` |
| Security | `Security_Tools_Used` |
| User | `User_Role` |
| Impact | `Data_Compromised_GB`, `Financial_Loss_INR`, `Affected_Users` |
| Duration & Response | `Attack_Duration_Min`, `Response_Time_Min` |
| Mitigation | `Mitigation_Method` |
| Outcome | `Outcome` |
| Reporting | `Reporting_Agency` |

---

## 2. Data Preparation

The dataset is prepared using **Python and Pandas**.

The implemented preprocessing workflow is:

    Raw Dataset
         ↓
    Load Dataset
         ↓
    Basic Data Inspection
         ↓
    Duplicate Removal
         ↓
    Missing Value Handling
         ↓
    Timestamp Conversion
         ↓
    Data Type Verification
         ↓
    Feature Normalization
         ↓
    TSI Calculation
         ↓
    TSI Rounding
         ↓
    Clean Dataset Export

The preprocessing pipeline prepares the raw cybersecurity incident data for analytical processing and downstream Power BI reporting.

---

## 3. Duplicate Removal

Duplicate records are removed using Pandas:

    df = df.drop_duplicates()

This ensures that duplicate records do not unnecessarily influence subsequent cybersecurity analysis.

---

## 4. Missing Value Handling

Missing values are handled according to the data type of each column.

### Text Columns

Missing values in text/object columns are replaced with:

    Unknown

### Numerical Columns

Missing values in numerical columns are replaced using the **median** value of the corresponding column.

This approach allows the dataset to retain its records while providing valid values for subsequent numerical analysis.

---

## 5. Timestamp Conversion

The `Timestamp` field is converted into Pandas datetime format:

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

This prepares the incident data for temporal analysis such as daily, monthly, quarterly, and yearly analysis.

---

## 6. Data Type Verification

After preprocessing, the data types of the dataset columns are checked.

This provides a final verification of the dataset structure before feature engineering and export.

---

# 7. Threat Severity Index (TSI)

A **Threat Severity Index (TSI)** is engineered to provide a combined analytical score for cybersecurity incidents.

The TSI combines five normalized components:

- Attack Severity
- Financial Loss
- Data Compromised
- Affected Users
- Response Time

---

## 7.1 Severity Normalization

Attack severity is normalized using:

    df["Severity_Norm"] = df["Attack_Severity"] / 10

The resulting feature is stored as `Severity_Norm`.

---

## 7.2 Financial Loss Normalization

Financial loss is normalized using Min-Max normalization:

    Loss_Norm =
    (Financial_Loss_INR - Minimum Financial Loss)
    /
    (Maximum Financial Loss - Minimum Financial Loss)

The resulting feature is stored as `Loss_Norm`.

---

## 7.3 Data Compromised Normalization

The amount of compromised data is normalized using Min-Max normalization:

    Data_Norm =
    (Data_Compromised_GB - Minimum Data Compromised)
    /
    (Maximum Data Compromised - Minimum Data Compromised)

The resulting feature is stored as `Data_Norm`.

---

## 7.4 Affected Users Normalization

The number of affected users is normalized using Min-Max normalization:

    Users_Norm =
    (Affected_Users - Minimum Affected Users)
    /
    (Maximum Affected Users - Minimum Affected Users)

The resulting feature is stored as `Users_Norm`.

---

## 7.5 Response Time Normalization

Response time is normalized using Min-Max normalization:

    Response_Norm =
    (Response_Time_Min - Minimum Response Time)
    /
    (Maximum Response Time - Minimum Response Time)

The resulting feature is stored as `Response_Norm`.

---

# 8. TSI Calculation

The final TSI score is calculated using a weighted combination of the five normalized components:

    TSI_Score =
        0.35 × Severity_Norm
      + 0.25 × Loss_Norm
      + 0.20 × Data_Norm
      + 0.10 × Users_Norm
      + 0.10 × Response_Norm

### TSI Weight Distribution

| Component | Weight |
|---|---:|
| Attack Severity | 35% |
| Financial Loss | 25% |
| Data Compromised | 20% |
| Affected Users | 10% |
| Response Time | 10% |
| **Total** | **100%** |

The TSI weighting scheme is a **project-defined analytical model**.

The calculated TSI score is rounded to **two decimal places** before the cleaned dataset is exported.

---

# 9. Clean Dataset

After data preparation and feature engineering, the processed dataset is exported as:

    Output/clean_data.csv

The cleaned dataset contains the original incident attributes together with the following engineered analytical features:

- `Severity_Norm`
- `Loss_Norm`
- `Data_Norm`
- `Users_Norm`
- `Response_Norm`
- `TSI_Score`

These features provide the analytical foundation for subsequent cybersecurity analysis.

---

# 10. Data Warehouse Design

A dimensional data warehouse was designed to support cybersecurity analytics and Power BI reporting.

The model follows a **Star Schema** architecture consisting of:

- One central fact table
- Time dimension
- Location dimension
- Threat dimension
- Operational dimension

---

## 10.1 Fact Table

### `cybersecuritydw.fact_incident`

The fact table acts as the central analytical table and stores incident-level measures together with foreign keys connecting the incident records to the relevant dimensions.

Key fields include:

- `Incident_ID`
- `Time_ID`
- `Location_ID`
- `Threat_ID`
- `Operational_ID`
- `Attack_Duration_Min`
- `Data_Compromised_GB`
- `Response_Time_Min`
- `Financial_Loss_INR`

The fact table serves as the central source for analytical calculations and reporting.

---

# 11. Dimension Tables

## 11.1 Time Dimension

### `cybersecuritydw.dim_time`

The time dimension provides temporal attributes for cybersecurity incident analysis.

Key attributes include:

- `Time_ID`
- `Timestamp`
- `Date`
- `Day`
- `Month`
- `Hour`
- `Year`

This dimension supports time-based filtering and analysis.

---

## 11.2 Location Dimension

### `cybersecuritydw.dim_location`

The location dimension provides geographic and organizational context for cybersecurity incidents.

Key attributes include:

- `Location_ID`
- `Location`
- `State`
- `City`
- `Industry`

This dimension supports geographic and location-based cybersecurity analysis.

---

## 11.3 Threat Dimension

### `cybersecuritydw.dim_threat`

The threat dimension organizes cybersecurity threat classifications.

Key attributes include:

- `Threat_ID`
- `Attack_Type`
- `Attack_Severity`
- `Threat_Severity`

This dimension supports threat classification and severity analysis.

---

## 11.4 Operational Dimension

### `cybersecuritydw.dim_operational`

The operational dimension stores operational and incident-response-related attributes.

Key attributes include:

- `Operational_ID`
- `Security_Tools_Used`
- `Target_System`
- `User_Role`
- `Mitigation_Method`

This dimension supports analysis of cybersecurity operations and incident response.

---

# 12. Star Schema Architecture

The dimensional model is organized around the central incident fact table.

    ┌─────────────────────┐
    │      dim_time       │
    │---------------------│
    │ Time_ID             │
    │ Date                │
    │ Day                 │
    │ Month               │
    │ Hour                │
    │ Year                │
    └──────────┬──────────┘
               │
               │
    ┌─────────────────────┐
    │    dim_location     │
    │---------------------│
    │ Location_ID         │
    │ Location            │
    │ State               │
    │ City                │
    │ Industry            │
    └──────────┬──────────┘
               │
               │
               ▼
    ┌─────────────────────┐
    │   fact_incident     │
    │---------------------│
    │ Incident_ID         │
    │ Time_ID             │
    │ Location_ID         │
    │ Threat_ID           │
    │ Operational_ID      │
    │ Financial_Loss_INR  │
    │ Response_Time_Min   │
    │ Data_Compromised_GB │
    │ Attack_Duration_Min │
    └──────┬────────┬─────┘
           │        │
           │        │
           │        ▼
           │   ┌─────────────────────┐
           │   │     dim_threat      │
           │   │---------------------│
           │   │ Threat_ID           │
           │   │ Attack_Type         │
           │   │ Attack_Severity     │
           │   │ Threat_Severity     │
           │   └─────────────────────┘
           │
           ▼
    ┌─────────────────────┐
    │  dim_operational    │
    │---------------------│
    │ Operational_ID      │
    │ Security_Tools_Used │
    │ Target_System       │
    │ User_Role           │
    │ Mitigation_Method   │
    └─────────────────────┘

The fact table provides measurable incident data, while the dimension tables provide descriptive context for filtering, grouping, and drill-down analysis.

---

# 13. Power BI Integration

The Star Schema provides the data-model foundation for Power BI analytics.

The model supports analysis across:

- Time
- Geography
- Attack classification
- Threat severity
- Security operations
- Incident impact
- Response performance

The dimensional structure provides a consistent foundation for the cybersecurity dashboards developed in subsequent milestones.

---

# 14. Milestone 1 Deliverables

## Data Preparation

- Raw cybersecurity incident dataset
- Dataset inspection
- Duplicate removal
- Missing-value handling
- Timestamp conversion
- Data type verification

## Feature Engineering

- `Severity_Norm`
- `Loss_Norm`
- `Data_Norm`
- `Users_Norm`
- `Response_Norm`
- `TSI_Score`

## Data Warehouse

- `fact_incident`
- `dim_time`
- `dim_location`
- `dim_threat`
- `dim_operational`
- Star Schema relationships

## Output

    Output/clean_data.csv

---

# 15. Tools & Technologies

| Technology | Purpose |
|---|---|
| Python | Data preparation and feature engineering |
| Pandas | Data loading, cleaning and transformation |
| Power BI | Data modeling and visualization |
| DAX | Analytical calculations |
| CSV | Dataset storage and exchange |
| Star Schema | Dimensional data warehouse design |

---



# 16. Milestone 1 Outcome

Milestone 1 establishes the data and modeling foundation for the cybersecurity analytics project.

The raw cybersecurity incident dataset is processed through a Python-based preprocessing pipeline that performs:

- Data inspection
- Duplicate removal
- Missing-value handling
- Timestamp conversion
- Data type verification
- Feature normalization
- Threat Severity Index calculation

The resulting clean dataset is then organized into a dimensional Star Schema consisting of a central incident fact table and supporting time, location, threat, and operational dimensions.

This foundation enables the subsequent milestones to perform:

- Threat Intelligence & Temporal Analytics
- Operational Security Analytics
- Security Risk Assessment
- Predictive Threat Analytics
- Executive Security Visualization

---

## Milestone Status

**Milestone 1 — Data Preparation & Data Warehouse Design: Complete**
