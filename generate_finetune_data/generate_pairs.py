import json
import re

category_list = ['ambiguous', 'futuristic', 'incomplete', 'incorrect']

for category in category_list:
    f2 = open(category + "_train_pairs.json", 'w')

    with open(category + '_final_train_question_answer.jsonl', 'r') as fcc_file:
        contents = fcc_file.readlines()

    with open(category + '_final_train_question.jsonl', 'r') as fcc_file_q:
        contents1 = fcc_file_q.readlines()

    i = 0
    for item in contents:
        fcc_data = json.loads(item)
        list_tmp = fcc_data["choices"][0]['turns']
        sentence = list_tmp[1].replace("\n", " ")
        fcc_data_q = json.loads(contents1[i])
        question = fcc_data_q["turns"][1][10:]
        dict1 = {
            'instruction': question,
            'input': '',
            'output': sentence
        }
        final_json_str = json.dumps(dict1)
        f2.write(final_json_str + ',\n')
        i += 1

