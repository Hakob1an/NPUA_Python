import requests
import json
import random
import string

# Function to generate a random string for anonymity
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

url = "https://example.com/api/posts"  # Replace with a generic URL

response = requests.get(url)
data = response.json()

filtered_titles = []
filtered_posts = []

for item in data:
    if len(item["title"].split()) > 6:
        filtered_titles.append(item["title"])
    if len(item["body"].split('\n')) > 3:
        filtered_posts.append(item)

print("Filtered titles with more than 6 words:")

for title in filtered_titles:
    print(title)

print("\nPosts with body containing more than 3 lines of description:")
for post in filtered_posts:
    print(f"\nTitle: {post['title']}")
    print(f"Body:\n{post['body']}")

new_post = {"title": "Programming", "body": "Python is a programming language.", "id": 101}
response = requests.post(url, new_post)
if response.status_code >= 200 and response.status_code <= 299:
    print("A new post has been added!")

new_post_updated = {"title": "Programming", "body": "C++ is a programming language."}
post_id_to_update = random.randint(1, len(data))
response = requests.put(f"{url}/{post_id_to_update}", new_post_updated)
if response.status_code >= 200 and response.status_code <= 299:
    print("A post has been updated!")

post_id_to_delete = random.randint(1, len(data))
response = requests.delete(f"{url}/{post_id_to_delete}")
if response.status_code >= 200 and response.status_code <= 299:
    print("A post has been deleted!")

