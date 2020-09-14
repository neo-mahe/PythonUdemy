import string
# here char =i is the vowel we are looking for
# char = 'i'
# vowel_string = 'aeiou'
# print(char.lower() in vowel_string)

# To check if the string has consonants
vowel_string = 'aeiou'
char = '1'
# this is including 1 which is a numeric value as consonant
print(char.lower() not in vowel_string)

# this will exclude 1 which is a numeric value from consonant
print(char.isalpha() and char.lower() not in vowel_string)
