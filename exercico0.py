a = 80000
b = 200000
t = 0 

while a < b:
    a *= 1.03 
    b *= 1.015
    t += 1
print(f"O ano que a cidade A passará de B é: {t}")
