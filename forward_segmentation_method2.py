def load_word_dict(file_path):
    word_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.split()[0]
            word_dict[word] = 0

    return word_dict

def load_prefix_dict(file_path):
    prefix_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            word = line.split()[0]
            for i in range(1, len(word)):
                prefix_dict[word[:i]] = 0
            prefix_dict[word] = 1

    return prefix_dict


def cut_method1(string, word_dict):
    words = []

    while string:
        n = len(string)
        word = string[:n]
        while word not in word_dict:
            if len(word) == 1:
                break
            n -= 1
            word = word[:n]
        words.append(word)
        string = string[len(word):]
    return words

def cut_method2(string, prefix_dict):
    words = []
    s, e = 0, 1
    window = string[s:e]
    find_word = window

    while s < len(string):
        if window not in prefix_dict or e > len(string):
            words.append(find_word)
            s = s + len(find_word)
            e = s + 1
            window = string[s:e]
            find_word = window

        elif prefix_dict[window] == 0:
            e +=1
            window = window[s:e]
        elif prefix_dict[window] == 1:
            find_word = window
            e += 1
            window = string[s:e]
    return words
 


path = './dict.txt'
word_dict = load_word_dict(path)
prefix_dict = load_prefix_dict(path)
print(cut_method1('今个天气挺好，挺风和日丽的？', word_dict))
print(cut_method2('今个天气挺好，挺风和日丽的？', prefix_dict))
