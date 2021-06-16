"""
208. Implement Trie (Prefix Tree)
Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to
efficiently store and retrieve keys in a dataset of strings. There are various
 applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

    Trie() Initializes the trie object.
    void insert(String word) Inserts the string word into the trie.
    boolean search(String word) Returns true if the string word is in the trie
    (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously
    inserted string word that has the prefix prefix, and false otherwise.
"""

from __future__ import annotations
from typing import Dict


class Node:
    def __init__(self, char: str, is_end: bool = False):
        self.char = char
        self.is_end = is_end
        self.children: Dict[str, Node] = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("root")

    def insert(self, word: str) -> None:
        """Inserts a word into the trie."""
        pointer = self.root
        for char in word:
            if char not in pointer.children:
                pointer.children[char] = Node(char)
            pointer = pointer.children[char]
        pointer.is_end = True

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        pointer = self.root
        for char in word:
            if char not in pointer.children:
                return False
            pointer = pointer.children[char]
        return pointer.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pointer = self.root
        for char in prefix:
            if char not in pointer.children:
                return False
            pointer = pointer.children[char]
        return True


def test_0():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
