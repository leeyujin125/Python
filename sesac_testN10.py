def solution(board, h, w):
    n = len(board)
    count = 0
    x = [1, -1, 0, 0]
    y = [0, 0, -1, 1]

    for i in range(4):
        y_check = h + y[i]
        x_check = w + x[i]
        if 0 <= y_check < n and 0 <= x_check < n:
            if board[y_check][x_check] == board[h][w]:
                count += 1
    return count
