def repeatedStrings(string_to_repeat,number_of_characters_to_consider):

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

    first_letter = string_to_repeat[0]
    new_string = ""
    number_of_chars_in_string = 0

    for i in range(number_of_characters_to_consider):
        new_string += string_to_repeat[i%len(string_to_repeat)]
        if new_string[i] == first_letter:
            number_of_chars_in_string += 1

    return number_of_chars_in_string


if __name__ == '__main__':
    print("Starting tests")
    assert repeatedStrings("aba",10) == 7
    print("Sucess 1/2")
    assert repeatedStrings("abcac",10) == 4
    print("Sucess 2/2")