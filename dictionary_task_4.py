# Dictionary of states and their capitals
state_capitals = {
    "California": "Sacramento",
    "Texas": "Austin",
    "Florida": "Tallahassee",
    "New York": "Albany",
    "Illinois": "Springfield"
}

state = input("Enter the name of the state: ")

capital = state_capitals.get(state)

if capital:
    print(f"The capital of {state} is {capital}.")
else:
    print(f"Sorry, {state} is not in the list.")