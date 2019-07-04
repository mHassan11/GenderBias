# r = requests.get('https://e.dawn.com/2019/06/28/pages/28_06_2019_001.html')
# this script is hardcoded for 28th of june, you will modify it in such a way that it will take
# a month and year,a nd will run this code for that entire month.
from bs4 import BeautifulSoup
import requests
import re
import os

start_page = 1
end_page = 183
# the start and end pages are hardcoded as of now, you will find the maximum page for a day and 
# edit the maximum page of a day
for page_num in range(start_page,end_page+1):

	if(0<page_num<10):
		page_num = str(page_num)
		page_num = "00"+page_num
	elif(10<page_num<100):
		page_num = str(page_num)
		page_num = "0"+page_num
	else:
		page_num = str(page_num)

	# CHANGE URL HERE
	r = requests.get('https://e.dawn.com/2019/06/28/pages/28_06_2019_'+page_num+'.html')
	url = 'https://e.dawn.com/2019/06/28/pages/28_06_2019_'+page_num+'.html'
	os.system("wget "+url+" -r -l 1 -k -k -E -w 0.1")
	print(url)


	soup = BeautifulSoup(r.text, 'html.parser')


	a = soup.find_all('area')


	advt = []
	story = []
	for i in a:
	    tag = str(i)
	    match = re.search('[0-9]+_[0-9]+_[0-9]+_[0-9]+_[0-9]+', tag).group()
	    if 'DetailNews' in tag:
	        story.append(match)
	    else:
	        advt.append(match)

	for s in story:
	    r = requests.get(f'https://epaper.dawn.com/DetailNews.php?StoryText={s}')
	    soup = BeautifulSoup(r.text, 'html.parser')
	    imgs = soup.find('td', attrs={'class':'palm-detail-news'}).find_all('img')
	    for i in imgs:
	        print(i['src'])
	        url = i['src']
	        os.system("wget "+url+ " -r -l 1 -k -k -E -w 0.1")
	        print(url)

	for a in advt:
	    r = requests.get(f'https://epaper.dawn.com/Advt.php?StoryImage={a}')
	    soup = BeautifulSoup(r.text, 'html.parser')
	    imgs = soup.find('div', attrs={'class':'story-container'}).find_all('img')
	    for i in imgs:
	        print(i['src'])
	        url = i['src']
	        os.system("wget "+url+ " -r -l 1 -k -k -E -w 0.1")
	        print(url)

