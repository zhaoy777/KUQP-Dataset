import json
import re

f2 = open("incomplete_final_train_question.jsonl", 'w')

with open('incomplete_seed_answer.jsonl', 'r') as fcc_file:
    contents = fcc_file.readlines()

with open('incomplete_seed.jsonl', 'r') as seed_file:
    contents_q = seed_file.readlines()

i = 0
for item in contents:
    fcc_data = json.loads(item)
    id = fcc_data["question_id"]
    list_tmp = fcc_data["choices"][0]['turns']
    sentence = list_tmp[1].replace("\n", " ")
    list_tmp1 = re.findall(r'(Revised Statement:.*?Question:)', sentence)
    list_tmp2 = re.findall(r'(Question:.*\?)', sentence)
    turns = ["The following question is incomplete. Please answer the question by pointing out its incompleteness.", 'Question: ' + list_tmp1[0][19:-11] + ' ' + list_tmp2[0][10:]]
    dict_tmp = {"question_id": i, "category": "reasoning", "turns": turns}
    final_json_str = json.dumps(dict_tmp)
    f2.write(final_json_str + '\n')
    origin_str = json.loads(contents_q[int(id)])['turns'][1]
    list_tmp1 = re.findall(r'(Statement:.*?$)', origin_str)
    turns2 = ["The following question is known. Please answer the question.",
             'Question: ' + list_tmp1[0][11:] + ' ' + list_tmp2[0][10:]]
    dict_tmp2 = {"question_id": i + 1, "category": "reasoning", "turns": turns2}
    final_json_str2 = json.dumps(dict_tmp2)
    f2.write(final_json_str2 + '\n')
    i += 2
