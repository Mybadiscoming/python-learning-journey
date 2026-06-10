import requests
url = "https://official-joke-api.appspot.com/random_joke"
a = input("Want to hear a joke? (y/n): ")

if a == "y":
    response = requests.get(url)
    data = response.json()
    print(f"{data['setup']} {data['punchline']}")
else:
    quit
