import re

text = input("Введите текст: ")
dates = r"20\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01]) (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d(?![0-9])"
matches = re.findall(dates, text)

for match in matches:
    print(match)
