class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            print(stack)
            if i.startswith("-"):
                stack.append(-int(i.lstrip("-")))
            if i.isnumeric():
                stack.append(int(i))
            if i == "+":
                stack.append(int(stack[-1])+int(stack[-2]))
            if i == "D":
                stack.append(int(stack[-1])*2)
            if i == "C":
                stack.pop()   

        # print(stack)
        total_sum = 0
        for i in stack:
            total_sum += i
        return total_sum