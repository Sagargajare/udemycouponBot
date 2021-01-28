from telebot import TeleBot

app = TeleBot(__name__)


@app.route('/command ?(.*)')
def example_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "Command Recieved: {}".format(cmd)

    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
   chat_dest = message['chat']['id']
   user_msg = message['text']
   print(user_msg)
   # if chat_id == 795965225 and msg['text'] == '/start':
   #     print("verified")
   #     bot.sendMessage(chat_id, "Processing Started", parse_mode='HTML')
   #     a = geeksgod('https://geeksgod.com/category/freecoupons/udemy-courses-free/')
   #     bot.sendMessage(chat_id, a.message, parse_mode='HTML')
   # elif "-" in str(chat_id):
   #     bot.sendMessage("795965225", f"Message Posted On Channel by {chat_id}", parse_mode='HTML')
   # else:
   #     bot.sendMessage(chat_id, "You are not Admin", parse_mode='HTML')
   #     bot.sendMessage("795965225", "Someone trying to use bot", parse_mode='HTML')


   msg = "Parrot Says: {}".format(user_msg)
   app.send_message(chat_dest, msg,parse_mode='HTML')


if __name__ == '__main__':
    app.config['api_key'] = '1094348087:AAHcAlaT9k1mQmRwX8JnOzfBehnZHYyw5hQ'
    app.poll(debug=True)
