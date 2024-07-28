n=int(input("Enter a number to check whether it is a Prime Number or Not"))



def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number %i==0:
            is_prime=False
    if is_prime:
        print("It is a Prime Number")
    else:
        print("Its not a Prime Number")

prime_checker(number=n)
