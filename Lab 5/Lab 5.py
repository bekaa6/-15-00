lst = [1, 2, 3, 4, 5]
reversed_lst = lst[::-1]
print("Исходный список:", lst)
print("Обратный порядок:", reversed_lst)

def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)

lst = [-10, 3, -5, 7, -1]
sorted_lst = list_sort(lst)
print("Исходный список:", lst)
print("Отсортированный по убыванию абсолютных значений:", sorted_lst)

def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

lst = [1, 2, 3, 4]
changed_lst = change(lst)
print("Изменённый список:", changed_lst)
