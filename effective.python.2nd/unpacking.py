snacks = [("bacon", 350), ("donut", 240), ("muffin", 190), ("bacon", 450), ("muffin", 170), ("donut", 280)]

# 1 부터 시작
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'#{rank}: {name} has {calories} calories')

