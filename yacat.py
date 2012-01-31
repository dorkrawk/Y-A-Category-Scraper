'''
Y!A Category Scraper

- Scrape Yahoo! Answers Category Names and IDs
- Currently outputs contents for a PHP array in the form: "Category Name" => id#
- Modify the output as you see fit

'''

from BeautifulSoup import BeautifulSoup
import urllib2

def print_array_stuff(p_cat_id):
	
	url_of_cat = "http://answers.yahoo.com/dir/index;_ylt=AkHAbu8Qmg2YzCQ1VEQ.7Kye5HNG;_ylv=3?sid=" + p_cat_id
	
	req = urllib2.Request(url_of_cat)
	res = urllib2.urlopen(req)
	the_page = res.read()
	
	soup = BeautifulSoup(the_page)
	cat_div = soup.findAll("div", {"class": "bd"})
	links = cat_div[0].findAll("a");
	
	for link in links:
		the_url = link["href"]
		id_start = the_url.find("=") + 1
		the_id = the_url[id_start:]
		the_cat = link.contents[0]
		print '"{0}" => {1},'.format(the_cat,the_id)
	
	

def main():
	url_of_page = "http://answers.yahoo.com/dir/index;_ylt=AgashJEG65jtuqrBEQXEhT.g5HNG;_ylv=3" 
	
	req = urllib2.Request(url_of_page)
	res = urllib2.urlopen(req)
	the_page = res.read()
	
	soup = BeautifulSoup(the_page)
	cat_div = soup.findAll("div", {"class": "bd"})
	links = cat_div[0].findAll("a");
	
	for link in links:
		the_url = link["href"]
		id_start = the_url.find("=") + 1
		the_id = the_url[id_start:]
		print_array_stuff(the_id)

		
if __name__ == '__main__':
	main()