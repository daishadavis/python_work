messages = ['Hello there', 'How are you', 'Its nice to meet you']
sent_messages = []

def show_messages(sent_messages):
    """Print each message in the list after they have been sent"""
    print("\nThe following messages have been sent:")
    for message in sent_messages:
        print(message)

def send_messages(messages, sent_messages):
    """
    Send each message until none are left.
    Move each message to sent messages after printing
    """
    while messages:
        unsent_message = messages.pop()
        print(f"Sending message: {unsent_message}")
        sent_messages.append(unsent_message)


send_messages(messages [:], sent_messages)
show_messages(sent_messages)

print(messages)
print(sent_messages)