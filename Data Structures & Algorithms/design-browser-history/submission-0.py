class ListNode:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode("")
        self.tail = ListNode("")
        self.curr = ListNode(homepage)
        self.head.next = self.curr
        self.tail.prev = self.curr
        self.curr.next = self.tail
        self.curr.prev = self.head

    def visit(self, url: str) -> None:
        visit, next, prev = ListNode(url), self.tail, self.curr
        visit.next = next
        visit.prev = prev
        prev.next = visit
        next.prev = visit
        self.curr = visit

    def back(self, steps: int) -> str:
        curr = self.curr
        while steps > 0 and curr.prev != self.head:
            curr = curr.prev
            steps -= 1
        self.curr = curr
        return self.curr.url            

    def forward(self, steps: int) -> str:
        curr = self.curr
        while steps > 0 and curr.next != self.tail:
            curr = curr.next
            steps -= 1
        self.curr = curr
        return self.curr.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)