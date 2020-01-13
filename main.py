import requests


with open("euroCountries.txt") as f:
  countriesList = f.readlines()

countriesList = [line.rstrip('\n') for line in open("euroCountries.txt")]

listLength = len(countriesList)

i = 0

while i < listLength:
    query = "Why+is+" + countriesList[i] + "+so+"

    results = requests.get("http://suggestqueries.google.com/complete/search?q="+query+"&client=firefox&hl=en")

    resultsJSON = results.json()

    print(resultsJSON[1][0])
    i+=1
