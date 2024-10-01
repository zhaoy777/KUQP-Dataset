import json

f2 = open("ambiguous_seed.jsonl", 'w')

with open('chats.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    for i in range(len(fcc_data)):
        dict_tmp = {"question_id": i, "category": "reasoning", "turns": [fcc_data[i][0]["content"], fcc_data[i][1]["content"]]}
        print(dict_tmp)
        final_json_str = json.dumps(dict_tmp)
        f2.write(final_json_str + '\n')