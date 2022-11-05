# Week 1: Thursday + Friday

### **Short overview**

------

Today is a new day to learn something new! And in the upcoming two days, we will learn how to program some expressions and use functions in a modular way!

### How to take these days

------

1. Complete all the Assignments
2. Fill out the Submission Form

### Resources

------

[test.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6be25847-a470-4110-a2e7-710a24525ed9/test.py)

### **Assignments**

------

**Assignment name:** Math Operations

**Testing**

From now on, we will provide you with a test file (as you can see under the resources section) that should help you asses yourself and your code.

Testing your code is an important skill of its own. (some will argue that it is one of the most important skills after collaborating with others maybe), there are many philosophies regarding how to go about testing, and there is no right or wrong, but all of those approaches agree on one thing, and that is, that it is immensely important.

The question is how to do it, not if to do it.

Our test files should help you understand if your code works as it should. If it’s not, that is where you should start debugging your code and find what isn't working properly There will be more comprehensive debugging & testing using the pytest lib. (Don’t worry, an explanation will come later on, down the road)

The way to debug your code properly and how pass all tests in the first place is by simply trying to think about all the edge cases and scenarios of inputs for your function.

So go ahead and add the test file under the same folder where your code is and run the test script after finishing the entire assignment (if you want to test just part of the functions, you can [comment](https://www.w3schools.com/python/python_comments.asp) out the code lines that are relevant to these functions)

**Ok, let's continue to the assignment itself**

create a new file named [expressions.py](http://expressions.py) in the Week 1 Folder

1. **Basic Calculator**

   - Declare a new function inside the file with the name:

     `def calc_math_expression(num1, num2, operator):`

     The function takes 3 inputs:

     1. int
     2. int
     3. operator (string)

     The operators are of the type, ‘+’ , ‘-’ , ‘*’ , ‘:’  (keep in mind mathematical order! it is important in dividing and in subtracting)

     If you get an illegal input for this function, return None.

   - Create another function:

     `def calc_math_expression_from_str(str_input):`

     it gets a single string, splits to parameters, and sends it to the previous function

2. **Largest and Smallest Numbers**

   - Create the following function

     `def``find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):`

     The function goal is to compare three parameters and returns the largest and the smallest.

     The function will return a tuple where the first parameter is the largest, and the second is the smallest

     **Tip**

     First, solve it so that it will work correctly!

     Then try to solve it again with the least amount of  “if” “else” and “elif” statements as possible, and compare with your peers to see who could do it in the most efficient way!)

**4. Quadratic equation Solver:**

The next function goal is to solve a quadratic equation for any given input!

(where this golden piece of technology was through my high school years?

- Quadratic equation solution will satisfy the following:

  ​	$ax^2 + bx + c = 0$

  The solution is the x values, and a,b,c are numeric values that are known and supplied to the equation.

  For example:

  ​	$2x^2 + (-9x) + (-12.5) = 0$

  ​	(a = 2 , b = -9 and c = -12.5)

  The solution for this equation will be all values that, if we replace the X instances with them, will make the left side of the equation equal to zero just as this equation claims, making it a true claim and satisficing the equation.

  **Keep in mind that -** sometimes there is only one solution or even no solution at all

  To find the solution, we will use the following formula:

  ​	$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$

- Declare a function with the name quadratic_equation that excepts input a ,b and c. just as in the following:

  `def quadratic_equation_solver(a, b, c):`

  if there are two solutions, return the tuple: (solution1, solution2)

  if there is only one solution, return the tuple (solution1, None)

  if there is no solution, return the tuple (None, None)

  - a=0 is not a valid input!)
  - Don’t forget to test your code by running many kinds of inputs!

- Define the following function:

  `def quadratic_equation_solver_from_user_input()`

  This function asks for a string input from the user.

  The input should look like the following:

  “a b c”

  For instance:

  “2 -9 -12.5”

  Then convert each number to a variable by splitting the string (read about the split function) and pass them to the `quadratic_equation`, and then print the answer and returns it.

  - again, check for illegal inputs that are not in the right format.

1. **Last function for today**

   `def temp_checker(``min_temp, temp_1, temp_2, temp_3)`

   This function returns True if and only if 2 or more days that are warmer than the threshold

   Don’t forget to test yourself!

Well done! you deserve a dessert!

Spoil yourself with something you love!

You did a great job!