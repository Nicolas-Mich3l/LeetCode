from leetcode373_ndam.kPairs import Solution 
import pytest 


@pytest.mark.parametrize("l1,l2,k,expected",[
    ([1,7,11],[2,4,6],3,[[1,2],[1,4],[1,6]]),
    ([1,1,2],[1,2,3],2,[[1,1],[1,1]]),
    ([0,0,0,0,0],[-3,22,35,56,76],22,[[0,-3],[0,-3],[0,-3],[0,-3],[0,-3],[0,22],[0,22],[0,22],[0,22],[0,22],[0,35],[0,35],[0,35],[0,35],[0,35],[0,56],[0,56],[0,56],[0,56],[0,56],[0,76],[0,76]])
    ])

def test_basic(l1,l2,k,expected):
    implementation = Solution()
    assert implementation.kSmallestPairs(l1,l2,k) == expected
