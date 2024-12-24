import pickle
import os
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
from dotenv import load_dotenv, find_dotenv
from datetime import date

load_dotenv(find_dotenv())

ds = pd.read_csv(os.getenv("DATASET"), sep=',')

def apply_fpgrowth(data):
    pids = data['pid'].unique()
    matrix = [data.loc[data['pid'] == pid, 'track_uri'].tolist() for pid in pids]

    te = TransactionEncoder()
    te_ary = te.fit(matrix).transform(matrix)
    data_transformed = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = fpgrowth(data_transformed, min_support=0.1, use_colnames=True)

    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
    rules = rules[['antecedents', 'consequents', 'antecedent support', 'consequent support', 'confidence']]
    rules = rules.sort_values(by=["confidence"], ascending=False)
    return frequent_itemsets, rules

frequent_itemsets, rules = apply_fpgrowth(ds)

# with open('model/frequent_itemsets.pkl', 'wb') as f:
#     pickle.dump(frequent_itemsets, f)

with open('/model/rules.pkl', 'wb') as f:
    pickle.dump(rules, f)

with open('/model/date.pkl', 'wb') as f:
    pickle.dump(date.today(), f)


print(frequent_itemsets)
print(len(frequent_itemsets))
print()
print(rules)
print(len(rules))