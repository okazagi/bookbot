def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    counts = {}
    contents = text.lower()
    for char in contents:
        counts[char] = counts.get(char, 0) + 1
    return counts


def get_stats_sorted(chars_dict):
    return [
        [k, v]
        for k, v in sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    ]
