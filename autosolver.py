import pyautogui
import __autosolver
from itertools import permutations
import operator

##


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

    def compute(self, a, b):
        return self.op(a,b)
        #raise ("Invalid operand")

    def __repr__(self):
        return self.strOperand
        #raise ("Invalid operand")

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
        ## solve

        ## move

        ## ensure is solved
            # if it is, continue to next room
            # otherwise reset
