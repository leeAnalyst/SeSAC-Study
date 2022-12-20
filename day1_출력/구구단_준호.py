#혼자시도
for i in range(1,10):
    mul = 2
    if i == 1:
        print('2단')
    print('{}X{}={}'.format(mul,i,mul*i))

# 같이해봄
for i in range(2,10):
    print('{}단'.format(i))
    for j in range(1,10):
        print('{}X{}={}'.format(i,j,i*j))
