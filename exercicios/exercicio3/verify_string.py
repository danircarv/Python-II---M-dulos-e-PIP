import re

text = input("Digite a frase para a verficação:\n")
pattern = "[a-z]+[A-Z]+[0-9]"
result = re.findall(pattern, text)
if result == []:
    print(f"{text} não possui as strings válidas")
else:
    print("Tudo certao")