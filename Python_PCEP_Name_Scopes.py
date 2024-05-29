# Example of Name Scope
def show_truth():
    mysterious_var = 'New Surprise!'
    print(mysterious_var)
show_truth()
# Output:
# New Surprise!

def show_truth():
    print(mysterious_var)
mysterious_var = 'Surprise!'
show_truth()
# Output:
# Surprise!
def show_truth():
    mysterious_var = 'Surprise!'
    print(mysterious_var)
show_truth()
# Output:
# Surprise!
