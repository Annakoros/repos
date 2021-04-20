data_inputed = False
goods_data = []
count = 1
while data_inputed != True:
    name = input('Введите название товара\n(для завершения нажмите "к"): ')
    if name == 'к':
        data_inputed = True
        break
    price = input('Цена данного товара: ')
    number = input('Количество: ')
    unit = input('Единица измерения: ')
    goods_dict = {'Название': name, 'Цена': price, 'Количество': number, 'ед.': unit}
    goods_tuple = (count, goods_dict)
    goods_data.append(goods_tuple)
    count += 1
print(goods_data)

names = []
prices = []
numbers = []
units = []
newdict = {}
for good_data in goods_data:
    for good_tuple in good_data:
        if type(good_tuple) == dict:
            names.append(good_tuple.get('Название'))
            prices.append(good_tuple.get('Цена'))
            numbers.append(good_tuple.get('Количество'))
            units.append(good_tuple.get('ед.'))
newdict.update({'Название': names, 'Цена': prices, 'Количество': numbers, 'ед.': units})
print(newdict)