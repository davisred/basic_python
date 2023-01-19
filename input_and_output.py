# x = input('Input something: ')
# print(f'Output something. {x}')

# beatles = open('C:\sample.txt', mode='r')
# for line in beatles:
#     print(line, end='')
# beatles.close()

# beatles = open('C:\sample.txt', mode='r')
# for line in beatles:
#     if 'still' in line.lower():
#         print(line, end='')
# beatles.close()

# with open('C:\sample.txt', mode='r') as beatles:
#     for line in beatles:
#         if 'still' in line.lower():
#             print(line, end='')

# with open('C:\sample.txt', mode='r') as beatles:
#     line = beatles.readline()
#     while line:
#         print(line, end='')
#         line = beatles.readline()

# with open('C:\sample.txt', mode='r') as beatles:
#     lines = beatles.readlines()
# print(lines)
# for line in lines[::-1]:
#     print(line, end='')

with open('C:\sample.txt', mode='r') as beatles:
    text = beatles.read()
print(text)

