from word_generator import get_random_word

lives = 0
out = []
word = ''
empty_char = '_'

def start_game():
	global lives
	global word
	lives= 6
	word = get_random_word().rstrip()
	for i in range(len(word)):
		out.append(empty_char)
		
	print_output()
	take_input()

def print_output():
	for x in out:
		print(x, end = ' ')

def take_input():
	inp = input('Enter the character:')
	indices = find_indices(inp[0])

	if len(indices) == 0:
		global lives
		lives = lives - 1
		print('Wrong')
		print(f'{lives} lives left')
		if lives == 0:
			print('Game Over')
			print(word)
			return
	else:
		for x in indices:
			out[x] = inp

		if not (empty_char in out):
			print('You Won!!!')
			return

	print_output()
	take_input()


def find_indices(c):
	global word
	indices = []
	for i in range(len(word)):
		if word[i].lower() == c.lower():
			indices.append(i)
	
	return indices


if __name__ == '__main__':
    start_game()