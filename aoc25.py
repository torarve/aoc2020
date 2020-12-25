def get_input():
    with open('input25.txt') as file:
        return [int(x.strip()) for x in file]

def transform(subject_number, loop_size, modulo):
    return pow(subject_number, loop_size, modulo)

def brute_force(public_key, subject_number, modulo):
    private_key = 1
    current = subject_number
    while current!=public_key:
        current = (current * subject_number) % modulo
        private_key += 1
    return private_key

public_key_1, public_key_2 = get_input()

private_key_1 = brute_force(public_key_1, 7, 20201227)
private_key_2 = brute_force(public_key_2, 7, 20201227)

print(private_key_1, private_key_2)
print(transform(public_key_2, private_key_1, 20201227))