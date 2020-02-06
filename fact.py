fact=int(input("enter a number"))
factorial =1
if fact<0:
    print("factorial is not found:")
elif fact==0:
    print("factorial is 0")
else:
    for i in range(1,fact+1):
        factorial=factorial*i

print("the factorial is ",factorial)