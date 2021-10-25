def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for num in items:
            i = num.get(args[0])
            if i != None:
                yield i
    else:
        for num in items:
            i = {key: val for key, val in num.items() if key in args and val != None}
            if i != {}:
                yield i

if __name__ == "__main__":
    goods = [
        {'title': None, 'price': 2000, 'color': 'green'},
        {'title': 'Ковер', 'price': None, 'color': 'black'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': None}
    ]
    for i in field(goods, 'title'):
        print(i)
    for i in field(goods, 'title', 'price'):
        print(i)
    for i in field(goods, 'price', 'color'):
        print(i)
    wait = input("PRESS ENTER TO CONTINUE.")
