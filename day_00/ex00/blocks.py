"""Exercise 00: Blockchain

Requirements:
    * Correct lines are 32 characters long
    * They start with exactly 5 zeroes

So, for the example above your script should print:
```python
00000254b208c0f43409d8dc00439896
0000085a34260d1c84e89865c210ceb4
0000071f49cffeaea4184be3d507086v
```
Your code should accept the number of lines as an argument, like this:
```shell
$ cat data_hashes_10lines.txt | python blocks.py 10
```
"""

from sys import argv
from typing import Any, Callable


def _validate_args(args: list[str]) -> int:
    if len(args) > 1:
        raise ValueError("The number of arguments > 1")
    nbr: str = (args[0]).strip() if args else "0"
    if not nbr.isdigit():
        raise TypeError(f"The {nbr} is not digits-only.")
    return int(nbr)


def _default_hash_validator(hash_: str) -> bool:
    if (len(hash_) == 32) and hash_.startswith("00000") and hash_[5] != "0":
        return True
    return False


def main(
    num_of_lines: int, hash_validator: Callable[[str], Any] = _default_hash_validator
):
    """The main entry point."""

    try:
        for _ in range(num_of_lines):
            hash_ = input()
            if hash_validator(hash_):
                print(hash_)
    except EOFError:
        pass


if __name__ == "__main__":
    try:
        nlines = _validate_args(argv[1:])
        main(nlines)
    except Exception as err:
        print(f"Error: {err}")
