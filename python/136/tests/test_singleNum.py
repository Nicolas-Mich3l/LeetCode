from leetcode136_ndam.singleNum import Solution 
import pytest 


implementation = Solution()

def test_Empty():
    assert implementation.singleNumber([]) is 0

@pytest.mark.parametrize("test_input,expected",[
    ([2,2,1],1),
    ([4,1,2,1,2],4),
    ([1],1),
    ])

def test_basic(test_input,expected):
    assert implementation.singleNumber(test_input) is expected
