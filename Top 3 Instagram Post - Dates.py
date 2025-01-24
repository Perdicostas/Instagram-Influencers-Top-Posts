import instaloader
from datetime import datetime

L = instaloader.Instaloader()

username = "INFLUENCER_USERNAME" #Add Influencer's Username

profile = instaloader.Profile.from_username(L.context, username)

start_date = datetime(2021, 11, 1) #Select Date start
end_date = datetime(2024, 11, 1)   #Select Date end

posts = list(profile.get_posts())

filtered_posts = [post for post in posts if start_date <= post.date <= end_date]

filtered_posts.sort(key=lambda post: post.likes, reverse=True)

top_3_posts = filtered_posts[:3]

for i, post in enumerate(top_3_posts, start=1):
    print(f"Post {i}:")
    print(f"https://www.instagram.com/p/{post.shortcode}/")
    print(f"Date: {post.date}\n")