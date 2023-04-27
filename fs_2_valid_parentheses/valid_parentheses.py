def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count = 0
    for paren in parens:
        if count < 0:
            return False
        elif paren == "(":
            count += 1
        elif paren == ")":
            count -= 1

        print(paren, count)
    return True if count == 0 else False
