PATTERN = 7777777
NUMBERS_LENGTH = 10

digits_to_add = NUMBERS_LENGTH - len(str(PATTERN))
number_of_cases = digits_to_add + 1
number_list = []


def prime_number_check(combination):
    amount = 0
    for i in combination:
        is_prime = True
        for x in range(2, int(i**0.5) + 1):
            if (i % x) == 0:
                is_prime = False
                break
        if is_prime:
            amount += 1
    return amount


def generate():
    number_bit_range = [i for i in range(0, 10**digits_to_add)]
    for bit in number_bit_range:
        bit = str(bit)
        if len(bit) < digits_to_add:
            bit = '0'*(digits_to_add - len(bit)) + bit
        for case_position in range(len(bit)+1):
            number = bit[:case_position] + str(PATTERN) + bit[case_position:]
            number = int(number)
            if len(str(number)) == NUMBERS_LENGTH:
                if number not in number_list:
                    number_list.append(number)
    return(number_list)


print(prime_number_check(generate()))