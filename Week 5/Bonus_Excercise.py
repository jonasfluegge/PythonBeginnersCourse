user_input = int(input("Up to which number do you want all prime numbers: "))


def is_prime(user_input):
    input = user_input
    if input > 1:
        for i in range(2, input):
            if (input % i) == 0:
                return False
        else:
            return True
    else:
        return False


def prime_list(input_prime):
    listOfPrimes = []
    for i in range(2, input_prime):
        if is_prime(i):
            listOfPrimes.append(i)
    return listOfPrimes


print(prime_list(user_input))
