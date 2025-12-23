'''
Interview Question — Valid Anagram
Interviewer:
You are given two strings s and t.
Determine whether t is an anagram of s.
Two strings are anagrams if they contain the same characters in the same frequencies, but the characters may appear in a different order.
Return true if t is an anagram of s, otherwise return false.

Example 1
Input:
s = "anagram"
t = "nagaram"
Output:
true

Example 2
Input:
s = "rat"
t = "car"
Output:
false

Example 3 (repeated characters)
Input:
s = "aacc"
t = "ccac"
Output:
false

Constraints (as typically stated)
1 ≤ length of s, t ≤ 50,000
Strings contain only lowercase English letters

Clarifying follow-up questions (what you should ask in an interview)
You would typically ask:
“Are the strings case-sensitive?”
“Do spaces or special characters matter?”
“Can the strings be of different lengths?”
'''

# Input:
s = "anagram"
t = "nagaram"
# Output:
# true


def is_anagram(s,t):
    # If lengths differ, they cannot be anagrams
    if len(s) != len(t):
        return False

    freq = {}

    # Count characters in s
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Reduce counts using t
    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] < 0:
            return False

    return True


# Tests
assert is_anagram("anagram", "nagaram") is True
assert is_anagram("rat", "car") is False
assert is_anagram("aacc", "ccac") is False
assert is_anagram("", "") is True

