frase = 'O python é uma linguagem de programação multiparadigma. Ele foi criado por Guido Rossum.'

i = 0
qtd = 0
letra_maisVezes = 0

while i < len(frase):
  letra_atual = frase[i]
  if letra_atual ==" ":
     i +=1
     continue

  qtd_atual = frase.count(letra_atual)

  if qtd < qtd_atual:
    qtd = qtd_atual
    letra_maisVezes = letra_atual
  i +=1

print("Letra que mais apareceu foi:",letra_maisVezes,",",qtd,"vezes")


