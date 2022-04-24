#Mad libs template


class MadLibs:
    def __init__(self,word_descriptions,template):
        self.template = template
        self.word_descriptions = word_descriptions


#User input 
# def get_words_from_user(word_description:)
word_descriptions = ["noun" ,"verb","adjective","prepostion","conjuction","pronoun"]
words = []
print("Please provide the following words:")
for desc in word_descriptions:
    user_input = input(desc) 
    words.append(user_input)
print(words)  




        