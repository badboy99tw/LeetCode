"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:

    Input: "cbbd"
    Output: "bb"
"""
from typing import Optional

import pytest


class Solution:
    def getLongestOddPalindrome(self, s: str, center: int) -> Optional[dict]:
        longestPalindrome = {
            "start": center,
            "end": center,
        }
        longestHelfLength = min(center, len(s) - center - 1)
        for i in range(1, longestHelfLength + 1):
            if s[center - i] == s[center + i]:
                longestPalindrome = {
                    "start": center - i,
                    "end": center + i,
                }
            else:
                return longestPalindrome
        return longestPalindrome

    def getLongestEvenPalindrome(self, s: str, centerLeft: int) -> Optional[dict]:
        if centerLeft + 1 >= len(s):
            return None

        if s[centerLeft] != s[centerLeft + 1]:
            return None

        longestPalindrome = {
            "start": centerLeft,
            "end": centerLeft + 1,
        }
        longestHelfLength = min(centerLeft, len(s) - centerLeft - 1 - 1)
        for i in range(1, longestHelfLength + 1):
            if s[centerLeft - i] == s[centerLeft + 1 + i]:
                longestPalindrome = {
                    "start": centerLeft - i,
                    "end": centerLeft + 1 + i,
                }
            else:
                return longestPalindrome
        return longestPalindrome

    def longestPalindrome(self, s: str) -> str:
        result = None
        resultLength = 0

        for center in range(len(s)):
            maxPossibleLength = min(center, len(s) - center - 1) * 2 + 2
            if maxPossibleLength < resultLength:
                break

            odd = self.getLongestOddPalindrome(s, center)
            even = self.getLongestEvenPalindrome(s, centerLeft=center)
            oddLength = odd["end"] - odd["start"] + 1
            evenLength = even["end"] - even["start"] + 1 if even else 0

            if oddLength > resultLength:
                result = odd
                resultLength = oddLength
            if evenLength > resultLength:
                result = even
                resultLength = evenLength

        if result:
            return str(s[result["start"] : result["end"] + 1])
        else:
            return s


@pytest.mark.timeout(1)
def test():
    s = Solution()
    assert s.longestPalindrome("") == ""
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("babad") in ["bab", "aba"]
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("aaaaaa") == "aaaaaa"

    input_ = "babaddtattarrattatddetartrateedredividerb"
    expected = "ddtattarrattatdd"
    assert s.longestPalindrome(input_) == expected

    "anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"
    expected = "ddtattarrattatdd"
    assert s.longestPalindrome(input_) == expected

    input_ = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
    expected = input_
    assert s.longestPalindrome(input_) == expected

    input_ = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    expected = input_
    assert s.longestPalindrome(input_) == expected
