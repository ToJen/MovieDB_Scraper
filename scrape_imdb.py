import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('../Solve 2048/assets/chromedriver')
driver.get('http://imdb.com/chart/top')

# movie_details = driver.find_elements_by_css_selector('table.chart > tbody.lister-list > tr')
# print(type(movie_details))

# movies = driver.find_elements_by_css_selector('.titleColumn > a')
# for movie in movies:
# 	# print(movie.text, "\t" , movie.get_attribute("href"))
# 	print(movie.text, "\t" , )

"""
shallow scrape:
	name, year, rating
"""
movie_names = driver.find_elements_by_css_selector('td.titleColumn > a')
movie_years = driver.find_elements_by_class_name('secondaryInfo')
movie_ratings = driver.find_elements_by_css_selector('td.imdbRating > strong')

with open('movie_details.csv', 'w') as csvfile:

for name, year, rating in zip(movie_names, movie_years, movie_ratings):
	movie_details = '{:<20} {:>10} {:>20}'.format(name.text, year.text, rating.text)
	# print(name.text, "\t\t", year.text, "\t\t", rating.text)
	print(movie_details)

"""
deep scrape:
	name, rating, genre, year, cast, rating count, country, language, release date, 
	box office budget, box office gross, runtime, color, director, writer, stars
"""
