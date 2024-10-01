import json

f2 = open("incomplete_seed.jsonl", 'w')

with open('chats.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    for i in range(len(fcc_data)):
        dict_tmp = {"question_id": i, "category": "writing",
                    "turns": [
                        fcc_data[i][0]["content"],
                        fcc_data[i][1]["content"] + ' ' + fcc_data[i][2]["content"] + ' ' + fcc_data[i][3][
                            "content"] + ' ' + fcc_data[i][4]["content"] + ' ' + fcc_data[i][5]["content"] + ' ' +
                        fcc_data[i][6]["content"],  fcc_data[i][7]["content"]]}
        final_json_str = json.dumps(dict_tmp)
        f2.write(final_json_str + '\n')
