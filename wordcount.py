
def get_user_input():
    while True:
        user_input=input("please enter a sentence or paragraph:")
        if user_input.strip():
            return user_input
        else:
            print("enter:input cannot be empty.please try again.")
text=get_user_input()
print("you entered:",text)
def count_words(text):
    """count the number of words in the input text."""
    words=text.split()
    return len(words)

word_count=count_words(text)
print("word count:",word_count)
print(f"the number of words in the input text is: {word_count}")
