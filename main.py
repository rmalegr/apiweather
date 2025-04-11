import requests 
reponse = requests.get("https://api.github.com/users/octocat")
print(reponse.status_code)