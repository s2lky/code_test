num_count = int(input())

x_list = []
y_list = []

for _ in range(num_count):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

max_point = (max(x_list), max(y_list))
min_point = (min(x_list), min(y_list))

print((max_point[0] - min_point[0]) * (max_point[1] - min_point[1]))