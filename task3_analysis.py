import pandas as pd
import numpy as np

# Load the cleaned CSV file from Task 2
df = pd.read_csv("data/trends_clean.csv")

# Print the first 5 rows
print("First 5 rows:")
print(df.head())

# Print the shape of the DataFrame
print("\nLoaded data:", df.shape)

# Calculate average score and average comments
average_score = df["score"].mean()
average_comments = df["num_comments"].mean()

print("\nAverage score   :", round(average_score, 2))
print("Average comments:", round(average_comments, 2))


# -------------------------------
# NumPy Statistics
# -------------------------------

# Convert score column into a NumPy array
scores = np.array(df["score"])

# Calculate mean, median and standard deviation
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)

# Find highest and lowest scores
max_score = np.max(scores)
min_score = np.min(scores)

print("\n--- NumPy Stats ---")
print("Mean score   :", round(mean_score, 2))
print("Median score :", round(median_score, 2))
print("Std deviation:", round(std_score, 2))
print("Max score    :", max_score)
print("Min score    :", min_score)


# Find the category containing the most stories
category_counts = df["category"].value_counts()
most_common_category = category_counts.idxmax()
most_common_count = category_counts.max()

print(
    f"\nMost stories in: {most_common_category} "
    f"({most_common_count} stories)"
)


# Find the story with the most comments
most_commented = df.loc[df["num_comments"].idxmax()]

print(
    f'\nMost commented story: "{most_commented["title"]}" '
    f'— {most_commented["num_comments"]} comments'
)


# -------------------------------
# Add New Columns
# -------------------------------

# Engagement measures comments received compared with score
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Mark stories whose score is above the average score
df["is_popular"] = df["score"] > average_score


# -------------------------------
# Save the analysed data
# -------------------------------

df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved to data/trends_analysed.csv")