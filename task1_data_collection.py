import requests
import time
headers = {"User-Agent": "TrendPulse/1.0"}

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    story_ids = response.json()[:500]
    print("Number of story IDs:", len(story_ids))
else:
    print("Failed to fetch story IDs")
stories = []

for story_id in story_ids:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        story_response = requests.get(
    story_url,
    headers=headers,
    timeout=10
)

        if story_response.status_code == 200:
            story = story_response.json()

            if story:
                stories.append(story)

        else:
            print(f"Failed to fetch story {story_id}")

    except requests.RequestException as error:
        print(f"Error fetching story {story_id}: {error}")

print("Stories fetched:", len(stories))
categories = {
    "technology": [
        "AI", "software", "tech", "code", "computer",
        "data", "cloud", "API", "GPU", "LLM"
    ],
    "worldnews": [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ],
    "sports": [
        "NFL", "NBA", "FIFA", "sport", "game",
        "team", "player", "league", "championship"
    ],
    "science": [
        "research", "study", "space", "physics",
        "biology", "discovery", "NASA", "genome"
    ],
    "entertainment": [
        "movie", "film", "music", "Netflix", "game",
        "book", "show", "award", "streaming"
    ]
}
# Create empty lists for each category
# Create empty lists for each category
category_stories = {
    "technology": [],
    "worldnews": [],
    "sports": [],
    "science": [],
    "entertainment": []
}

# Check each story title against the category keywords
for story in stories:
    title = story.get("title", "").lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in title:
                if len(category_stories[category]) < 25:
                    category_stories[category].append(story)
                break

# Display category counts
print("\nCategory results:")

for category, items in category_stories.items():
    print(category, ":", len(items))
    time.sleep(2)
from datetime import datetime

# Store the current date and time
collected_at = datetime.now().isoformat()

final_stories = []

# Extract only the fields required by the assignment
for category, items in category_stories.items():
    for story in items:
        formatted_story = {
            "post_id": story.get("id"),
            "title": story.get("title", ""),
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", ""),
            "collected_at": collected_at
        }

        final_stories.append(formatted_story)

print("\nTotal stories collected:", len(final_stories))
import os
import json

# Create the data folder if it does not exist
os.makedirs("data", exist_ok=True)

# Create the filename using today's date
date_string = datetime.now().strftime("%Y%m%d")
file_path = f"data/trends_{date_string}.json"

# Save all collected stories to the JSON file
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(final_stories, file, indent=4, ensure_ascii=False)

print(f"Collected {len(final_stories)} stories. Saved to {file_path}")