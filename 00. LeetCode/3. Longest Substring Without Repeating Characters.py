class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            char = s[right]
            while char in seen: # 문자가 seen에 보이면
                seen.remove(s[left])
                left += 1 # 문자 중복이니까 왼쪽꺼 뺌
            seen.add(char)
            ans = max(ans, right - left + 1)
        return ans