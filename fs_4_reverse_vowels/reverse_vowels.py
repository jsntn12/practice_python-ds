def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowel = "aeiou"
    letters = list(s)
    reverse_letter = []

    for char in letters:
        if char.lower() in vowel:
            reverse_letter.insert(0, char)

    for i in range(len(letters)):
        if letters[i].lower() in vowel:
            letters[i] = reverse_letter.pop(0)

    return "".join(letters)
