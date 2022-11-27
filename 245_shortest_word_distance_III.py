"""

## Problem 245: Shortest Word Distance III

## Author: Neha Doiphode
## Date:   11-26-2022

## Description:
    Given an array of strings wordsDict and two strings that already exist in the array word1 and word2,
    return the shortest distance between these two words in the list.

    Note that word1 and word2 may be the same.
    It is guaranteed that they represent two individual words in the list.

## Example:
    Example 1:
        Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
        Output: 1

    Example 2:
        Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
        Output: 3

## Constraints:
    1 <= wordsDict.length <= 105
    1 <= wordsDict[i].length <= 10
    wordsDict[i] consists of lowercase English letters.
    word1 and word2 are in wordsDict.

## Time complexity: O(n), where n is the length of words list.

## Space complexity: O(1), no auxiliary space is used.


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
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ind1, ind2, prev_ind = None, None, None
        shortest_distance = float("inf")

        for index in range(len(wordsDict)):
            if wordsDict[index] == word1 and word1 != word2:
                ind1 = index

            elif wordsDict[index] == word2 and word1 != word2:
                ind2 = index

            elif wordsDict[index] == word1 and word1 == word2:
                if prev_ind != None:
                    shortest_distance = min(shortest_distance, abs(prev_ind - index))
                prev_ind = index

            if ind1 != None and ind2 != None:
                shortest_distance = min(shortest_distance, abs(ind1 - ind2))

        return shortest_distance

# Driver code
solution = Solution()
words, word1, word2 = get_input()
print(f"Input: List of words: {words}")
print(f"Input: word1 = {word1}, word2 = {word2}")
print(f"Output: One pass traversal: Shortest distance between '{word1}' and '{word2}' is: {solution.shortestWordDistance(words, word1, word2)}")
