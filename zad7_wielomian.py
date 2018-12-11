# !python

print("==========zadanie7==========")

abc = input("Wprowadz wspolczynniki wielomianu(oddzielone \",\"): ").split(",")
abc = list(map(int, abc))

delta=abc[1]*abc[1] - 4*abc[0]*abc[2]
if delta > 0:
    x1=(-abc[1]-delta)/(2*abc[0])
    x2=(-abc[1]+delta)/(2*abc[0])
    print("Pierwiastki wielomianu to: " + str(x1) + " i " + str(x2))
elif delta == 0:

    print("Jeden pierwiastek: " + str(-abc[1]/(4*abc[0]*abc[2])))
else:
    print("Brak pierwisatków, delta < 0")
