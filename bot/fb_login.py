import json
import requests

# Step 1: cookies.txt se cookies load karo
def load_cookies(file_path="cookies.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            cookies = json.load(f)  # JSON format me load kar rahe hain
        return cookies
    except Exception as e:
        print(f"❌ Error: Cookies load nahi ho rahi! ({e})")
        return None

# Step 2: Facebook login test karo
def check_facebook_login(cookies):
    session = requests.Session()
    session.cookies.update(cookies)

    response = session.get("https://www.facebook.com")
    
    if "home_icon" in response.text:
        print("🎉 Successfully logged in to Facebook using cookies!")
    else:
        print("❌ Login failed! Cookies expire ho sakti hain.")

# Step 3: Run the login process
if __name__ == "__main__":
    cookies = load_cookies()
    if cookies:
        check_facebook_login(cookies)
