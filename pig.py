VOWELS = ['a', 'e', 'i', 'o', 'u']
def pig_latin(sentence):
    pig_list = sentence.split()

    # for word in pig_list:
    #     if word[0] not in vowels:
    #         word = word[1:] + word[0] + "ay"

    for i in range(len(pig_list)):
        first_char = pig_list[i][0]
        if first_char not in VOWELS:
            pig_list[i] = pig_list[i][1:] + first_char + "ay"

    return " ".join(pig_list)


# Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")