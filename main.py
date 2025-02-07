import heapq
import copy
#import TreeNode


#Puzzles to be inputted from the project psuedocode
trivial = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
veryEasy = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
easy = [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
doable = [[0, 1, 2], [4, 5, 3], [7, 8, 6]]
oh_boy = [[8, 7, 1], [6, 0, 2], [5, 4, 3]]
eight_goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


class TreeNode:
    def __init__(self, puzzle, cost, heuristic, parent=None):
        self.puzzle = puzzle
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic  # f(n) = g(n) + h(n)
        self.parent = parent


    def lowestCost(self, other):
        return self.total_cost < other.total_cost
   
    def board_to_tuple(self):
        return tuple(tuple(row) for row in self.puzzle)


def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + "\n")

    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())
    if puzzle_mode == "2":
        print("Enter your puzzle, using zero to reprsent the blank." + "Please enter only valid 8-puzzles." + "\n")
        puzzle_r1 = input("Enter first row: ")
        puzzle_r2 = input("Enter second row: ")
        puzzle_r3 = input("Enter third row: ")

        puzzle_r1 = puzzle_r1.split()
        puzzle_r2 = puzzle_r2.split()
        puzzle_r3 = puzzle_r3.split()


        for i in range(3):
            puzzle_r1[i] = int (puzzle_r1[i])
            puzzle_r2[i] = int (puzzle_r2[i])
            puzzle_r3[i] = int (puzzle_r3[i])
       
        userPuzzle = [puzzle_r1, puzzle_r2, puzzle_r3]
        select_and_init_algorithm(userPuzzle)


    return
def init_default_puzzle_mode():
    selectedDiff = input("Choose the difficulty for the puzzle on scale of 0-4" + "\n")
    if selectedDiff == "0":
        print("Trivial selected")
        return trivial
    if selectedDiff == "1":
        print("Trivial selected")
        return veryEasy
    if selectedDiff == "2":
        print("Trivial selected")
        return easy
    if selectedDiff == "3":
        print("Trivial selected")
        return doable
    if selectedDiff == "4":
        print("Trivial selected")
        return oh_boy
    #if selectedDiff == "5":
       # print("Trivial selected")
        #return impossible
   
def printPuzzle(puzzle):
    for i in range(0,3):print(puzzle[i])
    print("\n")


def printPath(node):
    path = []
    while node:
        path.append(node.puzzle)
        node = node.parent
    for puzzle in reversed(path):
        printPuzzle(puzzle)
## More code needs to go here


def select_and_init_algorithm(puzzle):
    algorithm = input ("Select Algorithm. (1) Uniform Cost Search (2)Misplaced Tile Heuristic (3)Manhattan Distance Heuristic " + "\n")

    if algorithm == "1":
        general_search_algorithm(puzzle, uniform_cost_search)
    if algorithm == "2":
        general_search_algorithm(puzzle, misplaced_tile_heuristic)
    if algorithm == "3":
        general_search_algorithm(puzzle, manhattan_distance_heuristic)
       
#implemented general search algorithm, then changed the heuristics for ucs, mth, and mdh. I implemented it this way becuase it was easier for me to understand
def general_search_algorithm(startPuzzle, heuristic):
    startNode = TreeNode(startPuzzle, 0, heuristic)
    working_queue= []
    repeated_states = dict()
    heapq.heappush(working_queue, startNode)
    nodesExpanded = 0
    maxQueueSize = 0
    repeated_states[tuple(map(tuple, startPuzzle))] = "This is the parent board"
    stack = []


    while len(working_queue) > 0:
        maxQueueSize = max(maxQueueSize, len(working_queue))
        currNode = heapq.heappop(working_queue)
        currPuzzle = currNode.puzzle
        currCost = currNode.cost
        puzzTuple = tuple(map(tuple, currPuzzle))
        repeated_states[currNode.board_to_tuple()] = "This can be anything"


        if currPuzzle.puzzle == eight_goal_state:
            while len(stack) > 0:
                printPuzzle(stack.pop())
            print("Number of nodes expanded:, nodesExpanded")
            print("Max queue size:, maxQueueSize")
            return currNode
       
        stack.append(currNode.puzzle)
        nodesExpanded += 1


        for neighbor in generate_neighbors(currNode.puzzle):
            child = TreeNode(currNode, neighbor, currNode.cost + 1, heuristic)
            childTuple = child.board_to_tuple()
            if childTuple not in repeated_states or repeated_states[childTuple] > child.total_cost:
                repeated_states[childTuple] = child.total_cost
                heapq.heappush(working_queue, child)


def uniform_cost_search(puzzle):
    return 0; #based on project writeup UCS is "A* with h(n) hardcoded to 0" and it uses the general search algo hence returning 0

def misplaced_tile_heuristic(puzzle):
    misplacedTiles = 0


    for i in range(3):
        for j in range(3):
            tile = puzzle[i][j]


        if tile != 0 and tile != eight_goal_state[i][j]:
            misplacedTiles += 1


    return misplacedTiles


def manhattan_distance_heuristic(puzzle):
    manDist = 0
    for i in range(3):
        for j in range(3):
            tile = puzzle[i][j]
            if tile != 0:
                goalRow = (tile -1) //3
                goalCol = (tile -1) % 3


                manDist += abs(i - goalRow) + abs(j - goalCol)
    return manDist


def generate_neighbors(puzzle):
    moves = []
    row, col = [(r, c) for r in range(3) for c in range(3) if puzzle[r][c] == 0][0]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_puzzle = copy.deepcopy(puzzle)
            new_puzzle[row][col], new_puzzle[new_row][new_col] = new_puzzle[new_row][new_col], new_puzzle[row][col]
            moves.append(new_puzzle)

    return moves

if __name__ == '__main__':
    main()