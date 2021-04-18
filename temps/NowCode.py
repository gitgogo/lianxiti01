# 1反转链表
def reverse_list(list_node):
    if not list_node:
        return
    if not list_node.next:
        return list_node
    node = reverse_list(list_node.next)
    node.next.next = node
    node.next = None
    return node


# 2最小的K个数
def find_k_min(arr, k):
    return sorted(arr)[:k]


def find_k_min2(arr, k):
    for i in range(1, k):
        j = i - 1
        v = arr[i]
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v

    for i in range(k, len(arr)):
        if arr[i] < arr[k - 1]:
            j = k - 1
            v = arr[i]
            while j >= 0 and arr[j] > v:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = v
    return arr[:k]


# 3两数之和
def two_sum(arr, tar):
    temp = {}
    length = len(arr)
    for i in range(length):
        if tar - arr[i] in temp:
            return temp[tar - arr[i]], i
        else:
            temp[arr[i]] = i


# 4最长无重复子串
def max_length(arr):
    max_len, i = 0, 0
    temp = {}
    for j in range(len(arr)):
        if arr[j] in temp:
            i = max(i, temp[arr[j]] + 1)
        temp[arr[j]] = j
        max_len = max(max_len, j - i + 1)
    return max_len


# 5括号序列
def is_valid(s):
    while '{}' in s or '()' in s or '[]' in s:
        s = s.replace('[]', '').replace('()', '').replace('{}', '')
    return s == ''


def is_valid2(s):
    mapping = {'}': '{', ']': '[', ')': '('}
    stack = []
    for c in s:
        if c not in mapping:
            stack.append(c)
        else:
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop()
    return stack == []


# 有重复数字的升序数组查找
def search(nums, tar):
    i, j, mid = 0, len(nums) - 1, 0
    while i <= j and mid < len(nums):
        mid = (j + i) // 2
        if tar == nums[mid]:
            while mid > 0:
                if tar != nums[mid-1]:
                    return mid
                mid -= 1
            return mid
        elif tar < nums[mid]:
            j = mid - 1
        else:
            i = mid + 1
    return -1


# 最长回文子串,用Python2执行
def get_longest_palindrome(s):
    max_len = 1
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                print('i==j',i,j)
                max_len = max(max_len, len(s[i:j+1]))
    return max_len


def get_longest_palindrome2(A):
    max_offset1 = 1
    max_offset2 = 1
    for i in range(1, len(A) - 1):
        offset = 1
        while A[i - offset] == A[i + offset]:
            offset += 1
            if i - offset < 0 or i + offset > len(A) - 1:
                break
        if offset > max_offset1:
            max_offset1 = offset

        offset = 0
        while A[i - offset] == A[i + 1 + offset]:
            offset += 1
            if i - offset < 0 or i + 1 + offset > len(A) - 1:
                break

        if offset > max_offset2:
            max_offset2 = offset

    return max(max_offset1 * 2 - 1, max_offset2 * 2)


if __name__ == '__main__':
    arr = [5, 3, 11, 7, 3, 6, 10, 1, 7, 9]
    arr1 = [1, 2, 2, 3, 4]
    print(get_longest_palindrome2('igqqi'))
