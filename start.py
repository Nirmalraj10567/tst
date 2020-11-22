from telethon import TelegramClient, events, Button
import requests
from headers import headers
import urls
import os
#from flask import request

client = TelegramClient('anfghohn', int(os.environ.get("APP_ID" )), os.environ.get("API_HASH")).start(bot_token= os.environ.get("TG_BOT_TOKEN"))
@client.on(events.NewMessage(pattern='/start'))
async def handler(event):
    chat = await event.get_chat()
    await client.send_message(chat,"""💁Hey i am created by infinitrocyber subscribe my channel https://m.youtube.com/channel/UCLHZQApnu1vN2j7fKDgv74w 👍👍👍👍👍👍
    i support zee5 and mx player-movies full mx player later develop send me mx players like https://www.mxplayer.in/movie/ba472677b661a6d09ab73f47d33c0c90 """)
    

@client.on(events.NewMessage(pattern='(?i)https://www.zee5.com'))
async def handler(event):
    link =event.text.split('/')[-1]
    
    chat = await event.get_chat()
    w =link
    markup = client.build_reply_markup(Button.url("https://www.zee5.com/tvshows/details/sembaruthi/0-6-675/sembaruthi-november-18-2020/0-1-manual_7adlhget67b0"+link))
    req1 = requests.get(urls.token_url1, headers=headers).json()
    req2 = requests.get(urls.platform_token).json()["token"]
    headers["X-Access-Token"] = req2
    req3 = requests.get(urls.token_url2, headers=headers).json()
           
    r1 = requests.get(urls.search_api_endpoint + w,headers=headers, params={"translation":"en", "country":"IN"}).json()
    g1 = (r1["hls"][0].replace("drm", "hls") + req1["video_token"])
   # await client.send_file(chat,r1["image_url"],caption = r1["title"])
    markup = client.build_reply_markup(Button.url("Zee Stream",urls.stream_baseurl+g1))
    await client.send_message(chat, """Support @SerialCoIn & @urlicupload\n\n + 🎥 +r1["title"]+\n\n + 📑 +r1["description"]\n\nTap this Button to Stream it with Different Qualities for Free 👇""",file=r1["image_url"], buttons=markup)
            
            #rgx = w
   # await client.send_message(chat, g1)
   #await client.send_message(chat,"445")
    
@client.on(events.NewMessage(pattern='(?i)https://www.mxplayer.in'))
async def handler(event):
    link =event.text.split('/')[-1]
    video_d = "https://llvod.mxplay.com/"
    A =requests.get("https://api.mxplay.com/v1/web/detail/video?type=movie&id="+link+"&platform=com.mxplay.desktop&device-density=2&userid=30bb09af-733a-413b-b8b7-b10348ec2b3d&platform=com.mxplay.mobile&content-languages=hi,en,ta").json()
    chat = await event.get_chat()
    markup = client.build_reply_markup(Button.url("Mx Stream",video_d+A["stream"]['hls']['high']))
    await client.send_message(chat,"Support @SerialCoIn & @urlicupload "+A["title"],buttons=markup)
    print(A)
    print(link)
 
    
client.start()
client.run_until_disconnected()
