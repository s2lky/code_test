x, y, w, h = map(int, input().split())

current_location = (x, y)
left_lower_location = (0, 0)
right_upper_location = (w, h)

a = current_location[0] - left_lower_location[0]
b = right_upper_location[0] - current_location[0]
c = current_location[1] - left_lower_location[1]
d = right_upper_location[1] - current_location[1]

print(min(a, b, c, d))