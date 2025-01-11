words = []

def number_to_name(n):
    zero=["zero"]
    ones=["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens=["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens=["","","twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    hundred=[""]
    
    return tens[n // 10] + (teens[n%10] if n%100//10 == 1 else ones[n%10]) + ("zero" if n == 0 else "")

for i in range(90):
    print(i, ": ", number_to_name(i))



