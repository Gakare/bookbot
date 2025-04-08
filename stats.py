def get_num_words(text):
    text = text.split()
    wc = 0
    for w in text:
        wc += 1
    return wc


def get_letter_count(text):
    char_cnt = {}
    for c in text.lower():
        if c not in char_cnt:
            char_cnt.update({c: 1})
        else:
            char_cnt[c] += 1
    return char_cnt
