# Advent2024
Solutions to advent of code 2024 by [@patricknormile](https://github.com/patricknormile/)

## Environment
The dependencies are managed with poetry. To use the same packages, install poetry with `pip install poetry`.

Then, from the directory with [pyproject.toml](pyproject.toml), run `poetry install` and then `poetry shell`.

Additionally, I stored my cookies in a `.env` file. This is used to retrieve the data from advent of code's website. To use the utility funtion `get_days_data` in [utils/get_data.py](./utils/get_data.py), create your own `.env` file in the root directory with `AOC_SESSION=<your cookie here>`