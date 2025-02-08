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


    def __lt__(self, other): #finds the least cost
        return self.total_cost < other.total_cost


    def solved(self):
        return self.puzzle == eight_goal_state
   
    def board_to_tuple(self):
        return tuple(tuple(row) for row in self.puzzle)
   
    def generate_neighbors(self):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #move up, move down, move left, move right 

        zeroPosrow, zeroPoscol = None, None
        #gets the position of where the zero is in the board 
        for r in range(3):
            for c in range(3):
                if self.puzzle[r][c] == 0:
                    zeroPosrow, zeroPoscol = r, c
                    break
            if zeroPosrow is not None:
                break

        #checks if the zero can move in that way
        for rowOffset, columnOffset in directions:
            newRow= zeroPosrow + rowOffset
            newCol = zeroPoscol + columnOffset
            if 0 <= newRow < 3 and 0 <= newCol < 3: #checks in the newRow and newCol are in the boundaries 
                new_puzzle = copy.deepcopy(self.puzzle)
                new_puzzle[zeroPosrow][zeroPoscol], new_puzzle[newRow][newCol] = new_puzzle[newRow][newCol], new_puzzle[zeroPosrow][zeroPoscol] #Swaps tiles 
                
                moves.append(new_puzzle) #adds the newpuzzle to the moves

        return moves

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
        printPuzzle(trivial)
        return trivial
    if selectedDiff == "1":
        print("Very Easy selected")
        printPuzzle(veryEasy)
        return veryEasy
    if selectedDiff == "2":
        print("Easy selected")
        printPuzzle(easy)
        return easy
    if selectedDiff == "3":
        print("Doable selected")
        printPuzzle(doable)
        return doable
    if selectedDiff == "4":
        print("Oh Boy selected")
        printPuzzle(oh_boy)
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
    startNode = TreeNode(startPuzzle, 0, heuristic(startPuzzle))
    workingQueue = []
    repeatedStates = {}
    heapq.heappush(workingQueue, startNode)

    nodesExpanded = 0
    maxQueueSize = 1
    repeatedStates[startNode.board_to_tuple()] = startNode.cost


    while len(workingQueue) > 0:
        maxQueueSize = max(len(workingQueue), maxQueueSize)
        node_from_queue = heapq.heappop(workingQueue)

        #repeatedStates[node_from_queue.board_to_tuple()] = "This can be anything"
        #nodesExpanded += 1
       #print(f"Expanding node: {node_from_queue.puzzle}")


        print(f"The state to expand with g(n) = {node_from_queue.cost} and h(n) = {node_from_queue.heuristic} is...")
        printPuzzle(node_from_queue.puzzle)


        if node_from_queue.solved():
            print("Solved!")
            #while stackPrint:
                #printPuzzle(stackPrint.pop())
            print("Depth:", node_from_queue.cost)
            print("Number of nodes expanded:", nodesExpanded)
            print("Max queue size:", maxQueueSize)
            #print("Best State Path Below:")
            #printPath(node_from_queue)
            return node_from_queue          
   
        nodesExpanded += 1

        for neighbor in node_from_queue.generate_neighbors():
                child = TreeNode(neighbor, node_from_queue.cost + 1, heuristic(neighbor), node_from_queue)
                child_tuple = child.board_to_tuple()
                if child_tuple not in repeatedStates or repeatedStates[child_tuple] > child.cost:
                    heapq.heappush(workingQueue, child)
                    repeatedStates[child_tuple] = child.cost

    print("Failure: No solution found")
    return None  

    #print("Number of nodes expanded:", nodesExpanded)
    #print("Max queue size:", maxQueueSize)


def uniform_cost_search(puzzle):
    return 0; #based on project writeup UCS is "A* with h(n) hardcoded to 0" and it uses the general search algo hence returning 0

def misplaced_tile_heuristic(puzzle): #need to compare to goal state then check how many tiles misplaced
    misplacedTiles = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != 0 and puzzle[i][j] != eight_goal_state[i][j]:
                misplacedTiles += 1
                
    return misplacedTiles

def manhattan_distance_heuristic(puzzle):
    manDist = 0 

    for i in range(3):
        for j in range(3):
            tile = puzzle[i][j]
            if tile != 0:
                goalRow = (tile -1) //3 # converted the divmod to this because it wasn't working
                goalCol = (tile -1) % 3
                manDist += abs(i - goalRow) + abs(j - goalCol)
    return manDist

if __name__ == '__main__':
    main()