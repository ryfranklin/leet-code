class Solution:
    def isPalindrome(self, x: int) -> bool:
        conv_string = str(x)
        last_dig = -1
        for dig in conv_string:
            if dig == conv_string[last_dig]:
                last_dig-=1
            else: 
                return False
            
        return True

if __name__ == "__main__":
    s = Solution()

    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))
    print(s.isPalindrome(-101))