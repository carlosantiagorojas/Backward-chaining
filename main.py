from rule import Rule

def main():
    rules_base = [
        Rule(conclusions=["S"], premises=["Z", "L"]),
        Rule(conclusions=["E"], premises=["A", "N"]),
        Rule(conclusions=["Z"], premises=["D" or "M"]),
        Rule(conclusions=["M"], premises=["A"]),
        Rule(conclusions=["N"], premises=["Q", "-W", "-Z"]),
        Rule(conclusions=["E"], premises=["L", "M"]),
        Rule(conclusions=["Q"], premises=["B", "C"]),
    ]

    goal = "E"
    known_facts = ["A","L"]
    
    # Check if the goal can be proven with the known facts
    if backward_chaining(goal, known_facts, rules_base):
        print(f"The goal {goal} can be proven with the known facts {known_facts}")
    else:
        print(f"The goal {goal} cannot be proven with the known facts {known_facts}")

    
def backward_chaining(goal, known_facts, rules_base):
    
    # Declare the a list to keep track of the backward chaining path 
    backward_chaining_path= []
    backward_chaining_backtracking(goal, rules_base, backward_chaining_path)
    
    print(f"Backward chaining path : {backward_chaining_path}")
    
    # Check if the backward chaining path contains all the known facts
    if all(fact in backward_chaining_path for fact in known_facts):
        return True
    else:
        return False
    

def backward_chaining_backtracking(goal: str, rules_base: list[Rule], backward_chaining_path: list[str]):

    # Select the current fact
    fact = goal
    print(f"Fact: {fact}")
    
    # Add the proven fact to the path of the backward chaining
    backward_chaining_path.append(fact)
    
    # For every rule in the knowledge base
    for rule in rules_base:
        # If the fact is in a conclusion of a rule
        if fact in rule.conclusions:
        # For every premise of that rule 
            for premise in rule.premises:
            # Call the function again with the premise as the new fact to do the backward chaining with backtracking
                backward_chaining_backtracking(premise, rules_base, backward_chaining_path) 

if __name__ == "__main__":
    main()
