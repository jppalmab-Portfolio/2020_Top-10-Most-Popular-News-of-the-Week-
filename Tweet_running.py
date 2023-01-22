import tweepy
import time
import hidden

print("The instance has started...")

exec(open("hidden.py").read())
exec(open("news_of_the_week.py").read())

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None

oauth = OAuth()
api = tweepy.API(oauth)

#declare = api.update_status("Querida comunidad, en el marco de un proyecto en el que estoy trabajando, desde HOY y TODOS los DOMINGOS publicare un TOP 10 de las noticias mas compartidas de la semana")
#declare = api.update_status("Tal y como la semana anterior voy con el TOP 10 de las noticias mas compartidas de la semana en Chile")
#time.sleep(120)

main_tweet = api.update_status("Este es el TOP 10 CHILE de las noticias mas compartidas de la SEMANA #TOP10CHILE")
print("The main post has been posted")
time.sleep(30)

# Numero 10
x = "[TOP 10 NOTICIAS EN CHILE: NUMERO " + str(10) + "]"
y = df.loc[9 ,'headers']
z = df.loc[9 ,'links']
post = "\n".join([x, y, z])
tweet = api.update_status(str(post), in_reply_to_status_id=main_tweet.id, auto_populate_reply_metadata=True)
print("Posted tweet number 1 of 10")
time.sleep(30)

# TOP 9 to 1
for i, n in zip(range(8, -1, -1), range(9,0,-1)):
    x = "[TOP 10 NOTICIAS EN CHILE: NUMERO " + str(n) + "]"
    y = df.loc[i ,'headers']
    z = df.loc[i ,'links']
    post = "\n".join([x, y, z])
    tweet = api.update_status(str(post), in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
    print("Posted tweet number " + str(10 - i) + " of 10")
    time.sleep(30)

print("The instance has finished! Well done!")