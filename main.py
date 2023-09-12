from rule import Rule


def main():
    rules_base = read_archive() # Call the function to read the rules

    if rules_base != None:
        # Define known facts and goal separately
        known_facts = ["A", "L"]
        goal = "E"
    
        print(f"\nKnown Facts: {known_facts}")
        print(f"Goal: {goal}")
    
        # Check if the goal can be proven with the known facts
        if backward_chaining(goal, known_facts, rules_base):
            print(
                f"The goal {goal} can be proven with the known facts {known_facts}")
        else:
            print(
                f"The goal {goal} cannot be proven with the known facts {known_facts}")
    else:
        print("Invalid rules base")


def read_archive() -> list[Rule]:
    # Read rules from a text file
    file_path = "./rules.txt"

    # Initialize variables
    rules_base = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            
            # Remove leading and trailing whitespace from line
            line = line.strip()
            
            if not line:
                continue  # Skip empty lines
            
            parts = line.split("=>") # Split line by "=>"
            if len(parts) != 2:
                print(f"Invalid format in line: {line}")
                return None
            
            # Extract the premises and conclusion from the line
            premises, conclusion = map(str.strip, parts)

            # Extract the rule name from the first part of premises
            rule_name = premises.split()[0]
    
            # Remove the rule name from premises
            premises = premises[len(rule_name):].strip()

            # Split premises by "&" or "|"
            if "&" in premises:
                premises = premises.split("&")
            elif "|" in premises:
                premises = premises.split("|")
            
            # Remove leading and trailing whitespace from premises
            premises = [p.strip() for p in premises]
            # print(f"Premises: {premises}")
            
            # Create a new rule    
            rule = Rule(name=rule_name, conclusions=[conclusion.strip()], premises=premises)
            rules_base.append(rule)
    
    print("\nRules base...")
    for rule in rules_base:
        print(f"Rule {rule.name} -", end=" ")
        print(f"Premises: {rule.premises} -",end=" ")
        print(f"Conclusion: {rule.conclusions}")

    return rules_base


def backward_chaining(goal, known_facts, rules_base):

    # Declare the a list to keep track of the backward chaining path
    backward_chaining_path = []
    
    print("\nBackward chaining with backtracking...")
    backward_chaining_backtracking(goal, rules_base, backward_chaining_path)

    print(f"\nBackward chaining path : {backward_chaining_path}")

    # Check if the backward chaining path contains all the known facts
    if all(fact in backward_chaining_path for fact in known_facts):
        return True
    else:
        return False


def backward_chaining_backtracking(goal: str, rules_base: list[Rule], backward_chaining_path: list[str], depth:int = 0):

    # Select the current fact
    indent = "  " * depth
    fact = goal
    print(f"{indent}Fact: {fact}")

    # Add the proven fact to the path of the backward chaining
    backward_chaining_path.append(fact)

    # For every rule in the knowledge base
    for rule in rules_base:
        # If the fact is in a conclusion of a rule
        if fact in rule.conclusions:
            # For every premise of that rule
            for premise in rule.premises:
                # Call the function again with the premise as the new fact to do the backward chaining with backtracking
                backward_chaining_backtracking(
                    premise, rules_base, backward_chaining_path, depth + 1)


if __name__ == "__main__":
    main()
