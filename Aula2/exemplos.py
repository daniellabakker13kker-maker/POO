# l_num = list(map(int, input().split()))
# pares = (n for n in l_num if n % 2 == 0)
# impares = (n for n in l_num if n % 2 != 0)
# print(f"Soma pares: {sum(pares)} || Soma impares: {sum(impares)}")
# QUESTÃO 1 ^^^^^^^^^^^^^^^^


num = int(input())
meses = ["janeiro", "feveireiro", "março", "abril", "junho", "julho", "maio", "agosto", "setembro", "outubro", "novembro", "dezembro"]
trimestres = ["primeiro", "segundo", "terceiro", "quarto"]

if num >= 0 and num <= 2:
    tri = trimestres[0]
elif num >= 3 and num <= 5:
    tri = trimestres[1]
elif num >= 6 and num <= 8:
    tri = trimestres[2]
else:
    tri = trimestres[3]
print(f"O mês de {meses[num-1]} é o do {tri} trimestre do ano")
