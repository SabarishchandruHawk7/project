import csv
import re
import time
import psutil

#----starting time for performance file creation----#
start = time.time()

#------the find_words.txt file for reading---------#
words_txt = open(r".\find_words.txt", "r")
search_words = words_txt.read()
words_txt.close()
search_words_inlist = search_words.split()

#----------reading the find_words.txt file and counting how often each word appears--------#
recurrence = {}
william_text = open(r".\t8_shakespeare.txt", 'r')
text_string = william_text.read().lower()
match_ideal = re.findall(r'\b[a-z]{3,15}\b', text_string)

#-------Reading the dictionary.csv using a csv module to use a csv file as a dictionary--------#
with open(r".\french_dictionary.csv", mode='r') as dp:
    reviewer = csv.reader(dp)
    dict_from_csv = {rows[0]: rows[1] for rows in reviewer}

#--------making a list of all English terms in the find_words file in English---------#
absolute_eng = []
for word in match_ideal:
    if word in search_words_inlist:
        absolute_eng.append(word)
eng = set(absolute_eng)
eng = list(eng)    

#-----------making a list of all the French words in the find_words file in French--------#
french_lst = []
for x in eng:
    for key, value in dict_from_csv.items():
        if x in key:
            french_lst.append(value)

#----making a list of all words, recurrence and the number of times each word was replaced------#
recurrence = {}
for y in absolute_eng:
    count = recurrence.get(y, 0)
    recurrence[y] = count + 1

recurrence_list = recurrence.keys()
p = []
for z in recurrence_list:
    p.append(recurrence[z])

#------zipping to lists of words with corresponding frequencies in English and French (join tuples together)------#
last = list(zip(eng, french_lst, p))

#----generating regularity. English Word, French Word,---#
#----and recurrence should be the first line of a csv file, and this should be the first line of the file.----#
title = ['English Word', 'French Word', 'Recurrence']
with open(r'.\recurrence.csv', 'w', encoding='UTF8') as k:
    editor = csv.writer(k)

#----write the title(write the csv file)-----#
    editor .writerow(title)

    for row in last:
        for x in row:
            k.write(str(x) + ',')
        k.write('\n')

#------making t8.shakespeare.translated.txt, the processed output file containing the French translations of the words from Shakespeare-----#
trial_str = text_string
print("The correct string is : " + str(trial_str))
lookp_dict = dict_from_csv

inter = trial_str.split()
res = []
for wrds in inter:
    res.append(lookp_dict.get(wrds, wrds))

res = ' '.join(res)

f = open(r".\t8_shakespeare.translated.txt", "w")
f.write(str(res))
f.close()

#----creating performance.txt having the time taken for the script to complete and the second line should have the-----#
#----memory used by your script-----#
time_taken = time.time() - start
memory_taken = psutil.cpu_percent(time_taken)
f = open(r".\performance.txt", "w")
f.write(f'Time to process: 0 minutes {time_taken} seconds\nMemory used: {memory_taken} MB')
f.close()

