
#fileName = str(input())
fileName = "email.txt"

file = open(fileName, 'r', encoding="utf8")
content = file.readlines()

print(content)


file.close()