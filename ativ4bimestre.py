matriz = [
    [3, 8, 1],
    [4, 9, 6],
    [2, 7, 5]
]

print("=== EXIBIÇÃO DA MATRIZ EM FORMATO DE GRADE ===")
for i in range(3):
    for c in range(3):
        print(f"{matriz [i] [c]}", end=" ")
    print()

print(f"elemento na linha 0, coluna 1; {matriz[0][1]}")
print(f"elemento na linha 2, coluna 2; {matriz[2][2]}")

soma_diagonal = 0 
for i in range(3):
    for c in range(3):
        if i == c:
            soma_diagonal += matriz[i][c]
print(f"soma dos elementos da diagonal principal:{soma_diagonal}")
