def my_docor(func): 
    def my_inner_func(*args, **kwargs):
        for arg in args:
            print(arg)
        result = func(*args, **kwargs)        
        return result
    return my_inner_func

@my_docor
def merge_sort(l: list) -> list:
    if len(l) <= 1:
        return l
    
    left = merge_sort(l[:len(l)//2])
    right = merge_sort(l[len(l)//2:])

    return merge_sorted_lists(left, right)

def merge_sorted_lists(a: list[int], b: list[int]) -> list[int]:
    a_indx = 0
    b_indx = 0

    sorted_list = []

    while a_indx < len(a) and b_indx < len(b):
        if a[a_indx] <= b[b_indx]:
            sorted_list.append(a[a_indx])
            a_indx += 1
        else:
            sorted_list.append(b[b_indx])
            b_indx += 1

    while a_indx < len(a):
        sorted_list.append(a[a_indx])
        a_indx += 1
    while b_indx < len(b):
        sorted_list.append(b[b_indx])
        b_indx += 1

    return sorted_list

def main():
    print(merge_sort([5, 1, 4, 2, 3]))                    

if __name__ == "__main__":
    main()