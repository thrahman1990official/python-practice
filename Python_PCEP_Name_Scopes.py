# Example of Name Scope
def show_truth():
    print(mysterious_var)
mysterious_var = 'Surprise!'
show_truth()

def show_truth():
    mysterious_var = 'Surprise!'
    print(mysterious_var)
show_truth()
# Output:
# Surprise!
