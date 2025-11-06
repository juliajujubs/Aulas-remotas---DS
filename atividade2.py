numero_texto = input("Digite um número para ver a tabuada: ")
numero = int(numero_texto)

print(f"=== Tabuada de {numero} ===")

for i in range(1, 11):
    
    resultado = numero * i
    
    print(f"{numero} x {i} = {resultado}")
