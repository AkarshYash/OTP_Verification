from twilio.rest import Client

account_sid = 'ACeacdd556a87f15bb145bd1213acd6860'
auth_token = '[a2b0e56c130b02dca8323684f1a2f78f]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to='+917742148084'
)

print(message.sid)