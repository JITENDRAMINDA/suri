from pyrogram import Client, Filters


@app.on_message(Filters.private)
def main(client, message):
 client.send_message(message.chat.id,""" I am not working currently. 

Use @Cfadmin_bot for now.

this is my alternative bot.

Feel free to use 😘☺️""")
 

app.run()
