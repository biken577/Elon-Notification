from snscrape.modules.twitter import TwitterUserScraper,TwitterSearchScraper
import pandas as pd
from datetime import datetime

def twitteruserscraper(name):
  """
  search the user and provides its content
  """
  date=[]
  contents=[]
  users=[]
  
  for i,tweets in enumerate(TwitterUserScraper(name).get_items()):
    if i >50:
      break
    date.append(tweets.date)
    contents.append(tweets.content)
    users.append(tweets.user.username)
  df=pd.DataFrame({"Date":date,"Content":contents,"User":users})
  return df

#print(twitteruserscraper('elonmusk'))

def twittersearchscraper(search):
  """
  search the query and provides its content
  """
  date=[]
  contents=[]
  users=[]
  for i,tweets in enumerate(TwitterSearchScraper(search).get_items()):
    if i > 50:
      break
    date.append(tweets.date)
    contents.append(tweets.content)
    users.append(tweets.user)
  df=pd.DataFrame({"Date":date,"Content":contents,"User":users},index=date)
  return df


# Code starts here
df=twittersearchscraper("from:unusual_whales")
today=datetime.now()
df=df[df.index.day==today.day]

tickers=["BBBY","BAC","AAPL","TSLA","AMZN"]

print(df["Content"][0])
print(type(df["Content"][0]))
