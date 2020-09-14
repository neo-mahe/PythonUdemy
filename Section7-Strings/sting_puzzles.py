import string

# to split the words in a sentance in an individual line
string_example = "This is a great thing"
print(string_example.split())
for word in string_example.split():
    print(word)

# If the sentence contains new line characters
string_example2 = "from\nstring\nexample\n2"
print(string_example2)
print(string_example2.splitlines())
for word in string_example2.splitlines():
    print(word)