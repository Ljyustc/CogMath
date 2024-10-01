import json
def load_jsonl(file):
    data = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            d = json.loads(line)
            data.append(d)
    return data

def write_jsonl(res, outfile):
    f = open(outfile, 'w', encoding='utf-8')
    for d in res:
        f.writelines(json.dumps(d, ensure_ascii=False))
        f.writelines('\n')
    f.close()

type_name = 'dimension_1'

# Inquiry agent
prompt_head = '"""Now you are a question rewriting agent with interleaving Thought, Action.Thought can be the process of rewriting.Action MUST BE THE REWRITE QUESTION WHICH REPHRASES THE QUESTION.\nYou will be provided with a math problem. Please rephrase the question in a different way.\nHere are an example:\nQuestion: Gloria is shoe shopping when she comes across a pair of boots that fit her shoe budget. However, she has to choose between the boots and two pairs of high heels that together cost five dollars less than the boots. If one pair of heels costs $33 and the other costs twice as much, how many dollars are the boots.\nThought: Identify the main elements (character Gloria, items boots and high heels, price relationship), analyze the price relationship (high heels cost $33 and $66, total $99 is $5 less than boots, making boots $104), find the logical relationship (choice, price relationship, and calculation), and change the character (to Alice) and item names (to sneakers and sandals) to rewrite the problem while keeping the prices and relationships the same.\nAction:Alice is shopping for footwear when she finds a pair of sneakers that fit her budget. However, she has to choose between the sneakers and two pairs of sandals that together cost five dollars less than the sneakers. If one pair of sandals costs $33 and the other costs twice as much, how many dollars are the sneakers?\n\nNow, here is your question:\nQuestion:'
prompt_end = '"""'
test_data = load_jsonl("GSM8K_test.jsonl")
test_gsm8k_trans = []
for i in range(len(test_data)):
    id_ = type_name + '@' + str(i)
    test_gsm8k_trans.append({"id": id_, "query": prompt_head+test_data[i]['question']+prompt_end})


# Judge agent
paraphrase_eval_prompt = """Now you are a judge agent with interleaving Thought, Action.Your task is to determine if the rewritten question is a rephrased version of the original question.Thought can be articulating the logical relationship between the original question and the rewritten question, and analyze whether the logical relationship between the two is consisten. Action must be Yes or No.
Here are an example:
Original question: Janet\u2019s ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?
Rewritten question: \nKevin\u2019s chickens lay 16 eggs each day. He consumes three for his morning meal and uses four to make pastries each day for his neighbors. The remaining eggs are sold at the local farmers' market daily for $2 per egg. How much money does Kevin earn from egg sales each day at the market?
Thought:
Original Question Key Elements:
Subject: Janet’s ducks
Daily egg production: 16 eggs
Daily consumption: 3 eggs for breakfast, 4 eggs for muffins
Selling price: $2 per egg
Question focus: Daily earnings from selling eggs at the farmers' market

Rewritten Question Key Elements:
Subject: Kevin’s chickens
Daily egg production: 16 eggs
Daily consumption: 3 eggs for morning meal, 4 eggs for pastries
Selling price: $2 per egg
Question focus: Daily earnings from selling eggs at the farmers' market

the rewritten question is a rephrased version of the original question. Both questions convey the same information and ask the same type of question, with only the subject (Janet’s ducks vs. Kevin’s chickens) and the specific uses of the eggs (breakfast vs. morning meal, muffins vs. pastries) being slightly different. The logical relationship between the two questions is consistent.
Action:Yes

Now, here are your raw question and rewritten question:
Original question:{question}
Rewritten question:{rewritten_question}
"""

new_data = load_jsonl("result of test_gsm8k_trans")
rephrase_eval = []
for d in new_data:
    prompt = paraphrase_eval_prompt.replace("{question}", new_data[d]['ori_question']).replace("{rewritten_question}", new_data[d]['new_question'])
    rephrase_eval.append({"id": d, "query": prompt})
write_jsonl(rephrase_eval, "GSM8K_dimension1_judge.json")