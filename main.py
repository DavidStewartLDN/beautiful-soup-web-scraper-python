import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# This provides us with the entire results container
results = soup.find(id="ResultsContainer")

# This creates an iterable containing all the HTML for all the job listings displayed on that page.
job_elems = results.find_all('section', class_='card-content')

# print(results.prettify())

# Iterate to show each element of Beuatiful Soup list
# and return the items we are interested in

for job_elem in job_elems:
  # Each job_elem is a new BeautifulSoup object.
  # we can use the same methods on it as we did before.
  title_elem = job_elem.find('h2', class_='title')
  company_elem = job_elem.find('div', class_='company')
  location_elem = job_elem.find('div', class_='location')
  # Skip to next element in job_elems if any of above variables return None type.
  if None in (title_elem, company_elem, location_elem):
    continue
  print(title_elem.text.strip())
  print(company_elem.text.strip())
  print(location_elem.text.strip())
  print()

