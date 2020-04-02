import csv
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def run():
	url = input("Please enter a valid URL: ")

	if not url:
		url = "https://summerofcode.withgoogle.com/archive/2019/projects/"

	data = []

	page_data, next_link = request_url_and_extract_data(url)
	data += page_data

	while next_link:
		page_data, next_link = request_url_and_extract_data(next_link)
		data += page_data

	with open('output.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile,
			fieldnames=['name', 'organization', 'project'])

		if data:
			writer.writeheader()
			writer.writerows(data)

def request_url_and_extract_data(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	next_link = soup.find("a", class_="md-button", string="Next")
	next_link = next_link.get('href') if next_link else None
	next_link = urljoin(url, next_link) if next_link else None

	header_elements = soup.find_all("div", class_="archive-project-card__header")
	data = []

	for element in header_elements:
		data.append(extract_info(element))

	return data, next_link

def extract_info(element):
	info = {}
	info['name'] = element.find(
		"h4", class_="archive-project-card__student-name").get_text(strip=True)

	divs =  element.find_all("div")
	for div in divs:
		if "Organization" in div.string:
			div_text = div.get_text(strip=True)
			info["organization"] = div_text.split(": ")[-1]
		else:
			info["project"] = div.get_text(strip=True)

	return info


if __name__ == "__main__":
	run()