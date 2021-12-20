lst = [11.99, 99.41, 7.85, 66.96, 72.36, 64.44, 97.6, 7.89, 77.11, 24.06, 92.9, 47.0, 19.85, 96.15, 70.38, 13.38, 58.75,
       0.2, 66.48, 29.37]

lst_id = id(lst)
for price in sorted(lst):
    print(f'{str(price).split(".")[0].zfill(2)} руб {str(price).split(".")[1].zfill(2)} коп', end=', ')


print('\nID списка после цикла сохранился? ', id(lst) == lst_id)

lst_desc = sorted(lst, reverse=True)
print('Список по убыванию: ', lst_desc)
print('Это новый список?', id(lst) != id(lst_desc))

for price in sorted(lst_desc[:5]):
    print(f'{str(price).split(".")[0].zfill(2)} руб {str(price).split(".")[1].zfill(2)} коп')
