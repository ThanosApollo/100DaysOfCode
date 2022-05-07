

from api_key import * 
import requests
from datetime import date, timedelta
from newsapi import NewsApiClient
from twilio.rest import Client 
from twilio.rest import Client 

STOCK = "AAPL"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

today = date.today()
yesterday = today - timedelta(days=1)
twodaysago = today -timedelta(days=2)


params_stock = {
    'function' : 'TIME_SERIES_DAILY',
    'symbol' : STOCK,
    'apikey' :  stock_api
}

request = requests.get(url='https://www.alphavantage.co/query', params= params_stock)
data = request.json()

def get_today_price():
    try :
        todays_price = data['Time Series (Daily)'][str(today)]
        return todays_price
    except : 
        print('Stock market is not opened yet')


yesterday_price = float(data['Time Series (Daily)'][str(yesterday)]['4. close'])
twodaysago_price = float(data['Time Series (Daily)'][str(twodaysago)]['4. close'])

change = yesterday_price - twodaysago_price
difference = abs(change / yesterday_price) * 100 



newsapi = NewsApiClient(api_key='7f1a7b8ac1ce47bf8401a6594a15a838')
top_headlines = newsapi.get_top_headlines(q='Apple')


def get_news():
    title = top_headlines['articles'][0]['title']
    content = top_headlines['articles'][0]['description']
    link = top_headlines['articles'][0]['url']
    when = top_headlines['articles'][0]['publishedAt']




    
    account_sid = account_Sid 
    auth_token = auth_Token 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(     
                                messaging_service_sid='MG19f49ef4624c8b66ec8c16d7fddd8e54',    
                                to='+359879151441', 
                                body=f'Todays price:{yesterday_price}\nchange:{change}\n{title}\n{content}'
                            ) 
 
    print(message.sid)

if difference > 3 : 
    get_news()


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

