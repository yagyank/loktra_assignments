import urllib2
import sys
from bs4 import BeautifulSoup
#keyWord = raw_input("Enter Keyword\n")
if len(sys.argv)<2:
	print 'Invalid input'
elif len(sys.argv)==2:
	keyWord = sys.argv[1]
	page = urllib2.urlopen("http://www.shopping.com/products?KW="+keyWord)
	soup = BeautifulSoup(page,"html.parser")
	span = soup.find_all('span', attrs={'class':'numTotalResults'})
	ind = 0
	str = ""
	for sp in span:
		str = sp.string
		ind = sp.string.index('o')
	#print str[1]
	if(str == ""):
		print 0
	else:
		ind += 3
		res = 0
		len = len(str)
		#print len
		#print str[10]
		#print str[ind]
		while(str[ind]>='0' and str[ind]<='9' and ind<len):
			res = res*10
			res = res + ord(str[ind]) - ord('0')
			ind +=1
			#print str[ind]

		if(str[ind]=='+'):
			print '{}+'.format(res)
		else:
			print res
		#print soup.prettify()
		#print soup.get_text()
		#print soup.findAll(True, {'"numTotalResults"'})
elif len(sys.argv)==3:
	pageNumber = sys.argv[1]
	keyWord = sys.argv[2]
	page = urllib2.urlopen("http://www.shopping.com/products~PG-"+pageNumber+"?KW="+keyWord)
	soup = BeautifulSoup(page,"html.parser")
	span = soup.find_all('a', attrs={'class':'productName'})
	#print span
	if not span:
		print "Wrong keyword or pageNumber entered"
	else:
		for sp in span:
			try:
				print sp['title'].encode('utf-8')
			except KeyError:
				a = sp.find('span')
				try:
					#print a
					print a['title'].encode('utf-8')
				except KeyError:
					print ""
else:
	print 'Invalid Input'