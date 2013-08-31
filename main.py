import pprint

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


def triemethod(string, words):
    trie = Trie(*words)
    print trie
    word_ranges = set()
    for start_pos in xrange(len(string)):
        cur_dict = trie.root
        curlen = 1
        #check this substring
        for pos, letter in enumerate(string[start_pos:]):
            if letter in cur_dict:
                #delve in to the trie
                cur_dict = cur_dict[letter]
                if _end in cur_dict:
                    #valid word
                    word_ranges.add((start_pos + pos+1-curlen, start_pos + pos+1))
                curlen += 1
            else:
                cur_dict = trie.root
                curlen = 1
                if letter in cur_dict:
                    #delve in to the trie
                    cur_dict = cur_dict[letter]
                    if _end in cur_dict:
                        #valid word
                        word_ranges.add((pos-curlen, pos+1))
                    curlen += 1

    valid_words = []
    for word_range in word_ranges:
        valid_words.append(string[slice(*word_range)])

    return valid_words

print triemethod('hotelfate', ['hotel', 'elf', 'fate', 'ate', 'hot'])

