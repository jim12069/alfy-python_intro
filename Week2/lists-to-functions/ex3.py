def input_list_helper():
    """Helper function for 'input_list()'.
    Collects numbers from user input. Asks for a number from
    user until user submits empty string."""
    num_str = input()
    num_list = []
    while num_str != "":
        num = int(num_str)
        num_list.append(num)
        num_str = input()
    return num_list
    

def input_list():
    """Takes a list of numbers from user input, calculates their sum,
    and returns the list of numbers, with the last number being
    the sum of all the others"""
    user_input = input_list_helper()
    total = 0
    for num in user_input:
        total += num
    user_input.append(total)
    return user_input

#print(input_list())

def check_monotonic_sequence(sequence):
    """Monotonicity type from a sequence of numbers.
    Returns list of 4 Booleans representing 4 monotonicity characters:
    # Index 0: monotonicity up
    # Index 1: monotonicity up strong
    # Index 2: monotonicity down
    # Index 3: monotonicity down strong
    """
    bool_list = [True, True, True, True]
    if sequence == None or len(sequence) <= 1:
        return bool_list
    for idx, seq in enumerate(sequence):
        if idx != len(sequence) - 1:
            if sequence[idx + 1] > seq:
                bool_list[2] = False
                bool_list[3] = False

            elif sequence[idx + 1] < seq:
                bool_list[0] = False
                bool_list[1] = False

            elif sequence[idx + 1] == seq:
                bool_list[1] = False
                bool_list[3] = False
    return bool_list

#print(check_monotonic_sequence ([1,2,3,4,5,6,7,8]))
#print(check_monotonic_sequence ([1,2,2,3]))
#print(check_monotonic_sequence ([7.5, 4, 3.141, 0.111]))
#print(check_monotonic_sequence ([1, 0, -1, 1]))

def check_monotonic_sequence_inverse(def_bool):
    """Checks list of 4 booleans against valid lists of monotonicity cases.
    If it matches, the corresponding monotonicity case is returned.
    Otherwise, 'None' is returned.
    """
    match def_bool:
        case [True, True, False, False]:
            return [0, 1, 2, 3]
        case [True, False, False, False]:
            return [0, 1, 1, 2]
        case [False, False, True, True]:
            return [3, 2, 1, 0]
        case [False, False, True, False]:
            return [2, 1, 1, 0]
        case _:
            return None

#print(check_monotonic_sequence_inverse([True, False, False, False]))


def primes_generator(n):
    """Finds and returns a list of prime numbers with 'n' primes in it.
    Starting from 'prime_candidate' of 2, check if it is prime.
    If the prime_candidate is a prime, append it to the 'primes' list,
    increment prime_candidate by 1, and check if the new number is prime.
    Keep going until the list of prime numbers has 'n' numbers.
    """
    prime_candidate = 2  # number to test to see if it is a prime
    primes = []  # list to hold the prime numbers found

    # Check for primes until number of primes discovered reaches 'n'
    while len(primes) < n:
        isPrime = True
        
        for num in range(2, prime_candidate + 1):

            # Check if remainder occurs.
            # If it does, change flag to False.
            if prime_candidate % num == 0 and prime_candidate != num:
                isPrime = False  # remains false throughout for loop
                
        if isPrime == True:
            primes.append(prime_candidate)
        prime_candidate += 1
                
    return primes

#print(primes_generator(10))


def is_empty_vector(vec_list):
    """Helper function for 'vectors_list_sum()'.
    Checks if a vector list is empty.
    Returns True when empty and False when not empty.
    """
    if len(vec_list) == 0:
        return True
    return False

def vectors_list_sum(vec_list):
    """Takes list of vectors and returns a vector of their sum"""
    if is_empty_vector(vec_list) == False:
        vec_sum = []
        for index in range(len(vec_list[0])):
            sum = 0
            for vec in vec_list:
                sum += vec[index]
            vec_sum.append(sum)
        return vec_sum
    else:
        return "empty"

#print(vectors_list_sum([]))
#print(vectors_list_sum([[1, 1], [1, 3]]))
#print(vectors_list_sum([[1, 1, 1], [1, 0, 0], [0, 0, 100]]))
    


def calc_the_inner_product(vec_1, vec_2):
    """Helper function for 'orthogonal_number()'.
    Calculates the inner product of two lists.
    """
    if len(vec_1) != len(vec_2):
        return None
    sum = 0
    for index in range(len(vec_1)):
        sum += vec_1[index] * vec_2[index]
    return sum

def orthogonal_number(vectors):
    """Determine how many pairs of vectors in
    a list of vectors are orthogonal.
    Return the number of pairs as an 'int'.
    """
    count = 0
    for idx_1st in range(len(vectors) - 1):
        for idx_2nd in range(idx_1st + 1, len(vectors)):
            inner_product = calc_the_inner_product(vectors[idx_1st], vectors[idx_2nd])
            if inner_product == 0:
                count += 1
    return count

#print(orthogonal_number([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
#print(orthogonal_number([[0, 0, 0], [0, 1, 0], [0, 0, 1]]))
#print(orthogonal_number([[0, 0], [1, 2], [10, 5]]))
#print(orthogonal_number([[1, 1, 1, 1],
                          #[2, 1, 3, 3],
                          #[0, 0, 100, 33],
                          #[8, 8, 8, 1.5],
                          #[9, 9, 9, 9]]))
#print(orthogonal_number([[0], [0], [0], [0]]))
