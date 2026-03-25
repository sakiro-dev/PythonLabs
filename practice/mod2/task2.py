import re

text = input("Введите текст: ")
emails = r"[\w+#-]+@[\w.-]+\.[a-zA-Z]{2,}"
matches = re.findall(emails, text)

for match in matches:
    print(match)
