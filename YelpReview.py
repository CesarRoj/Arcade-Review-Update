import requests
from bs4 import BeautifulSoup

URL = "https://www.yelp.com/biz/arcade-downtown-riverside-2?sort_by=date_desc"

page = requests.get(URL)



soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id = "reviews")

reviews = results.find_all("li", class_= "margin-b5__09f24__pTvws border-color--default__09f24__NPAKY")

for review in reviews:
    userRating = review.find("div", class_= "five-stars__09f24__mBKym five-stars--regular__09f24__DgBNj display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY")
    print(userRating)["aria-label"]
    