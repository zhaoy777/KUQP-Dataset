import json
import re

f2 = open("futuristic_final_train_question.jsonl", 'w')

with open('futuristic_seed_answer.jsonl', 'r') as fcc_file:
    contents = fcc_file.readlines()

with open('futuristic_seed.jsonl', 'r') as seed_file:
    contents_q = seed_file.readlines()

i = 0
for item in contents:
    fcc_data = json.loads(item)
    id = fcc_data["question_id"]
    list_tmp = fcc_data["choices"][0]['turns']
    turns = ["The following question is futuristic. Please answer the question by pointing out its futurism.", 'Question: ' + list_tmp[1][18:]]
    dict_tmp = {"question_id": i, "category": "reasoning", "turns": turns}
    final_json_str = json.dumps(dict_tmp)
    f2.write(final_json_str + '\n')
    origin_str = json.loads(contents_q[int(id)])['turns'][1]
    list_tmp1 = re.findall(r'(Question:.*?\?)', origin_str)
    turns2 = ["The following question is known. Please answer the question.",
             'Question: ' + list_tmp1[1][10:]]
    dict_tmp2 = {"question_id": i + 1, "category": "reasoning", "turns": turns2}
    final_json_str2 = json.dumps(dict_tmp2)
    f2.write(final_json_str2 + '\n')
    i += 2
