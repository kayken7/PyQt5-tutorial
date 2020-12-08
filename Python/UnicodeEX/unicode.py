import sys

# 시스템 인코딩 설정의 출력

print('1.현재 문자 인코딩 :', sys.getdefaultencoding())
print('2.현재 파일 인코딩 :', sys.getfilesystemencoding())
print()

# 한글 인코딩 CP949, UTF-8, UTF-16

name1 = "MR (가) (ㅏ) (나) (달) (랅)".encode("EUC-KR")
name2 = "MR (ㄱ) (ㅏ) (나) (달) (랅)".encode("CP949")
name3 = "MR (가) (ㅏ) (나) (달) (랅)".encode("UTF-8")
name4 = "MR (ㄱ) (ㅏ) (나) (달) (랅)".encode("UTF-16")
name5 = "MR ASCII CODE".encode("ASCII")
name6 = "가".encode("UTF-32")
name7 = "가".encode("UTF-16")

# 코드 출력하기

print("[인코딩 문자 출력]")
print("[EUC-KR] : ", name1)
print("[CP949]  : ", name2)
print("[UTF-8]  : ", name3)
print("[UTF-16] : ", name4)
print("[ASCII]  : ", name5)
print("[UTF-32]  : ", name6)
print("[UTF-16]  : ", name7)
print()

# 디코딩(복호화) 출력하기

print("[디코딩 문자 출력]")
print(name1.decode('EUC-KR'))
print(name2.decode('CP949'))
print(name3.decode('UTF-8'))
print(name4.decode('UTF-16'))
print(name5.decode('ASCII'))
print()

# 코드를 사용한 디코딩(복호화)

print(b'\xa4\xa1'.decode('EUC-KR'))
print(b'\xa4\xa1'.decode('CP949'))
print()

# CP949를 UTF-8로 변환

decoded = 'ㄱ'.encode('CP949').decode('CP949')
encoded = decoded.encode('utf-8')
print("CP949코드 'ㄱ': ", 'ㄱ'.encode('CP949'))
print("UTF-8코드 'ㄱ': ", encoded)
print()

# 0 ~ 65535까지 유니코드 출력하기

# count = 0
# for i in range(0xac00, 0xd7a4):
#     if i % 15 == 0:
#         print()
#
#     print(hex(i),'|', chr(i), end=' ')
#
# print(0xd7a4 - 0xac00)
# print()


print('[유니코드] :', chr(0xB098), hex(0xB098))
print('0xB0 : ', bin(0xB0))
print('0x98 : ', bin(0x98))
print()

utf8byte1 = 0b11100000
utf8byte2 = 0b10000000
utf8byte3 = 0b10000000

print('[UTF-8 binary format]')
print('1st Byte:', bin(utf8byte1), end=', ')
print('2nd Byte:', bin(utf8byte2), end=', ')
print('3rd Byte:', bin(utf8byte3))
print('1st Byte: 0b1110XXXX, 2nd Byte: 0b10XXXXXX, 3rd Byte: 0b10XXXXXX')


h1 = 0xB0 >> 4
print('h1:', bin(h1)[2:].zfill(4))

h2 = 0xB0 << 2
h2 = h2 & 0b0000111100
print('h2:', bin(h2)[2:].zfill(4))

h3 = 0x98 >> 6
print('h3:', bin(h3)[2:].zfill(2))

h4 = 0x98 & 0b00111111
print('h4:', bin(h4)[2:].zfill(6))
print()

c1 = bin(utf8byte1 | h1)
c2 = bin(utf8byte2 | h2 | h3)
c3 = bin(utf8byte3 | h4)

print('[바이트 3개]')
print(c1)
print(c2)
print(c3)
print()

print('[UTF-8 인코딩 완료]')
print(hex(int(c1, 2)), end=' ')
print(hex(int(c2, 2)), end=' ')
print(hex(int(c3, 2)))

test1 = "나".encode("UTF-8")
print(test1)





