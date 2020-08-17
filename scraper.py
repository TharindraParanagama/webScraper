import requests
from bs4 import BeautifulSoup

content = requests.get("https://towardsdatascience.com/@fneves")
parsablePage = BeautifulSoup(content.text, "html.parser")
author = parsablePage.h1
profession = parsablePage.p
articles = parsablePage.findAll(
    "h3", class_="graf graf--h3 graf-after--figure graf--title"
)
claps = parsablePage.findAll(
    "button",
    class_="button button--chromeless u-baseColor--buttonNormal js-multirecommendCountButton u-disablePointerEvents",
)

print("Author: " + author.get_text() + "\n")
print("Profession: " + profession.get_text().split(",")[0] + "\n")

for i in range(0, len(articles)):
    print("article: " + articles[i].get_text() + " claps:" + claps[i].get_text())
