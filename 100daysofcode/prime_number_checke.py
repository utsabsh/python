num = int(input("enter a number: "))
def check(num):
    is_prime = True
    for i in range(2,num):
        if num %i == 0:
         is_prime = False
    if is_prime:
       print("its a prime number")
    else:
       print("it is not prime number")     
check(num)