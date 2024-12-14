#!/usr/bin/env python3


def main():
    with open("main.py", "r") as file:
        content = file.read()
    content.replace("\n", "\\n")
    with open("create.sh", "wb") as file:
        file.write(content.encode("utf-8"))


if __name__ == "__main__":
    main()
