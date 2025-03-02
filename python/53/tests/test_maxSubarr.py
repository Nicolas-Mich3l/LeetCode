from leetcode53_ndam.maxSubarr import Solution 
import pytest 


implementation = Solution()

def test_Empty():
    assert implementation.maxSubArray([]) is 0

@pytest.mark.parametrize("test_input,expected",[
    ([-2,1,-3,4,-1,2,1,-5,4],6),
    ([1],1),
    ([5,4,-1,7,8],23),
    ])

def test_basic(test_input,expected):
    assert implementation.maxSubArray(test_input) is expected
