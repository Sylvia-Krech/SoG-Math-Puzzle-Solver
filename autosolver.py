import pyautogui
from itertools import permutations
import operator
import config_importer
# Grab config
config = config_importer.grab_config("autosolver.config")
## hardcoded:
imageFolder = "images/" #consider putting this in config
intFileLocations = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "0.png"]
for file in intFileLocations:
    file = imageFolder + file
operatorFileLocations = ["+.png", "-.png", "x.png", "div.png"]
for file in operatorFileLocations:
    file = imageFolder + file

## Functions + Class to help mathematically solve the puzzle
class operand():
    def __init__(self, op):
        self.strOperand = op
        if self.strOperand == "+":
            self.op = operator.add
        elif self.strOperand == "-":
            self.op = operator.sub
        elif self.strOperand == "*":
            self.op = operator.mul
        elif self.strOperand == "/":
            self.op = operator.truediv
        if self.op is None:
            raise ("Invalid operand")
    def compute(self, a, b):
        return self.op(a,b)

    def __repr__(self):
        return self.strOperand

def solve_puzzle(numbers, operands, targetValue):
    for numberPermutation in permutations(numbers):
        for operandPermutation in permutations(operands):
            if permutation_evaluation(numberPermutation, operandPermutation) == targetValue:
                return (numberPermutation, operandPermutation)
    raise Exception("No solution was found")

def permutation_evaluation(numberPermutation, operandPermutation):
    if len(numberPermutation) - 1 != len(operandPermutation):
        raise Exception("Invaild quantity of numbers and operands")

    output = numberPermutation[0]
    for i in range(len(operandPermutation)):
        output = operandPermutation[i].compute(output, numberPermutation[i+1])
    return output

## Functions to move the character around the screen
def move():
    pass




## Functions to identify what the puzzle itself is
def identify(screen, images, location):
    croppedScreen = screen.crop(location)
    outputDict = {}
    for img in images:
        temp = pyautogui.locateAll(screen, img)
        if temp != None:
            outputDict[img[:-4]] = temp #[-4] to remove the .png or .jpg from the key

    outputList = []
    # append the numeral the quantity of times each it was found
    for numeral, quantity in outputDict.items():
        for i in range(quantity):
            outputList.append(numeral)
    return outputList

if __name__ == "__main__":
    ints = [5,1,7,2]
    ops = [operand("-"), operand("+"), operand("*")]
    tar = 38
    print(solve_puzzle(ints, ops, tar))
    ## main loop
    loopFlag = True
    while loopFlag:
        break
        ## grab screen
        screen = pyautogui.screenshot()

        ## identify numbers + operators
            # screenshot, then use locate on the screenshot, with pre-existing images of the
        numbers = identify(screen, intFileLocations, config["intLocations"])
        operators = identify(screen, operatorFileLocations, config["operatorLocations"])
        target = identify(screen, targetFileLocations, config["targetLocations"])

        ## solve
        solution = solve_puzzle(numbers, operators, target)
        ## move

        ## ensure is solved
            # if it is, continue to next room
            # otherwise reset
