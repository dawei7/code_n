def solve(sentence, search_word):
    word_index = 1
    start = 0

    while start < len(sentence):
        end = sentence.find(" ", start)
        if end == -1:
            end = len(sentence)

        if end - start >= len(search_word) and sentence.startswith(search_word, start):
            return word_index

        word_index += 1
        start = end + 1

    return -1
