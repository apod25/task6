lst = [30, 75, 9, 97, 50, -4, 70, 59]
lst.sort()
print(lst[-1])
lst.reverse()
lst.pop()
print(lst[2:-1])
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
count = 0
for sublist in main_lst:
    if isinstance(sublist,list)and "python" in sublist:
        count+= 1
print(count)
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
sentence = ' '.join(word.title() for word in my_lst)
print(sentence)
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
copied_lst = []
for item in my_lst:
    copied_lst.append(item)
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
if len(my_lst) >= 5 :
     my_lst[2] , my_lst[4]= my_lst[4] , my_lst[2]
print(my_lst)
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
sumlst = sum(nums)
print(sumlst)
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = tuple1 +(9,)
print(tuple2)
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
new_tuple = tuple1+tuple2
print(new_tuple)
