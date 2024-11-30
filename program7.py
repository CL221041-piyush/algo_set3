
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text if char in vowels)

num_to_text = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 
    12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 
    70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred"
}

def number_to_text(num):
    if num <= 19:
        return num_to_text[num]
    elif num < 100:
        tens = (num // 10) * 10
        ones = num % 10
        return num_to_text[tens] + (num_to_text[ones] if ones != 0 else "")
    else:
        return "hundred"

def count_pairs(nums, D):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == D:
                count += 1
    return count

def main():
    T = int(input())  
    
    for _ in range(T):
        nums = list(map(int, input().split()))  
        
        total_vowels = 0
        for num in nums:
            text = number_to_text(num)
            total_vowels += count_vowels(text)
        
        D = total_vowels  
        pair_count = count_pairs(nums, D)
        
        result_text = ["zero", "one", "two", "three", "four", "five", 
                       "six", "seven", "eight", "nine", "ten", "eleven", 
                       "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
                       "seventeen", "eighteen", "nineteen", "twenty"]
        if pair_count > 100:
            print("greater 100")
        else:
            print(result_text[min(pair_count, 20)])








main()
