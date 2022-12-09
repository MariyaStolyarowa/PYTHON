# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
# in
# Number of words: -1
# out
# The data is incorrect
import random

txt = "абв"
count_word = (int(input("Количество слов в тексте: ")))
def create_text(count_word):
    str = ""
    for x in range(count_word):
        ran_txt = random.sample(txt, 3)
        str = str + ''.join(ran_txt) + " "
    return str
text = create_text(count_word)
print("Случайный текст: ")
print(text)
def del_no_need(text):
    no_need = input("Из текста нужно удалить: ")
    print(f"Текст без {no_need}: ")
    new_text = [i for i in text.split() if no_need not in i]
    return new_text
print(" ".join(del_no_need(text)))