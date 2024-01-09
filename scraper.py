import requests
import brotli
from bs4 import BeautifulSoup

""""
A script that will scrape all the
flashcard data from securityplus.training
"""
# get address to scrape
addr = "https://securityplus.training/flashcard/flashcard-a/"

# create headers to avoid 403 error(s)
headers = {
'Cookie':'cookielawinfo-checkbox-necessary=yes;cookielawinfo-checkbox-functional=yes;cookielawinfo-checkbox-performance=yes;cookielawinfo-checkbox-analytics=yes;cookielawinfo-checkbox-advertisement=yes;cookielawinfo-checkbox-others=yes;_hp2_id.34805961=%7B%22userId%22%3A%227080190327956199%22%2C%22pageviewId%22%3A%224701798593631841%22%2C%22sessionId%22%3A%222339352691092148%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D;userty.core.s.f5cc77=__WQiOiIzYzE1N2JhMTc4NzIxNDZlNzE4MmI5NjFkM2I0M2E0MyIsInN0IjoxNzA0NzQxODAyODgyLCJyZWFkeSI6dHJ1ZSwid3MiOiJ7XCJ3XCI6MTUzNixcImhcIjo3MTF9Iiwic2UiOjE3MDQ3NDU3MjQ5MDIsInB2Ijo0fQ==eyJza;userty.core.p.f5cc77=__2VySWQiOiI0ZWNjZTkyZjNhMzJlYTBiMmJjMTg3ZTM2NDJlZWMyOSJ9eyJ1c;viewed_cookie_policy=yes;cli_user_preference=en-cli-yes-checkbox-necessary-yes-checkbox-functional-yes-checkbox-performance-yes-checkbox-analytics-yes-checkbox-advertisement-yes-checkbox-others-yes;CookieLawInfoConsent=eyJ2ZXIiOiIxIiwibmVjZXNzYXJ5IjoidHJ1ZSIsImZ1bmN0aW9uYWwiOiJ0cnVlIiwicGVyZm9ybWFuY2UiOiJ0cnVlIiwiYW5hbHl0aWNzIjoidHJ1ZSIsImFkdmVydGlzZW1lbnQiOiJ0cnVlIiwib3RoZXJzIjoidHJ1ZSJ9;_ga_BBZGHCXQKP=GS1.1.1704741801.3.1.1704741821.0.0.0;_ga=GA1.2.2059446125.1704681357;_gid=GA1.2.1436906423.1704681357',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://securityplus.training/flashcard/flashcard-e/',
'Upgrade-Insecure-Requests': '1',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-User': '?1',
'Te': 'trailers',
'Connection': 'close',
}

#blah...
response = requests.get(addr, headers=headers)
url = BeautifulSoup(response.text, "html.parser")

#create dictionary of cards
cards = {}

questions = url.findAll('div', {'class':'card_question'})
answers = url.findAll('div', {'class':'card_answer'})

#add answers and questions to dictionary
for i in range(len(questions)):
    question = questions[i].text
    answer = answers[i].text
    cards[question] = answer

for question, answer in cards.items():
    print(question, "\n", answer)
    print("\n")


"""""
for question in questions:
    print(question.text)

print("*******************************************************")
print("*******************************************************")

for answer in answers:
    print(answer.text)

"""""


