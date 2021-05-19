# for 반복문과 * 문자를 이용해서 트리만들기

## 1. 삼각형 만들기


`i`는 세로방향, `j`는 가로방향을 나타낸다

첫 행은 `i`가 0인데, j는 0~4까지 있다.
따라서 첫행에서 `i >= j`를 한다면 별이 1개만 출력된다.

삼각형을 만들려면 `for` 문을 만들고 그 안에 두개의 `j` 초기화식이 필요하다.

## 2. 막대기 만들기

막대기를 만들고 싶어서 for문을 사용했는데 문제가 발생했다. 위에 공백 1칸이 발생해서 어떻게 처리해야하나 고민했다.
`print()`를 삭제하면 `*`이 밀려버렸기 때문이다.

여기에서 줄간격을 위해 쓴 `print()`가 `\n` 때문에 공백을 만드는 것을 알았다.

그래서 맨 마지막 `print()`를 `print(' ' * 3, '*')`으로 작성해서 간격을 맞추고 `*`을 삽입했다.


```python
for i in range(5):
    for j in reversed(range(5)):
        if j <= i:
            print('*', end='', )
        else:
            print(' ', end='')
    for j in range(5):
        if j < i:
            print('*', end='')    
    print()
print(' ' * 3, '*')
for i in range(2):
    for j in reversed(range(5)):
        if i == j:
            print(' ' * 3, '*', end='')
    print()
print(' '* 2 ,'*'  * 3)```
