"""Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1
to n and obeys the following requirement: Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|,
|a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.
If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1
distinct integer: 1.

Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2
distinct integers: 1 and 2.

Note:
The n and k are in the range 1 <= k < n <= 104."""


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1:
            return list(range(1, n + 1))

        kR = list(range(k, 1, -1))
        N = list(range(1, n + 1))
        j = 0
        for i in kR:
            x = self.find(N[j:], i, N[j])
            N.pop(N.index(x))
            N.insert(j + 1, x)
            j += 1

        return N

    def find(self, arr, num, h):
        for x in arr:
            if x - h == num or h - x == num:
                return x


class Solution2:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1:
            return list(range(1, n + 1))

        kR = list(range(k, 0, -1))
        N = [1]

        for i in kR:
            if N[-1] + i - 1 > k:
                N.append(N[-1] - i)
            else:
                N.append(N[-1] + i)

        x = list(range(1, n + 1))
        for w in x:
            if w not in N:
                N.append(w)

        return N

class Solution3:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [0] * n
        a = 1
        z = k+1
        for i in range(k+1):
            if i % 2:
                ans[i] = z
                z -= 1
            else:
                ans[i] = a
                a += 1
        for i in range(k+1,n):
            ans[i] = i + 1
        return ans

# Submission Details:
# >97%/>93%
