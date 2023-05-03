#swap 2 numbers
# a=[1,2,3,4,5,6,7,8,9]
# b=a[-3]
# a[-3]=a[4]
# a[4]=b
# print(a)


#largest no.
# x=int(input("enter first number: "))
# y=int(input("enter second number: "))
# z=int(input("enter third number: "))
# if (x>=y) and (x>=z):
#     print(f"{x} is the largest number")
# elif (y>=x) and (y>=z):
#     print(f"{y} is the largest number")
# else:
#     print(f"{z} is the largest number")


#reverse string
# a="uttkarsh chauhan"[::-1]
# print(a)


#multiply
# def multiply(a,b,c,d,e):
#     answer=(a*b*c*d*e)
#     return answer 
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# c=int(input("enter third number: "))
# d=int(input("enter fourth number: "))
# e=int(input("enter fifth number: "))
# product=multiply(a,b,c,d,e)
# print("Answer after multiplication: ",product)


#string present or not
a=["India is a beautiful country with various cultures and religions"]

for x in a:
    if "India" in x:
        print("India is present in the string")
    else:
        print("India is not present in the string")
