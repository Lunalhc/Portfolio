"""""
This calculator can only deal with the function with one variable x
It only works for trig function and function with e, not for other special math symbles
It can not deal with chain rule but not product rule or quotient rule
It only works for one single term, means no such thing like x+2x

"""""

import math

def main():

    # get original input
    input_original = input("Please enter the funtion and use x as your variable:")

    trig_function = ["sin","cos","tan","cot","sec","csc"]
    
    #check if it's just a number
    if "x" not in input_original:
        result = 0
    # if it's not just a number
    else:
        # check if there is trig in input
        result = ""
        for element in trig_function:

            if element in input_original:
                
                trig_part = input_original

                result = de_trig(trig_part) 
            
        if result == "":
            if "e" in input_original:
                result = de_e(input_original)
                
            else:
                result = de_basic(input_original)
        
        
    print(f'The derivative of it is {result}')
        
        

        

def de_basic(term):

    #get x term
    index_of_x =term.find("x")
    x_term = term[index_of_x:]

    #get x_exponent
    if len(x_term)==1:
        exponent_x = 1
    else:
        exponent_x = int(x_term[2:])

    #get coefficient of x
    coefficient = int(term[:index_of_x])

    # result for the basic part
    new_coefficient= coefficient * exponent_x
    new_exponent = exponent_x -1

    if new_exponent == 1:
        result_basic= str(new_coefficient)+"x"
    elif new_exponent == 0:
        result_basic = str(new_coefficient)
    else:
        result_basic = str(new_coefficient) + "x^" + str(new_exponent)

    return result_basic


def de_trig(term):

    trig_function = ["sin","cos","tan","cot","sec","csc"]
    trig_formula = ["(1)*cos","(-1)*sin","(1)*sec^2","(-1)*csc^2","(1)*secx*tan","(-1)*cscx*cot"]

    for trig in trig_function:

        #find index of trig from input 
        trig_index_input = term.find(trig)
        
        #find index of x from input
        x_index_input = term.find("x")

        if trig_index_input >= 0:
            
            #get trig function from input
            trig_term_no_x = term[trig_index_input:trig_index_input+3]

            #get trig_term from input
            trig_term = term[trig_index_input:x_index_input+1]

            #get trig term index in function list
            index_trig_function = trig_function.index(trig_term_no_x)
            
            #get trig formula in formula list
            formula = trig_formula[index_trig_function]
            
            # get coefficient from input
            if trig_index_input > 0:
                coefficient = term[:trig_index_input]
            else:
                coefficient = 1
            
            #get constant brfore x in input
            constant_x = term[trig_index_input+3:x_index_input]
            
            if index_trig_function <= 3:
                formula_with_x = formula + "(" + constant_x +"x" + ")"
            else:
                index_for_insert = formula.find("x") 
                formula_with_x = formula[:index_for_insert] +constant_x + formula[index_for_insert:] + constant_x + "x"
            if len(term) == 4:

                result_trig = formula_with_x

            # when there is coefficient but no constatnt before x
            elif trig_term[0] != term[0] and len(trig_term) == 4:

                result_trig = str(coefficient) + formula_with_x

            # when no coefficient but there's constant before x
            else:

                new_coefficient = int(coefficient) * int(constant_x)
                result_trig = str(new_coefficient) + formula_with_x
        
    return result_trig




def de_e(term):
    
    #find index of e from input
    index_e = term.find("e")
   
    # find e term from input
    e_term = term[index_e:]

    #find constant from input
    if term[:index_e] == "":
      constant =1
    else:
      constant = term[:index_e]

    # find exponent of e from input
    exponent = term[index_e+2:]

    #find constant of exponent
    constant_exponent = exponent[:-1]
    if constant_exponent == "":
      constant_exponent = 1

    result =str(int(constant) * int(constant_exponent)) + e_term

    return result




if  __name__=="__main__":
    main()
