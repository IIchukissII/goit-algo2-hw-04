from pytrie import Trie
from typing import List, Optional


class LongestCommonWord(Trie):
    def __init__(self):
        self._root = {}

    def put(self, word: str, value: int) -> None:
        """
        Додає слово в дерево префіксів із відповідним значенням.

        Args:
            word: Слово, яке потрібно додати.
            value: Значення, пов'язане зі словом.
        """
        current = self._root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['value'] = value  # Зберігаємо значення для слова

    def find_longest_common_word(self, strings: List[str]) -> str:
        """
        Finds the longest common prefix among all strings in the given array.

        Args:
            strings: List of strings to find common prefix from

        Returns:
            str: The longest common prefix, or empty string if none exists

        Raises:
            TypeError: If strings is not a list or contains non-string elements
            ValueError: If strings is empty
        """
        # Input validation
        if not isinstance(strings, list):
            raise TypeError("Input must be a list of strings")
        if not strings:
            return ""
        if not all(isinstance(s, str) for s in strings):
            raise TypeError("All elements must be strings")
        if any(not s for s in strings):  # Check for empty strings
            return ""

        # Insert all strings into the trie
        for i, word in enumerate(strings):
            self.put(word, i)

        # Find the longest common prefix
        def find_common_prefix(node, prefix: str) -> str:
            """
            Helper function to traverse the trie and find the longest common prefix.
            Returns the prefix when we hit a node with multiple children or end of a word.
            """
            # If we have more than one child or no children, return current prefix
            child_keys = [k for k in node.keys() if k != "value"]
            if len(child_keys) != 1:
                return prefix

            # Continue with the single child path
            char = child_keys[0]
            return find_common_prefix(node[char], prefix + char)

        return find_common_prefix(self._root, "")


if __name__ == "__main__":
    # Test 1: Basic case
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    # Test 2: Longer common prefix
    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    # Test 3: No common prefix
    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    # Test 4: Empty input
    trie = LongestCommonWord()
    assert trie.find_longest_common_word([]) == ""

    # Test 5: Single string
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["hello"]) == "hello"

    # Test 6: With empty string
    trie = LongestCommonWord()
    assert trie.find_longest_common_word(["", "b", "c"]) == ""

    # Test 7: Error handling
    trie = LongestCommonWord()
    try:
        trie.find_longest_common_word(None)
    except TypeError:
        print("TypeError caught successfully")

    try:
        trie.find_longest_common_word([1, 2, 3])
    except TypeError:
        print("TypeError caught successfully for non-string elements")