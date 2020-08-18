import re

def match(regex, string):
    p = re.compile(regex)
    return p.search(string)

def spam ():
    print("spam")
    exit()


fileName = str(input())
#fileName = "email.txt"

file = open(fileName[:-1], "r")
content = file.readlines()

regexList = ["-{5}beginmessage-{5}", \
    "from: [^@]+@[^@]+\.[^@]+", \
    "to: [^@]+@[^@]+\.[^@]+", \
    "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", \
    "^(19|20)\d\d\.(0[1-9]|1[012])\.(0[1-9]|[12][0-9]|3[01]) (?:([01]?\d|2[0-3]):([0-5]?\d):)?([0-5]?\d)$", \
    "^(-{23})$"]


if len(content) < 6:
    spam() 
for i in range(5):
    if not match(regexList[i], content[i]):
        spam()

mensagem = ""
counter = 0
for j in range(6, len(content)):
    if match("^-{5}endmessage-{5}$", content[j]):
        break
    else:
        mensagem += content[j]
        counter += 1
if len(content)-6 <= counter:
    spam()

spamWord = re.search(r"[^@]+@[^@]+\.[^@]+|</?head>|</?body>|</?img>|alt|href|milionario|emprestimo|loteria|banco|heranca|seguidor|desconto", mensagem)
if spamWord:
    spam()
palavraGrande = re.findall(r"\w{11,}", mensagem)
if palavraGrande:
    for palavra in palavraGrande:
        consoantes = re.findall(r'b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z', palavra)
        if len(consoantes) > len(palavra)/2:
            spam()
pontuacao = re.findall(r';|\.|,', mensagem)
if len(pontuacao) > 15:
    spam()

print("ham")


file.close()