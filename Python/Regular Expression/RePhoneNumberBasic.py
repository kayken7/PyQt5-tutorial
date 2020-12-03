import re

phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d\d)-(\d\d\d\d)')

mo = phoneNumRegex.search('내 전화번호 (010)-1111-2222')
print('전화번호 전체 : ' + mo.group(0))
print('전화번호 앞자리 : ' + mo.group(1))
print('전화번호 중간 : ' + mo.group(2))
print('전화번호 뒷자리 : ' + mo.group(3))
print(mo.groups())
base, number1, number2 = mo.groups()
print(base)
print(number1)
print(number2)
