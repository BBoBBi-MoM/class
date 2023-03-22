#%%

def magicsquare():
    try:
        input_value = int(input('홀수차 배열의 크기를 입력하시오:'))
    except:
        print('잘못된 입력입니다..')
        return magicsquare()
    if input_value%2 ==0:
        print('짝수를 입력하였습니다. 다시 입력하세요.')
        return magicsquare()
    
    square_array = [[0 for j in range(input_value)] for i in range(input_value)]
    x = 0
    y = input_value//2
    value =1
    for i in range(input_value):
        for j in range(input_value):
            square_array[x%input_value][y%input_value] = value
            if square_array[(x-1)%input_value][(y+1)%input_value]!=0:
                x+=1
            else:
                x-=1
                y+=1
            value+=1
    
    for i in range(input_value):
        for j in range(input_value):
            print("{0:>4}".format(square_array[i][j]),end=' ')
        print('')

    
magicsquare()


