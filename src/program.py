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
	indices = find_indices(inp)
	print(indices)

	if len(indices) == 0:
		global lives
		lives = lives - 1
		print('Wrong')
		if lives == 0:
			print('Game Over')
			print(word)
			return
	else:
		for x in indices:
			out[x] = inp
		if word.find(empty_char) == -1:
			print('You Won!!!')
			return

	print_output()
	take_input()


def find_indices(c):
	global word
	out = []
	for i in range(len(word)):
		print(word[i] == c)
		if word[i] == c:
			out.append(i)
	
	return out


if __name__ == '__main__':
    start_game()