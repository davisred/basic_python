rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue',
                  'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set = set()
print(empty_set)
print(type(empty_set))
number_list = [1, 43, 56]
text_tuple = ('sdfsd', 'asdasd', 'sjdbfjks')
set_from_list = set(number_list)
set_from_tuple = set(text_tuple)

set_from_list.add(777)
set_from_tuple.add('hello')
x = set_from_list.pop()

# ///// не возвращает ничего /////
y = set_from_list.remove(777)

set_from_list.discard(43)
set_from_list.discard(0)
set_from_list.clear()

print(set_from_list)
print(set_from_tuple)
print(x)
