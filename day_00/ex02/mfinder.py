"""Exercise 02: Track and Capture

All your code has to do is to print 'True'
if this M-pattern exists in a given input image or 'False' otherwise.
Other characters (outside the M pattern) should be different.

An example of an 'M' letter pattern.
*111*
**2**
*3*3*
"""

from re import match
from sys import stdin


def _read_ascii_image_from_stdin() -> list[str]:
    nlines: int = 1
    ascii_image: list[str] = []
    for line in stdin:
        if nlines > 3:
            raise ValueError(f"The number of lines ({nlines}) exceeds 3 lines")
        line_ = line.strip()
        if " " in line_:
            line_ = "".join(line_.split())
        if len(line_) != 5:
            raise ValueError(f"The line '{line_}' does not consist of 5 items")
        ascii_image.append(line_)
        nlines += 1
    return ascii_image


def _has_m_letter(image: list[str]) -> bool:
    line1, line2, line3 = image
    if (
        match(r"^[^*]{3}\*\*$", line1)
        and match(r"^\*[^*]\*{3}$", line2)
        and match(r"^[^*]\*[^*]\*{2}$", line3)
    ):
        return True
    if (
        match(r"^\*[^*]{3}\*$", line1)
        and match(r"^\*{2}[^*]\*{2}$", line2)
        and match(r"^\*[^*]\*[^*]\*$", line3)
    ):
        return True
    if (
        match(r"^\*{2}[^*]{3}$", line1)
        and match(r"^\*{3}[^*]\*$", line2)
        and match(r"^\*{2}[^*]\*[^*]$", line3)
    ):
        return True
    return False


def main() -> None:
    """The main entry point."""

    img: list[str] = _read_ascii_image_from_stdin()
    print(_has_m_letter(img))


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error: {err}")
