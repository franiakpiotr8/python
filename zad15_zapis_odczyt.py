# !python

print("==========zadanie15==========")
path = input("Wprowadź scieżkę do pliku który ma zostać otworzony: ")

try:
    file = open(path, 'r')
    text = file.read()
except FileNotFoundError:
    print("Nie ma takiego pliku: " + path)
except IOError:
    print("Błąd podczas otwierania pliku: " + path)
else:
    print("Zawartość wskazanego pliku: " + text)
    file.close()

try:
    file = open(path, 'a')
except FileNotFoundError:
    print("Nie ma takiego pliku: " + path)
except IOError:
    print("Błąd podczas otwierania pliku: " + path)
else:
    file.write("Przykładowy tekst który powinien znaleźć się w pliku.")
    file.close()
