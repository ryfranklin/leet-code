class Solution:


    def romanToInt(self, s: str) -> int:
        totals = 0
        value_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for val in range(len(s)):
            if val - 1 >= 0:
                if (s[val] == "V" and s[val - 1] == "I"):
                    totals += 3
                
                elif (s[val] == "X" and s[val - 1] == "I"):
                    totals += 8
                
                elif (s[val] == "L" and s[val - 1] == "X"):
                    totals += 30

                elif (s[val] == "C" and s[val - 1] == "X"):
                    totals += 80

                elif (s[val] == "D" and s[val - 1] == "C"):
                    totals += 300 
                
                elif (s[val] == "M" and s[val - 1] == "C"):
                    totals += 800

                else:
                    totals += value_dictionary[s[val]]


            else:
                totals += value_dictionary[s[val]]
            
        
        return int(totals)
            

if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("III"))
    print(s.romanToInt("IV"))
    print(s.romanToInt("IX"))
    print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV")) #1994
