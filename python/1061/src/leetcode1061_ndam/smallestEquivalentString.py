#You are given two strings of the same length s1 and s2 and a string baseStr.
#We say s1[i] and s2[i] are equivalent characters.
#    For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
#Equivalent characters follow the usual rules of any equivalence relation:
#    Reflexivity: 'a' == 'a'.
#    Symmetry: 'a' == 'b' implies 'b' == 'a'.
#    Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
#For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.
#Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

import string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        equivMap = {char: [char] for char in string.ascii_lowercase}
        output = ""
        for i in range(len(s1)):
            merged = list(set(equivMap[s1[i]]) | set(equivMap[s2[i]]))
            for character in merged:
                equivMap[character] = merged
        for character in baseStr:
            output = output + min(equivMap[character])
        return output

i = Solution()
s1 = "leetcode"
s2 = "programs"
base = "sourcecode"
i.smallestEquivalentString(s1,s2,base)
