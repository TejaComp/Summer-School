def parse_list(lst, index):
    result = []
    while index < len(lst):
        item = lst[index]
        if item == '(':
            sublist, index = parse_list(lst, index + 1)
            result.append(sublist)
        elif item == ')':
            return result, index
        else:
            result.append(item)
        index += 1
    return result, index

def evalexp(exp, env):
    if isinstance(exp, list):
        if exp[0] == 'let':
            variables = exp[1]
            body = exp[2]
            new_env = env.copy()
            for var, val_exp in variables:
                val = evalexp(val_exp, env)
                new_env[var] = val
            return evalexp(body, new_env)
        elif exp[0] == 'lambda':
            params = exp[1]
            body = exp[2]
            return lambda *args: evalexp(body, {**env, **dict(zip(params, args))})
        elif exp[0] == '+':
            return sum(evalexp(item, env) for item in exp[1:])
        elif exp[0] == '-':
            return evalexp(exp[1], env) - sum(evalexp(item, env) for item in exp[2:])
        elif exp[0] == '*':
            result = 1
            for item in exp[1:]:
                result *= evalexp(item, env)
            return result
        elif exp[0] == '/':
            result = evalexp(exp[1], env)
            for item in exp[2:]:
                result /= evalexp(item, env)
            return result
    elif exp in env:
        return env[exp]
    else:
        try:
            return int(exp)
        except ValueError:
            raise ValueError(f"Unknown expression: {exp}")


with open("x.sexp", "r") as f:
    lis = f.read().strip()
    lis = lis.replace('(', ' ( ').replace(')', ' ) ')
    x = lis.split(" ")
    y = ' '.join(x).split()
    z = list(y)
    modified_list, _ = parse_list(z, 0)

env = {"a": 6}

result = evalexp(modified_list[0], env)
print(result)

