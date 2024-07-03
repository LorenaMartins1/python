print("JOGO DA PALAVRA SECRETA")

palavra_secreta = "laranja"
acertos= []
letras_erradas= []
erros = 0

while True:
  letra = input("Adivine uma letra: ").lower()

  if len(letra) > 1:
      print("Digite apenas uma letra")
      continue
  
  if letra in acertos or letra in letras_erradas:
    print("Você já tentou essa letra")
    continue
  
  if letra in palavra_secreta:
    acertos.append(letra)
  else:
    letras_erradas.append(letra)
    erros +=1
  
  for letra in palavra_secreta:
    if letra in acertos:
      print(letra, end='')
    else:
      print("*", end='')

  print()

  if all(letra in acertos for letra in palavra_secreta):
    print("Parabéns! Você descobriu a palavra secreta.")
    print("Erros:",erros)
    break
