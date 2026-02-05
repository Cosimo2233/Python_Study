# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# if a>b:
#     if b>c:
#         print("a>b>c")
#     elif a>c:
#         print("a>c>b")
#     elif c>a:
#         print("c>a>b")
# else:
#     if b>c:
#         if c>a:
#             print("b>c>a")
#         else:
#             print("b>a>c")

# 转换为数字进行数值比较
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if a > b:
    if b > c:
        print("a>b>c")
    else:  # b <= c
        if a > c:
            print("a>c>b")
        else:  # c >= a
            print("c>a>b")
else:  # a <= b
    if b > c:
        if a > c:
            print("b>a>c")
        else:  # c >= a
            print("b>c>a")
    else:  # b <= c
        print("c>b>a")        