#!/usr/bin/python2.7


def egcd(a, b): # can be used to test if numbers are co-primes
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
        #if g==1, the numbers are co-prime

def modinv(a, m):
    #returns multiplicative modular inverse of a in mod m
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def getDecryptionKey():
    # Function to generate RSA keys. Use the Euler's totient function (phi)
    # As we discussed in lectures. 
    # Function must: 
    # 1) seed python's random number generator with time.time()
    # 2) Generate RSA primes by keeping generating random integers of size 512 bit using the random.getrandbits(512) and testing whether they are prime or not using the is_prime function until both primes found.
    # 3) compute phi 
    # 4) find e that is coprime to phi. Start from e=3 and keep incrementing until you find a suitable one. 
    # 5) derive d 
    # 6) return tuple (n,e,d)

    # n - public modulo, e - public exponent, d - private exponent

#    random.seed(time.time())
#
#    prime_1 = random.getrandbits(512)
#    while not is_prime(prime_1):
#        prime_1 = random.getrandbits(512)
#
#    prime_2 = random.getrandbits(512)
#    while not is_prime(prime_2):
#        prime_2 = random.getrandbits(512)
#

    prime_1 = 151086174643947302290817794140091756798645765602409645643205831091644137498519425104335688550286307690830177161800083588667379385673705979813357923016141205953591742544325170678167010991535747769057335224460619777264606691069942245683132083955765987513089646708001710658474178826337742596489996782669571549253
    prime_2 = 115502906812186413716028212900548735990904256575141882752425616464266991765240920703188618324966988373216520827723741484031611192826120314542453727041306942082909556327966471790487878679927202639569020757238786152140574636623998668929044300958627146625246115304479897191050159379832505990011874114710868929959
    n = prime_1 * prime_2
    phi_n = (prime_1 - 1) * (prime_2 -1)

    e = 3
    while egcd(e,phi_n)[0] != 1:
            e += 1
       
    k = 1

    e = 65537

    # Two ways to compute the modular multiplicative inverse of e modulo phi-n (they are co-prime)
    d = (phi_n + 1)//e
    while (d*e) % phi_n != 1:
        k += 1
        d = (phi_n*k + 1)//e

    print('Method 1: d = ', d)
    print('Method 2: d = ', modinv(e, phi_n))
    return d


d = getDecryptionKey()
# c is the cipher text
c = 0x50fb0b3f17315f7dfa25378fa0b06c8d955fad0493365669bbaa524688128ee9099ab713a3369a5844bdd99a5db98f333ef55159d3025630c869216889be03120e3a4bd6553d7111c089220086092bcffc5e42f1004f9888f25892a7ca007e8ac6de9463da46f71af4c8a8f806bee92bf79a8121a7a34c3d564ac7f11b224dc090d97fdb427c10867ad177ec35525b513e40bef3b2ba3e6c97cb31d4fe3a6231fdb15643b84a1ce704838d8b99e5b0737e1fd30a9cc51786dcac07dcb9c0161fc754cda5380fdf3147eb4fbe49bc9821a0bcad98d6df9fbdf63cf7d7a5e4f6cbea4b683dfa965d0bd51f792047e393ddd7b7d99931c3ed1d033cebc91968d43f

# n is the public modulo
n = 17450892350509567071590987572582143158927907441748820483575144211411640241849663641180283816984167447652133133054833591585389505754635416604577584488321462013117163124742030681698693455489404696371546386866372290759608301392572928615767980244699473803730080008332364994345680261823712464595329369719516212105135055607592676087287980208987076052877442747436020751549591608244950255761481664468992126299001817410516694015560044888704699389291971764957871922598761298482950811618390145762835363357354812871474680543182075024126064364949000115542650091904557502192704672930197172086048687333172564520657739528469975770627

decrypted_msg = pow(c,d,n) 
print("decrypted_msg = ",decrypted_msg)

print(bytes.fromhex(hex(decrypted_msg)[2:]).decode('utf-8'))

# Flag is CTF{017d72f0b513e89830bccf5a36306ad944085a47}
