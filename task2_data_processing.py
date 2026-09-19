import json
import pandas as pd

# Load the JSON file created in Task 1
with open("data/trends_20260919.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert the JSON data into a Pandas DataFrame
df = pd.DataFrame(data)

# Print the number of stories loaded
print(f"Loaded {len(df)} stories from data/trends_20260919.json")


# 1. Remove duplicate stories using post_id
df = df.drop_duplicates(subset=["post_id"])

print(f"After removing duplicates: {len(df)}")


# 2. Remove rows where post_id, title, or score is missing
df = df.dropna(subset=["post_id", "title", "score"])

print(f"After removing nulls: {len(df)}")


# 3. Convert score and num_comments to numeric values
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

# Remove rows where score could not be converted
df = df.dropna(subset=["score"])

# Replace missing comment values with 0
df["num_comments"] = df["num_comments"].fillna(0)

# Convert both columns to integers
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)


# 4. Remove low-quality stories with score less than 5
df = df[df["score"] >= 5]

print(f"After removing low scores: {len(df)}")


# 5. Remove extra whitespace from titles
df["title"] = df["title"].str.strip()


# Save the cleaned DataFrame as CSV
df.to_csv("data/trends_clean.csv", index=False)

print(f"\nSaved {len(df)} rows to data/trends_clean.csv")


# Print the number of stories in each category
print("\nStories per category:")
print(df["category"].value_counts())