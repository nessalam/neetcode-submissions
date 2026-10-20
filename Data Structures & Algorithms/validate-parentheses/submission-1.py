class Solution:
    def isValid(self, s: str) -> bool:
        match = { ")" : "(", "]" : "[", "}" : "{" }
        temp = []
        if s:
            for c in s:
                if c in match:
                    if temp and temp[-1] == match[c]:
                        temp.pop()
                    else:
                        return False
                else:
                    temp.append(c)
        return True if not temp else False
                