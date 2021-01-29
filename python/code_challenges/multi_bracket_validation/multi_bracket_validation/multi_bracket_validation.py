def multi_bracket_validation(input):
    pairs = {
        "[" : "]",
        "{" : "}",
        "(" : ")"
    }

    verify_list = []

    for i in input:
        if i in pairs:
            verify_list.append(i)
        elif i in pairs.values():
            if not len(verify_list):
                return False
            opener = verify_list.pop()
            if i != pairs[opener]:
                return False
    
    return len(verify_list) == 0





# Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

# Round Brackets : ()
# Square Brackets : []
# Curly Brackets : {}


# multi_bracket_validation('([]{SHOULD BE 12})')
