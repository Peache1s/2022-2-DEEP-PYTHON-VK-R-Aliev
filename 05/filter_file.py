def filter_file(name_of_file, word_list):
    temp_word_list = " ".join(word_list).lower().split()
    with open(name_of_file, 'r') as file:
        for line in file:
            temp_lst = line.replace('\n', '').lower().split()
            for word in temp_word_list:
                if word in temp_lst:
                    yield line.replace('\n', '')
                    break
