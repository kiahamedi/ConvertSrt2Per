
#  kia  hamedi
# www.kiahamedi.ir
#kia.arta9793@gmail.com

import sys
from importlib import reload
from googletrans import Translator


reload(sys)

translator = Translator()

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

f_out = open(output_file_name, 'w')

with open(input_file_name) as f_in:
    lines = f_in.readlines()

    for line in lines:
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

f_in.close()
f_out.close()



