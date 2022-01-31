# exercise 1
import random

def place_ring(board):
    l=list(range(0,3))
    global rings_s, rings_m, rings_l
    # Choosing the ring size and the place it'll be placed on.
    size=random.choice(l)
    i=random.choice(l)
    j=random.choice(l)

    # If the game runs out of rings it ends. I don't think it's possible for
    # it to run out of rings though.
    if rings_s==0 and rings_m==0 and rings_l==0:
        return 1

    # Checking if chosen place is available and if there are enough rings
    # of chosen size.
    if(size==0 and rings_s>0 or size==1 and rings_m>0 or size==2 and rings_l>0):
        if board[i][j][size]==0:
            board[i][j][size]=1
            if size==0:
                rings_s-=1
            elif size==1:
                rings_m-=1
            else:
                rings_l-=1
    else:
        # If place and/or size isn't available, call the function again.
        place_ring(board)
    return 0

#Checks if the game is over.
def check_over(board):

    # k is the size of the ring.
    for k in range(3):
        # Checks the diagonals for a line of 3 same size rings.
        if board[0][0][k]==1 and board[1][1][k]==1 and board[2][2][k]==1:
            return 1
        if board[0][2][k]==1 and board[1][1][k]==1 and board[2][0][k]==1:
            return 1
        # Checks each row and column for a line of 3 same size rings.
        for i in range(3):
            if (board[i][0][k]==1 and board[i][1][k]==1 and
            board[i][2][k]==1):
                return 1
            if (board[0][i][k]==1 and board[1][i][k]==1 and
            board[2][i][k]==1):
                return 1
    # Checks the diagonals for a line of 3 rings in both ascending and
    # descending order.
    if board[0][0][0]==1 and board[1][1][1]==1 and board[2][2][2]==1:
        return 1
    if board[0][0][2]==1 and board[1][1][1]==1 and board[2][2][0]==1:
        return 1
    if board[0][2][0]==1 and board[1][1][1]==1 and board[2][0][2]==1:
        return 1
    if board[0][2][2]==1 and board[1][1][1]==1 and board[2][0][0]==1:
        return 1

    # Checks each row and column for a line of 3 in both ascending and
    # descending order.
    for i in range(3):
        if (board[i][0][0]==1 and board[i][1][1]==1 and
        board[i][2][2]==1):
            return 1
        if (board[i][0][2]==1 and board[i][1][1]==1 and
        board[i][2][0]==1):
            return 1
        if (board[0][i][0]==1 and board[1][i][1]==1 and
        board[2][i][2]==1):
            return 1
        if (board[0][i][2]==1 and board[1][i][1]==1 and
        board[2][i][0]==1):
            return 1

    # Checks if there are any rings left.
    global rings_s, rings_m, rings_l
    if rings_s==0 and rings_m==0 and rings_l==0:
        return 1

    # Returns 0 in case none of the other if's are true.
    return 0


def game():
    global count
    # Making the board.
    # I made the board as a list of 3 lists that contain 3 lists.
    # I added 3 values in each list, which signify if there is a ring of
    # a certain size in that position. 1st position is small sized ring,
    # 2nd is medium and 3rd is large. For example, if there is a large ring
    # in the 1st row and 2nd line, board[0][1][2] would be equal to 1.
    board=[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0], \
    [0,0,0],[0,0,0]]]
    # Making variables that count the amount of rings available.
    global rings_s, rings_m, rings_l
    rings_s=9
    rings_m=9
    rings_l=9
    over=0
    while(over==0):
        # The function place_ring returns 1 only if the game runs out of rings.
        # I didn't know if it was possible for it to run out of rings without
        # the game being over, so I added it as a possibility just in case.
        over=place_ring(board)
        over=check_over(board)
        count+=1

# Main
sum=0
for play in range(100):
    count=0
    game()
    sum+=count
avg=sum/100
print(avg)
