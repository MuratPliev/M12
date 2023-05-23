per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму, которую вы планируете положить под проценты: "))

deposit = [int(money * rate / 100) for rate in per_cent.values()]

print("Накопленные средства за год вклада в каждом из банков:")
for bank, amount in zip(per_cent.keys(), deposit):
    print(f"{bank}: {amount}")

max_deposit = max(deposit)
print(f"Максимальная сумма, которую вы можете заработать: {max_deposit}")
