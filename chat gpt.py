import random

SIZE = 10

def create_board():
    return [["." for _ in range(SIZE)] for _ in range(SIZE)]

def print_board(board, score):
    print("\n" + "=" * (SIZE*2))
    for row in board:
        print(" ".join(row))
    print("=" * (SIZE*2))
    print(f"Score: {score}")

def spawn_food(snake):
    while True:
        r = random.randint(0, SIZE-1)
        c = random.randint(0, SIZE-1)
        if [r, c] not in snake:
            return [r, c]

def main():
    
    snake = [[SIZE//2, SIZE//2]]
    direction = "RIGHT"
    food = spawn_food(snake)
    score = 0

    while True:

        board = create_board()
        for r, c in snake:
            board[r][c] = "O"
        head_r, head_c = snake[0]
        board[head_r][head_c] = "@"
        board[food[0]][food[1]] = "*"
        print_board(board, score)

        
        move = input("Move (W/A/S/D, Q=quit): ").strip().upper()
        if move == "Q":
            print("Game Over! Final Score:", score)
            break
        if move in ["W","A","S","D"]:
            direction = {"W":"UP","S":"DOWN","A":"LEFT","D":"RIGHT"}[move]

        
        dr, dc = 0, 0
        if direction == "UP": dr, dc = -1, 0
        elif direction == "DOWN": dr, dc = 1, 0
        elif direction == "LEFT": dr, dc = 0, -1
        elif direction == "RIGHT": dr, dc = 0, 1

        new_head = [snake[0][0] + dr, snake[0][1] + dc]

        
        if (new_head[0] < 0 or new_head[0] >= SIZE or
            new_head[1] < 0 or new_head[1] >= SIZE or
            new_head in snake):
            print("💀 You hit something! Game Over. Final Score:", score)
            break

        
        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = spawn_food(snake)
        else:
            snake.pop()

if __name__ == "__main__":
    main()
