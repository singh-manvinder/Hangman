from random import randint

file_path = '../data/sowpods.txt'

def get_random_word():
    with open(file_path) as f:
        lines = f.readlines()
        rand_int = randint(0, len(lines))

    return lines[rand_int]

if __name__ == '__main__':
    print(get_random_word())