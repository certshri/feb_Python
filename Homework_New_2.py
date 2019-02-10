# for i in range(1,4):
#     print(" ")
#     number = 0
#     for j in range(i, i+5):
#
#      print("%02d"%j,end = " ")
#      number = j
#     print(" ")
#     for number in range(number,number-5,-1):
#
#      print("%02d"% number,end = " ")
"""
Q 11 pattern
number = 1
for i in range(1,4):
    print(" ")
    for j in range(1,6):
        j=number*j
        print("%02d"%j,end =" ")
    print(" ")
    for j in range(j+number,i,-i):
        j=j-number
        print("%02d" % j, end=" ")
    number+=1
"""
