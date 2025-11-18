# Bug 4 수정: 임시 리스트를 인자로 받도록 변경
def merge_sort(A, left, right):
    """
    병합 정렬을 재귀적으로 수행하는 함수
    """
    if left < right:
        # Bug 1: 정수 나눗셈(//)으로 수정
        mid = (left + right) // 2

        merge_sort(A, left, mid)

        # Bug 2: 재귀 호출 범위 수정 (left -> right)
        merge_sort(A, mid + 1, right)

        merge(A, left, mid, right)


# Bug 3, 4 수정: 'sorted' 대신 'sorted_list' 인자를 받음
def merge(A, left, mid, right):
    """
    두 개의 정렬된 하위 배열을 병합하는 함수
    """
    k = left  # sorted_list의 시작 인덱스

    # Bug 5: 왼쪽 배열 시작 인덱스 수정 (right -> left)
    i = left  # 왼쪽 하위 배열의 시작 인덱스

    j = mid + 1  # 오른쪽 하위 배열의 시작 인덱스

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]  # sorted -> sorted_list
            i, k = i + 1, k + 1
        else:
            sorted[k] = A[j]  # sorted -> sorted_list
            j, k = j + 1, k + 1

    # 남아있는 요소들을 복사
    if i > mid:
        sorted[k:k + right - j + 1] = A[j:right + 1]
    else:
        sorted[k:k + mid - i + 1] = A[i:mid + 1]

    # 원본 배열 A에 정렬된 결과를 복사
    A[left:right + 1] = sorted[left:right + 1]



A = [8, 1, 7, 3, 9, 2, 4, 5]
print("정렬전 리스트:", A)


# Bug 4: 임시 리스트(sorted_list) 정의
sorted = [0] * len(A)

# Bug 6: 호출 인덱스 수정 (len(A)+1 -> len(A)-1)
merge_sort(A, 0, len(A) - 1)

print("정렬된 리스트:", A)