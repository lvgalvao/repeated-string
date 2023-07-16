def repeatedStrings(string_to_repeat, number_of_characters_to_consider):
    """
    repeatedStrings (string_to_repeat: str, number_of_characters_to_consider: int) -> int:
    repeatedStrings ("aba", 10) -> 7
    repeatedStrings ("abcac", 10) -> 4

    Process:

    Get the first letter of the string_to_repeat
    Calculate the number of full repetitions and the remainder of string_to_repeat in number_of_characters_to_consider
    Count the number of occurrences of the first letter in the repetitions and the remainder

    Outputs:

    number_of_occurrences = int
    """

    # Handle the edge case of an empty string
    if not string_to_repeat:
        return 0
    
    # Get the first letter
    first_letter = string_to_repeat[0]

    # Handle the edge case where there are no 'a's in the string
    if first_letter not in string_to_repeat:
        return 0

    count_x_in_s = string_to_repeat.count(first_letter)

    # Calculate the number of full repetitions of s in the first n characters
    repetitions, remainder = divmod(number_of_characters_to_consider, len(string_to_repeat))

    # The total number of 'a's in the first n characters is the number of 'a's in s
    # times the number of full repetitions of s, plus the number of 'a's in the remainder
    total_count_a = repetitions * count_x_in_s + string_to_repeat[:remainder].count(first_letter)

    return total_count_a

if __name__ == '__main__':
    print("Starting tests")
    assert repeatedStrings("aba",10) == 7
    print("Sucess 1/2")
    assert repeatedStrings("abcac",10) == 4
    print("Sucess 2/2")