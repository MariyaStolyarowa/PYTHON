# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся
#  в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q
file_name = input('Введите имя файла с текстом: ')
with open(file_name, 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст необходимый для сжатия: '))
with open(file_name, 'r') as file:
    txt = file.readline()
    txt_compresed = txt.split()
print(txt)

def encode(txt):
 
    encod_str = "" 
 
    i = 0
    while i < len(txt):
        count = 1
        while i + 1 < len(txt) and txt[i] == txt[i + 1]:
            count = count + 1
            i = i + 1
        encod_str += str(count) + txt[i]
        i = i + 1
    return encod_str

def decode(txt):
    decod_str = ''
    char_count = ''
    for i in range(len(txt)):
        if txt[i].isdigit():
            char_count += txt[i]
        else:
            decod_str += txt[i] * int(char_count)
            char_count = ''
    return decod_str
txt_compresed = encode(txt)
txt_decompresed = decode(txt_compresed)
encod_file_name = input('Введите имя файла для записи сжатого текста: ')

with open(encod_file_name, 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compresed}')
print(txt_compresed)

decod_file_name = input('Введите имя файла для записи восстановленного текста: ')

with open(decod_file_name, 'w', encoding='UTF-8') as file:
    file.write(f'{txt_decompresed}')
print(txt_decompresed)