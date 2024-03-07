from telethon.sync import TelegramClient
import time

api_id = '22750064'
api_hash = 'bad926f0bcaa010fac4823630d26ca74'
phone_number = 'write your phone number here'

# Sign in with Telegram API
client = TelegramClient('session_name', api_id, api_hash)
client.start()  # Start session

# If not logged in, verify with phone number
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the verification code:'))

# Targeted group chat ID (chat ID)
destination_group = None

# Show all dialogs and ask the user to select the chat ID of the targeted group
dialogs = client.get_dialogs()
print("Dialogues:")
for dialog in dialogs:
    print(f"{dialog.id}: {dialog.title}")

try:
    destination_group = int(input("Enter the chat ID of the targeted group: "))
except ValueError:
    print("Invalid number entry. Program termination.")
    exit()

latest_message_ids = {source: None for source in ['enter telegram invite link', 'enter telegram invite link', 'enter telegram invite link']}    #   Example: 't.me/CoingraphNews' (you can enter as many telegram links as you want)
sent_messages = set()

while True:
    for source in ['enter telegram invite link', 'enter telegram invite link', 'enter telegram invite link']:
        # Get the channel's latest message
        messages = client.get_messages(source, limit=1)

        if messages and messages[0].id != latest_message_ids[source] and messages[0].id not in sent_messages:
            # There is a new message and it has not been sent before
            latest_message_ids[source] = messages[0].id

            if messages[0].text:
                # Send original message directly
                message_text = f"{messages[0].text}"

                # If "https://" is not mentioned in the message, send
                if "https://" not in message_text:
                    client.send_message(destination_group, message_text)
            elif messages[0].media:
                # If media file is available, receive and send media
                client.send_message(destination_group, file=messages[0].media)

            sent_messages.add(messages[0].id)

    # Wait for a certain period of time and check again
    time.sleep(5)  # For example, you can wait 5 seconds (5 seconds)
