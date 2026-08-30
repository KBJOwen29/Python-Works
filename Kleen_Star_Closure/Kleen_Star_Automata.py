# Function to create a Kleene Star Automaton from an input automaton A
def kleene_star_automata(A):
    # Copy states and add a new start/accept state 'S*'
    states = set(A['states']) | {'S*'}
    alphabet = set(A['alphabet'])
    start_state = 'S*'
    
    # Add 'S*' as an accept state in addition to A's accept states
    accept_states = set(A['accept_states']) | {'S*'}
    
    # Copy existing transitions
    transitions = dict(A['transitions'])
    
    # Add epsilon-transitions:
    # From 'S*' to A's start state (on any symbol), 
    # this allows restarting the automaton on new input.
    for symbol in alphabet:
        transitions[('S*', symbol)] = A['transitions'].get((A['start_state'], symbol), A['start_state'])
    
    # For each accept state, loop back transitions to A's start state
    for acc in A['accept_states']:
        for symbol in alphabet:
            transitions[(acc, symbol)] = A['transitions'].get((A['start_state'], symbol), A['start_state'])
    
    # Return the new automaton definition
    return {
        'states': states,
        'alphabet': alphabet,
        'start_state': start_state,
        'accept_states': accept_states,
        'transitions': transitions
    }

# Function to print automaton in a readable format
def print_automaton(automaton):
    print("States:", automaton['states'])
    print("Alphabet:", automaton['alphabet'])
    print("Start state:", automaton['start_state'])
    print("Accept states:", automaton['accept_states'])
    print("Transitions:")
    
    # Print each transition rule
    for (state, symbol), next_state in automaton['transitions'].items():
        print(f"  δ({state}, '{symbol}') -> {next_state}")

# ============================
# User Input Section
# ============================

# Simple Functionalities dor rumning the system
print("Enter states (comma separated):")
states = set(input().strip().split(','))   # Input states
print("Enter alphabet (comma separated):")
alphabet = set(input().strip().split(',')) # Input alphabet
print("Enter start state:")
start_state = input().strip()              # Input start state
print("Enter accept states (comma separated):")
accept_states = set(input().strip().split(','))  # Input accept states

print("Enter state transitions (format: from_state,symbol,to_state). One per line. Enter empty line to finish:")
transitions = {}

# Keep reading transitions until user enters empty line
while True:
    line = input().strip()
    if not line:
        break
    parts = line.split(',')
    if len(parts) == 3:
        from_state, symbol, to_state = parts
        transitions[(from_state.strip(), symbol.strip())] = to_state.strip()

# Construct input automaton
A = {
    'states': states,
    'alphabet': alphabet,
    'start_state': start_state,
    'accept_states': accept_states,
    'transitions': transitions
}

# Apply Kleene Star transformation
result = kleene_star_automata(A)

# Print the transformed automaton
print("\nKleene Star Automaton:")
print_automaton(result)
