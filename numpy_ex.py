import numpy as np

#시험
a = np.array([True, False], dtype=bool)
print(a.dtype.kind)  # b: 불리언 계열이라는 뜻

b = np.array([1, 2], dtype='b')
print(b.dtype)       # int8: 여기서 'b'는 8비트 정수를 지정




# N19 · PPT 27페이지 (인쇄 쪽번호 26) · 기본 예제
# 시험 : 원본이 안바뀜
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
print('원본:', arr)
print('음수의 변환은 내림과 다름:', np.array([-3.9]).astype(int))



# N20 · PPT 29페이지 (인쇄 쪽번호 28) · 변형 예제
# 시험 [] 갯수가 차원을 결정한다
print(np.array([1,2,3]).ndim)
print(np.array([[1,2,3]]).ndim)




# 출력 괄호 주의. 시험에서 대괄호 갯수 주의
# Q01 · PPT 34페이지 (인쇄 쪽번호 33) · 직접 풀기
a = np.arange(1, 13)
answer = a.reshape(2,2,3)
print(answer, '\n', answer.ndim)

# N40 · PPT 51페이지 (인쇄 쪽번호 50) · 변형 예제
print(np.array_split(np.arange(7),3))
print(np.array_split(np.arange(3),5))

# N41 · PPT 52페이지 (인쇄 쪽번호 51) · 변형 예제
# 얕은복사 주의
a=np.array([1,2,3]); b=a
b[0]=99
print(a)

a=np.array([1,2,3]); b=a.copy()
b[0]=99
print(a)

# Q03 · PPT 53페이지 (인쇄 쪽번호 52) 직접 풀기
# 값만 때고 싶으면 answer[0]으로 값만 때와야 함
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
answer = np.where(a==b)
print(answer)
print(answer[0])
# 여기에 풀이를 작성하세요.