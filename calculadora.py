'''calculadora com while'''
while True:

  n1 = input("n1: ")
  n2 = input("n2: ")
  oper = input("Operador: (+-/*) ")

  sair = input("Deseja sair? S/N: ").lower()
  sair == "s"

  try:
    n1_float = float(n1)
    n2_float = float(n2)
    n_validos = True
  except ValueError:
    n_validos = False

  if n_validos is None:
    print("Um ou ambos números são inválidos!")
    continue

  oper_permitidos = "+-/*"

  if oper not in oper_permitidos or len(oper) != 1:
    print("Operador inválido!")
    continue

  print("Confira o resultado:")
  if oper == "+":
    print(f"{n1_float} + {n2_float} = {n1_float + n2_float}")
  elif oper == "-":
    print(f"{n1_float} - {n2_float} = {n1_float - n2_float}")
  elif oper == "/":
    if n2_float != 0:
      print(f"{n1_float} / {n2_float} = {n1_float / n2_float}")
    else:
      print("Erro: Divisão por zero!")
  elif oper == "*":
    print(f"{n1_float} * {n2_float} = {n1_float * n2_float}")

  if sair == "s":
    break