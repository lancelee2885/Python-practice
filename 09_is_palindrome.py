def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    # ltrs = list(phrase.lower().replace(" ", ""))
    # ltrs_reverse = ltrs.copy()
    # ltrs_reverse.reverse()
    # if ltrs_reverse == ltrs:
    #     return True
    # else:
    #     return False

    # slice a list will hand you a new list of items sliced
    # reverse doesn't return a new list

    ltrs = phrase.lower().replace(" ", "")
    return ltrs == ltrs[::-1]
