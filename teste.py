#Python

arquivo = open("DgLindo.txt", "w")

arquivo.write(str(input("Digita alguma coisa ai: ")))

arquivo.close()

arquivo = open("DgLindo.txt", "r")

dados = arquivo.read()

print(dados)

arquivo.close()




