class Solution:

    def reverse(self, x: int) -> int:
        result, x_remaining = 0, abs(x)
        while x_remaining:
            result = result * 10 + x_remaining % 10
            x_remaining //= 10
        
        if result < (-2**31) or result > ((2**31)-1):
            return 0
        if x < 0:
            return -result 
        else:
             return result 

if __name__ == "__main__":
    s = Solution()

    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(1200))


