from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN =""

Animelist = Client(
    name="Aniume-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )  


  print("Bot has Started")

  Animelist.run() 
 
    
