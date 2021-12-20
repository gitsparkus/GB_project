lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+05', 'градусов']

lst1 = []

for item in lst:
    sign = ''
    if item[0] in ('+', '-') and item[1:].isnumeric():
        sign, item = item[0], item[1:]
    if item.isnumeric():
        lst1 += ['"'] + [sign + item.zfill(2)] + ['"']
    else:
        lst1 += [item]

print(''.join(lst1))
