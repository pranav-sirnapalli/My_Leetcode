class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for ch in tokens:
            if ch == '+':
                st.append(st.pop()+st.pop())
            elif ch == '-':
                second, first = st.pop(), st.pop()
                st.append(first-second)
            elif ch == '*':
                st.append(st.pop()*st.pop())
            elif ch == '/':
                second, first = st.pop(), st.pop()
                st.append(int(first/second))
            else:
                st.append(int(ch))
        return st[0]