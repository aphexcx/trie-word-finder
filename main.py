import pprint

#ending 'sentinel' character
_end = '_end_'


class Trie(object):
    def __init__(self, *words):
        root = {}
        for word in words:
            cur_dict = root
            for letter in word:
                if letter not in cur_dict:
                    cur_dict[letter] = {}
                cur_dict = cur_dict[letter]
            cur_dict[_end] = _end
        self.root = root

    def __repr__(self):
        return pprint.pformat(self.root)


def find_words(string, words):
    """Using a trie, find all valid substrings of a given string given an
     iterable of valid words."""
    trie = Trie(*words)
    print trie
    word_ranges = set()
    for offset in xrange(len(string)):
        cur_dict = trie.root
        curlen = 1
        #check this substring
        for pos, letter in enumerate(string[offset:]):
            if letter not in cur_dict:
                #back out of the trie and reset our word length tracker
                cur_dict = trie.root
                curlen = 1
            if letter in cur_dict:
                #delve into the trie
                cur_dict = cur_dict[letter]
                if _end in cur_dict:
                    #valid word
                    word_ranges.add((offset + pos+1-curlen, offset + pos+1))
                curlen += 1

    print word_ranges
    valid_words = []
    for word_range in word_ranges:
        valid_words.append(string[slice(*word_range)])

    return valid_words

print find_words('hotelfate', ['hotel', 'elf', 'fate', 'ate', 'hot'])


import re


def regexmethod(string, words):
    valid_words = set()
    regex = ""
    for word in words:
        regex += "%s|" % word
        found = re.findall(regex, string)
        for found_word in found:
            valid_words.add(found_word)
    return valid_words

print regexmethod('hotelfate', ['hotel', 'elf', 'fate', 'ate', 'hot'])