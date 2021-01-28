from datetime import datetime
import re
from pprint import pprint
now = datetime.now()
import telepot
import time
import requests
from bs4 import BeautifulSoup

bot = telepot.Bot("1094348087:AAHcAlaT9k1mQmRwX8JnOzfBehnZHYyw5hQ")
import os
PORT = int(os.environ.get('PORT', 5000))
# import sys
import time
import telepot
from telepot.loop import MessageLoop

def shorten(l_url):
    x = requests.get(f'http://sh.st/st/9a210b43aa71289966f00caebe852cab/{l_url}')
    raw_url = x.url
    # print(f"raw_url is =  {raw_url}")
    url = re.findall(r"(http:\/\/gestyy.com\/[a-zA-Z0-9]+)", raw_url)
    return url[0]


def messsageProcessor(msg):
    print("process started")
    dateTimeObj = datetime.now()
    # get the date object from datetime object
    dateObj = dateTimeObj.date()
    date = dateObj.strftime("%b %d %Y ")
    # print(dateStr)
    final_mesage =  [f"🔰{date}🔰 \n \n"]
    #lst = re.findall(r"([a-zA-Z0-9?//.:-]+couponCode=[0-9a-zA-Z]+)",msg)
    lst = re.findall(r"([a-zA-Z0-9?//.:-]+Join-@UdemyFree4You&couponCode=[0-9a-zA-Z]+)", msg)
    for i in lst:
        a = lang(i)

        if a != None:
            code = re.findall(r"couponCode=([a-zA-z0-9-]+)", i)
            language, title , Shorten= a
            CouponCode = code[0]
            msg = f"""<b> 🔰 {title} 🔰 </b>
{language}
Coupon:- 🔥 <a href="{Shorten}">{CouponCode}</a> 🔥
{Shorten}

"""
            final_mesage.append(msg)
            print(msg)
    if len(final_mesage) > 1:
        check = True
    else:
        check = False

    lastextened = """ 🔥🔥Steps to open link.🔥🔥
1.Click on link
2. Deny notification
3. Wait for 5 seconds
4. Wait until skip ad appears
5. Click on skip ad.
6.Boom you will be redirected to site \n @udemy_free_course_2020"""

    retuMessage = "".join(final_mesage) + lastextened
    return retuMessage , check


def lang(udemy_url):
    shorted = shorten(udemy_url)
    x = requests.get(udemy_url)
    soup = BeautifulSoup(x.text, 'html.parser')
    # duration = re.findall(r"([ 0-9a-z]+)on-demand video", x.text)
    for item, title in zip(soup.select("div.clp-lead__element-item:nth-child(2)")[::-1],soup.select(".clp-lead__title")):
        language = item.get_text().replace("\n", "", 11)
        # print(language)
        if len(language) < 10:
            # print(language , duration[0] , str(title.text.replace("\n","")))
            return language ,  str(title.text.replace("\n","")) , shorted



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    reply , check = messsageProcessor(msg["text"])
    print(msg)
    print(msg["text"])
    if str(chat_id) == "795965225":
        bot.sendMessage(chat_id, "working xyz Message Sent", parse_mode='HTML')
    elif "-" in str(chat_id):
        bot.sendMessage("795965225", f"Message Posted On Channel by {chat_id}", parse_mode='HTML')


    else:
        bot.sendMessage(chat_id, "You are not Admin", parse_mode='HTML')
        bot.sendMessage("795965225", "Someone trying to use bot", parse_mode='HTML')



    if check:
        bot.sendMessage("-1001469943819", reply ,parse_mode='HTML')

# TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot("1094348087:AAHcAlaT9k1mQmRwX8JnOzfBehnZHYyw5hQ")

MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')


while 1:
    time.sleep(2)



if __name__ == '__main__':
    time.sleep(3)
    main()