highestNum = 0
num1 = 999
num2 = 999

def palinTest(testNum):
    int1 = int(testNum / 100000)
    int2 = int((testNum - (int1 * 100000)) / 10000)
    int3 = int((testNum - (int1 * 100000) - (int2 * 10000)) / 1000)
    int4 = int((testNum - (int1 * 100000) - (int2 * 10000)- (int3 * 1000)) / 100)
    int5 = int((testNum - (int1 * 100000) - (int2 * 10000)- (int3 * 1000) - (int4 * 100)) / 10)
    int6 = int(testNum - (int1 * 100000) - (int2 * 10000)- (int3 * 1000) - (int4 * 100) - (int5 * 10))
    
    reverseNumber = (int6 * 100000) + (int5 * 10000) + (int4 * 1000) + (int3 * 100) + (int2 * 10) + int1

    if (reverseNumber == testNum):
        return 1
    else:
        return 0
        
while num2 > 0:
    while num1 > 0:
        if(palinTest(num1 * num2)):
        
            if (num1 * num2) > highestNum:
                highestNum = num1 * num2
        num1 -= 1
    num1 = num2
    num2 -= 1
print highestNum
    

