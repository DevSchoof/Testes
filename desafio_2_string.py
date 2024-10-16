def cont_letra_a(texto):
    cont = 0
    for char in texto:
        if char.lower() == 'a':
            cont += 1
    return cont

string = input("Digite seu nome: ")
cont = cont_letra_a(string)

if cont > 0:
    print(f"A letra 'a' aparece {cont} vez(es) no nome {string}.")
else:
    print(f"A letra 'a' não aparece no nome {string}.")
    