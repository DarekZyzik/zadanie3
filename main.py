# Napisać program, który:
# # - czyta plik tekstowy
# # - usuwa kropki, przecinki,
# # zamienia litery na małe
# # - liczy liczbę różnych słów
# # - liczy liczbę powtórzeń danych slow

#1.1 czytamy plik tekstowy

path = 'C:\\Users\\yer0nos\\zadanie3\\rolling_stones.txt'
with open(path, 'r') as file:
    content = file.readlines()
    content_lista = file.read()
    print (content)

#1.2a zamiana na male litery
#1.2b usuwanie kropek, przecinkow

#1.2a
    with open(path, 'r') as file:
        content_lista = str(content)
        content_male_litery = content_lista.lower()
        print (content_male_litery)

#1.2b






