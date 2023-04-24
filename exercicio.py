pop_a = 80000
pop_b = 200000
t = 0 

while pop_a < pop_b:
    pop_a *= 1.03 
    pop_b *= 1.015
    t += 1   


    b.append(pop_b)
    tempo.append(t)


print(t)
print(a)
print(b)
plt.plot(tempo, a, "bo", label = "Pop A")
plt.plot(tempo, b, "bo", label = "Pop B")
plt.legend()
plt.ylabel("População")
plt.xlabel("tempo")
plt.title("População em função do tempo")
plt.grid()
plt.show()


#da biblioteca math (pesquisar, não deu certo)