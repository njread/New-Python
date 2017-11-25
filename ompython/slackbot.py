# Imports environment variables
import weather
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from slacker import Slacker

slack = Slacker(os.environ['SLACK_API_TOKEN'])

# Post a message to a channel
#slack.chat.post_message('#bots', 'Hello fellow slackers!')


 # Get a list of slack users
#response = slack.users.list()
#users = response.body['members']

#names = []

#for user in users:
#  names.append(user['name'])

#print(names)


# # Search for a Slack message
# search_results = slack.search.all(query="Hello fellow slackers!")
# print(search_results.body['messages'])


 # Post a message to a channel with customization
api_key = "f05f15a9dee99b552764a634f8d6407e"
address = "Oxford"

slack.chat.post_message('#bots', weather.Get_weather(address, api_key), username="njr", icon_url="https://s3.amazonaws.com/one-month-rails-production/assets/files/000/000/797/original/heavy_rain_showers.png")