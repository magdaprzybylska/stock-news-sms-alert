import requests
import os
from check_date import CheckDate
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
emoji = "🔻"
date = CheckDate()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

news_api_key = os.environ['NEWS_API_KEY']
stock_api_key = os.environ['STOCK_API_KEY']

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

from_number = os.environ['FROM_NUMBER']
to_number = os.environ['TO_NUMBER']

client = Client(account_sid, auth_token)

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': stock_api_key,
}

news_params = {
    'q': COMPANY_NAME,
    'from': date.last_day,
    'sortBy': 'popularity',
    'apiKey': news_api_key
}


stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

last_day_stock_closed = float(stock_data['Time Series (Daily)'][date.last_day]['4. close'])
before_last_day_stock_closed = float(stock_data['Time Series (Daily)'][date.before_last_day]['4. close'])


stock_difference = round(((before_last_day_stock_closed - last_day_stock_closed) / before_last_day_stock_closed * 100), 1)

if stock_difference < 0:
    stock_difference = stock_difference * -1
    emoji = "🔺"

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
final_news = news_data['articles'][:3]


def send_sms():
    for x in range(1):
        news_headline = final_news[x]['title']
        news_source = final_news[x]['source']['name']
        news_link = final_news[x]['url']

        message = client.messages.create(
           body=f"{STOCK}: {emoji}{stock_difference}%\n"
                f"Headline: {news_headline}\n"
                f"Source: {news_source}\n"
                f"Link: {news_link}",
           from_=from_number,
           to=to_number
        )


if stock_difference >= 2:
    send_sms()

