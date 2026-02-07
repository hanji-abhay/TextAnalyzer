class TextAnalyzer:

     #taking input from user out of the class

    def __init__(self, text):
        self.text = text.lower()
        self.words = self.text.split()
   
   #checking frequency of words in the sentence

    def word_frequency(self):
        freq = {}
        for word in self.words:
            freq[word] = freq.get(word, 0) + 1
        return freq
    
   #checking frequency of characters in the words

    def char_frequency(self):
       freq = {}
       for ch in self.text:
         if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
       return freq
    
    #checking most-frequent words in the sentence

    def most_frequent_words(self):
     freq = self.word_frequency()
     max_count = max(freq.values())
     result = []
     for word, count in freq.items():
        if count == max_count:
            result.append(word)
     return result, max_count
    
    #checking least-frequent words in the sentence

    def least_frequent_words(self):
     freq = self.word_frequency()
     least_count = min(freq.values())
     result = []
     for word, count in freq.items():
        if count == least_count:
            result.append(word)
     return result, least_count
    
    #checking if the word is palindrome or not

    def palindrome_check(self):
       palinDrome = self.word_frequency()
       Palindromic_word = [f"{word} is palindrome" if str(word) == str(word)[::-1] and len(word)>1 else f"{word} is not palindrome" for word in palinDrome.keys()]
       return Palindromic_word
    
    #counting the numbers of vowels and consonant in the sentence

    def vowelConsonantCount(self):
       Vowel = self.char_frequency()
       vowels = {"a", "e", "i", "o", "u"}
       vowel_count = 0
       consonant_count = 0
       for ch, count in Vowel.items():
         if ch.isalpha():
          if ch in vowels:
              vowel_count+=count
          else:
           consonant_count +=count
       return vowel_count, consonant_count
       
txt = input("Enter the text: \n") #taking user input

text = TextAnalyzer(txt) #created object named text of the class TextAnalyzer

print("\n Frequencies of words are: \n", text.word_frequency()) #calling and printing word_frequency method
print("\n Frequencies of characters are: \n", text.char_frequency()) #calling and printing char_frequency method
print("\n Most frequent words are: \n", text.most_frequent_words())  #calling and printing most_frequent_words method
print("\n Least frequent words are: \n", text.least_frequent_words()) #calling and printing least_frequent_words method
print("\n Palindrome check is: \n", text.palindrome_check())   #calling and printing palindrome_check method
v, c = text.vowelConsonantCount()             #calling and assigning vowelConsonantCount method in v and c variables
print(f"\n vowels count in the sentence: {v}, consonants count in the sentence: {c}")    #printing v and c