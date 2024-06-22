
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight!r})'

tools = [
    Tool('hammer', 3.5),
    Tool('screwdriver', 0.5),
    Tool('wrench', 1.2),
    Tool('saw', 4.6),
]

print('미정렬:', repr(tools))
tools.sort(key=lambda x: x.name)
print('정렬 by name:', tools)

tools.sort(key=lambda x: (x.weight, x.name))
print('정렬 by (weight, name):', tools)