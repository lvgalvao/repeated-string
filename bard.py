def repeatedStrings(s, n):

    """
    repeatedStrings (string_to_repeat: str, number_of_characters_to_consider: int) -> int:
    repeatedStrings ("aba", 10) -> 7
    repeatedStrings ("abcac", 10) -> 4

    Process

    Get the first letter
    Create the new string
    Count the numbers of strings into the new string

    Outputs

    first_letter = str
    new_string = str
    number_of_chars_in_string = int

    Code
    """

    count_a = 0
    length_s = len(s)
    if length_s == 1:
        return n
    n_div_len, n_mod_len = divmod(n, length_s)
    count_a += s.count('a') * n_div_len
    count_a += s[n_mod_len - 1] == 'a'
    return count_a


if __name__ == '__main__':
    print("Starting tests")
    assert repeatedStrings("aba",10) == 7
    print("Sucess 1/2")
    assert repeatedStrings("abcac",10) == 4
    print("Sucess 2/2")