class Convert:
    
    def intToRoman(self, arabic):
        
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans   = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        romanNumeral = ""
                                                           
        i = 0                                              
        while  arabic > 0:                                   
            for _ in range(arabic // integers[i]):         
                romanNumeral = romanNumeral + romans[i]    
                arabic = arabic - integers[i]                      
            i = i + 1                                     
        return romanNumeral                                


def main():
    print("The corresponding Roman numeral is: ", Convert().intToRoman(8))
    print("The corresponding Roman numeral is: ", Convert().intToRoman(16))
    print("The corresponding Roman numeral is: ", Convert().intToRoman(32))
    print("The corresponding Roman numeral is: ", Convert().intToRoman(64))


if __name__ == '__main__':
    main()