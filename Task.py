import matplotlib.pyplot as plt

with open('dane.txt', 'r') as plik:
    lista = plik.readlines()
gnuj = []
for linia in lista[:]:
    linia = linia.replace("\n", "")
    x, y = linia.split(";")
    gnuj.append([int(x), int(y)])
plt.plot(gnuj)
plt.show()

