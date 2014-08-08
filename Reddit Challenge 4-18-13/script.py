__author__ = 'ddsnowboard'
# The world championship in Tic Tac Toe, The X-Games is underway.
# We have been asked to write a program to see if there is a winning move possible.
# This tool will be used by live commentators to use in their play by play.
# (Next player's Move either an X or an O)
# (3 x 3 grid showing the current game)
# The grid can have 3 characters
# X for spot held by the X player
# O for spot held by the O player
# - for an empty spot
# Example Input 1:
# X
# XX-
# -XO
# OO-
# Example Input 2:
# O
# O-X
# -OX
# ---
# Example Input 3:
# X
# --O
# OXX
# ---
# Output: Shows the board with the winning move in place. If there is no winning move print out "No winning move"
# Example Output 1:
# XXX
# -XO
# OO-
# Extra Challenge:
# Boards where several moves can "win" display all boards showing the winning moves
# with a message saying how many wins are possible
# Boards with no winning move -- suggest a "block" move the player should make instead
# with a message saying "No winning move: Block here"

num = 0
inputs = open("inputs.txt", "r")
side = str(inputs.readline())
if side.

outputs = open("outputs.txt","w")
arr = inputs.readlines()
temp = []
for i in range(0,len(arr)):
    temp = []
    for l in range(0,len(arr[i])):
        temp.append(arr[i][l])
    arr[i] = temp
for i, j in enumerate(arr):
    for k, l in enumerate(arr[i]):
        if l == '\n':
            arr[i].pop(k)
for i in arr:
    print(i)
for i, j in enumerate(arr):
    num = 0
    for l in j:
        if l == side:
            num += 1
        if num == 2 and j.count("-") == 1:
            arr[i] = ['X', 'X', 'X']
for i in arr:
    print(i)