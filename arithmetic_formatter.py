def arithmetic_arranger(problems, show_answers=False):

    # Limit to 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_operands = []
    operators = []
    second_operands = []
    answers = []
        
    for problem in problems:
        
        # Split problems into parts
        first_operand = problem.split()[0]
        operator = problem.split()[1]
        second_operand = problem.split()[2]
        
        # Limit to just Addition (+) and Subtraction (-)
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
            
        # Limit operands to digits only
        elif first_operand.isnumeric() == False or second_operand.isnumeric() == False:
            return 'Error: Numbers must only contain digits.'
            
        # Limit operands to four digits only
        elif len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Append lists
        else:
            first_operands.append(first_operand)
            operators.append(operator)
            second_operands.append(second_operand)
            answer = str(eval(problem))
            answers.append(answer)

            first_line = ""
            second_line = ""
            third_line = ""
            answer_line = ""
            
            # Structure lines
            for i in range(len(first_operands)):
                width = (max(len(first_operands[i]), len(second_operands[i])) + 2)
                first_line += ((width - len(first_operands[i])) * " ") + first_operands[i]
                second_line += operators[i] + ((width - len(second_operands[i]) - 1) * " ") + second_operands[i]
                third_line += "-" * width
                answer_line += ((width - len(answers[i])) * " ") + answers[i]
                
                if i < len(first_operands) - 1:
                    first_line += "    "
                    second_line += "    "
                    third_line += "    "
                    answer_line += "    "
            
    if show_answers == True:
        return f"{first_line}\n{second_line}\n{third_line}\n{answer_line}"
    else:
        return f"{first_line}\n{second_line}\n{third_line}"

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
