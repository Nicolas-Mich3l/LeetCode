from isValidParens.twenty import Solution

def test_Matching():
    implementation = Solution()
    assert implementation.isValid("") is True
    assert implementation.isValid("(){}[]") is True
    assert implementation.isValid("([{}])") is True
    assert implementation.isValid("({[]}[]([]{}))") is True
    assert implementation.isValid("(") is False
    assert implementation.isValid("{]") is False
    assert implementation.isValid("([)]") is False
    assert implementation.isValid(")") is False
