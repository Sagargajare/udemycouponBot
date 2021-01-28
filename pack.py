from datetime import datetime

from bs4 import BeautifulSoup as bs, BeautifulSoup
import requests
import re
from telegrambot import telegram
from urllib.parse import unquote
import telepot
from telepot.loop import MessageLoop


class geeksgod():
    def __init__(self, geek_link):
        self.geek_link = geek_link
        self.lin_list = []
        self.coupons = []
        self.udemy_links = []
        self.linkpages = []
        self.cacheurls = []
        self.output = []
        self.main_page()
        self.sub_pages()
        self.cache()
        self.udemy_urls()
        self.message = self.with_coupons()

    def main_page(self):
        proxies = {
            'http': 'http://10.10.1.10:3128',
            'https': 'http://10.10.1.10:1080',
        }

        res = requests.get(self.geek_link)

        res = bs(res.text, 'html.parser')
        res = res.find(class_='td-pb-span8 td-main-content')
        lst = res.find_all(class_='entry-title td-module-title')
        for i in lst:
            try:
                self.lin_list.append(i.a.get('href'))
            except:
                self.lin_list.append("00")

            # print(i.a.get('href'))
        print('main_paged done=', len(self.lin_list))

    def sub_pages(self):
        for i in self.lin_list:
            res = requests.get(i)

            res = bs(res.text, 'html.parser')
            # coupons = res.find( 'elementor-heading-title')
            try:
                lst = res.find(class_='elementor-button-wrapper')
                self.linkpages.append(lst.a.get('href'))
            except:
                self.linkpages.append("00")
            # print(lst.a.get('href'))
            try:
                lst = res.find('p', class_='elementor-heading-title')
                self.coupons.append(lst.get_text())
            except:
                self.coupons.append("00")
            # print(self.coupons)
        print('sub-pages', len(self.coupons))

    def cache(self):
        for i in self.linkpages:

            try:
                res = requests.get(i)

                res = bs(res.text, 'html.parser')
                lst = res.find(id='timerbut')
                self.cacheurls.append(lst.get('href'))
            except:
                self.cacheurls.append('00')
            # print(self.cacheurls)
        print('cache urls', len(self.cacheurls))

    def udemy_urls(self):
        for i in self.cacheurls:
            a = re.findall(
                r"url=(https%3A%2F%2Fwww.udemy.com%2Fcourse%2F[a-zA-Z%0-9-]+)", i)
            try:
                self.udemy_links.append(a[0])
            except:
                self.udemy_links.append("0013")
            # print(a)
        print('udemy_urls', len(self.udemy_links))

    def with_coupons(self):
        for i, j in zip(self.udemy_links, self.coupons):
            try:
                url = unquote(i)

                url = url + f"?couponCode={j}"
                if "??" in url:
                    url = url.replace("??", "?")
                self.output.append(url)
            except:
                print('error ' + i + " " + j)
        print(self.output)
        a = telegram()
        msg, _ = a.messsageProcessor(self.output)
        print(msg)
        return msg


if __name__ == '__main__':
    bot = telepot.Bot("1094348087:AAHUCi3M-jmRCmeiKpsDocaag-HIphSJ9_s")
    a = geeksgod(
        'https://geeksgod.com/category/freecoupons/udemy-courses-free/')
    print("msg==", a.message)
    # -1001469943819 group
    bot.sendMessage('795965225', a.message, parse_mode='HTML')
# class telegram:
#     # def __init__(self,list):
#     #     self.udemy_urls = list
#     #     self.messsageProcessor()
#
#     def lang(self, udemy_url):
#         shorted = self.shorten(udemy_url)
#         x = requests.get(udemy_url)
#         soup = BeautifulSoup(x.text, 'html.parser')
#         # duration = re.findall(r"([ 0-9a-z]+)on-demand video", x.text)
#         for item, title in zip(soup.select("div.clp-lead__element-item:nth-child(2)")[::-1],
#                                soup.select(".clp-lead__title")):
#             language = item.get_text().replace("\n", "", 11)
#             # print(language)
#             if len(language) < 10:
#                 # print(language , duration[0] , str(title.text.replace("\n","")))
#                 return language, str(title.text.replace("\n", "")), shorted
#
#     def shorten(self, l_url):
#         x = requests.get(f'http://sh.st/st/9a210b43aa71289966f00caebe852cab/{l_url}')
#         raw_url = x.url
#         # print(f"raw_url is =  {raw_url}")
#         url = re.findall(r"(http:\/\/gestyy.com\/[a-zA-Z0-9]+)", raw_url)
#         return url[0]
#
#     def messsageProcessor(self, udemy_urls):
#
#         print("process started")
#         dateTimeObj = datetime.now()
#         # get the date object from datetime object
#         dateObj = dateTimeObj.date()
#         date = dateObj.strftime("%b %d %Y ")
#         # print(dateStr)
#         final_mesage = [f"🔰{date}🔰 \n \n"]
#         # lst = re.findall(r"([a-zA-Z0-9?//.:-]+couponCode=[0-9a-zA-Z]+)", msg)
#         # # lst = re.findall(r"([a-zA-Z0-9?//.:-]+Join-@UdemyFree4You&couponCode=[0-9a-zA-Z]+)", msg)
#         for i in udemy_urls:
#             a = self.lang(i)
#
#             if a != None:
#                 code = re.findall(r"couponCode=([a-zA-z0-9-]+)", i)
#                 language, title, Shorten = a
#                 CouponCode = code[0]
#                 msg = f"""<b> 🔰 {title} 🔰 </b>
#     {language}
#     Coupon:- 🔥 <a href="{Shorten}">{CouponCode}</a> 🔥
#     {Shorten}
#
#     """
#                 final_mesage.append(msg)
#                 print(msg)
#         if len(final_mesage) > 1:
#             check = True
#         else:
#             check = False
#
#         lastextened = """ 🔥🔥Steps to open link.🔥🔥
#     1.Click on link
#     2. Deny notification
#     3. Wait for 5 seconds
#     4. Wait until skip ad appears
#     5. Click on skip ad.
#     6.Boom you will be redirected to site \n @udemy_free_course_2020"""
#
#         retuMessage = "".join(final_mesage) + lastextened
#         self.retumessage = retuMessage
#         self.check = check
#         return self.retumessage, self.check
#
#
# # msg = "https://www.udemy.com/course/java-programming-complete-beginner-to-advanced/??couponCode=3048983SSGT"
# #
# # if "??" in msg:
# #     msg = msg.replace("??", "?")
# #
# # print(msg)
# lst = ['https://www.udemy.com/course/content-marketing-strategy-u/?couponCode=CONTENT65',
#        'https://www.udemy.com/course/adobe-photoshop-course-for-complete-beginners/?couponCode=PSD3DAYOFF',
#        'https://www.udemy.com/course/complete-guide-python-django-framework/?couponCode=PYDJ3DOFF',
#        'https://www.udemy.com/course/complete-javascript-for-beginners/?couponCode=JS3DOFF',
#        'https://www.udemy.com/course/complete-codeigniter-course-for-beginners-step-by-step/?couponCode=CI3DOFF',
#        'https://www.udemy.com/course/advanced-microsoft-excel-formulas-functions/?couponCode=EXCEL23',
#        'https://www.udemy.com/course/php-mysql-codeigniter-complete-guide/?couponCode=PICD3DOFF',
#        'https://www.udemy.com/course/fundamentals-of-electrical-and-electronics-engineering/?couponCode=49D1EA45C7D5541AC900',
#        'https://www.udemy.com/course/html5-css3-complete-course-for-beginners/?couponCode=HTCS3DOFF',
#        'https://www.udemy.com/course/crash-course-template-development-and-bootstrap-4-bootcamp/?couponCode=BOOTSTRAP_AND_SASS',
#        'https://www.udemy.com/course/the-complete-python-programmer-from-scratch-to-applications/?couponCode=ECE_LIFE',
#        'https://www.udemy.com/course/arduino-programming-for-absolute-beginners/?couponCode=ECE_LIFE',
#        'https://www.udemy.com/course/the-ai-ceo/?couponCode=77F8E02138277C46EE52',
#        'https://www.udemy.com/course/how-to-create-business-marketing-video/?couponCode=156954057D50C533BF93',
#        'https://www.udemy.com/course/make-money-online-blogging/?couponCode=9B4CCC78E262420E08AB',
#        'https://www.udemy.com/course/java-programming-complete-beginner-to-advanced/?couponCode=3048983SSGT']
# # print(len(lst))
# # a = telegram()
# # msg, _ = a.messsageProcessor(lst)
# # print(msg)
