import requests
import pickle

covers = []
with open('lib.csv', 'r') as myfile:
    print('here')
    data = myfile.read().split("\n")

for id in data:
    token = {"Authorization" : "Bearer BQAtiFejRqLU_AT5qKoo0NDqLEEaYAiEDKlopZUlcredDYZ2xpEJVIGvDxajVlLxbOzd72ReMP8TCCu7dSoB1y6Hh9QELU2iCtY_hRKhEeUt1z4RJMX6k8zzmGZnVzhdTcc_gj1zHIMj"}
    url = "https://api.spotify.com/v1/tracks/" + id
    r = requests.get(url, headers=token)
    #print(r.json())
    try:
        covers.append(r.json()['album']['images'][2]['url'])
    except KeyError:
        continue
    print(id)

covers = list(set(covers))

with open('covers.csv','a') as file:
    for cover in covers:
        file.write(cover + "\n")
