import json

f2 = open("futuristic_seed.jsonl", 'w')

with open('chats.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)
    for i in range(len(fcc_data)):
        dict_tmp = {"question_id": i, "category": "writing",
                    "turns": [
                        'Below I\'m going to give you a few questions that you need to modify into a question about the future that becomes unanswerable. You can change the part about time in the sentence to a time point in the future. Please output your revised question. '
                        "Question: " + fcc_data[i][3]["content"]]}
        final_json_str = json.dumps(dict_tmp)
        f2.write(final_json_str + '\n')
