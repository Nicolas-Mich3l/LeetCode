from leetcode215_ndam.kthLargest import Solution 
import pytest 


implementation = Solution()

def test_Empty():
    assert implementation.findKthLargest([],0) is 0

@pytest.mark.parametrize("test_input,k,expected",[
    ([3,2,1,5,6,4],2,5),
    ([3,2,3,1,2,4,5,5,6],4,4),
    ])

def test_basic(test_input,k,expected):
    assert implementation.findKthLargest(test_input,k) is expected
