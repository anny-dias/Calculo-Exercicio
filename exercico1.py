inicial = 10
mensal = 5
mes = 5
taxa = 1.01
soma = 0
t = 0 

while t < mes:
    soma += taxa ** t
    t += 1 

valor = inicial * taxa ** mes + mensal * soma
print(f"{valor}")

while mes < 24:
    valor = 1.01 ** mes
    soma += valor
    mes+= 1 
print(f"{valor}")