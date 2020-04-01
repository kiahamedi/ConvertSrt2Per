
#  kia  hamedi
# www.kiahamedi.ir
#kia.arta9793@gmail.com

import sys
from sys import platform
from os import system
from importlib import reload
from googletrans import Translator


reload(sys)

translator = Translator()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

number_of_lines = 0
translated_lines = 0

print('--------------------------------------------------')

if platform == "linux" or platform == "linux2":
    print("Total Lines:")
    system("cat {} | wc -l ".format(input_file_name.replace(' ','\ ')))

f_out = open(output_file_name, 'w')
with open(input_file_name) as f_in:
    lines = f_in.readlines()

    for line in lines:
        number_of_lines += 1
        print("> Line of: " + str(number_of_lines))
        if line.isdigit() and len(line) < 4:
            f_out.write(line)
            continue
 
        if line.startswith('0'):
            f_out.write(line)
            continue

        if line.startswith('<font'):
            f_out.write(line)
            continue
        
        if line.startswith('\n'):
            f_out.write(line)
            continue

        translated = translator.translate(line, src='en', dest='fa')
        f_out.write(translated.text + "\r\n")
        translated_lines += 1

f_in.close()
f_out.close()
print('--------------------------------------------------')
print("Total number of lines is:", str(number_of_lines))
print("Total number of translated lines is:", str(translated_lines))
