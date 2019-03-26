input_array = [14, 6, 8, 18, 20, 12, 2, 4, 10]
real_sum = 0
maxItem = input_array[0]
amountOfItem = len(input_array)
expect_sum = amountOfItem*(amountOfItem+1)
for i in range(0, amountOfItem):
    if input_array[i]>maxItem :
        maxItem = input_array[i]
    real_sum += input_array[i]
difference = real_sum - expect_sum    
print(maxItem - difference)
