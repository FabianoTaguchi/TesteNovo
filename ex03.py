frase = input("Digite uma frase: ").lower()
letra = input("Digite uma letra: ").lower()
contador = 0

for caractere in frase:
    if caractere == letra:
        contador += 1

print(f"A letra '{letra}' aparece {contador} vezes.")
