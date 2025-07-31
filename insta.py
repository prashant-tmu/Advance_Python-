from instagrapi import Client
import requests


cl = Client()


cl.login("wihol866425689456", "6joqxxxxxxxxxx")  


target_username = "username target"


user_info = cl.user_info_by_username(target_username)


profile_pic_url = user_info.profile_pic_url
print("Profile Picture URL:", profile_pic_url)

response = requests.get(profile_pic_url)

if response.status_code == 200:
    with open(f"{target_username}_profile.jpg", "wb") as f:
        f.write(response.content)
    print(f"Profile picture saved as {target_username}_profile.jpg")
else:
    print("Failed to download profile picture.")
