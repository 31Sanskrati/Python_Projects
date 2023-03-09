# Amazon_Price_Tracker 💵

## Project Description
This is a Python script that tracks the price of a product on Amazon and sends an email alert if the price drops below a certain threshold.

## Requirements
1. Python 3.7 or higher
2. Requests library
3. Beautiful Soup 4 library
4. smtplib library

## Installation
1. Clone the repository to your local machine:
2. bash
3. git clone https://github.com/yourusername/yourproject.git

## Install the required libraries using pip:
1. pip install requests
2. pip install beautifulsoup4
3. pip install secure-smtplib

## Open the price_tracker.py file in a text editor and replace the following variables with your own values:
1. makefile
2. BUY_PRICE = 1500
3. url = "https://www.amazon.in/dp/B08XM2CZQ7"
4. sender_email = "youremail@gmail.com"
5. sender_password = "yourpassword"
6. receiver_email = "youremail@gmail.com"

## Save the file and run it using the following command:
1. python main.py
#
Once the script is running, it will fetch the price of the specified product from Amazon at regular intervals. If the price drops below the specified threshold, it will send an email alert to the specified email address.
