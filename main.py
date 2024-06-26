import requests
from send_mail import send_email


topic= "techcrunch"

#create an account in newsapi.org,
#after creating the account, you will get the api_key
api_key="f649ca5e35a04ab09a2dcd72ee8df3de"

url="https://newsapi.org/v2/top-headlines?sources={topic}&apiKey=f649ca5e35a04ab09a2dcd72ee8df3de"


# made a request
request = requests.get(url)

# get a dictionary with data
content= request.json()

# access the article titles and description
body = " "
for article in content["articles"][:10]:
    if article["title"] is not None:
        body = "subject: Today's news" + "\n" \
        + body + article["title"] + "\n" \
        + article["description"] \
        + "\n" + article["url"] + 2*"\n"

 
body= body.encode("utf-8")
send_email(message = body)    
    

