number = int(input())
# number只能介於1~9間
if number > 0 and number < 10:
    for i in range(1,10,1):
        print(number, "x", i, "=", number*i)
else:
    print("wrong")
