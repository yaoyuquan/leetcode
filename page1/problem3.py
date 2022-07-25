class Solution(object):
    def lengthOfLongestSubstring(self, text):
        """
        :type text: str
        :rtype: int
        """
        store_map = {}
        result, start, end = 0, 0, 0
        while end < len(text):
            if text[end] in store_map:
                new_start = store_map[text[end]] + 1

                for key in list(store_map):
                    if store_map[key] < new_start:
                        del store_map[key]

                start = new_start

            store_map[text[end]] = end
            end = end + 1

            result = max(result, end - start)

        return result
