class Solution:

    def reverse_integer(self, x: int) -> int:
        conv_int = str(x)
        new_array = []
        

        if x == 0 :
            return x
        
        if x < 0 : 
            for i in reversed(conv_int[1:]):
                new_array.append(str(i))

        else:
            for i in reversed(conv_int):
                new_array.append(str(i))

        s = [str(i) for i in new_array]
        res = ("".join(s))
        
        
        if int(res) < (-2**31) or int(res) > ((2**31)-1):
            return 0

        if x < 0 :
            return int("-"+res)

        else: 
            return(int(res))
            

        


if __name__ == "__main__":
    s = Solution()

    print(s.reverse_integer(123))
    print(s.reverse_integer(-123))
    print(s.reverse_integer(1230))
    print(s.reverse_integer(100))