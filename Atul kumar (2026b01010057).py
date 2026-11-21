import pandas as pd

# Loading Dataset
df = pd.read_csv(r"C:\Users\gaura\Desktop\netflix_project\netflix_titles.csv")

# Display first 5 rows
print(df.head())

# Total rows and columns
print(df.shape)

# Complete dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Check duplicate records
print("Duplicate Records:", df.duplicated().sum())

# Handle Missing Values

df.fillna({
    "director": "Unknown",
    "cast": "Unknown",
    "country": "Unknown",
    "date_added": "Unknown",
    "rating": "Unknown",
    "duration": "Unknown"
}, inplace=True)

# Check missing values again
print(df.isnull().sum())

# Save Cleaned Dataset

df.to_csv("netflix_cleaned.csv", index=False)

print("Cleaned Dataset Saved Successfully!")

# Movies and TV Shows Count

print(df["type"].value_counts())


# Verify Cleaned Dataset

cleaned_df = pd.read_csv("netflix_cleaned.csv")

print("Total Rows and Columns:", cleaned_df.shape)

print("Remaining Missing Values:",
      cleaned_df.isnull().sum().sum())

print("Duplicate Records:",
      cleaned_df.duplicated().sum())
