# l_num = list(map(int, input().split()))
# pares = (n for n in l_num if n % 2 == 0)
# impares = (n for n in l_num if n % 2 != 0)
# print(f"Soma pares: {sum(pares)} || Soma impares: {sum(impares)}")
# QUESTÃO 1 ^^^^^^^^^^^^^^^^



# num = int(input())
# meses = ["janeiro", "feveireiro", "março", "abril", "junho", "julho", "maio", "agosto", "setembro", "outubro", "novembro", "dezembro"]
# trimestres = ["primeiro", "segundo", "terceiro", "quarto"]

# if num >= 0 and num <= 2:
#     tri = trimestres[0]
# elif num >= 3 and num <= 5:
#     tri = trimestres[1]
# elif num >= 6 and num <= 8:
#     tri = trimestres[2]
# else:
#     tri = trimestres[3]
# print(f"O mês de {meses[num-1]} é o do {tri} trimestre do ano")
# QUESTÃO 2 ^^^^^^^^^^^^^^^^



# l_num = list(map(int, input().split()))
# l_num.sort()
# print(f"Maior número: {l_num[3]} | Menor número: {l_num[0]} || Soma dos 2° maior/menor: {(l_num[1]+l_num[2])}")
# QUESTÃO 3 ^^^^^^^^^^^^^^^^


# d, m, a = map(int, input().split("/"))
# l_trinta = [4, 6, 9, 11]
# if d > 31:
#     print("Data invalida")
# elif m ==2 and d > 27:
#     print("Data invalida")
# elif m == l_trinta:
#     if d > 30:
#         print("Data invalida")
# elif a > 2100 or a < 1900:
#     print("Data invalida")
# else:
#     print("Data valida")
# QUESTÃO 4 ^^^^^^^^^^^^^^^^




# a, b, c = map(int, input().split())
# if a > b and a > c:
#     if b > c:
#         print(a, b, c)
#     else:
#         print(a, c, b)
# if b > a and b < c:
#     if a > c:
#         print(b, a, c)
#     else:
#         print(b, c, a)
# else:
#     if b > a:
#         print(c, b, a)
#     else:
#         print(c, a, b)
# parabens, jumento, voce fez a conta ao contrário >:W. agora deixa assim.
# QUESTÃO 5 ^^^^^^^^^^^^^^^^




# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in range(len(lista)):
#     if lista[i] % 2 == 0:
#         lista[i] = lista[i]*-1
# print(lista)
# QUESTÃO 6 ^^^^^^^^^^^^^^^^
