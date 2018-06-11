from bs4 import BeautifulSoup
import urllib.request

URL = "https://www.tripadvisor.com.au/Restaurants-g255068-c8-Brisbane_Brisbane_Region_Queensland.html"

def get_info(link):
    response = urllib.request.urlopen(link)
    soup = BeautifulSoup(response.read(),"lxml")
    for items in soup.find_all(class_="shortSellDetails"):
        name = items.find(class_="property_title").get_text(strip=True)
        bubble = items.find(class_="ui_bubble_rating").get("alt")
        review = items.find(class_="reviewCount").get_text(strip=True)
        print(name,bubble,review)

if __name__ == '__main__':
    get_info(URL)
