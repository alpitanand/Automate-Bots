import os
import bs4
import requests
url = 'http://www.quickmeme.com'
if not os.path.exists("D://Meme"):
    os.makedirs("D://Meme")
while not url.endswith('/100/'):
    print('Downloading from page {}'.format(url))
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print(exc)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comic = soup.select('img[class="post-image"]')
    if not comic:
        print('Can not find meme')
    else:
        for i in range(len(comic)):
            comicUrl = comic[i].get('src')
            print("Downloading "+comicUrl)
            res = requests.get(comicUrl)
            with open(os.path.join('D://Meme', os.path.basename(comicUrl)), 'wb') as ImageFile:
                for chunk in res.iter_content(100000):
                    ImageFile.write(chunk)
    nextLink = soup.select('a[id=""page-next]')[0]
    url = url + nextLink.get('href')
