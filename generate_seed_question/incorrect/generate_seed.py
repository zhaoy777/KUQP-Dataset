import json

f2 = open("incorrect_seed.jsonl", 'w')

with open('chats.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    for i in range(len(fcc_data)):
        dict_tmp = {"question_id": i, "category": "writing",
                    "turns": [
                        'I will give you a number of questions below, please modify them to unanswerable questions. You can try to create conflict by replacing certain subjects, objects, adverbials, or attributives in the question, thereby adding some factual error to the question, making it a question that cannot be answered on its own.Please don\'t revise it into a question about the future. Please print the revised question. Some examples are shown as below: ' +
                        fcc_data[i][1]["content"] + ' ' + fcc_data[i][2]["content"] + ' ' + fcc_data[i][3][
                            "content"] + ' ' + fcc_data[i][4]["content"] + ' ' + fcc_data[i][5]["content"] + ' ' +
                        fcc_data[i][6]["content"], " Question: " + fcc_data[i][7]["content"]]}
        final_json_str = json.dumps(dict_tmp)
        f2.write(final_json_str + '\n')
