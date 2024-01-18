def infix_to_postfix(infix):
    # Dictionary of operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Stack for operators and output queue
    op_stack = []
    output_queue = []

    # Split infix string into tokens
    tokens = infix.split()

    for token in tokens:
        # If token is an operator
        if token in precedence:
            # Pop operators from stack and add to output queue until
            # the top of the stack has lower precedence or is a left parenthesis
            while (op_stack and op_stack[-1] != '('
                   and precedence[token] <= precedence[op_stack[-1]]):
                output_queue.append(op_stack.pop())
            op_stack.append(token)
        # If token is a left parenthesis
        elif token == '(':
            op_stack.append(token)
        # If token is a right parenthesis
        elif token == ')':
            # Pop operators from stack and add to output queue until
            # a left parenthesis is found
            while op_stack and op_stack[-1] != '(':
                output_queue.append(op_stack.pop())
            # Discard the left parenthesis
            op_stack.pop()
        # If token is a number or variable
        else:
            output_queue.append(token)

    # Pop any remaining operators from the stack and add to output queue
    while op_stack:
        output_queue.append(op_stack.pop())

    # Join the output queue tokens into a single string and return
    return ' '.join(output_queue)


infix_expression = "a + b * c - d / e ^ f"
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)  # Output: "a b c * + d e f ^ / -"
