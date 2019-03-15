from sys import stdin
'''
def set_gear(input) :
    global total_gear
    a_gear=[]
    for i in range(0, 8):
        a_gear.append(input[i])
    total_gear.append(a_gear)

total_gear = []
n = int(stdin.readline())

while True:
    b = (stdin.readline()).strip('\n')
    x = 0
    if x <= 4:
        print(b)
        set_gear(b)
        print(total_gear)
        x +=1 
    else :
        break 
    '''
'''
def compare_gear(gear_number, gear_direction) :
    global total_gear 
    global total_gear_flag
    if (total_gear_flag[gear_number]==0):
        total_gear_flag[gear_number] = 1
        target_gear = total_gear[gear_number]
    else :
        return False
    if (gear_direction == -1) :
        first_element=target_gear[0]
        temp_gear = []
        for i in range (0,8) :
            if(i == 7) :
                temp_great[i].append(first_element)
            else :
                temp_gear[i].append(target_gear[i+1])
        return True
  '''          

def set_next_change_direction(change_direction):
    if change_direction == 1:
        return -1
    else:
        return 1
def set_left_gear(start_gear, start_direction): 
    global total_gear_flag
    global total_gear
    right_gear_index = start_gear
    left_gear_index = right_gear_index -1
    total_gear_flag[right_gear_index] = start_direction
    next_change_direction = set_next_change_direction(start_direction)
    #left로 끝까지 가보자
    while ( left_gear_index >= 0 ) :
        #change지점의 극이 다른 상황. 
        if (list_change[left_gear_index] ==1 ) :
            total_gear_flag[left_gear_index] = next_change_direction

            #다음꺼 setting
            right_gear_index = left_gear_index
            left_gear_index = right_gear_index - 1
            next_change_direction = set_next_change_direction(next_change_direction)

        else : 
            break

def set_right_gear(start_gear, start_direction): 
    left_gear_index = start_gear
    right_gear_index = left_gear_index + 1
    next_change_direction = set_next_change_direction(start_direction)

    while(right_gear_index < 4 ) :
        if (list_change[left_gear_index] == 1 ) :
            total_gear_flag[right_gear_index] = next_change_direction

            #다음꺼 setting
            left_gear_index = right_gear_index
            right_gear_index = left_gear_index + 1
            next_change_direction = set_next_change_direction(next_change_direction)

        else : 
            break
'''
def change_total_gear():
    #total_gear_flag 대로 ttaol_gear를 변경해줘야함
    global total_gear
    temp_total_gear = []
    
    for i in range(0,4) :
        temp_change_gear = []
        change_gear = total_gear[i]
        
        if total_gear_flag[i] == 0 :
            temp_change_gear = change_gear

    #반시계 회전 상황. 첫번째원소가 맨뒤로
        elif total_gear_flag[i] == -1 :
            first_value = change_gear[0]            
            for i in range(0,7) :
                temp_change_gear.append(change_gear[i+1])
            temp_change_gear.append(first_value)
        elif total_gear_flag[i] == 1 :
            last_value = change_gear[1]
            temp_change_gear.append(last_value)
            for i in range(0,7) :
                temp_change_gear.append(change_gear[i])
        
        temp_total_gear.append(temp_change_gear)
    total_gear = temp_total_gear
'''
def change_total_gear(total_gear):
    #total_gear_flag 대로 ttaol_gear를 변경해줘야함
    temp_total_gear = []
    
    for i in range(0,4) :
        temp_change_gear = []
        change_gear = total_gear[i]
        
        if total_gear_flag[i] == 0 :
            print("변화없음")
            temp_change_gear = change_gear

    #반시계 회전 상황. 첫번째원소가 맨뒤로
        elif total_gear_flag[i] == -1 :
            print("반시계")
            first_value = change_gear[0]            
            for i in range(0,7) :
                temp_change_gear.append(change_gear[i+1])
            temp_change_gear.append(first_value)
        elif total_gear_flag[i] == 1 :
            print("시계")
            last_value = change_gear[7]
            temp_change_gear.append(last_value)
            for i in range(0,7) :
                temp_change_gear.append(change_gear[i])
        
        temp_total_gear.append(temp_change_gear)
        print("temp"+ str(temp_total_gear))
    return temp_total_gear
        

#total_gear = [[1,0,1,0,1,1,1,1],[0,1,1,1,1,1,0,1],[1,1,0,0,1,1,1,0],[0,0,0,0,0,0,1,0]] 
#list_operate = [[3,-1],[1,1]]
#total_gear = [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
#list_operate = [[1,1],[2,1],[3,1]]
#total_gear = [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]]
#list_operate = [[1,1],[2,1],[3,1]]
#total_gear=[[1,0,0,0,1,0,1,1],[1,0,0,0,0,0,1,1],[0,1,0,1,1,0,1,1],[0,0,1,1,1,1,0,1]]
#list_operate = [[1,1],[2,1],[3,1],[4,1],[1,-1]]
total_gear=[[1,0,0,1,0,0,1,1],[0,1,0,1,0,0,1,1],[1,1,1,0,0,0,1,1],[0,1,0,1,0,1,0,1]]
list_operate=[[1,1],[2,1],[3,1],[4,1],[1,-1],[2,-1],[3,-1],[4,-1]]


total_gear_flag =[0,0,0,0]
right_compare_position = 6    
left_compare_position = 2
for item in list_operate:
    #반시계 -1
    #3군데에서 비교가 발생하게 됨.
    list_change = []
    total_gear_flag = [0,0,0,0]
    for i in range(0,3) :
        left_gear = total_gear[i]
        right_gear = total_gear[i+1]
        if (left_gear[left_compare_position] != right_gear[right_compare_position]):
            list_change.append(1)
        else:
            list_change.append(0)
    print(list_change)    


    #이제 돌기시작한 톱니 기준으로 비교가 시작됨
    start_gear = item[0] -1
    start_direction = item[1]
    total_gear_flag[start_gear] = start_direction

    set_left_gear(start_gear, start_direction)
    set_right_gear(start_gear, start_direction)
    #change_total_gear()
    total_gear = change_total_gear(total_gear)
    total_score = 0
    count = 1
    score = 1

    for item in total_gear:
        print(item[0])
        if(item[0]==1) :
            total_score += score 
        score = score * 2

        
    
    print(total_gear_flag)   
    print(total_gear)
    print(total_score)
    
