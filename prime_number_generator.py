import sys, time


primes = []

def calculate_prime_numbers(last, iterations):
    elapsed_time_sum = 0
    for i in range(iterations):
        start = time.time()
        primes = [2]
        for possiblePrime in range(3, last+1, 2):
            isPrime = True
            for num in range(2, possiblePrime):
                if possiblePrime % num == 0:
                    isPrime = False
                    break
            
            if isPrime:
                primes.append(possiblePrime)
        end = time.time()
        elapsed_time = round(end-start, 4)
        elapsed_time_sum += elapsed_time
        print('Iteration: {}\nElapsed time: {}'.format(i+1, elapsed_time))
        print(primes[0:-1])
    return(elapsed_time_sum/iterations)

def print_help():
    print('Hi, this script is a prime number generators. The script uses 2 values: the biggest number to try and the number of iterations.')
    print('The first number is the biggest number to try, the second number is the number of iterations.')
    print("You can use the following command line: 'python prime_number_generator 1000 2' or just 'python prime_number_generator' without arguments.")
    sys.exit()


if len(sys.argv) == 1:
    try:
        last = int(input("Type the biggest number: "))
        iterations = int(input("Type the number of iterations: "))
    except:
        print("Invalid input!")
        sys.exit(1)

if len(sys.argv) == 2:
    arg1 = sys.argv[1]
    if arg1 == 'help' or arg1 == '?':
        print_help()
    else:
        try:
            int(arg1) > 0
            last = int(arg1)
            iterations = 1
        except:
            print("Invalid input!")
            sys.exit()


if len(sys.argv) == 3:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    try:
        last = int(arg1)
        iterations = int(arg2)
    except:
        print("Invalid input!")
        sys.exit()

average_time_elapsed = round(calculate_prime_numbers(last, iterations), 4)
print("\nAverage time elapsed: {}".format(average_time_elapsed))