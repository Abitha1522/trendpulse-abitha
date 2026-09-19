import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the analysed data from Task 3
df = pd.read_csv("data/trends_analysed.csv")

# Create the outputs folder if it does not exist
os.makedirs("outputs", exist_ok=True)


# ---------------------------------
# Chart 1: Top 10 Stories by Score
# ---------------------------------

# Select the 10 stories with the highest scores
top_10 = df.nlargest(10, "score").copy()

# Shorten titles longer than 50 characters
top_10["short_title"] = top_10["title"].apply(
    lambda title: title[:50] + "..." if len(title) > 50 else title
)

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(top_10["short_title"], top_10["score"])

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")

# Show highest score at the top
plt.gca().invert_yaxis()

plt.tight_layout()

# Save before showing the chart
plt.savefig("outputs/chart1_top_stories.png")
plt.show()
plt.close()


# ---------------------------------
# Chart 2: Stories per Category
# ---------------------------------

# Count stories in each category
category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))

# Use different colours for each bar
plt.bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)

plt.title("Number of Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.tight_layout()

# Save before showing the chart
plt.savefig("outputs/chart2_categories.png")
plt.show()
plt.close()


# ---------------------------------
# Chart 3: Score vs Comments
# ---------------------------------

plt.figure(figsize=(9, 6))

# Separate popular and non-popular stories
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

# Plot both groups with different colours
plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    color="blue"
)

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    color="orange"
)

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()

plt.tight_layout()

# Save before showing the chart
plt.savefig("outputs/chart3_scatter.png")
plt.show()
plt.close()


# ---------------------------------
# Bonus: TrendPulse Dashboard
# ---------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# Dashboard title
fig.suptitle("TrendPulse Dashboard", fontsize=18)

# Chart 1 in dashboard
axes[0, 0].barh(top_10["short_title"], top_10["score"])
axes[0, 0].set_title("Top 10 Stories by Score")
axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Story Title")
axes[0, 0].invert_yaxis()

# Chart 2 in dashboard
axes[0, 1].bar(
    category_counts.index,
    category_counts.values,
    color=plt.cm.tab10(range(len(category_counts)))
)
axes[0, 1].set_title("Stories per Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Stories")

# Chart 3 in dashboard
axes[1, 0].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular",
    color="blue"
)

axes[1, 0].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular",
    color="orange"
)

axes[1, 0].set_title("Score vs Comments")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Number of Comments")
axes[1, 0].legend()

# Hide the unused fourth subplot
axes[1, 1].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.95])

# Save the dashboard
plt.savefig("outputs/dashboard.png")
plt.show()
plt.close()

print("\nAll charts saved successfully in the outputs folder.")