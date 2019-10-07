from pyrogram import Client, Filters

app = Client("session",bot_token="511016924:AAHHmS_NafrmUawma9PpfRueQUEFAOY7BJw",api_id=715451,api_hash="d2cba6f7bf5d1a45682da5bb9071a307")

@app.on_message(Filters.private)
def main(client, message):
 client.send_message(message.chat.id,""" I am not working currently. 

Use @Cfadmin_bot for now.

this is my alternative bot.

Feel free to use 😘☺️""")
 

app.run()
