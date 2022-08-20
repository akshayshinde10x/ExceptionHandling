l = [10, 20, 30, 40]
avgAge = 70
age = int(input("Age: "))
dict = {"name":"Paresh"}
try:
    print(l[age])
    lifeSpan = avgAge / age
    print(lifeSpan)
    print(dict["City"])
except ZeroDivisionError as e:
    print("Can't divide by zero")
except IndexError as ve:
    print("Please enter valid number")






