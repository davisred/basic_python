import unicodedata
# colors_list = ['red' , 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'dark green']
#
# with open(r'C:\Users\Davis\OneDrive\Документы\rainbow(1).txt', mode='w') as rainbow:
#     for color in colors_list:
#         print(color, file=rainbow)

colors_list = []
with open(r'C:\Users\Davis\OneDrive\Документы\rainbow(1).txt', mode='r') as rainbow:
    for color in rainbow:
        colors_list.append(color.strip('\n'))

print(colors_list)

with open(r'C:\Users\Davis\OneDrive\Документы\rainbow(1).txt', mode='a') as rainbow:
    print('dark green', file=rainbow)
    print('dark blue', file=rainbow)
