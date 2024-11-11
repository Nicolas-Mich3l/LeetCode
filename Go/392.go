// Given two strings s and t, return true if s is a subsequence of t, or false otherwise. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

import (
    "fmt"
)

func isSubsequence(s string, t string) bool {
    var tArr = strings.Split(t,"")
    var sArr = strings.Split(s,"")
    var curr = 0
    if s == "" {
        return true 
    }
    for i := range(tArr){
        if tArr[i] == sArr[curr] {
            curr += 1
        }
        if curr == len(sArr) {
            return true 
        }
    }
    return false 
}
