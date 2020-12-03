import re

regex = re.compile(r'apple|orange|kiwi')
mo1 = regex.search('I have an apple and 3 orange and 5 kiwi')
print(mo1.group())

mo2 = regex.search('My favorite is a cup of orange juice after '
                   'lunch. I do not like apple that much')
print(mo2.group())

mo3 = regex.search('everyone loves kiwi. it has special taste. '
                   'one apple after mango')
print(mo3.group())
