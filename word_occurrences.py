user_type = input("Text:")
user_text = user_type.split()
user_input = set(user_text)
for word in user_input:
    print(word, ":", user_text.count(word))