lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+05', 'градусов']

i = 0
while i < len(lst):
    sign = ''
    item = lst[i]
    if item[0] in ('+', '-') and item[1:].isnumeric():
        sign, item = item[0], item[1:]
    if item.isnumeric():
        lst[i] = lst[i].zfill(2)
        lst.insert(i, '"')
        lst.insert(i + 2, '"')
        i += 2
    i += 1

print(lst)
