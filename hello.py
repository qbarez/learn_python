#1
print('Hello, World!');
# => Hello, World!
print((8 / 4) - (8 + (2 - 1)) + 7 * 2)

#3
print(3 ** 5)
print(-8 / -4)
print(100 % 3)
print((3 ** 5)+(-8 / -4)+(100 % 3))

#7
apples_per_box = 60
boxes_per_container = 50
container = 4
apples_count = apples_per_box * boxes_per_container * container
print(apples_count)

#8
rubles_per_dollar = 60
dollars_count = 50 * 1.25  # 62.5
rubles_count = dollars_count * rubles_per_dollar  # 3750.0
# Функция str() превращает число в строку.
# О таких превращениях будет отдельный урок.
print('The price is ' + str(rubles_count) + ' rubles')
# => The price is 3750.0 rubles

#8.2
euros_count = 100
dollars_count = euros_count * 1.25
print(dollars_count)
rubles_count = dollars_count * 60
print(rubles_count)

#9
stark = 'Arya'
print(f'''Do you want to eat, {stark}?
Yes, I'm hungry, mom.''')
magic = '\nyou'
print(magic[1])  # => ?

#10
one = 'Naharis'
two = 'Mormont'
three = 'Sand'
word = one[2] + two[1] + three[3] + two[4] + two [2]
print(word)