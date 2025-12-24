import requests
url = "http://api.open-notify.org/iss-now.json"
print("Connecting to ISS satellite...")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Connection Successful!")
    print("Current Location:")
    print(f"Latitude: {data["iss_position"]["latitude"]}")
    print(f"Longitude: {data["iss_position"]["longitude"]}")