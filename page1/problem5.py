class Solution:
    def longestPalindrome(self, param: str) -> str:

        length = len(param)

        if length <= 1:
            return param
        else:
            result = ""
            for index, value in enumerate(param):
                left, right = index, index
                while left >= 0 and right < length and param[left] == param[right]:
                    if len(result) < right - left + 1:
                        result = param[left:right + 1]
                    left = left - 1
                    right = right + 1
                left = index
                right = index + 1
                while left >= 0 and right < length and param[left] == param[right]:
                    if len(result) < right - left + 1:
                        result = param[left:right + 1]
                    left = left - 1
                    right = right + 1
            return result

