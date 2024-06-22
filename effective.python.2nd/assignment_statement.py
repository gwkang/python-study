fresh_fruit = { 
    '사과': 10,
    '바나나': 8,
    '레몬': 5
}

def make_lemonade(count):
    fresh_fruit['레몬'] -= count
    print(f'{count} 만큼 레몬을 사용하여 레몬에이드를 만듭니다.')

def make_cider(count):
    fresh_fruit['사과'] -= count
    print(f'{count} 만큼 사과를 사용하여 사이다를 만듭니다.')

def out_of_stock():
    for k, v in fresh_fruit.items():
        if v == 0:
            print(f'{k} 품절')

# walrus operator를 사용하면 count가 if 문에서 선언되므로 코드가 더 간결해진다. python 3.8부터 사용 가능
if count := fresh_fruit.get('레몬', 0):
    make_lemonade(count)
else:
    out_of_stock()

if (count := fresh_fruit.get('사과', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()
