def chatgpt_algorithm(string_to_repeat, number_of_characters_to_consider):

    if not string_to_repeat:
        return 0  
    first_letter = string_to_repeat[0]

    if first_letter not in string_to_repeat:
        return 0

    count_x_in_s = string_to_repeat.count(first_letter)
    repetitions, remainder = divmod(number_of_characters_to_consider, len(string_to_repeat))
    total_count_a = repetitions * count_x_in_s + string_to_repeat[:remainder].count(first_letter)

    return total_count_a

if __name__ == '__main__':
    print("Starting tests")
    assert chatgpt_algorithm("aba",10) == 7
    print("Sucess 1/2")
    assert chatgpt_algorithm("abcac",10) == 4
    print("Sucess 2/2")