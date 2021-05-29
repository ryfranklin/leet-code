class Solution:
    def strStr(self, haystack, needle):
        index = haystack.find(needle)
        print(index)

if __name__ == "__main__":
    s = Solution()
    s.strStr("hello", "aa") #2