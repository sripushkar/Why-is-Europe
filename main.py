import requests
import json

query = "Why+is+Germany+so+"

results = requests.get("http://suggestqueries.google.com/complete/search?q="+query+"&client=firefox&hl=en")

resultsJSON = results.json()

print(resultsJSON[1][0])
