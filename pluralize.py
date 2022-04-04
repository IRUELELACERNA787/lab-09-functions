def pluralize(word):
    if(word == "moose"):
        return "moose"
    elif(word == "automaton"):
        return "automata"
    elif(word == "mouse"):
        return "mice"
    else:
        return word + "s"

inputWord = input("Please enter a word to be pluralized: ")
print(pluralize(inputWord))