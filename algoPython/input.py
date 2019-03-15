from sys import stdin
total_gear = []

while True:
    b = (stdin.readline()).strip('\n')
    x = 0
    if x < 4:
        temp_input = []
        for i in range (0,8):
            temp_input.append(int(b[i]))

        total_gear.append(temp_input)
        x=x+1

    else :
        break
    print(total_gear) 
repeat_number = int((stdin.readline()).strip('\n'))
list_operate= []
for i in range(0,repeat_number) : 
    b = (stdin.readline()).strip('\n')
    temp = b.splite(' ')
    temp = map(int, temp)
    list_operate.append(temp)
print(list_operate)
    
