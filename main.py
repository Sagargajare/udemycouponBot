from datetime import datetime


now = datetime.now()
import telepot


bot = telepot.Bot("1094348087:AAHUCi3M-jmRCmeiKpsDocaag-HIphSJ9_s")
import os
from pack import geeksgod

# PORT = int(os.environ.get('PORT', 5000))
# import sys
import time
import telepot
from telepot.loop import MessageLoop


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    print(msg['text'], '  chat_id== ', chat_id)
    if chat_id == 795965225 and msg['text'] == '/start':
        print("verified")
        bot.sendMessage(chat_id, "Processing Started", parse_mode='HTML')
        a = geeksgod('https://geeksgod.com/category/freecoupons/udemy-courses-free/')
        bot.sendMessage(chat_id, a.message, parse_mode='HTML')
    elif "-" in str(chat_id):
        bot.sendMessage("795965225", f"Message Posted On Channel by {chat_id}", parse_mode='HTML')
    else:
        bot.sendMessage(chat_id, "You are not Admin", parse_mode='HTML')
        bot.sendMessage("795965225", "Someone trying to use bot", parse_mode='HTML')

        # reply = a.message
    # print(msg)
    # print(msg["text"])
    # if str(chat_id) == "795965225":
    #     bot.sendMessage(chat_id, "working xyz Message Sent", parse_mode='HTML')
    # elif "-" in str(chat_id):
    #     bot.sendMessage("795965225", f"Message Posted On Channel by {chat_id}", parse_mode='HTML')
    #
    #
    # else:
    #     bot.sendMessage(chat_id, "You are not Admin", parse_mode='HTML')
    #     bot.sendMessage("795965225", "Someone trying to use bot", parse_mode='HTML')
    #
    # if check:
    #     bot.sendMessage("-1001469943819", reply, parse_mode='HTML')


# TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot("1094348087:AAHUCi3M-jmRCmeiKpsDocaag-HIphSJ9_s")

MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(2)

if __name__ == '__main__':
    time.sleep(3)
    main()
