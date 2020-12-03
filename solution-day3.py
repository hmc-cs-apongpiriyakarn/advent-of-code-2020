f = open('input3.txt')
data = f.readlines()
num_row = len(data) 
num_col = len(data[0]) 
right = 1
down = 2
count = 0
i = 0
j = 0
for i in range(0,num_row,down):
    data[i].strip()
    if j > num_col - 2: 
        j = j - num_col - 1 # don't count '\n'
    if data[i][j] == '#':
        count = count + 1
    # print(i,j, data[i][j], data[i])
    j = j + right
print(count)
