"""
Autocomplete algorithm.

Write an algorithm that will output a maximum of three keyword suggestions after each
character is typed by the customer in the search field.

If there are more than three acceptable keywords, return the keywords that are first in
 alphabetical order.
Only return keyword suggestions after the customer has entered two characters.
Keyword suggestions must start with the characters already typed

Both the repository and the customerQuery should be compared in a case-insensitive way.

Input
The input to the method/function consists of two arguments:
<em>repository, </em>a list of unique strings representing the various keywords from
the Amazon review comment section;
<em>customerQuery, </em>a string representing the full search query of the customer.

Output
Return a list of a list of strings in lower case, where each list represents the
keyword suggestions made by the system as the customer types each character of the
customerQuery. Assume the customer types characters in order without deleting or
removing any characters. If an output is not possible, return an empty array ([]).

Example
Input:
repository = [ "mobile", "mouse", "moneypot", "monitor", "mousepad" ]
customerQuery = "mouse"

Output:
["mobile", "moneypot", "monitor"]
["mouse", "mousepad"]
["mouse", "mousepad"]
["mouse", "mousepad"]

Explanation:
The chain of words that will generate in the search box will be
mo, mou, mous, mouse
and each line from output shows the suggestion of "mo", "mou", "mous", "mouse",
respectively in each line.
For the keyword suggestions made by the system that are generated for 'mo', the matches
that will be generated are:["mobile", "mouse", "moneypot", "monitor", "mousepad"]
Alphabetically, they will be reordered to
[ "mobile", "moneypot", "monitor", "mouse", "mousepad" ].
Thus the keyword suggestions made by the system are [ "mobile", "moneypot", "monitor"].
"""

from __future__ import annotations
from typing import List, Dict, Optional


class Node:
    """Represents a node of a Trie."""

    def __init__(self, data: str) -> None:
        self.data = data
        self.children: Dict[str, Node] = dict()
        self.is_word = False

    def traverse(self, query: str) -> Optional[Node]:
        """Tries to traverse starting from self, covering ´query´ and returning the node
        associated with the last char fo ´query´.
        """
        node = self
        for char in query.lower():
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def get_3_words(self) -> List[str]:
        """Return up to 3 words from node.

        In alphabetical order implies dfs.
        """

        root = self
        results = []

        def preorder(node: Node, cur_word: str, results: List[str]) -> None:
            if node is not None and len(results) < 3:
                cur_word += node.data
                if node.is_word:
                    results.append(cur_word)
                    return
                for child in node.children.values():
                    preorder(child, cur_word, results)

        preorder(root, cur_word="", results=results)
        return results


class Trie:
    """A Trie implementation."""

    def __init__(self, root: Node) -> None:
        self.root = root

    @classmethod
    def build_from_list(cls, repository: List[str]) -> Trie:
        root = Node("")
        for word in repository:
            word = word.lower()
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = Node(char)
                node = node.children[char]
            node.is_word = True
        return Trie(root)


def get_autocompletion(repository: List[str], custom_query: str):
    trie = Trie.build_from_list(repository)
    prefix = ""
    results = []
    node = trie.root
    for char in custom_query.lower():
        node = node.traverse(char)
        if node is None:
            break
        cur_results = node.get_3_words()
        cur_results = [prefix + word for word in cur_results]
        results.append(cur_results)
        prefix += char  # In the next iteration we miss this char


    return results


def test_x():
    repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    customer_query = "mouse"
    expected_result = [
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
    result = get_autocompletion(repository, customer_query)
    assert result == expected_result


if __name__ == "__main__":
    test_x()
