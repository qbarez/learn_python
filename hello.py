print('Hello, World!');
# => Hello, World!
print((8 / 4) - (8 + (2 - 1)) + 7 * 2)

print(3 ** 5)
print(-8 / -4)
print(100 % 3)
print((3 ** 5)+(-8 / -4)+(100 % 3))

rubles_per_dollar = 60
dollars_count = 50 * 1.25  # 62.5
rubles_count = dollars_count * rubles_per_dollar  # 3750.0

# Функция str() превращает число в строку.
# О таких превращениях будет отдельный урок.
print('The price is ' + str(rubles_count) + ' rubles')
# => The price is 3750.0 rubles

apples_per_box = 60
boxes_per_container = 50
container = 4
apples_count = apples_per_box * boxes_per_container * container
 
print(apples_count)

euros_count = 100
dollars_count = euros_count * 1.25
print(dollars_count)
rubles_count = dollars_count * 60
print(rubles_count)