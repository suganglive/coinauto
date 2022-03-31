import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage", headers={"Authorization": "Bearer"+token}, data={"channel": channel, "text": text})
    print(response,text)

token = 'xoxb-3309289486631-3323908360866-PEhuNBX98hTItTttof6HXGRu'
post_message(token, "#coin", "hiasdasd")