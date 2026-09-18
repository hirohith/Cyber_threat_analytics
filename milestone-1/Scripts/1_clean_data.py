import pandas as pd

# ===========================
# STEP 1: LOAD DATASET
# ===========================

df = pd.read_csv("Dataset/India_Cybersecurity_Incident_Dataset.csv")

print("Dataset Loaded Successfully")
print(df.head())

# ===========================
# STEP 2: CHECK BASIC INFO
# ===========================

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# ===========================
# STEP 3: REMOVE DUPLICATES
# ===========================

df = df.drop_duplicates()

print("\nDuplicates Removed")

# ===========================
# STEP 4: HANDLE MISSING VALUES
# ===========================

# Fill text columns with "Unknown"
text_columns = df.select_dtypes(include="object").columns

for col in text_columns:
    df[col] = df[col].fillna("Unknown")

# Fill numeric columns with median
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

print("Missing Values Handled")

# ===========================
# STEP 5: CONVERT TIMESTAMP
# ===========================

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

print("Timestamp Converted")

# ===========================
# STEP 6: CHECK DATA TYPES
# ===========================

print("\nData Types")
print(df.dtypes)

# ==========================================
# THREAT SEVERITY INDEX (TSI)
# ==========================================
# Normalize Severity
df["Severity_Norm"] = df["Attack_Severity"] / 10

# Normalize Financial Loss
df["Loss_Norm"] = (
    (df["Financial_Loss_INR"] - df["Financial_Loss_INR"].min()) /
    (df["Financial_Loss_INR"].max() - df["Financial_Loss_INR"].min())
)

# Normalize Data Compromised
df["Data_Norm"] = (
    (df["Data_Compromised_GB"] - df["Data_Compromised_GB"].min()) /
    (df["Data_Compromised_GB"].max() - df["Data_Compromised_GB"].min())
)

# Normalize Affected Users
df["Users_Norm"] = (
    (df["Affected_Users"] - df["Affected_Users"].min()) /
    (df["Affected_Users"].max() - df["Affected_Users"].min())
)

# Normalize Response Time
df["Response_Norm"] = (
    (df["Response_Time_Min"] - df["Response_Time_Min"].min()) /
    (df["Response_Time_Min"].max() - df["Response_Time_Min"].min())
)

# Calculate TSI
df["TSI_Score"] = (
    0.35 * df["Severity_Norm"] +
    0.25 * df["Loss_Norm"] +
    0.20 * df["Data_Norm"] +
    0.10 * df["Users_Norm"] +
    0.10 * df["Response_Norm"]
)

df["TSI_Score"] = df["TSI_Score"].round(2)

# ===========================
# STEP 7: SAVE CLEAN DATA
# ===========================
print("\nTSI Created Successfully")
print(df[["Attack_Severity", "Financial_Loss_INR",
          "Data_Compromised_GB", "Affected_Users",
          "Response_Time_Min", "TSI_Score"]].head())
df.to_csv("Output/clean_data.csv", index=False)

print("\nClean Dataset Saved Successfully")