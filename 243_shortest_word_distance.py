"""

## Problem 243: Shortest Word Distance

## Author: Neha Doiphode
## Date:   11-26-2022

## Description:
    Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2,
    return the shortest distance between these two words in the list.

## Examples:
    Example 1:
        Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
        Output: 3

    Example 2:
        Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
        Output: 1

## Constraints:
    2 <= wordsDict.length <= 3 * 104
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.
    word1 != word2


## Time complexity: Please refer to the respective doc-strings of approaches implemented below.

## Space complexity: Please refer to the respective doc-strings of approaches implemented below.

"""

from typing import List, Optional

def get_input():
    print("Enter the list of words with spaces: ", end = "")
    words = input()
    words = [word for word in words.split()]

    print("Enter two words you want to find the shortest distance between(with spaces): ")
    word1, word2 = input().split()

    return words, word1, word2

class Solution:
    def shortestDistance_brute_force(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        Time complexity: O(n^2), where n is the length of words list.
        Space complexity: O(1), no auxiliary space is used.
        """
        n = len(wordsDict)
        shortest_distance = float("inf")
        for ind1 in range(n):
            if wordsDict[ind1] == word1:
                for ind2 in range(n):
                    if wordsDict[ind2] == word2:
                        shortest_distance = min(shortest_distance, abs(ind1 - ind2))

        return shortest_distance

    def shortestDistance_one_pass_traversal(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        Time complexity: O(n), where n is the length of words list.
        Space complexity: O(1), no auxiliary space is used.
        """
        n = len(wordsDict)
        shortest_distance = float("inf")
        ind1 = ind2 = None

        for index in range(n):
            if wordsDict[index] == word1:
                ind1 = index

            elif wordsDict[index] == word2:
                ind2 = index


            if ind1 != None and ind2 != None:
                shortest_distance = min(shortest_distance, abs(ind1 - ind2))

        return shortest_distance

# Driver code
solution = Solution()
words, word1, word2 = get_input()
print(f"Input: List of words: {words}")
print(f"Input: word1 = {word1}, word2 = {word2}")
print(f"Output: Approach 1: Brute force: Shortest distance between '{word1}' and '{word2}' is: {solution.shortestDistance_brute_force(words, word1, word2)}")
print(f"Output: Approach 2: One pass traversal: Shortest distance between '{word1}' and '{word2}' is: {solution.shortestDistance_one_pass_traversal(words, word1, word2)}")
