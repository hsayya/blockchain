#!/usr/bin/python3
"""
You'll need in install telethon first before you can use this code:
	$ pip install telethon

Command used to run this is:
	$ python3 sanitize.py

Update the api_id, api_hash, and phone_number with an admin info.
"""

import csv
import datetime

from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import DeleteMessagesRequest
from telethon.tl.types import ChannelParticipantsSearch, InputChannel, UpdateNewChannelMessage
from telethon.tl import TLObject, Session

#######################
# If you want to run this, you'll need to enter in your own information found at https://my.telegram.org/.
#######################
channel_name = 't.me/xxx'
api_id = xxxxxxx # this is an int
api_hash = 'xxxxxxxxxxxxxxxxxx'
phone_number = '+1xxxxxxxxxx'

# Create the client object, authenticate, and create session files in directory
client = TelegramClient(phone_number, api_id, api_hash, update_workers=1, spawn_read_thread=False)
client.connect()
channel = client.get_entity(channel_name)


blacklistedPhrases = set()
blacklistedPhrases.add("exchange")
blacklistedPhrases.add("//t.me")
blacklistedPhrases.add("fuck")
blacklistedPhrases.add("dick")
blacklistedPhrases.add("cunt")
blacklistedPhrases.add("porn")

def sanitize():
	# Authenticate the client
	if not client.is_user_authorized():
		print("not auth")
		client.send_code_request(phone_number)
		client.sign_in(phone_number, input('Enter the code: '))


	client.add_update_handler(callback)
	client.idle()  # ends with Ctrl+C
	client.disconnect()


def callback(update):
        if isinstance(update, UpdateNewChannelMessage):
        #you can whitelist the admins of the channels so that they can post links:
                if not update.message.from_id == xxxxxxxx and not update.message.from_id == xxxxxxxxx and not update.message.from_id == xxxxxxxxx:

                    res = client.delete_messages(channel, update.message.id, True)

                    print(update.message.from_id)
                    print(update.message.message)

                for phrase in blacklistedPhrases:
                        if phrase in update.message.message.lower():
                                client.delete_messages(channel, update.message.id, True)
                                print('Blacklisted: ', update.message.message)



def lambda_handler(event, context):
	return sanitize()


if __name__ == '__main__':
    sanitize()
