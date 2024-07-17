numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  #Primes: [2, 3, 5, 7, 11, 13]
not_primes = []  #Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]
# count = 0
# for i in range(len(numbers)):
#     for j in range(1, numbers[i] + 1):
#         if numbers[i] % j == 0:
#             count += 1
#             if count > 2 or (j != 1 and j != numbers[i]):
#                 break
# print('Primes: ', i)

for i in numbers:
    #print(i)
    is_prime = True
    for j in range(2, i):
        #print('   ', j)
        if i % j == 0:
            is_prime = False
            break

    if is_prime == False:
        not_primes.append(i)
    else:
        primes.append(i)
primes.remove(1)

print('Primes: ', primes)
print('Not Primes: ', not_primes)

