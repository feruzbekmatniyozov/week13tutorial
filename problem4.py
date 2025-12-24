import requests

url = "http://universities.hipolabs.com/search"
country_name = input("Enter country: ")
def university_search(country):  
    unis_list = []  
    params = {
        "country": country
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for dict in data:
            unis_list.append(dict["name"])
        if not unis_list:
            print(f"No universities found for {country}.")
        else:
            print(f"Found {len(unis_list)} universities in Uzbekistan.")
            print("Here are the 5 first:")
            for i in range(5):
                if i < len(unis_list):
                    print(f"{i+1}. {unis_list[i]}")
    else:
        print("Requesting data error!")
    
university_search(country_name)