# Arithmetic Formatter

## Project Overview

This project provides a solution to format arithmetic problems vertically and side-by-side, as typically done by students in primary school. It also includes error handling to ensure valid input and can optionally display the answers.

## Features

- **Vertical and Side-by-Side Formatting**: Takes a list of arithmetic problems and arranges them vertically and side-by-side.
- **Error Handling**: Handles various error scenarios such as:
  - Too many problems (more than five).
  - Invalid operators (only supports `+` and `-`).
  - Non-numeric operands.
  - Operands with more than four digits.
- **Answer Display**: Optionally, you can choose to display the answers below the arithmetic problems.

## Requirements

- Python 3.x

## Usage

### Function: `arithmetic_arranger(problems, show_answers=False)`

This function takes a list of arithmetic problems and arranges them according to the specified rules. You can choose to display the answers as well.

### Parameters:
- `problems`: A list of strings, where each string represents an arithmetic problem in the format: `<operand1> <operator> <operand2>`.
- `show_answers` (optional): A boolean value. If `True`, the answers will be displayed beneath each problem. Default is `False`.

### Returns:
- A string containing the formatted arithmetic problems, optionally with answers.

### Example:

#### Without answers:
```python
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
```

### Example Output:

#### Without answers:
```diff
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

#### With answers:
```python
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
```

**Output:**
```yaml
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

## Error Handling

The function checks for and returns the following errors:

- **Too many problems**: If there are more than five problems, the function returns:  
  `"Error: Too many problems."`

- **Invalid operator**: If an operator other than `+` or `-` is used, the function returns:  
  `"Error: Operator must be '+' or '-'."`

- **Non-numeric operands**: If any operand is not a number, the function returns:  
  `"Error: Numbers must only contain digits."`

- **Operand length**: If an operand is longer than four digits, the function returns:  
  `"Error: Numbers cannot be more than four digits."`

## How It Works

1. **Input Parsing**: The function splits each problem into operands and operators.
2. **Error Checking**: The function validates each problem based on the rules for valid operands and operators.
3. **Formatting**: The problems are formatted vertically, with each operand right-aligned.
4. **Answer Display**: If `show_answers=True`, the answers are calculated and displayed beneath each problem.

## Example Code:
```python
def arithmetic_arranger(problems, show_answers=False):
    # Limit to 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_operands = []
    operators = []
    second_operands = []
    answers = []
    
    for problem in problems:
        first_operand = problem.split()[0]
        operator = problem.split()[1]
        second_operand = problem.split()[2]
        
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        elif not first_operand.isnumeric() or not second_operand.isnumeric():
            return 'Error: Numbers must only contain digits.'
        elif len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Append lists
        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)
        answers.append(str(eval(problem)))

    first_line = ""
    second_line = ""
    third_line = ""
    answer_line = ""
    
    for i in range(len(first_operands)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line += ((width - len(first_operands[i])) * " ") + first_operands[i]
        second_line += operators[i] + ((width - len(second_operands[i]) - 1) * " ") + second_operands[i]
        third_line += "-" * width
        answer_line += ((width - len(answers[i])) * " ") + answers[i]
        
        if i < len(first_operands) - 1:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            answer_line += "    "
    
    if show_answers:
        return f"{first_line}\n{second_line}\n{third_line}\n{answer_line}"
    else:
        return f"{first_line}\n{second_line}\n{third_line}"
```

## License

This project is licensed under the MIT License.
