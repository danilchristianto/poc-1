# hello_ipinfo.py
import requests

def main():
    # Print hello message
    print("Hello, World!")

    # Fetch IP info using ipinfo.io API
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("\nYour IP Information:")
            print(f"IP: {data.get('ip')}")
            print(f"City: {data.get('city')}")
            print(f"Region: {data.get('region')}")
            print(f"Country: {data.get('country')}")
            print(f"Org: {data.get('org')}")
        else:
            print("Failed to retrieve IP info.")
    except Exception as e:
        print(f"Error fetching IP info: {e}")

if __name__ == "__main__":
    main()
