student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
value: object
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")

result = {}
for (index, row) in data.iterrows():
    result.update({row.letter: row.code})
print(result)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = str(input("Enter the word: "))

my_list = []
for letter in word:
    for (key, value) in result.items():
        if letter.upper() == key:
            my_list.append(value)

print(my_list)






