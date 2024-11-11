//Given the head of a singly linked list, reverse the list, and return the reversed list.

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

import (
    "fmt"
 )

func reverseList(head *ListNode) *ListNode {
    var prev, current, nextNode *ListNode
    current = head
    
    for current != nil {
        nextNode = current.Next 
        current.Next = prev 
        prev = current 
        current = nextNode
    }
    
    return prev
}

