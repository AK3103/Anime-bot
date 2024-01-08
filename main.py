from pyrogram import Client, filters


API_ID = "23472307"
API_HASH = "15311dad78288ffec031dc8b8b717c21"
BOT_TOKEN ="6946934155:AAFx4VojSkQyTf6sx8lvhbsC8U-2Wb_yEok"

Animelist = Client(
    name="Aniume-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )


  @Aniumelist.on_message(filters.command("start"))
  async def start_cmd(client, message):
      print("START command")


   


  print("Bot has Started")

  Animelist.run() 
 
    
