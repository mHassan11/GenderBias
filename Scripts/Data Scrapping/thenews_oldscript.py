import os
# import calender

# url = "e.thenews.com.pk/lahore/6-27-2019/mainpage/page1.jpg"
# os.system("wget "+url+ " -r -l 1 -k -k -E -w 0.1")
# print(url)

# url = "e.thenews.com.pk/lahore/6-27-2019/mainpage/page200.jpg"
# os.system("wget "+url+ " -r -l 1 -k -k -E -w 0.1")
# print(url)


# url = "e.thenews.com.pk/lahore/6-26-2019/mainpage/page1.jpg"
# os.system("wget "+url+ " -r -l 1 -k -k -E -w 0.1")
# print(url)

month = input("Which month (digital)? ")
year = input("Which year (digit)? ")
start_date = input("What is the starting date (digit)? ")
end_date = input("What is the last date (digits)? ")

start_date = int(start_date)
end_date = int(end_date)

for day in range(start_date,end_date+1):
	for page_num in range(1,30):
		
		url = "e.thenews.com.pk/lahore/"+str(month)+"-"+str(day)+"-"+str(year)+"/mainpage/page"+str(page_num)+".jpg"
		os.system("wget "+url+ " -r -l 1 -k -k -E -w 0.1")
		print(url)

	

# for x in xrange(1,50):
	
# 	# url = "learnyouahaskell.com"
# 	url = "http://e.thenews.com.pk/lahore/6-27-2019/page"+str(x)+".asp"
# 	os.system("wget "+url+ " -r -l 1 -k -k -E -w 0.1")
# 	print(url)
