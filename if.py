digit=range(100)
count=0
for n in digit:
    for temp in range(2,n):
        if n%temp==0:
            print(f"{n}不是素数")
            break
        else:
            print(f"{n}是素数")
            count+=1
            break
print(f"一个有{count}个素数")