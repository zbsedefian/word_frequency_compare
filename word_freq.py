from string import punctuation


def create_dict(f):
    """Creates list of all words in .txt file
    """
    words = []
    with open(f) as fin:
        for line in fin:
            words += line.lower().split()
    return words


def most_frequent(s):
    """Creates dictionary: key is words from list and value is 
    its frequency in the list.
    """
    frq = {}
    for char in s:
        count = 1
        if char in frq:
            count = frq[char] + 1
        frq[char] = count
    return frq


def get_percentages(d):
    """Converts the frequency counted list to one with percentages.
    """
    new_f = {}
    for key in d:
        val = d[key] / total_chars * 100
        new_f[key] = val
    return new_f


def get_most_common():
    """Creates a list of the most common English words in order
    to filter out uninteresting results of the frequency dict.
    """
    most_common_eng_words = []
    f = open('1-1000.txt', 'r')
    for line in f:
        most_common_eng_words.append(line.strip().lower())
    return most_common_eng_words


def get_data():
    file_name = input("Input filename with .txt extension: ")
    most_common_eng_words = get_most_common() 
    f = open(file_name, 'r')
    word_list = [word.strip(punctuation) for line in f for word in line.lower().split()]
    word_list.sort(reverse=True)
    freq = most_frequent(word_list)
    freq = get_percentages(freq)
    print("The most common words, with frequencies:")
    freq_sorted_keys = sorted(freq, key=freq.get, reverse=True)
    count = 0
    final_most_freq = []
    for r in freq_sorted_keys:
        if r not in most_common_eng_words:
            val = str(freq[r])
            val = val[:4] + "%"
            final_most_freq.append(r)
            print (r, val)
            count += 1
        if count >= 30:
            break
    return final_most_freq


def main():
    print("This program analyzes a text file and returns the most frequent words found,")
    print("excluding the 1000 most common words in the English language.")
    books = int(input("How many files to compare? (2, 3, or 4): "))
    
    if books == 2:
        fre1 = get_data()
        fre2 = get_data()
        print("Both texts contained the following in their 30 most common words:")
        for i in range(30):
            if fre1[i] in fre2:
                print(fre1[i])
    elif books == 3:
        fre1 = get_data()
        fre2 = get_data()
        fre3 = get_data()
        print("All texts contained the following in their 30 most common words:")
        for i in range(30):
            if fre1[i] in fre2 and fre1[i] in fre3:
                print(fre1[i])
    elif books == 4:
        fre1 = get_data()
        fre2 = get_data()
        fre3 = get_data()
        fre4 = get_data()
        print("All texts contained the following in their 30 most common words:")
        for i in range(30):
            if fre1[i] in fre2 and fre1[i] in fre3 and fre1[i] in fre4:
                print(fre1[i])
    else:
        print("Invalid input.")


if __name__ == "__main__":
    main()


