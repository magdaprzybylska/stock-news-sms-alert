# Stock News SMS Alert
## Program Overview

This Python program retrieves the stock data and related news for a specified company (Tesla Inc in this case) and sends an SMS notification if the stock price difference between the last two days is greater than or equal to 5%. The program utilizes the Alpha Vantage API to fetch stock data and the News API to obtain relevant news articles.

## Dependencies
To run this program, you need to have the following dependencies installed:

- Python 3.x
- `requests` library (for making HTTP requests)
- `twilio` library (for sending SMS messages)
- `check_date` module (custom module to calculate date intervals, available in the project directory)
- Environment variables set for the required API keys and Twilio credentials:

  - NEWS_API_KEY: API key for the News API
  - STOCK_API_KEY: API key for the Alpha Vantage API
  - TWILIO_ACCOUNT_SID: Twilio Account SID
  - TWILIO_AUTH_TOKEN: Twilio Auth Token
  - FROM_NUMBER: Twilio phone number to send SMS from
  - TO_NUMBER: Recipient's phone number to receive SMS notifications (please note that this phone number needs to be a Verified Caller ID on Twilio)

## Usage
1. Make sure you have set up the necessary environment variables with the required API keys and Twilio credentials.

2. Install the required libraries if you haven't already.
3. Place the check_date.py module in the same directory as the main Python script. 
4. Run the Python script to check the stock data and send SMS notifications. 

## Program Flow

1. Import necessary modules and libraries:

- `requests`: For making HTTP requests to APIs.
- `os`: For accessing environment variables.
- `CheckDate`: A custom module to calculate date intervals.
- `twilio.rest`: Twilio's module to send SMS messages.

2. Define constants and initialize variables:
- `STOCK`: Stock symbol (e.g., "TSLA" for Tesla).
- `COMPANY_NAME`: Company name for news search (e.g., "Tesla Inc").
- `emoji`: Emoji representation of the stock trend (up or down).
- `date`: Instance of the CheckDate class to calculate date intervals.
- `STOCK_ENDPOINT`: URL for the Alpha Vantage API.
- `NEWS_ENDPOINT`: URL for the News API.
- API keys and Twilio credentials retrieved from environment variables.

3. Set up API parameters for stock data (stock_params) and news (news_params).

4. Fetch stock data using Alpha Vantage API:
- Make a request to the API with stock_params.
- Parse the JSON response and retrieve relevant stock data.

5. Calculate the stock difference between the last two days and update the `emoji` accordingly.

6. Fetch news data related to the specified company using the News API:
- Make a request to the API with news_params.
- Collect the JSON response and extract relevant news articles.

7. Define the send_sms function to send SMS notifications using Twilio:
- Iterate through the top 3 news articles.
- Format the SMS message with stock data and news information.
- Send the SMS using Twilio's client.messages.create method.
8. If the stock difference is greater than or equal to 5%, call the `send_sms` function to notify the user via SMS.

## Note
- Ensure that the required API keys and Twilio credentials are valid and set as environment variables before running the program.
- The program sends SMS notifications only if the stock difference is greater than or equal to 5%. You can adjust this threshold as needed.
- The program fetches and sends the top 3 news articles related to the specified company. You can modify the send_sms function to send more or fewer news articles as required.

## Disclaimer 
This program is for educational purposes only and should not be used for real trading or investment decisions. The stock data and news obtained from external APIs may not be completely accurate or up-to-date. Always conduct proper research and consult financial professionals before making any investment decisions. The author and contributors of this program are not responsible for any financial losses or damages incurred by using this code.