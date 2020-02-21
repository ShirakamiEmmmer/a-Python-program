from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

son_html = urlopen('https://www.youtube.com/watch?v=cXP8OxMN_SQ').read().decode('utf-8')
son_soup = BeautifulSoup(son_html, 'lxml')

for title in son_soup.find_all('h1'):
    print(title)

m = re.search('(?<=v=)...........', 'https://www.youtube.com/watch?v=cXP8OxMN_SQ')
m.group(0)
print(m.group(0))

# ok_all_info = son_soup
# for i in ok_all_info:
#         if (len(i))<100:
#             son_soup.remove(i)

# for info in son_soup:
#     print(info)
#     print('\n')
