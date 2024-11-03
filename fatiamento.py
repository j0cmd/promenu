import random

lista = [0, 1, 2, 3, 4, 5, 6]

print(lista[:7:2])

board = [['-'] * 3 for i in range(3)]
print(board)

lista.sort(reverse=True)
print(lista)

print(random.shuffle(lista))
