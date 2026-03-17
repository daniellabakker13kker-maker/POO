l_num = list(map(int, input().split()))
pares = (n for n in l_num if n % 2 == 0)
impares = (n for n in l_num if n % 2 != 0)
print(f"Soma pares: {sum(pares)} || Soma impares: {sum(impares)}")