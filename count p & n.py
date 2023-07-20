def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num %i==0:
            return False
        return True
def count_primes_and_composites(number):
    prime_count=0
    composite_count=0
    for num in numbers:
        if is_prime(num):
            prime_count+=1
        else:
            composite_count+=1
    return prime_count, composite_count
numbers = input('enter a list of numbers separated by spaces:').split()
numbers=[int(num) for num in numbers]
prime_count,composite_count=count_primes_and_composites(numbers)
print('number of prime numbers:',prime_count)
print('number of composite numbers:',composite_count)
