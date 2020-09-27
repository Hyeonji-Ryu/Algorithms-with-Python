# 프렌즈4블록

# 블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
# 같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
# 만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 
# 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.
# 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.
# 만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
# 위 초기 배치를 문자로 표시하면 아래와 같다.

# TTTANT
# RRFACC
# RRRFCC
# TRRRAA
# TTMMMF
# TMMTTJ

# 각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다
# 입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

# 입력 형식
# 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
# 2 ≦ n, m ≦ 30
# board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.

# 출력 형식
# 입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.



def solution(m, n, board):
    def find_double(m,n,board):
        lis = []
        total = []
        for i in range(m):
            for j in range(n-1):
                if board[i][j] == board[i][j+1]:
                    lis.append([board[i][j],i,j,j+1])
        for i in range(len(lis)-1):
            for j in range(i,len(lis)):
                if lis[i][2:4] == lis[j][2:4] and lis[j][1]-lis[i][1] == 1 and lis[j][0]==lis[i][0] != '*':
                    total.append([lis[j],lis[i]])
        return total
    
    def delete_and_pull(board, doubles):
        for i in range(len(doubles)):
                board[doubles[i][0][1]][doubles[i][0][2]] = '*'
                board[doubles[i][0][1]][doubles[i][0][3]] = '*'
                board[doubles[i][1][1]][doubles[i][0][2]] = '*'
                board[doubles[i][1][1]][doubles[i][0][3]] = '*'

        for j in range(m-1,0, -1):
            for k in range(n):
                count = j-1
                while  board[j][k] == '*' and count != -1:
                    board[j][k] = board[count][k]
                    board[count][k] = '*'
                    count -= 1
                    
        return board

    board = [list(board[i]) for i in range(m)]
    doubles = find_double(m,n,board)
    while len(doubles) != 0:
        board = delete_and_pull(board, doubles)
        doubles = find_double(m,n,board)
    answer = 0
    for i in range(m):
        answer += board[i].count('*')

    return answer
