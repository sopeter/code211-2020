# import all the extensions to be used
from bs4 import BeautifulSoup
import requests
import re
import html5lib
import pandas as pd

# url for the website we are using
URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

# use requests to gain access of the url
r = requests.get(URL)

# put the script of the html into a Soup so users can see the code
soup = BeautifulSoup(r.content, 'html5lib')

# finds every instance of the class "col-sm-4 col-lg-4 col-md-4" since it is the container of every laptop
classSoup = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')

# prints the first soup so that we can base our code for web scraping
print(classSoup[0])

# initalize arrays that we will use
names = []
descriptions = []
prices = []
ratings = []

#for each loop to go through each class one by one
for container in classSoup:

    #finds the tag where the name of the laptop is located
    nameNotDone = container.find('a', attrs = {'class':'title'})

    # retrieves the name of the laptop located in "title"
    name = nameNotDone['title']

    # pushes the name into the array
    names.append(name)

    description = container.find('p', class_ = 'description').text
    descriptions.append(description)
    price = container.find('h4', class_ = 'pull-right price').text
    prices.append(price)

    # finds the location where the ratings are first available
    rating = container.find('p', class_ = '')

    # inside the class, find the subclass called "ratings"
    ratingNotDone = container.find('div', class_ = 'ratings')

    # count the amount of children in this class and subtract by two to get the number of images of stars shown
    ratings.append(len(ratingNotDone.findChildren()) - 2)
print(names)
print(descriptions)
print(prices)
print(ratings)

# using pandas we can create a graph of the our data
test_df = pd.DataFrame({'name': names, 'description': descriptions, 'price': prices, 'rating': ratings})

#prints the info of our dataframe (only viewable in Jupyter Notebook)
print(test_df.info())
test_df

#exports the dataframe into an excel file so that it is viewable
export_excel = test_df.to_excel (r'C:\Users\so4845.D211\Desktop\export_dataframe.xlsx', index = None, header=True)