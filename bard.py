def bard_algorithm(string_to_repeat, number_of_characters_to_consider):

    count_a = 0
    length_s = len(string_to_repeat)
    first_letter = string_to_repeat[0]
    if length_s == 1:
        return number_of_characters_to_consider
    n_div_len, n_mod_len = divmod(number_of_characters_to_consider, length_s)
    count_a += string_to_repeat.count(first_letter) * n_div_len
    count_a += string_to_repeat[n_mod_len - 1] == first_letter
    return count_a


if __name__ == '__main__':
    print("Starting tests")
    assert bard_algorithm("aba",10) == 7
    print("Sucess 1/2")
    assert bard_algorithm("abcac",10) == 4
    print("Sucess 2/2")