###문제:
##입력: 정수의 배열, 출력:  정점의 위치
## 정점:  주변보다 큰 값    왼쪽 오른쪽보다 큰 값
### 이진 탐색 참고


## 말로 설명
## 배열 봐봐 중간값 찍고  그거랑  그거 기준 주변값과 비교하기 ->  둘중 더 큰 값은? ->
# 더 큰 값 쪽으로 이동 양쪽다 큰값이면 이동하면되지
## 근데 둘다 큰값이 아니면?  그럼 그거가 정점이 되는듯?
##근데 양 끝에 있는거에 기회주려면   패딩 해줘야함 -> 그럼 인덱스가 바뀜
## 패딩하려면   끝에는 그냥 append 하면되니까 상관없고 처음거는 처음 인덱스보다 하나 작은 위치를 인덱스 0으로 바꾸면 다 이동시켜야함


## 근데 패딩해줘도   양끝단까지 갈수 있으려나?
# 일단 핵심 로직부터
#


# 내가짠거 ->  9가 안나오고  4가나옴 -> 뭔가 이상
def peak_find(A, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if (A[middle] > A[middle - 1]) and (A[middle] > A[middle + 1]):  ## 중간이  왼쪽보다 크고, 중간이 오른쪽보다 크면  그점이 정점
            return middle
        elif (A[middle] < A[middle - 1]):  # 중간보다 왼쪽이 크면  -> 그쪽으로
            return peak_find(A, low, middle - 1)
        elif (A[middle] < A[middle + 1]):  # 중간보다 오른쪽이 크면 -> 그쪽으로
            return peak_find(A, middle + 1, high)


A = [2, 4, 6, 8, 9, 3, 1]
p = peak_find(A, 0, len(A))
v = A[p]
print(f"정점 위치: {p}, 정점 값: {v}")
# def peak_find(A, left, right):
#     while left <= right:
#         middle = (left+right)//2
#         if(A[middle-1] <A[middle] and A[middle] > A[middle+1]):
#             return middle   # 패딩하면 middle -1
#         if A[middle-1] <A[middle]:
#             left += 1
#         else:
#             right -=1
#
#
#


# A = [2, 4, 6, 8, 9, 3, 1]


A = [3, 5, 4, 8, 9, 8]


def peak_find(A, low, high):
    if (low <= high):
        middle = (low + high) // 2

        left_val = float('-inf') if middle == 0 else A[middle - 1]

        right_val = float('-inf') if middle == len(A) - 1 else A[middle + 1]

        if (A[middle] > left_val) and (A[middle] > right_val):
            return middle
        elif (A[middle] < left_val):  # 왼쪽이 더 크면
            return peak_find(A, low, middle - 1)
        else:  # (A[middle] < right_val) # 오른쪽이 더 크면
            return peak_find(A, middle + 1, high)


print("Original : ", A)
peak_index = peak_find(A, 0, len(A) - 1)
print(f"Peak Index: {peak_index}")
print(f"Peak Value: {A[peak_index]}")