from leetcode1061_ndam.smallestEquivalentString import Solution 
import pytest 


implementation = Solution()

@pytest.mark.parametrize("s1, s2, base, expected",[
    ("parker","morris","parser","makkek"),
    ("hello","world","hold","hdld"),
    ("leetcode","programs","sourcecode","aauaaaaada"),
    ])

def test_basic(s1,s2,base,expected):
    assert implementation.smallestEquivalentString(s1,s2,base) == expected
