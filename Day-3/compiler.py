#!/usr/bin/env python3
import json
import sys

in_prog=json.loads(sys.stdin.read())
#print(in_prog)

#in_prog = json.loads(sys.stdin.read())
#print(in_prog)

def convert_to_json(in_prog):
    outer_func = in_prog[0]
    define_list = in_prog[1]
    
    define = define_list[0]
    func, n = define_list[1]
    ret, ret_val = define_list[2]
    
    new_list = [
        "brilisp",
        [define, [[func, "int"], [n, "int"]], [ret, ret_val],[define[[g n]]]]
    ]
    
    ex_list = []
    for item in new_list:
        if isinstance(item, list):
            ex_list.extend(item)
        else:
            ex_list.append(item)
    
    return ex_list

output = convert_to_json(in_prog)

#print(output)

out_prog = json.dumps(output)
print(out_prog)

