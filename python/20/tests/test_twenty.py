from leetcode20_ndam.twenty import Solution
import pytest

def test_Empty():
    implementation = Solution()
    assert implementation.isValid("") is True

def test_Correct():
    implementation = Solution()
    assert implementation.isValid("(){}[]") is True
    assert implementation.isValid("([{}])") is True
    assert implementation.isValid("({[]}[]([]{}))") is True
    
@pytest.mark.parametrize("test_input,expected",[
    ("(",False),
    ("{]",False),
    ("([}])",False),
    (")",False),
    ])

def test_Incorrect(test_input,expected):
    implementation = Solution()
    implementation.isValid(test_input) is expected
