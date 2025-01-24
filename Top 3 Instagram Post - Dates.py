import instaloader
from datetime import datetime

L = instaloader.Instaloader()

username = "stella_fragkoulaki"

profile = instaloader.Profile.from_username(L.context, username)

start_date = datetime(2022, 10, 11)
end_date = datetime(2024, 10, 11)

posts = list(profile.get_posts())

filtered_posts = [post for post in posts if start_date <= post.date <= end_date]

filtered_posts.sort(key=lambda post: post.likes, reverse=True)

top_3_posts = filtered_posts[:3]

for i, post in enumerate(top_3_posts, start=1):
    print(f"Post {i}:")
    print(f"https://www.instagram.com/p/{post.shortcode}/")
    print(f"Date: {post.date}\n")