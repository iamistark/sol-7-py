def reverse_words(s):
    words = s.split()  
    reversed_words = [word[::-1] for word in words]  
    reversed_sentence = ' '.join(reversed_words)  
    return reversed_sentence
#Driver code
s = "Let's take LeetCode contest"
print(reverse_words(s))  
