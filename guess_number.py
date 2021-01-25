import random
random_number = random.randint(1, 100)
count = 0
while True:
	count += 1 # count += 1 就是 count = count + 1的快速寫法
	print('目前猜第', count, '次')
	guess_number = int(input('請猜數字1-100: '))
	if guess_number > random_number:
		print('比答案大')
	elif guess_number < random_number:
		print('比答案小')
	else: # 也可寫elif guess_number == random_number:
		print('終於猜對了!')
		break
