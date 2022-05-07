

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
                                body=f'Todays price:{yesterday_price}\nchange:{difference}%\n{title}\n{content}'
                            ) 
 
    print(message.sid)

if difference > 3 : 
    get_news()


