

a = [('Al', 2),('Bill', 1),('Carol', 2), ('Abel', 3), ('Zeke', 2), ('Chris', 1), ('Zain', 3)]



a.sort(key=lambda x: x[1], reverse=True)
a.sort(key=lambda y: y[0])

with open('names.csv', newline='') as csvfile:
    pass