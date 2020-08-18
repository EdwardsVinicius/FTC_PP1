import re

#fileName = str(input())
fileName = "email.txt"

file = open(fileName, 'r', encoding="utf8")
content = file.readlines()

#Checa inicio da mensagem
match = re.search(r"-{5}beginmessage-{5}", content[0])

if match:
    print("begin message")
    # Checa remetente
    match = re.search(r"from: [^@]+@[^@]+\.[^@]+", content[1])

    if match:
        print("EMAIL AAAAAAAA")
        # Checa Destinatário
        match = re.search(r"to: [^@]+@[^@]+\.[^@]+", content[2])

        if match:
            print("EMAIL BBBBBBB")
            # Checa endereço IP
            match = re.search(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", content[3])
        
            if match:
                print("IP valido")
                # Checa Formato de data e hora (aceita ano bissexto)
                match = re.search(r"^(19|20)\d\d\.(0[1-9]|1[012])\.(0[1-9]|[12][0-9]|3[01]) (?:([01]?\d|2[0-3]):([0-5]?\d):)?([0-5]?\d)$", content[4])

                if match:
                    print("data e hora correta")

                    match = re.search(r"^(-{23})$", content[5])

                    if match:
                        print("Fim do cabeçalho")

print(content)


file.close()