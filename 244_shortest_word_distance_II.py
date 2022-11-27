"""

## Problem 244: Shortest Word Distance II

## Author: Neha Doiphode
## Date:   11-26-2022

## Description:
    Design a data structure that will be initialized with a string array,
    and then it should answer queries of the shortest distance between two different strings from the array.

    Implement the WordDistance class:
        WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
        int shortest(String word1, String word2) returns the shortest distance between word1 and word2
        in the array wordsDict.

## Examples:
    Example 1:
        Input:
            ["WordDistance", "shortest", "shortest"]
            [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
        Output:
            [null, 3, 1]

        Explanation:
            WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
            wordDistance.shortest("coding", "practice"); // return 3
            wordDistance.shortest("makes", "coding");    // return 1

## Constraints:
    1 <= wordsDict.length <= 3 * 104
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.
    word1 != word2
    At most 5000 calls will be made to shortest.

## Time complexity: Please refer to the respective doc-strings of approaches implemented below.

## Space complexity: Please refer to the respective doc-strings of approaches implemented below.

"""

import sys
from typing import List, Optional
from collections import defaultdict

def get_input():
    print("Enter the list of words with spaces: ", end = "")
    words = input()
    words = [word for word in words.split()]
    return words

class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self._mapper = defaultdict(lambda: [])
        self._initialize_mapper(wordsDict)

    def _initialize_mapper(self, wordsDict):
        for index, word in enumerate(wordsDict):
            self._mapper[word].append(index)

    def shortest_two_pass(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(m*n), where m number of occurrences of word1 in words list and
                                         n is the number of occurrences of word2 in the words list.
        Space complexity: O(N), where N is the length of words list as we create auxiliary dictionary to store
                                occurrences of different words.
        """
        shortest_distance = float("inf")
        for ind1 in self._mapper[word1]:
            for ind2 in self._mapper[word2]:
                shortest_distance = min(shortest_distance, abs(ind1 - ind2))

        return shortest_distance

    def shortest_one_pass(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(m + n), where m number of occurrences of word1 in words list and
                                         n is the number of occurrences of word2 in the words list.
        Space complexity: O(N), where N is the length of words list as we create auxiliary dictionary to store
                                occurrences of different words.
        """
        shortest_distance = float("inf")
        ptr1 = ptr2 = 0
        l1 = len(self._mapper[word1])
        l2 = len(self._mapper[word2])

        while ptr1 < l1 and ptr2 < l2:
            shortest_distance = min(shortest_distance, abs(self._mapper[word1][ptr1] -
            self._mapper[word2][ptr2]))

            if self._mapper[word1][ptr1] < self._mapper[word2][ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        return shortest_distance

# Driver code
words = get_input()
word_distance = WordDistance(words)

while True:
    print("Enter two words you want to find the shortest distance between(with spaces): ")
    word1, word2 = input().split()

    print(f"Input: word1 = {word1}, word2 = {word2}")
    print(f"Output: Approach 1: Brute force: Shortest distance between '{word1}' and '{word2}' is: {word_distance.shortest_two_pass(word1, word2)}")
    print(f"Output: Approach 2: One pass traversal: Shortest distance between '{word1}' and '{word2}' is: {word_distance.shortest_one_pass(word1, word2)}")
    print()
    print("continue?(y/n) : ", end = "")
    choice = input()
    if choice == "n":
        sys.exit(0)
    print()
