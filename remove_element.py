class Solution:
    def removeElement(self, nums, val):
        nums[:] = [i for i in nums if i!= val]
        return len(nums)


if __name__ == "__main__":
    s = Solution()

    print(s.removeElement([0,1,2,2,3,0,4,2], 2)) # should return 5 []