data = [
    range(2015, 2019),
    range(2017, 2020),
    range(2016, 2017),
    range(2011, 2022)
]

start = min([x[0] for x in data])
end = max([x[-1] + 1 for x in data])

output = []
max_key = 0
for i in range(start, end + 1):
    c = 0
    for x in data:
        if i in x:
            c = c + 1
    if c > max_key:
        output = [i]
        max_key = c
    elif c == max_key:
        output.append(i)

print(output)
