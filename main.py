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



def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own.")

    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())
    if puzzle_mode == "2":
        print("Enter your puzzle, using zero to reprsent the blank." + "Please enter only valid 8-puzzles." + "\n")
        puzzle_r1 = input("Enter first row: ")
        puzzle_r2 = input("Enter second row: ")
        puzzle_r3 = input("Enter third row: ")

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


## More code needs to go here 

def select_and_init_algorithm(puzzle):
    algorithm = input ("Select Algorithm. (1) Uniform Cost Search (2)Misplaced Tile Heuristic (3)Manhattan Distance Heuristic " + "\n")

    if algorithm == "1":
        general_search_algorithm(puzzle, uniform_cost_search)
    if algorithm == "2":
        general_search_algorithm(puzzle, misplaced_tile_heuristic)
    if algorithm == "3":
        general_search_algorithm(puzzle, manhattan_distance_heuristic)
        
#implemented general search algorithm, then changed the heuristics for ucs, mth, and mdh.
def general_search_algorithm(startPuzzle, heuristic):
    return 


def uniform_cost_search(puzzle):
    return 0; #based on project writeup UCS is "A* with h(n) hardcoded to 0" hence returning 0

def misplaced_tile_heuristic(puzzle):
    return 

def manhattan_distance_heuristic(puzzle):
    return 

