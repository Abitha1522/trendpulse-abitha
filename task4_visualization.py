import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned CSV file
df = pd.read_csv("data/trends_cleaned.csv")

# Count stories in each category
category_counts = df["category"].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 5))
category_counts.plot(kind="bar")

# Add chart title and labels
plt.title("Number of Stories by Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()
# Calculate average score for each category
average_scores = df.groupby("category")["score"].mean()

# Create a bar chart for average scores
plt.figure(figsize=(8, 5))
average_scores.plot(kind="bar")

# Add chart title and labels
plt.title("Average Score by Category")
plt.xlabel("Category")
plt.ylabel("Average Score")

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()
# Select the top 10 stories by score
top_10 = df.nlargest(10, "score")

# Create a bar chart for top 10 stories
plt.figure(figsize=(10, 6))
plt.barh(top_10["title"], top_10["score"])

# Add chart title and labels
plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")

# Reverse the order so the highest score appears at the top
plt.gca().invert_yaxis()

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()