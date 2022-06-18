# https://leetcode.com/problems/prefix-and-suffix-search/


class Trie:
    def __init__(self):
        self.start = {}
        self.end_marker = '\0'
        self.weight_marker = '\1'

    def add_word(self, word: str, weight: int) -> None:
        # it updates any weight already in the character.
        current = self.start
        for character in word:
            current = current.setdefault(character, {})
            current[self.weight_marker] = weight
        # not really useful here but worth to know about: current[self.end_marker] = True

    def search_word_by_prefix(self, prefix: str) -> int:
        # returns the weight or -1 if not found
        current = self.start
        for character in prefix:
            try:
                current = current[character]
            except KeyError:
                return -1
        return current[self.weight_marker]


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, word in enumerate(words):
            word = '#' + word

            self.trie.add_word(word, i)
            for character in word[::-1]:
                word = character + word
                self.trie.add_word(word, i)

    def f(self, prefix: str, suffix: str) -> int:
        return self.trie.search_word_by_prefix(suffix + "#" + prefix)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)