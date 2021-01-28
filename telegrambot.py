from datetime import datetime

from bs4 import BeautifulSoup
import requests
import re
from urllib.parse import unquote


class telegram:
    # def __init__(self,list):
    #     self.udemy_urls = list
    #     self.messsageProcessor()

    def lang(self, udemy_url):
        try:
            shorted = self.shorten(udemy_url)
            x = requests.get(udemy_url)
            soup = BeautifulSoup(x.text, 'html.parser')
            # duration = re.findall(r"([ 0-9a-z]+)on-demand video", x.text)
            for item, title in zip(soup.select("div.clp-lead__element-item:nth-child(2)")[::-1],
                                   soup.select(".clp-lead__title")):
                language = item.get_text().replace("\n", "", 11)
                # print(language)
                if len(language) < 10:
                    # print(language , duration[0] , str(title.text.replace("\n","")))
                    return language, str(title.text.replace("\n", "")), shorted
        except :
            return 'English',' Affiliate Marketing Domination: Become A Super Affiliate ','http://gestyy.com/ew77Lx'

    def shorten(self, l_url):
        # headers = {
        #     'public-api-token': '9a210b43aa71289966f00caebe852cab',
        # }
        #
        # data = {
        #     'urlToShorten': f'{l_url}'
        # }
        # try:
        #     response = requests.put('https://api.shorte.st/v1/data/url', headers=headers, data=data)
        #
        #     # response = {'status': 'ok', 'shortenedUrl': 'http://gestyy.com/ew6bxs'}
        #     response =response.json()
        #     url =response['shortenedUrl']
        # except :
        #     print("error ",l_url)
        #     url = ['errorlink']
        # # print(f"raw_url is =  {raw_url}")

        return l_url

    def messsageProcessor(self, udemy_urls):

        print("process started")
        dateTimeObj = datetime.now()
        # get the date object from datetime object
        dateObj = dateTimeObj.date()
        date = dateObj.strftime("%b %d %Y ")
        # print(dateStr)
        final_mesage = [f"🔰{date}🔰 \n \n"]
        # lst = re.findall(r"([a-zA-Z0-9?//.:-]+couponCode=[0-9a-zA-Z]+)", msg)
        # # lst = re.findall(r"([a-zA-Z0-9?//.:-]+Join-@UdemyFree4You&couponCode=[0-9a-zA-Z]+)", msg)
        for i in udemy_urls:
            a = self.lang(i)

            if a != None and a!=('English',' Affiliate Marketing Domination: Become A Super Affiliate ','http://gestyy.com/ew77Lx'):
                code = re.findall(r"couponCode=([a-zA-z0-9-]+)", i)
                language, title, Shorten = a
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

    #     lastextened = """ 🔥🔥Steps to open link.🔥🔥
    # 1.Click on link
    # 2. Deny notification
    # 3. Wait for 5 seconds
    # 4. Wait until skip ad appears
    # 5. Click on skip ad.
    # 6.Boom you will be redirected to site \n @udemy_free_course_2020"""
        lastextened = """ \n @udemy_free_course_2020"""

        retuMessage = "".join(final_mesage) + lastextened
        self.retumessage = retuMessage
        self.check = check
        return self.retumessage, self.check
