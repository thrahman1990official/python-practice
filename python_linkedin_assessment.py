# https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes/blob/main/python/python-quiz.md
  
# Q1. What is an abstract class?
# ANSWER: An abstract class exists only so that other "concrete" classes can inherit from the abstract class.

# Q2. What happens when you use the build-in function any() on a list?
# ANSWER: The any() function returns True if any item in the list evaluates to True. Otherwise, it returns False.

# Q3. What data structure does a binary tree degenerate to if it isn't balanced properly?
# ANSWER: linked list

# Q4. What statement about static methods is true?
# ANSWER: Static methods serve mostly as utility methods or helper methods, since they can't access or modify a class's state

# Q5. What are attributes?
# ANSWER: Attributes are a way to hold data or describe a state for a class or an instance of a class.
# EXPLANATION: Attributes defined under the class, arguments goes under the functions. arguments usually refer as parameter, whereas attributes are the constructor of the class or an instance of a class.

# Q6. What is the term to describe this code?
count, fruit, price = (2, 'apple', 3.5)
# ANSWER: tuple unpacking

# Q7. What built-in list method would you use to remove items from a list?
# ANSWER: .pop() method
# EXAMPLE:
my_list = [1,2,3]
my_list.pop(0)
my_list
>>>[2,3]

# Q8. What is one of the most common use of Python's sys library?
# ANSWER: to capture command-line arguments given at a file's runtime

# Q9. What is the runtime of accessing a value in a dictionary by using its key?
# ANSWER: O(1), also called constant time.

# Q10. What is the correct syntax for defining a class called Game, if it inherits from a parent class called LogicGame?
# ANSWER:
class Game(LogicGame): pass
# EXPLANATION: The parent class which is inherited is passed as an argument to the child class. Therefore, here the first option is the right answer.

# Q11. What is the correct way to write a doctest?
def sum(a, b):
    """
    >>> sum(4, 3)
    7

    >>> sum(-4, 5)
    1
    """
    return a + b
 
# Q12. What built-in Python data type is commonly used to represent a stack?
# list

# Q13. What would this expression return?
college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
return list(enumerate(college_years, 2019))
#Output: [(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]

# Q14. What is the purpose of the "self" keyword when defining or calling instance methods?
# ANSWER: self refers to the instance whose method was called.
