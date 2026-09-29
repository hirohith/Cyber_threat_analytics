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

The data warehouse follows a **Star Schema** architecture consisting of:

- One central fact table
- Four dimension tables:
  - Date Dimension
  - Location Dimension
  - Threat Dimension
  - Operational Dimension

The **Fact_Incident** table is connected to each dimension through key columns using **one-to-many (1:*) relationships**.

---

## 10.1 Fact Table

### `Fact_Incident`

The `Fact_Incident` table acts as the central analytical table and stores incident-level measures along with keys that connect each incident to the appropriate dimension.

### Key Fields

- `Incident_ID`
- `Date_Key`
- `Location_Key`
- `Threat_Key`
- `Operational_Key`

### Incident Measures

- `Affected_Users`
- `Attack_Duration_Min`
- `Data_Compromised_GB`
- `Financial_Loss_INR`
- `Response_Time_Min`

### Derived Analytical Fields

- `Data_Norm`
- `Loss_Norm`
- `Response_Norm`
- `Risk_Level`
- `Risk_Level_4`

The fact table serves as the central source for analytical calculations, risk analysis, incident impact measurement, and Power BI reporting.

---

# 11. Dimension Tables

## 11.1 Date Dimension

### `Dim_Date`

The Date dimension provides a structured time-based view of cybersecurity incidents.

### Key Attributes

- `Date_Key`
- `Date`
- `Month`
- `Month_Name`
- `Quarter`
- `Year`

This dimension enables time-based filtering, aggregation, and trend analysis such as monthly, quarterly, and yearly incident patterns.

---

## 11.2 Location Dimension

### `Dim_Location`

The Location dimension provides geographic and organizational context for cybersecurity incidents.

### Key Attributes

- `Location_Key`
- `City`
- `State`
- `Industry`
- `Organization`

This dimension enables analysis of cybersecurity incidents across different cities, states, industries, and organizations.

---

## 11.3 Threat Dimension

### `Dim_Threat`

The Threat dimension contains descriptive information about the type and severity of cybersecurity threats.

### Key Attributes

- `Threat_Key`
- `Attack_Type`
- `Attack_Severity`
- `Threat_Severity`
- `Target_System`

This dimension supports analysis of attack classifications, severity levels, and affected target systems.

---

## 11.4 Operational Dimension

### `Dim_Operational`

The Operational dimension stores information related to cybersecurity incident handling and response.

### Key Attributes

- `Operational_Key`
- `Security_Tools_Used`
- `Mitigation_Method`
- `Outcome`
- `Reporting_Agency`

This dimension supports analysis of security tools, mitigation methods, incident outcomes, and reporting agencies.

---

# 12. Star Schema Architecture

The dimensional model is organized around the central `Fact_Incident` table.

The four dimension tables are connected to the fact table using **one-to-many (1:*) relationships**:

| Dimension Table | Key | Fact Table Key | Relationship |
|---|---|---|---|
| `Dim_Date` | `Date_Key` | `Date_Key` | 1 : * |
| `Dim_Location` | `Location_Key` | `Location_Key` | 1 : * |
| `Dim_Threat` | `Threat_Key` | `Threat_Key` | 1 : * |
| `Dim_Operational` | `Operational_Key` | `Operational_Key` | 1 : * |

The dimension tables are on the **one (1) side**, while `Fact_Incident` is on the **many (*) side**.

### Star Schema Structure

```text
                         ┌─────────────────────┐
                         │      Dim_Threat     │
                         │─────────────────────│
                         │ Threat_Key          │
                         │ Attack_Type         │
                         │ Attack_Severity     │
                         │ Threat_Severity     │
                         │ Target_System       │
                         └──────────┬──────────┘
                                    │ 1
                                    │
                                    │ *
                         ┌──────────▼──────────┐
                         │    Fact_Incident    │
                         │─────────────────────│
                         │ Incident_ID         │
                         │ Date_Key            │
                         │ Location_Key        │
                         │ Threat_Key          │
                         │ Operational_Key     │
                         │ Affected_Users      │
                         │ Attack_Duration_Min │
                         │ Data_Compromised_GB │
                         │ Financial_Loss_INR  │
                         │ Response_Time_Min   │
                         │ Data_Norm           │
                         │ Loss_Norm            │
                         │ Response_Norm       │
                         │ Risk_Level          │
                         │ Risk_Level_4        │
                         └──────┬────────┬──────┘
                                │        │
                              * │        │ *
                                │        │
                           1    │        │    1
                  ┌─────────────┘        └─────────────┐
                  │                                    │
       ┌──────────▼───────────┐          ┌─────────────▼──────────┐
       │     Dim_Location     │          │    Dim_Operational     │
       │──────────────────────│          │────────────────────────│
       │ Location_Key         │          │ Operational_Key        │
       │ City                 │          │ Security_Tools_Used    │
       │ State                │          │ Mitigation_Method       │
       │ Industry             │          │ Outcome                 │
       │ Organization         │          │ Reporting_Agency        │
       └──────────────────────┘          └─────────────────────────┘

                         ┌─────────────────────┐
                         │       Dim_Date      │
                         │─────────────────────│
                         │ Date_Key            │
                         │ Date                │
                         │ Month               │
                         │ Month_Name          │
                         │ Quarter             │
                         │ Year                │
                         └──────────┬──────────┘
                                    │ 1
                                    │
                                    │ *
                                    ▼
                              Fact_Incident
The Fact_Incident table contains measurable incident-level information, while the dimension tables provide descriptive context for filtering, grouping, aggregation, and drill-down analysis.

This structure separates measures from descriptive attributes, making the model easier to analyze and maintain.

---
# 13. Power BI Integration

The Star Schema provides the data-model foundation for Power BI cybersecurity analytics.

The model supports analysis across the following areas:

- **Time Analysis**
  - Daily incident trends
  - Monthly incident trends
  - Quarterly and yearly analysis

- **Geographical Analysis**
  - City-wise incidents
  - State-wise incidents
  - Organization-wise incidents

- **Industry Analysis**
  - Incident distribution by industry
  - Comparison of cybersecurity incidents across industries

- **Attack Classification**
  - Attack type analysis
  - Target system analysis
  - Attack severity analysis

- **Threat Analysis**
  - Threat severity analysis
  - Classification of different cybersecurity threats

- **Security Operations**
  - Security tools used
  - Mitigation methods
  - Incident outcomes
  - Reporting agencies

- **Incident Impact**
  - Affected users
  - Financial loss
  - Data compromised
  - Attack duration

- **Response Performance**
  - Response time analysis
  - Normalized response performance

- **Risk Analysis**
  - Risk level analysis
  - Risk-level categorization
  - Derived risk indicators

The dimensional structure provides a consistent foundation for Power BI dashboards, KPI analysis, filtering, aggregation, and drill-down analysis.

---

# 14. Data Model Relationships

The Power BI data model uses **one-to-many (1:*) relationships** between the dimension tables and the central `Fact_Incident` table.

| Dimension | Dimension Key | Fact Key | Cardinality | Cross-Filter |
|---|---|---|---|---|
| `Dim_Date` | `Date_Key` | `Date_Key` | 1 : * | Single |
| `Dim_Location` | `Location_Key` | `Location_Key` | 1 : * | Single |
| `Dim_Threat` | `Threat_Key` | `Threat_Key` | 1 : * | Single |
| `Dim_Operational` | `Operational_Key` | `Operational_Key` | 1 : * | Single |

The dimension tables contain unique key values, while the corresponding keys in `Fact_Incident` can occur across multiple incident records.

This relationship structure allows filters applied to dimension tables to propagate to the related incident records in the fact table.

---

# 15. Analytical Structure

The updated Star Schema separates the data into two major components:

### Fact Table

`Fact_Incident` stores the measurable incident-level information used for calculations and KPIs.

Examples include:

- Financial loss
- Response time
- Attack duration
- Data compromised
- Affected users
- Risk levels
- Normalized analytical measures

### Dimension Tables

The dimension tables provide descriptive context for the incident records.

| Dimension | Purpose |
|---|---|
| `Dim_Date` | Time-based analysis |
| `Dim_Location` | Geographic and organizational analysis |
| `Dim_Threat` | Threat and attack classification |
| `Dim_Operational` | Security operations and response analysis |

This structure allows the same incident measures to be analyzed from multiple perspectives without duplicating the underlying fact data.

---

# 16. Benefits of the Star Schema

The updated dimensional model provides the following benefits:

- Simplifies Power BI data modeling
- Provides clear separation between facts and dimensions
- Enables efficient filtering and aggregation
- Supports drill-down analysis
- Enables time-based trend analysis
- Supports geographical and industry-level analysis
- Supports threat and attack classification
- Enables operational and response analysis
- Provides a structured foundation for KPI development
- Supports risk and incident-impact analysis

The Star Schema therefore provides the structural foundation for the cybersecurity analytics and reporting layer developed in Power BI.
# 17. Milestone 1 Deliverables

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

# 18. Tools & Technologies

| Technology | Purpose |
|---|---|
| Python | Data preparation and feature engineering |
| Pandas | Data loading, cleaning and transformation |
| Power BI | Data modeling and visualization |
| DAX | Analytical calculations |
| CSV | Dataset storage and exchange |
| Star Schema | Dimensional data warehouse design |

---



# 19. Milestone 1 Outcome

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
