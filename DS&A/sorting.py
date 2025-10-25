

def selection_sort(data):
    n = len(data)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if data[j] < data[min]:
                min = j
        data[i], data[min] = data[min], data[i]
        print(f"(Selection) Step {i} =", data)


def insertion_sort(data):
    # 리스트의 두 번째 원소부터 시작하여 마지막 원소까지 반복
    for i in range(1, len(data)):
        key = data[i]  # 현재 삽입할 원소를 'key'로 지정
        j = i - 1  # 비교할 첫 번째 이전 원소의 인덱스

        # key가 j 위치의 값보다 작고, j가 음수가 아닐 때까지 반복
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]  # 현재 위치의 값을 한 칸 뒤로 밀기
            j -= 1  # 왼쪽으로 이동하며 비교

        data[j + 1] = key  # 올바른 위치에 key 삽입
        print(f"(insertion) Step {i} =", data)
def partition(A, left, right):
    pivot = A[left]
    low = left +1
    high = right
    while(low<=high):
        while low<= right and A[low] <= pivot:
            low +=1
        while high >= left and A[high] > pivot:
            high -= 1
        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    print(f"quick: {data}")
    return high
def quick_sorting(A, left, right):
    if left <right:
        q = partition(A,left,right)
        quick_sorting(A,left,q-1)
        quick_sorting(A,q+1, right)
data = [1,2]
print("Original : ", data)
quick_sorting(data,0, len(data)-1)
print("Selection :", data)



