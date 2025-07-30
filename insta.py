from instagrapi import Client
import requests

# Create a client instance
cl = Client()

# 🔐 Login to Instagram
cl.login("wihol866425689456", "6joqf(3ix8f3")  # Replace with your username & password

# 👤 Target username
target_username = "username target"

# 📥 Get user info
user_info = cl.user_info_by_username(target_username)

# 🖼️ Get profile picture URL
profile_pic_url = user_info.profile_pic_url
print("Profile Picture URL:", profile_pic_url)

# 💾 Download and save the image
response = requests.get(profile_pic_url)

if response.status_code == 200:
    with open(f"{target_username}_profile.jpg", "wb") as f:
        f.write(response.content)
    print(f"Profile picture saved as {target_username}_profile.jpg")
else:
    print("Failed to download profile picture.")
