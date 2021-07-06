def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    freq = {}
    vowels = {"a", "e", "i", "o", "u"}

    for ltr in phrase.lower():
        if ltr in vowels:
            freq[ltr] = freq.get(ltr, 0) + 1

    return freq
