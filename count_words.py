file = open('count_words.txt', 'r')
r= file.read()
per_word =r.split()
print('Total Words:', len(per_word))

