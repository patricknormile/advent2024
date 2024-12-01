import os
import requests
from dotenv import load_dotenv

def get_days_data(year, day):
    """
    get the data for a given day and year
    requires access to your cookies in .env file.
    """
    load_dotenv()
    SESSION_COOKIE = os.getenv("AOC_SESSION")
    if not SESSION_COOKIE:
        raise RuntimeError("Missing session cookie! Set it in the .env file or environment variable.")
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={SESSION_COOKIE}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        raise RuntimeError(f"Failed to fetch puzzle input: {response.status_code}")
if __name__ == "__main__":
    year = 2024
    day = 1
    get_days_data(year, day)