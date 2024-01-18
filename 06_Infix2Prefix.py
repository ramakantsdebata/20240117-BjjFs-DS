def infix_to_prefix(infix):
    infix = infix.replace(' ', '')
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    prefix = ''
    for char in infix[::-1]:
        if char.isalpha() or char.isdigit():
            prefix += char
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != ')' and precedence[char] < precedence[stack[-1]]:
                prefix += stack.pop()
            stack.append(char)
    while stack:
        prefix += stack.pop()
    return prefix[::-1]

# Example usage
infix_exp = "A + B * C - D / E + F"
prefix_exp = infix_to_prefix(infix_exp)
print("Infix Expression:", infix_exp)
print("Prefix Expression:", prefix_exp)
