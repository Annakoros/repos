from functools import reduce
result = []
firm_dict = {}
looser_dict = {}
profit_num = 0
with open('firm_data_5_7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        data_l = line.split()
        name = data_l[0]
        profit = int(data_l[2]) - int(data_l[3])
        if profit > 0:
            firm_dict.update({name: profit})
            profit_num += 1
        else:
            looser_dict.update({name: profit})
av_profit = sum(firm_dict.values())/profit_num
firm_dict.update(looser_dict)
result.extend([firm_dict, {"average_profit": av_profit}])
import json
with open("firm_data_5_7.json","w") as f_json:
    json.dump(result, f_json)