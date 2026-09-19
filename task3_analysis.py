import pandas as pd
import numpy as np

# Load the cleaned CSV file from Task 2
df = pd.read_csv("data/trends_cleaned.csv")

# Display basic information about the dataset
print("Total stories:", len(df))

print("\nColumns:")
print(df.columns.tolist())

# Display the first five rows
print("\nFirst 5 rows:")
print(df.head())

# Count the number of stories in each category
category_counts = df["category"].value_counts()

print("\nStories by category:")
print(category_counts)

# Find the top 10 stories by score
top_stories = df.nlargest(10, "score")

print("\nTop 10 stories by score:")
print(top_stories[["title", "category", "score"]])

# Convert scores into a NumPy array
scores = np.array(df["score"])

# Calculate basic score statistics
average_score = np.mean(scores)
maximum_score = np.max(scores)
minimum_score = np.min(scores)

print("\nScore statistics:")
print("Average score:", round(average_score, 2))
print("Maximum score:", maximum_score)
print("Minimum score:", minimum_score)

# Calculate comment statistics using NumPy
comments = np.array(df["num_comments"])

average_comments = np.mean(comments)
maximum_comments = np.max(comments)
minimum_comments = np.min(comments)

print("\nComment statistics:")
print("Average comments:", round(average_comments, 2))
print("Maximum comments:", maximum_comments)
print("Minimum comments:", minimum_comments)

# Calculate average score for each category
category_scores = df.groupby("category")["score"].mean().round(2)

print("\nAverage score by category:")
print(category_scores)