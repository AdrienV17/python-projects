from twilio.rest import Client 
 
account_sid = 'AC0feb1983762a6910e4a637d69f6564be' 
auth_token = '7339c10b68fc2bfff783da8ba4ade4c2' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
            from_='+12029461305',
            body="I just cant believe it!!!!",        
            to='+50768159323' 
        ) 

print(message.sid)