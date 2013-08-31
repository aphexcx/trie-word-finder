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

    def __contains__(self, item):
        cur_dict = self.root
        for letter in item:
            if letter in cur_dict:
                cur_dict = cur_dict[letter]
            else:
                return False
        else:
            if _end in cur_dict:
                return True
            else:
                return False

    def __repr__(self):
        return pprint.pformat(self.root)


def triemethod(string, words):
    trie = Trie(*words)
    print trie
    word_ranges = set()
    for start_pos in xrange(len(string)):
        cur_dict = trie.root
        subpos = start_pos
        curlen = 1
        for pos, letter in enumerate(string[start_pos:]):
            print letter
            if letter in cur_dict:
                cur_dict = cur_dict[letter]
                if _end in cur_dict:
                    #valid word
                    word_ranges.add((start_pos + pos+1-curlen, start_pos + pos+1))
                    print word_ranges
                curlen += 1
                    # curlen = 1
                    # cur_dict = trie.root
                    # subpos = pos
            else:
                cur_dict = trie.root
                curlen = 1
                subpos = pos
                if letter in cur_dict:
                    cur_dict = cur_dict[letter]
                    if _end in cur_dict:
                        #valid word
                        word_ranges.add((pos-curlen, pos+1))
                        print word_ranges
                    curlen += 1
                        # curlen = 1
                        # subpos = pos
                # else: ???
                    #subpos = pos + 1

    print word_ranges
    valid_words = []
    for word_range in word_ranges:
        valid_words.append(string[slice(*word_range)])

    #find valid word combos
    remaining_range = (0, len(string))
    complete_combo = []
    for word_range in word_ranges:
        remaining_range = (remaining_range[0] - word_range[0], remaining_range[1] - word_range[1])
        for other_range in word_ranges:
            pass

    return valid_words

print triemethod('hotelfate', ['hotel', 'elf', 'fate', 'ate', 'hot'])