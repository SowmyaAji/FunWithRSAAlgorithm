'''
A demostration of the RSA Algorithm using two prime numbers greater than 100 and less than 200

'''
import random


def get_primes():
    ''' Get all prime numbers between 100 and 200 '''

    primes_list = [x for x in range(2, 200)
                   if all(x % y != 0 for y in range(2, x)) and x > 100]
    return primes_list


def get_pq(primes):
    ''' 
    Choose two prime numbers between 100 and 200 as basic keys 
    '''

    p = random.choice(primes)
    q = random.choice(primes)
    return p, q


def get_n(p, q):
    '''
    Get public key n by multiplying p and q
    '''
    return p * q


def gcd(a, b):
    '''
    Calculate the greatest common divisor of the two chosen numbers
    '''
    if a == 0:
        return b

    return gcd(b % a, a)


def get_possible_e(p, q, n):
    '''
    Get list of possible greatest common divisors and choose encryption key from them
    '''
    possibles = []
    for i in range(10, n-1):
        answer = gcd(i, ((p-1)*(q-1)))
        if answer == 1:
            possibles.append(i)
    e = random.choice(possibles)
    return e


def get_dk(p, q, e, n):
    '''
    Identify decrpytion key based on the encryption key and find k to multiply with ((p-1) * (q-1)) > also referred to as  theta(n)
    '''
    d = 2
    k = 0
    while d < n:
        d = ((k * (p-1)*(q-1)) + 1) / e
        if d.is_integer():
            break
        k += 1
    return int(d), k


def get_key_dict():
    '''
    Print a dictionary of keys and messages for demonstration purposes
    '''
    key_dict = {70: 'What is up?',
                71: 'You are fast!',
                72: 'All your trinkets belong to us.',
                73: 'Someone on our team thinks someone on your team are in the same class.',
                74: 'You are the weakest link.',
                75: 'Encryption is fun;',
                76: 'Spring is my favorite season',
                77: 'Enjoy your morning beverage',
                78: 'I am an early riser',
                79: 'I am not an early riser',
                80: 'Wake Tech is my school',
                81: 'CSC 120 Computing Fundamentals',
                82: 'Best wishes to you'
                }   # end of dictionary
    return key_dict


def get_input_key(key_dict):
    '''
    Get user input > a key to match to the messages in the key dictionary
    '''
    user_input = int(
        input("Pick a number key from this dictionary to encrypt your message! : "))
    if user_input in key_dict:
        return user_input
    else:
        print(f'Sorry that was an invalid key! See you around!')


def encrypt_key(user_input, e, n):
    '''
    Encrypt the message using the RSA Algorithm
    '''
    c = (user_input**e) % n
    return c


def decrypt_key(c, d, n):
    '''
    Decrypt the message using the RSA Algorithm
    '''
    m = (c**d) % n
    return m


def print_all():
    '''
    Holding function to print all the responses
    '''
    print(f'Let\'s have fun with the RSA Algorithm!')
    primes = get_primes()
    p, q = get_pq(primes)
    print(f'1. p = {p} and  q = {q}')
    n = get_n(p, q)
    e = get_possible_e(p, q, n)
    print(f'2. Public key: e = {e} and n = {n}')
    print(f'3. The gcd of e and (p-1) * (q-1) = {gcd(e, ((p-1)*(q-1)))}')
    d, k = get_dk(p, q, e, n)
    print(f'4. d = {d}  and  k = {k}')
    print(
        f'4a. The value of (e*d - 1)/(p-1)*(q-1) is: {int((e*d - 1)/(p-1)*(q-1))} ')
    key_dict = get_key_dict()
    print(f'5. Here is your original dictionary {key_dict}')
    user_input = get_input_key(key_dict)
    if user_input:
        c = encrypt_key(user_input, e, n)
        print(f'6. The encoded text for your message is: {c}')
        m = decrypt_key(c, d, n)
        print(
            f'7. The key and its original value are: key = {m}, value = { key_dict[m]}.')
        print(f'Have a nice day!')


if __name__ == '__main__':
    print_all()
