import json
import re

f2 = open("ambiguous_final_train_question.jsonl", 'w')

with open('ambiguous_seed_answer.jsonl', 'r') as fcc_file:
    contents = fcc_file.readlines()

with open('ambiguous_seed.jsonl', 'r') as seed_file:
    contents_q = seed_file.readlines()

i = 0
sum1 = 0
for item in contents:
    fcc_data = json.loads(item)
    id = fcc_data["question_id"]
    list_tmp = fcc_data["choices"][0]['turns']
    sentence = list_tmp[1].replace("\n", " ")
    list_tmp_q = re.findall(
        r'((What |What\'|How |Should|Can |Why |Is |Are |Did |Does |Were |Was |Do |Which |Who |Would |Could |Where |When).*?(\?))',
        sentence)
    list_tmp_rewritten = re.findall(r'(Rewritten statement 1.*?\.)', sentence)
    sentence_part = ""
    if len(list_tmp_rewritten) != 0:
        print(list_tmp_rewritten[0][23:])
        sentence_part = list_tmp_rewritten[0][23:]
    origin_str = json.loads(contents_q[int(id)])['turns'][1]
    list_tmp1 = re.findall(r'(Sentence: .*?Word:)', origin_str)
    turns = ["The following question is ambiguous. Please answer the question by pointing out its ambiguity.",
             'Question: ' + list_tmp1[0][10:-6] + ' ' + list_tmp_q[0][0]]
    turns2 = ["The following question is known. Please answer the question.", 'Question: ' + sentence_part + ' ' + list_tmp_q[0][0]]
    dict_tmp = {"question_id": i, "category": "reasoning", "turns": turns}
    dict_tmp2 = {"question_id": i + 1, "category": "reasoning", "turns": turns2}
    final_json_str = json.dumps(dict_tmp)
    final_json_str2 = json.dumps(dict_tmp2)
    i += 2
    f2.write(final_json_str + '\n')
    f2.write(final_json_str2 + '\n')
