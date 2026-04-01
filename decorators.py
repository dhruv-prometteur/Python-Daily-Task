
# def pass_required(func):
#     def wrapper():
#         password=int(input("enter your password : "))
#         if password == 1234:
#             print("access granted")
            
#         else:
#             print("access denied")
#     return wrapper
# @pass_required
# def view_profile():
#     print("here is your profile info")

# view_profile()
# *************************************************************************

"""Create a decorator that measures how long a function takes to run and prints the time.
 Apply it to a function that performs a loop or some calculation."""
# import time
# def time_calculator(func):
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         result=func(*args,*kwargs)
#         end=time.time()
#         print(f"{func.__name__} is executed in {end-start : .4f} seconds")
#         return result
#     return wrapper
# @time_calculator
# def compute_squares(n):
#     return [i**2 for i in range(n)]

# re=compute_squares(100)
# print(re)


# *************************************************************************
"""
Create a decorator that prints the function name and all its arguments every time it is called.
 Apply it to a function that takes at least 2 arguments.
"""
# def log_argument(func):
#     def wrapper(*args,**kwargs):
        
#         print(f"the function name is {func.__name__}")
#         print(f"the arguments are args : {args} and kwargs : {kwargs}")
#         return func(*args,**kwargs)
#     return wrapper
# @log_argument
# def demo(*args,**kwargs):
#     print("hello this side")

# demo(7,8)

# ------------------------------------------------------------------------------
"""Create a decorator that retries a function 3 times if it raises an exception.
Apply it to a function that randomly raises an exception."""
# import random

# def retries_func(func):
#     def wrapper(*args,**kwargs):
#             trial=3
#             while trial > 0:
#                 try:
#                     result=func(*args,**kwargs)
#                     print("no exception raise ")
#                     print(f"trial attempted { 3-trial}")
#                     return result
#                 except:
#                     print("exception was raised")
#                     trial-=1
#             print("all attempts failed")
#     return wrapper
      

# @retries_func
# def raise_excp():
#         if random.randint(0,10) > 5 :
#              raise Exception("this is for testing exception") 
#         print("function succeed")
# raise_excp()

"""
Create a decorator that allows a function to run only if a global variable user_role 
matches the required role passed as an argument to the decorator. Otherwise, print “Access denied.”
        """


# def role_verified(func):
#     access_role="manager"
    
#     def wrapper(role):
#         if role==access_role:
#             return func(role)
#         print("Access Denied")
#     return wrapper

# @role_verified
# def delete_account(role):
#     print("Access Granted")

# delete_account("manager")


"""Create a decorator that stores the results of a function so that if the same input is used again, 
it returns the cached result instead of recomputing. 
Apply it to a recursive function like Fibonacci."""


def caching_deco(func):
    cache=[]
    def wrapper(*args,**kwargs):
        if func(*args,**kwargs) in cache:
            return cache[args]
        else :
            return func(*args,**kwargs)
    
    return wrapper
        
@caching_deco    
def fibonaci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    elif num==2:
        return [0,1]
    else:
        seq=fibonaci(num-1)
        seq.append(seq[-1]+seq[-2])
        return seq

result=fibonaci(5)
print(result)



