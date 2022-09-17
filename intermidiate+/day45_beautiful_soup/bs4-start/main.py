from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
# print(articles)
article_texts = []
article_links = []
article_upvotes = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))


article_upvotes = [int(article_upvote.getText().strip(" points")) for article_upvote
                   in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)
max_value = max(article_upvotes)
max_index = article_upvotes.index(max_value)

print(f"The {article_texts[max_index]} has the highest number of srore!")





















# with open("website.html") as website:
#     contents = website.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# #
# # print(soup.prettify())
#
# # print(soup.a)
# # print(soup.li)
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# h3_heading = soup.find_all("h3", class_="heading")
# print(h3_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings)