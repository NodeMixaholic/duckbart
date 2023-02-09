import requests
import duckduckgo

headers = {"Authorization": "Bearer xxxxxxxxxxxxxxxxxxxxxxxxxx"} #change xxxxxxxxxxxxxxxxx to YOUR user token for huggingface.

def query(payload, API_URL):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

print("DuckBart Started!")
while True:
  q = input("prompt:")
  try:
    try:
      o = query({
      "inputs": q,
      }, "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium")
      ans = o['generated_text']
      if ('don\'t understand' in ans or 'don\'t know' in ans or 'try' in ans or 'not sure' in ans):
        raise Exception
      print(ans)
    except:
      s = duckduckgo.get_zci(q)
      o = query({
      "inputs": s,
      }, "https://api-inference.huggingface.co/models/google/pegasus-xsum")
      print(o[0]['summary_text'])
  except:
    print("Result not found.")
