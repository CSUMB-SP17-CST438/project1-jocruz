import llaves
import requests
authUrl = "https://api.twitter.com/oauth2/token"
headers = {"Authorization":" Basic ", "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
                "grant_type":"client_credentials"}

def authorize():
    response = requests.post(authUrl,auth=(llaves.twitKey,llaves.twitSecret),
                data = {"grant-type":"client_credentials"})
    resData = response.json()
    if resData.get('token_type') != 'bearer':
        print("This is not a bearer token, this is a " + str(resData.get('token_type')))
    else:
        return response['access_token']
        
        
print(authorize())