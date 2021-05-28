import sys
class Solution:
    def longestCommonPrefix(self, strs):
        maximum=max(strs)
        minimum=min(strs)
        i=0
        j=0
        str=""
        while i<len(maximum) and j<len(minimum):
            if maximum[i]==minimum[j]:
                str=str+maximum[i]
            elif maximum[0]!=minimum[0]:
                return ""
            else:
                break
            i=i+1
            j=j+1
        return str






if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower", "elow", "flights"]) )
    print(s.longestCommonPrefix(["dog", "racecar", "car"]))

