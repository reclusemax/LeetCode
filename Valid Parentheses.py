
def isValid(s: str) -> bool:
    stack = []
    lookup = {'(':')', '[':']','{':'}'}

    for br in s:
        if stack and br == lookup.get(stack[-1]):
            stack.pop()
        else:
            stack.append(br)
    return not bool(stack)
print(isValid('(((({{{{[[[{}]]]}}}}))))'))
