# 反转链表
def reverse_list(list_node):
    if not list_node:
        return
    if not list_node.next:
        return list_node
    node = reverse_list(list_node.next)
    node.next.next = node
    node.next = None
    return node


# 最小的K个数
def find_k_min(arr, k):
    return sorted(arr)[:k]


def find_k_min2(arr, k):
    for i in range(1, k):
        j = i-1
        v = arr[i]
        while j >= 0 and arr[j] > v:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = v

    for i in range(k, len(arr)):
        if arr[i] < arr[k-1]:
            j = k - 1
            v = arr[i]
            while j >= 0 and arr[j] > v:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = v
    return arr[:k]


# 两数之和
def two_sum(arr, tar):
    temp = {}
    length = len(arr)
    for i in range(length):
        if tar - arr[i] in temp:
            return temp[tar - arr[i]], i
        else:
            temp[arr[i]] = i


if __name__ == '__main__':
    arr = [5, 3, 11, 7, 3, 6, 10, 1, 7, 9]
    print(two_sum(arr, 10))
