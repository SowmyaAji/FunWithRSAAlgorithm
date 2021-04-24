# 1.	Select two distinct primes larger than 100.  Call them p  q.   (do not ask the user )
# 2.	Let n = p*q
# print n, p, and q
# 3.	Select an integer e  in the range 1 < e < n such that gcd (e, (p-1)(q-1) ) == 1 with e > 10
# The gcd calculation means that e and (p-1)*(q-1) do not share a common factor.  Recall that 35(==7*5) and 6(==2*3) are relatively prime even though neither is prime
# print e, gcd(e,(p-1)*(q-1) )
# The public key is the pair (e,n)
# 4.	Compute d in the range 1 < d < n  such that d*e = 1 mod ( ( p-1)*(q-1) ) which means
#  e*d -1 == k*(p-1)*(q-1)  for k = 1,2,3, etc
# This can be computed as follows:
# Find d such that
# e*d -1 == k(p-1)*(q-1)    d =  [k(p-1)*(q-1) +1] /e  for k = 1, 2 3 4 5 etc.
# Suggestion:  use a while loop for k = 1, 2, 3,  4 until [k(p-1)*(q-1) +1] /e  does NOT result in a decimal value for d this is your d
# The private key is the pair (d,n)  This should be kept secret!
# print d
# print( (e*d -1 )/(p-1)*( q-1) )   # should be an integer
# 5.	Ask the user for a key (integer) from the dictionary below (see source code tab)
# See the keys and their values but the user input should be an integer in the range 70 – 82
# print key and the value
# 6.	Encode the key by using the public key as follows:
# c  = me mod n  See Khan video for assistance
# 	print c   as follows: print(“the encoded text is “,c)
# 7.	Decode:  We decrypt message c to obtain the original key using the private key d
#  m = cd mod n
# print (key, value) (should be the key and the original message )
# for example if the user enters the integer 77 in step 5 then you should print out 77 and  the text 'Enjoy your morning beverage'
# Use the messages dictionary available in the Source code tab RSATemplate.py and duplicated here:
# # dictionary
import random


def get_primes():
    primes_list = [x for x in range(2, 200)
                   if all(x % y != 0 for y in range(2, x)) and x > 100]
    return primes_list


def get_pq(primes):
    p = random.choice(primes)
    q = random.choice(primes)
    return p, q


def get_n(p, q):
    return p * q


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


def get_possible_e(p, q, n):
    possibles = []
    for i in range(10, n-1):
        answer = gcd(i, ((p-1)*(q-1)))
        if answer == 1:
            possibles.append(i)
    e = random.choice(possibles)
    return e


def get_dk(p, q, e, n):
    d = 2
    k = 0
    while d < n:
        d = ((k * (p-1)*(q-1)) + 1) / e
        if d.is_integer():
            break
        k += 1
    return int(d), k


def get_key_dict():
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
    user_input = int(
        input("Pick a number key from this dictionary to encrypt your message! : "))
    if user_input in key_dict:
        return user_input
    else:
        print(f'Sorry that was an invalid key! See you around!')


def encrypt_key(user_input, e, n):
    c = (user_input**e) % n
    return c


def decrypt_key(c, d, n):
    m = (c**d) % n
    return m


def print_all():
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
