def number_of_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def number_of_characters(text):
    car = {}
    for t in text:
        lower = t.lower()
        if lower not in car:
            car[lower] = 1
        else:
            car[lower] += 1

    return car

def sort_on(item):
    return item["num"]

def sort_characters(chars):
    alpha = {}
    for char in chars:
        if char.isalpha():
            alpha[char] = chars[char]
    char_list = []
    for a, b in alpha.items():
        record = {"char":a, "num":b}
        char_list.append(record)
    char_list.sort(key=sort_on, reverse=True)
    return char_list