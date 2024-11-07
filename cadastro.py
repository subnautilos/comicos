import random
primeiro_nome = str(input("Digite seu primeiro nome: "))

id = random.randint(1, 5)
nomeid = [primeiro_nome, id]

print(f"seu id será: {nomeid[1]}")
