# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

how_many = {}
temp = ""

for i in sentences:
    temp = i.split()
    for j in temp:
        j = j.lower()
        if j not in how_many:
            how_many[j] = 1
        else:
            how_many[j] += 1

for i in range(1, 4):
    max_value = max(how_many.values())
    max_key = max(how_many, key=how_many.get)
    print("# " + str(i) + ". " + '"' + str(max_key) + '"' + " - " + str(max_value))
    del(how_many[max_key])
