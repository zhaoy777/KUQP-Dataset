import json

f2 = open("incorrect_final_train_question.jsonl", 'w')

with open('incorrect_seed_answer.jsonl', 'r') as fcc_file:
    contents = fcc_file.readlines()

with open('incorrect_seed.jsonl', 'r') as seed_file:
    contents_q = seed_file.readlines()

i = 0
for item in contents:
    fcc_data = json.loads(item)
    id = fcc_data["question_id"]
    list_tmp = fcc_data["choices"][0]['turns']
    turns = ["The following question is incorrect. Please answer the question by pointing out its incorrectness.", 'Question: ' + list_tmp[2][18:]]
    dict_tmp = {"question_id": i, "category": "reasoning", "turns": turns}
    final_json_str = json.dumps(dict_tmp)
    f2.write(final_json_str + '\n')
    origin_str = json.loads(contents_q[int(id)])['turns'][2][10:]
    turns2 = ["The following question is known. Please answer the question.",
              'Question: ' + origin_str]
    dict_tmp2 = {"question_id": i + 1, "category": "reasoning", "turns": turns2}
    final_json_str2 = json.dumps(dict_tmp2)
    f2.write(final_json_str2 + '\n')
    i += 2
