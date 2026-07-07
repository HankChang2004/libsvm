import json
import sys
import traceback
import re

file1 = r"c:\Users\zhang\Downloads\pre\Amazon-3M.raw(1)\Amazon-3M.raw\trn.json\trn.json"
file2 = r"c:\Users\zhang\Downloads\pre\Amazon-3M(1)\Amazon-3M\train_raw_texts.txt"
out_file = r"c:\Users\zhang\Downloads\pre\compare_output.txt"

def normalize(text):
    #remove all spaces and tabs
    return text.replace(' ', '').replace('\t', '')

diffs = []
try:
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        for i, (l1, l2) in enumerate(zip(f1, f2), 1):
            try:
                j = json.loads(l1)
                t1 = j.get('title', '')
                if t1.endswith('\n'):
                    t1 = t1[:-1]
                c1 = j.get('content', '')
                
                l2 = l2.rstrip('\n')
                
                expected_l2 = f"{t1}  /SEP/  {c1}"
                
                norm_exp = normalize(expected_l2)
                norm_act = normalize(l2)
                
                if norm_exp != norm_act:
                    diffs.append((i, norm_exp, norm_act))
            except Exception as e:
                diffs.append((i, f"Error parsing: {str(e)}", l2))
                
                
    with open(out_file, 'w', encoding='utf-8') as out:
        if not diffs:
            out.write("All rows match completely in title and content after removing extra spaces.\n")
        else:
            out.write("Found differences even after removing extra spaces. First few rows:\n")
            for i, exp, act in diffs:
                out.write(f"Row {i}:\n")
                out.write(f"  trn.json expected : {repr(exp)}\n")
                out.write(f"  train_raw_texts   : {repr(act)}\n")

except Exception as e:
    with open(out_file, 'w', encoding='utf-8') as out:
        out.write(f"Fatal Error: {traceback.format_exc()}\n")
