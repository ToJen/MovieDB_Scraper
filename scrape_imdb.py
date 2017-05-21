import csv, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('../Solve 2048/assets/chromedriver')
driver.get('http://imdb.com/chart/top')


def get_elements(list_element):
	elems = []
	for elem in list_element:
		elems.append(elem.text)
	return elems

"""
shallow scrape:
	name, year, movie_ratings			# use webbrowser or bs4 instead?
"""
def shallow_scrape():
	print('Starting shallow scrape...')

	movie_names = driver.find_elements_by_css_selector('td.titleColumn > a')
	movie_years = driver.find_elements_by_class_name('secondaryInfo')
	movie_ratings = driver.find_elements_by_css_selector('td.imdbRating > strong')

	outputFile = open('movie_details_shallow.csv', 'w', newline='')
	outputWriter = csv.writer(outputFile)
	outputWriter.writerow(['Name', 'Release Year', 'Rating'])

	for name, year, rating in zip(movie_names, movie_years, movie_ratings):
		outputWriter.writerow([name.text, year.text, rating.text])

	outputFile.close()
	# driver.close()

"""
deep scrape:
	name, rating, genre, year, cast, rating count, country, language, release date, 
	box office budget, box office gross, runtime, color, director, writer, stars
"""
def deep_scrape():
	print('Starting deep scrape...')

	movie_details = []	# temp list before writing to csv file

	movie_link = driver.find_element_by_css_selector('td.titleColumn > a')
	movie_link.click()

	name = driver.find_element_by_css_selector('div.title_wrapper > h1')
	rating = driver.find_element_by_css_selector('div.ratingValue > strong')
	# content_rating = driver.find_element_by_css_selector('div.title_wrapper > div.subtext > #text')
	# content_rating = driver.find_element_by_xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/div/meta[@itemprop="contentRating"]')
	# content_rating = driver.find_element_by_xpath('//meta[@itemprop="contentRating"]@content')
	runtime = driver.find_element_by_css_selector('div.title_wrapper > div.subtext > time')
	genre = driver.find_elements_by_css_selector('div.title_wrapper > div.subtext > a > span.itemprop')

	movie_details.append(name.text)
	movie_details.append(rating.text)
	# movie_details.append(content_rating.get_attribute('content'))
	# movie_details.append(content_rating.text)
	movie_details.append(runtime.text)
	movie_details.append(get_elements(genre))

	print(movie_details)

	driver.close()


# shallow_scrape()
deep_scrape()