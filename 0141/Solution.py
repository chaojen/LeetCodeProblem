# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Runtime: 57 ms
# Memory: 20.48 MB
class Solution:
    def hasCycle(self, head: [ListNode]) -> bool:
        # 龜兔賽跑法，假設如果列表中有回循環，跑得快的指標會追上跑得慢的指標
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False

nodeA = ListNode(3)
nodeB = ListNode(2)
nodeC = ListNode(0)
nodeD = ListNode(-4)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
# nodeD.next = nodeA

print(f"hasCycle: {Solution().hasCycle(nodeA)}")