"""Exercise 01: Decypher

Can you guess the hidden sense?
```shell
$ python decypher.py "Have you delivered eggplant pizza at restored keep?"
```

Answer: Hyde Park
https://en.wikipedia.org/wiki/Hyde_Park,_London
"""

from sys import argv


def main(strings: list[str]):
    """The main entry point."""

    for string in strings:
        answer = "".join([word[0] for word in string.split()])
        print(answer)


if __name__ == "__main__":
    try:
        main(argv[1:])
    except Exception as err:
        print(f"Error: {err}")
