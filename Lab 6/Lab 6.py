A = [4, -3, 2, 0, 5, -1, 6, -7, 3, 1]

positive_squares = [x**2 for x in A if x > 0]

if positive_squares:
    average = sum(positive_squares) / len(positive_squares)
else:
    average = 0

print("Оң элементтер:", [x for x in A if x > 0])
print("Олардың квадраттары:", positive_squares)
print("Квадраттардың арифметикалық ортасы:", average)


A = [
    [4, 7, 1, 6],
    [3, 5, 8, 2],
    [6, 9, 0, 4],
    [7, 3, 2, 5]
]

sum_less_than_5 = sum(x for row in A for x in row if x < 5)

print("A матрицасы:")
for row in A:
    print(row)

print("5-тен кіші элементтердің қосындысы:", sum_less_than_5)

