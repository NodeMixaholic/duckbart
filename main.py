import requests
import duckduckgo

API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"
headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxx"} #change xxxxxxxxxxxxxxxxx to YOUR user token.

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

print("DuckBart Started!")
while True:
  q = input("prompt:")
  s = duckduckgo.get_zci(q)
  o = query({
	  "inputs": s,
  })
  answer = o[0]['summary_text']
  print(answer)