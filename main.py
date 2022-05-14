# example python script that generates a table in markdown and saves it as table.md
from tomark import Tomark
import requests

response = requests.get(
    'https://api.github.com/repos/matyifkbt/github-actions-md/issues?state=all&direction=asc')
data = response.json()
parsed_data = [{
    'issue #': f'#{issue["number"]}',
    'title': issue['title'],
    'state':issue['state'],
    'age': f'https://img.shields.io/github/issues/detail/age/matyifkbt/github-actions-md/{issue["number"]}'
} for issue in data]

markdown = Tomark.table(parsed_data)

with open('table.md', 'w') as f:
    print(markdown, file=f)
