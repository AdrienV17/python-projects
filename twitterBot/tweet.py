import tweepy
import time

auth = tweepy.OAuthHandler('ME6w4OXks2s5hSDeVozXAoLLx', 'pUFSo3q0xr3bFPqu26fPITNPmJc1uiwNxi6Rqfl7L1zojUQvsL')
auth.set_access_token('1227646700954750976-cowZSP5WNfSzpTzIsbztZXATRTVOe5', 'cVwE4avYoMJHGeAF3Nruz8xV2NzaEW8WszynnzSCCvHVQ')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:       
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# Generous Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'Nnesand_05':
        follower.follow()
        break