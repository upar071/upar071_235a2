import csv
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import ssl

row_names = ['movie_id', 'movie_title']
with open("Data1000MoviesWithPics.csv", encoding='utf-8-sig') as infile:
    reader = csv.reader(infile)
    next(infile)
    for row in reader:
        movie_id = row[0]
        movie_title = row[1]
        domain = 'http://www.imdb.com'
        search_url = domain + '/find?q=' + urllib.parse.quote_plus(movie_title)
        #print(search_url)
        gcontext = ssl.SSLContext()
        with urllib.request.urlopen(search_url, context=gcontext) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            # Get url of 1st search result
            try:
                title = soup.find('table', class_='findList').tr.a['href']
                movie_url = domain + title
                with open('movie_url.csv', 'a', newline='') as out_csv:
                    writer = csv.writer(out_csv, delimiter=',')
                    writer.writerow([movie_id, movie_url])
            # Ignore cases where search returns no results
            except AttributeError:
                pass
