def int_func(text):
    user_input_capital = list(text)
    user_input_capital[0] = text[0].upper()
    return "".join(user_input_capital)


result = ""
user_input = input("Введите любую фразу: ")
user_input = user_input.split()
for word in user_input:
    result += int_func(word) + " "

print(result)
