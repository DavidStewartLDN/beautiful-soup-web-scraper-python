import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# This provides us with the entire results container
results = soup.find(id="ResultsContainer")

# This creates an iterable containing all the HTML for all the job listings displayed on that page.
job_elems = results.find_all('section', class_='card_content')

print(results.prettify())

# Iterate to show each element of Beuatiful Soup list
for job_elem in job_elems:
  print(job_elem, end='\n'*2)
