

try:
    a=int(input("enter the number for a : "))
    b=int(input("enter the number for b : "))
    result=a/b
    print(result)
except ZeroDivisionError as zde:
    print("second value cant be zero for deviding",zde)

except ValueError as ve:
    print("please enter the valid value",ve)

except Exception as e:
    print("an Unexpected error is occured")

finally:
    print("Resource is Closed")

print("execution Completed")

