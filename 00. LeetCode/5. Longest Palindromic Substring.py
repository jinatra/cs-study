class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            # 홀수 길이 (중심: i 하나)
            odd = self.expand(s, i, i)
            # 짝수 길이 (중심: i, i+1 두개)
            even = self.expand(s, i, i+1)
            
            # 더 긴거로 생신
            if len(odd) > len(ans):
                ans = odd
            if len(even) > len(ans):
                ans = even
        return ans

    def expand(self, s, left, right):
        # 양쪽이 같은 동안 계속 퍼뜨림
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 마지막에 한번 더 나갔으니까 안쪽으로 한칸씩 좁혀서 반환
        return s[left+1:right]