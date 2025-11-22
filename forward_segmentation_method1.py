def load_prefix_dict(file_path):
    prefix_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.split()[0]
            for i in range(1, len(word)):
                prefix = word[:i]
                prefix_dict[prefix] = 0
            prefix_dict[word] = 1

    return prefix_dict


def cut_method(string, prefix_dict):
    words = []
    start, end = 0, 1
    find_word = string[start:end]
    window = find_word
    while start < len(string):
        if window not in prefix_dict or end > len(string):
            words.append(find_word)
            start += len(find_word)
            end = start + 1
            window = string[start:end]
            find_word = window
        elif prefix_dict[window] == 1:
            find_word = window
            end += 1
            window = string[start:end]
        elif prefix_dict[window] == 0:
            end += 1 
            window = string[start:end]
    
    if prefix_dict.get(window) != 1:
        words += list(window)
    else:
        words.append(window)

    return words


if __name__ == '__main__':
    s = '今个天气怎么样啊'
    prefix_dict = load_prefix_dict('./dict.txt')
    # print(prefix_dict)

    words = cut_method(s, prefix_dict)
    print(words)