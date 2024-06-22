import itertools

names = ['Cecilia', '남궁민수', '하하하']
counts = [len(n) for n in names]
print(counts)

names.append('김태희')

print('======zip======')
for name, count in zip(names, counts):
    print(f'{name}: {count}')

print('======zip_longest======')
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')
