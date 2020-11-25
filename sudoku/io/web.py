import warnings

from bs4 import BeautifulSoup
from requests import get


def get_string(url="http://nine.websudoku.com/?level=1"):
    resp = get(url)
    if not resp.status_code == 200:
        warnings.warn(f"{url} returned status code {resp.status_code}")
    soup = BeautifulSoup(resp.text, "html.parser")
    board = soup.find(id="puzzle_grid")
    string = ""
    for row in board.find_all("tr"):
        for cell in row.find_all("td"):
            string += list(cell.children)[0].get("value", ".")
    return string


if __name__ == "__main__":
    print(get_string())
