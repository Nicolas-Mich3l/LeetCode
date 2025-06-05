#You are given two strings of the same length s1 and s2 and a string baseStr.
#We say s1[i] and s2[i] are equivalent characters.
#    For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
#Equivalent characters follow the usual rules of any equivalence relation:
#    Reflexivity: 'a' == 'a'.
#    Symmetry: 'a' == 'b' implies 'b' == 'a'.
#    Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
#For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.
#Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
class Solution:
    class UnionFind:
        def __init__(self):
            self.parent = list(range(26))
        
        def find(self,i):
            rep = self.parent[i]
            if self.parent[rep] != rep:
                self.parent[i] = self.find(rep)
                return self.parent[i]
            return rep

        def union(self,i,j):
            iRep = self.find(i)
            jRep = self.find(j)
            if iRep > jRep:
                self.parent[iRep] = jRep
            elif jRep > iRep:
                self.parent[jRep] = iRep

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = self.UnionFind()
        output = ""
        offset = ord('a')
        for i in range(len(s1)):
            tS1 = ord(s1[i]) - offset
            tS2 = ord(s2[i]) - offset
            uf.union(tS1,tS2)
        for character in baseStr:
            tChar = ord(character) - offset
            rep = chr(uf.find(tChar) + offset)
            output = output + rep
        return output

i = Solution()
s1 = "leetcode"
s2 = "programs"
base = "sourcecode"
print(i.smallestEquivalentString(s1,s2,base))
