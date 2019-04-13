from word_generator import get_random_word

lives = 0

def start_game():
    lives= 6
    word = get_random_word()
    for x in range(len(word)):
        print('_', end = ' ')

if __name__ == '__main__':
    start_game()