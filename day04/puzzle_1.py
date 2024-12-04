import sys
from pathlib import Path
root = Path(__file__).parent.parent
sys.path.append(str(root))

from utils.get_data import get_days_data

def make_text_array(data):
    rows = data.split("\n")
    data_rows = [list(row) for row in rows if row]
    return data_rows

def search_generic(i, j, text_array, updown, leftright):
    """
    Args:
        i: row index
        j: column index
        text_array: array of chars
        updown: move up (1) or down (-1) or not at all (0)
        leftright: move left (-1) or right (1) or not at all (0)
    """
    match = False
    try:
        candidates = (
            text_array[i][j],
            text_array[i+updown][j+leftright],
            text_array[i+updown*2][j+leftright*2],
            text_array[i+updown*3][j+leftright*3],
        )
        # since python allows for negative indices, this is clunky
        if (
            i+updown<0 or 
            j+leftright<0 or 
            i+updown*2<0 or 
            j+leftright*2<0 or 
            i+updown*3<0 or 
            j+leftright*3<0):
            raise IndexError("out of bounds")
        if "".join(candidates) == "XMAS":
            return True
    except IndexError:
        pass
    return match

def counter(text_array):
    updowns = [1, -1, 0]
    leftrights = [1, -1, 0]
    count = 0
    for i in range(len(text_array)):
        for j in range(len(text_array[i])):
            if text_array[i][j] != "X":
                continue
            for updown in updowns:
                for leftright in leftrights:
                    if updown == 0 and leftright == 0:
                        continue
                    if search_generic(i, j, text_array, updown, leftright):
                        count += 1
    return count
                
def main():
    data = get_days_data(2024, 4)
    array = make_text_array(data)
    print(counter(array))

if __name__ == "__main__":
    main()
