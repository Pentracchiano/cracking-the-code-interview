# https://leetcode.com/problems/search-suggestions-system/

ALPHABET_SIZE = ord('z') - ord('a') + 1
END_MARKER_INDEX = -1


def trie_index(character: str) -> int:
    return ord(character) - ord('a')


def letter(trie_index: int) -> str:
    return chr(trie_index + ord('a'))


def trie_factory(alphabet_size: int) -> Callable[[], List]:
    def trie_builder():
        return [None] * alphabet_size + [False]  # for the end marker

    return trie_builder


def find_words(trie: List, current_word: List, max_words: int, words: List = None) -> List:
    if words is None:
        words = []

    if trie is None:
        return words

    if len(words) == max_words:  # TODO why does it matter that this is on top?
        return words
    if trie[END_MARKER_INDEX]:
        words.append("".join(current_word))
    # can't it be here too???

    for trie_index in range(ALPHABET_SIZE):
        current_word.append(letter(trie_index))
        find_words(trie[trie_index], current_word, max_words, words)
        current_word.pop()

    return words


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # build a trie such that we can extract the lexicographically minima first
        trie_builder = trie_factory(ALPHABET_SIZE)
        trie = trie_builder()

        for product in products:
            current = trie
            for character in product:
                i = trie_index(character)
                if current[i] is None:
                    current[i] = trie_builder()
                current = current[i]

            current[END_MARKER_INDEX] = True

        all_suggestions = []
        current_search = []
        i = 0
        while i < len(searchWord):
            current_character = searchWord[i]
            current_search.append(current_character)

            try:
                trie = trie[trie_index(current_character)]
                result = find_words(trie, current_search, 3)
            except TypeError:
                result = []
            all_suggestions.append(result)
            i += 1
        return all_suggestions
