import random
start = int(input('請輸入從多少開始猜: '))
end = int(input('請輸入猜到多少: '))
random_number = random.randint(start, end)
count = 0
while True:
	count += 1 # count += 1 就是 count = count + 1的快速寫法
	print('目前猜第', count, '次')
	guess_number = int(input('請開始猜數字: '))
	if guess_number > random_number:
		print('比答案大')
	elif guess_number < random_number:
		print('比答案小')
	else: # 也可寫elif guess_number == random_number:
		print('終於猜對了!')
		break
