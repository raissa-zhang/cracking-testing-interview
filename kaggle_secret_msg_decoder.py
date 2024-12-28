import requests
from bs4 import BeautifulSoup

# The url for this problem
# https://www.kaggle.com/code/nickalden/secret-msg-decoder/notebook
# When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.


def fetch_content(google_url):
    content_web_request = requests.get(google_url)

    if content_web_request.status_code != 200:
        raise ValueError(f'Could not retrieve data :{content_web_request.status_code}')

    # get the content of this page
    html_content = content_web_request.text

    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.find_all('tr')[1:]

    max_x = 0
    max_y = 0
    # store the x,y and char
    position_map = []
    for row in rows:
        columns = row.find_all('td')
        x = columns[0].text.strip()
        char = columns[1].text.strip()
        y = columns[2].text.strip()

        if int(x) > max_x:
            max_x = int(x)

        if int(y) > max_y:
            max_y = int(y)

        position_map.append((int(x), int(y), char))

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for item in position_map:
        grid[int(item[1])][int(item[0])] = item[2]

    print('****the original grid****')
    for row in grid:
        print(''.join(row))

    # the coordinates(0, 0) is correspond to the corner of [0,2], so we need to reverse the grid

    print('****the reversed grid****')

    for row in reversed(grid):
        print(''.join(row))


google_url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
google_url1 = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
fetch_content(google_url1)
