from bs4 import BeautifulSoup as bs
import requests
import re
from urllib.parse import unquote


#
res = requests.get("https://geeksgod.com/category/freecoupons/udemy-courses-free/")

res = bs(res.text,'html.parser')
res = res.find(class_='td-pb-span8 td-main-content')
lst = res.find_all(class_='entry-title td-module-title')
lin = []
for i in lst:
  lin.append(i.a.get('href'))
  print(i.a.get('href'))
print(len(lin))
lin_lst = ['https://geeksgod.com/udemy-free-course/content-marketing-strategy-techniques-beginner-to-expert/',
           'https://geeksgod.com/udemy-free-course/adobe-photoshop-course-the-complete-guide-step-by-step/',
           'https://geeksgod.com/udemy-free-course/python-django-framework-course-the-complete-guide/',
           'https://geeksgod.com/udemy-free-course/javascript-course-complete-guide-step-by-step/',
           'https://geeksgod.com/udemy-free-course/codeigniter-course-the-complete-guide-step-by-step/',
           'https://geeksgod.com/udemy-free-course/advanced-microsoft-excel-formulas-functions-course-2020/',
           'https://geeksgod.com/udemy-free-course/php-mysql-codeigniter-course-complete-guide/',
           'https://geeksgod.com/udemy-free-course/fundamentals-of-electrical-and-electronics/',
           'https://geeksgod.com/udemy-free-course/html5-css3-course-the-complete-guide-step-by-step/',
           'https://geeksgod.com/udemy-free-course/crash-course-template-development-and-bootstrap-4-bootcamp/',
           'https://geeksgod.com/udemy-free-course/the-complete-python-programmer-from-scratch-to-applications/',
           'https://geeksgod.com/udemy-free-course/arduino-programming-for-absolute-beginners/',
           'https://geeksgod.com/udemy-free-course/ai-for-ceos/',
           'https://geeksgod.com/udemy-free-course/how-to-create-stunning-marketing-video-using-freepaid-tools/',
           'https://geeksgod.com/udemy-free-course/learn-4-steps-to-make-money-online-by-blogging/',
           'https://geeksgod.com/udemy-free-course/java-programming-complete-beginner-to-advanced-2/', 'https://geeksgod.com/cisco-is-hiring-data-engineer/', 'https://geeksgod.com/hewlett-packard-enterprise-is-hiring-software-engineer/', 'https://geeksgod.com/byjus-is-hiring-business-development-associate-bda/', 'https://geeksgod.com/bentley-systems-hiring-associate-software-quality-analyst/', 'https://geeksgod.com/qualcomm-hiring-software-engineer-associate/', 'https://geeksgod.com/udemy-free-course/learn-excel-from-beginner-to-advance-with-example/', 'https://geeksgod.com/ibm-is-hiring-technical-support-associate/', 'https://geeksgod.com/udemy-free-course/content-marketing-strategy-techniques-beginner-to-expert/', 'https://geeksgod.com/udemy-free-course/adobe-photoshop-course-the-complete-guide-step-by-step/', 'https://geeksgod.com/udemy-free-course/python-django-framework-course-the-complete-guide/', 'https://geeksgod.com/udemy-free-course/javascript-course-complete-guide-step-by-step/', 'https://geeksgod.com/udemy-free-course/codeigniter-course-the-complete-guide-step-by-step/', 'https://geeksgod.com/udemy-free-course/advanced-microsoft-excel-formulas-functions-course-2020/', 'https://geeksgod.com/udemy-free-course/php-mysql-codeigniter-course-complete-guide/', 'https://geeksgod.com/philips-is-hiring-internsinternship-drives-2020/', 'https://geeksgod.com/toyota-motors-limited-off-campus-drive-2020-recruitment-drive/', 'https://geeksgod.com/ibm-off-campus-drive-2020/', 'https://geeksgod.com/udemy-free-course/java-programming-complete-beginner-to-advanced-2/', 'https://geeksgod.com/udemy-free-course/python-bootcamp-2020-build-15-working-applications-and-games-2/']

#elementor-button-wrapper -> a -> href
# link_page=['https://geeksgod.com/link-page/17823/', 'https://geeksgod.com/link-page/24949/', 'https://geeksgod.com/link-page/24946/', 'https://geeksgod.com/link-page/24943/', 'https://geeksgod.com/link-page/24940/']
#p.elementor-heading-title
# for i in lin_lst[:5]:
#     res = requests.get(i)
# 
#     res = bs(res.text,'html.parser')
#     lst = res.find( 'p', class_='elementor-heading-title')
#     print(lst.get_text())

# id = = timerbut

# urls =['https://click.linksynergy.com/deeplink?id=KLBDeI3Y*Vs&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fcontent-marketing-strategy-u%2F%3F', 'https://click.linksynergy.com/deeplink?id=KLBDeI3Y*Vs&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fadobe-photoshop-course-for-complete-beginners%2F', 'https://click.linksynergy.com/deeplink?id=KLBDeI3Y*Vs&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fcomplete-guide-python-django-framework%2F', 'https://click.linksynergy.com/deeplink?id=KLBDeI3Y*Vs&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fcomplete-javascript-for-beginners%2F', 'https://click.linksynergy.com/deeplink?id=KLBDeI3Y*Vs&mid=39197&murl=https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fcomplete-codeigniter-course-for-beginners-step-by-step%2F']

# for i in link_page[:5]:
#     res = requests.get(i)
#
#     res = bs(res.text,'html.parser')
#     lst = res.find(id='timerbut')
#     urls.append(lst.get('href'))
#     print(lst.get('href'))
# udemy_links = ['https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fcontent-marketing-strategy-u%2F%3F', 'https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fadobe-photoshop-course-for-complete-beginners%2F', 'https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fcomplete-guide-python-django-framework%2F', 'https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fcomplete-javascript-for-beginners%2F', 'https%3A%2F%2Fwww.udemy.com%2Fcourse%2Fcomplete-codeigniter-course-for-beginners-step-by-step%2F']

# for i in urls:
#   a=re.findall(r"url=(https%3A%2F%2Fwww.udemy.com%2Fcourse%2F[a-zA-Z%0-9-]+)",i)
#   udemy_links.append(a[0])

# print(udemy_links)
# for i in udemy_links:
#   url = unquote(i)
#   print(url)

