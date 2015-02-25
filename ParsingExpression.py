'''
EXPRESSION PARSING

Evaluated by a stack of numbers
    * Read expression left to right
        * Number : push it onto stack
        * Operator : pop top 2 numbers off stack; perform operation
                     (first number popped is second operand). Push result on stack

Converting Infix to Postfix
Precedence rules : Exponentiation has precedence over multiply, divide, which are
                   over add and substrate
Convert infix to postfix with operator stack
Read expression left to right
    * Number : Print it out
    * Operator : put it on stack until an operator with lower or equal precedence oppears
                 (for exponentiation, strictly lower), where we pop it & print it
    * String ends : Pop & print int and each items on stack
'''
__author__ = 'Ingoo'
import re
def in_to_post(exp) :
    result = str()
    value = { '^' : 2, '*' : 1, '/': 1, '+' : 0, '-':0}
    stack = []
    for x in exp :
        if x.isdigit() :
            result += x
        elif re.match('[\*\+/\-]',x) :
            result += ' '
            if len(stack) == 0 :
                pass
            elif value[x] <= value[stack[-1]] :
                for y in range(len(stack)) :
                    result += ' ' + stack.pop() + ' '
            stack.append(x)
        elif re.match('\^',x) :
            result += ' '
            print(stack)
            if len(stack) == 0 :
                pass
            elif value[x] < value[stack[-2]] :
                for y in range(len(stack)) :
                    result += ' ' + stack.pop() + ' '
            stack.append(x)
    stack.reverse()
    for x in stack :
        result += ' ' + x + ' '
    print("result : ", result)
    return result

def postfix(exp) :
    parsed = exp.split()
    number = []
    for x in parsed :
        if x.isdigit() :
            number.append(x)
            print(number)
        elif x == '^' :
            i = int(number.pop())
            j = int(number.pop())
            number.append(j**i)
        else :
            i = int(number.pop())
            j = int(number.pop())
            exec('result = j %s i' % x)
            exec('number.append(result)')
    return number[0]

asdf = '2^3*3+1'
print(postfix(in_to_post(asdf)))
