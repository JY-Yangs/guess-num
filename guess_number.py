import random
random_number = random.randint(1, 100)
while True:
	guess_number = int(input('請猜數字1-100: '))
	if guess_number > random_number:
		print('比答案大')
	elif guess_number < random_number:
		print('比答案小')
	else: # 也可寫elif guess_number == random_number:
		print('終於猜對了!')
		break
