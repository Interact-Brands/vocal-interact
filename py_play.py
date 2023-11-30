import requests

url = "https://api.play.ht/api/v2/cloned-voices"

headers = {
    "accept": "application/json",
    "AUTHORIZATION": "9090a6f074be4743998ea85923104613",
    "X-USER-ID": "IKnTE7B9DDSPBx1boiJ40ESDtFn2"
}

response = requests.get(url, headers=headers)

print(response.text)