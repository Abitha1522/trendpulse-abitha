import json
import pandas as pd

# Open the JSON file created in Task 1
with open("data/trends_20260919.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Display the number of stories loaded
print("Stories loaded:", len(data))

# Convert the JSON data into a Pandas DataFrame
df = pd.DataFrame(data)

# Display the first few rows before cleaning
print("\nBefore cleaning:")
print(df.head())

# Check for missing values in each column
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Check for duplicate post IDs
print("\nDuplicate post IDs:", df["post_id"].duplicated().sum())

# Remove duplicate posts using post_id
df = df.drop_duplicates(subset=["post_id"])

# Remove extra spaces from text columns
df["title"] = df["title"].str.strip()
df["category"] = df["category"].str.strip().str.lower()
df["author"] = df["author"].str.strip()

# Make sure numeric columns contain numbers
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
df["num_comments"] = pd.to_numeric(
    df["num_comments"], errors="coerce"
).fillna(0).astype(int)

# Check how many titles are empty
print("\nEmpty titles:", (df["title"] == "").sum())

# Display the cleaned data
print("\nAfter cleaning:")
print(df.head())

# Display the number of rows after cleaning
print("\nRows after cleaning:", len(df))
# Save the cleaned data as a CSV file
df.to_csv("data/trends_cleaned.csv", index=False)

print("\nCleaned data saved to data/trends_cleaned.csv")