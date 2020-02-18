# This script scrapes the entirety of Urban Dictionarys' terms, obtained from the 
# /sitemap.xml.gz file.

import re
import urllib
import requests

SITEMAP_INDEX = 'https://www.urbandictionary.com/sitemap.xml.gz'


def main():
    index = requests.get(SITEMAP_INDEX).text

    sitemaps = re.findall(r'sitemap([0-9]+)\.xml\.gz', index)

    for sitemap in sitemaps:
        print 'Downloading %s of %s.' % (sitemap, sitemaps[-1])
        response = requests.get('http://www.urbandictionary.com/sitemap%s.xml.gz' % sitemap).text

        words = re.findall(r'define\.php\?term=(.*?)<\/loc>', response)

        with open('wordlist', 'ab+') as f:
            for word in words:
                f.write(urllib.unquote(word.encode('ascii')) + "\n")


if __name__ == '__main__':
    main()
