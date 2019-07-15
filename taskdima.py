"""Dima's tasks for testing"""

def task4(seq_num):
    """Creates a list and tuple of numbers """
    # seq_num is a string of the sequence number separated by comma
    list_data = seq_num.split(',')
    tuple_data = tuple(list_data)
    return list_data, tuple_data

def task10(sentence):
    """Prints sorted words from the sentence """
    list_words = sentence.split(' ')
    set_words = set(list_words)
    set_sorted = sorted(set_words)
    sentence_new = ' '.join(set_sorted)
    return sentence_new

def task16(entry_data):
    """Creates a list of even square numbers"""
    list_data = entry_data.split(',')
    list_final = [int(i)**2 for i in list_data if int(i)%2 != 0]
    return list_final

def task22(sentence):
    """Prints frequency of the words from the input"""
    list_words = sentence.split(' ')
    set_words = set(list_words)
    dict_words = {}
    for i in set_words:
        dict_words[i] = list_words.count(i)
    keys = sorted(dict_words.keys())
    dict_new = {}
    for k in keys:
        dict_new[k] = dict_words[k]
    return dict_new

def task28(string_1, string_2):
    """Prints the string with maximum length"""
    length_1 = len(string_1)
    length_2 = len(string_2)
    if length_1 > length_2:
        return string_1
    if length_2 > length_1:
        return string_2
    return string_1, string_2

def task34(numb_elem):
    '''Random numbers of squares between (1, 20)'''
    from random import randint
    list_sq = []
    for _ in range(numb_elem):
        list_sq.append(randint(1, 20)**2)
    return list_sq

def task40(tuple_initial):
    """Picks up even numbers from the tuple"""
    list_even = [i for i in tuple_initial if i%2 == 0]
    tuple_new = tuple(list_even)
    return tuple_new

def task46():
    """Picks up even numbers from the tuple"""
    list_i = [i for i in range(1, 21)]
    map_i = map(lambda x: x**2, list_i)
    return map_i

def task52(num):
    """Fibo-like sequence"""
    # Enter an integer N>0
    temp = 100
    if num == 1:
        return temp
    for _ in range(2, num+1):
        temp += 100
    return temp

def task58():
    """Random number divisible by 5 and 7"""
    from random import randint
    while True:
        val = randint(0, 100)
        if val%5 == 0 and val%7 == 0:
            return val
