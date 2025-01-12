from pytrie import Trie
from typing import Dict, Optional

class Homework(Trie):
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

    def count_words_with_suffix(self, pattern: str) -> int:
        """
        Counts the number of words in the trie that end with the given pattern.
        
        Args:
            pattern: The suffix pattern to search for
            
        Returns:
            int: Number of words ending with the pattern
            
        Raises:
            TypeError: If pattern is not a string
            ValueError: If pattern is empty
        """
        if not isinstance(pattern, str):
            raise TypeError("Pattern must be a string")
        if not pattern:
            raise ValueError("Pattern cannot be empty")

        
            
        def _find_all_words(node: Dict, current_word: str) -> list:
            """Helper function to find all words in the trie starting from a given node."""
            words = []
            if node.get("value") is not None:
                words.append(current_word)
            
            for char, child in node.items():
                if char != "value":
                    words.extend(_find_all_words(child, current_word + char))
            return words
        
        count = 0
        all_words = _find_all_words(self._root, "")
        
        for word in all_words:
            if word.endswith(pattern):
                count += 1
                
        return count

    def has_prefix(self, prefix: str) -> bool:
        """
        Checks if there are any words in the trie with the given prefix.
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            bool: True if prefix exists, False otherwise
            
        Raises:
            TypeError: If prefix is not a string
            ValueError: If prefix is empty
        """
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        if not prefix:
            raise ValueError("Prefix cannot be empty")
            
        current = self._root
        
        # Navigate to the node corresponding to the last character of the prefix
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
            
        # If we've made it here, we found the prefix
        return True

if __name__ == "__main__":
    # Test cases
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Test suffix counting
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Test prefix checking
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat

    # Test error handling
    try:
        trie.count_words_with_suffix(None)
    except TypeError:
        print("TypeError caught successfully for count_words_with_suffix")

    try:
        trie.has_prefix("")
    except ValueError:
        print("ValueError caught successfully for has_prefix")