def multi_bracket_validation(input):
    input_length = len(input)
    sep_input = list(input)
    input_checker = []
    validator = []

    if input_length == 0:
        return 'Please enter a valid input'

    for i in sep_input: 
        if i == '(' or i == '{' or i == '[' or i == ')' or i == '}' or i == ']':
            input_checker.append(i)
            validator.append(i)
        else:
            continue

    if len(input_checker) == 0:
        return 'Please enter an input with brackets to be validated'
    for i in input_checker: 
        if i == '(':
            for x in validator:
                if x == ')':
                    validator.remove(i)
                    validator.remove(x)
                    continue
                else:
                    continue                 
        elif i == '{':
            for x in validator:
                if x == '}':
                    validator.remove(i)
                    validator.remove(x)
                    continue
                else:
                    continue    
        elif i == '[':
            for x in validator:
                if x == ']':
                    validator.remove(i)
                    validator.remove(x)
                    continue
                else:
                    continue     
        else: 
            continue
    if len(validator) == 0:
        return True
    else:
        return False          






# Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

# Round Brackets : ()
# Square Brackets : []
# Curly Brackets : {}


# multi_bracket_validation('([]{SHOULD BE 12})')
