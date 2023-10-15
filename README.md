# Backward Chaining with Backtracking Project
This project implements a backward chaining with backtracking algorithm for automated reasoning based on a set of rules. The system takes a goal and a set of known facts as input and tries to prove whether the goal can be derived from the known facts using the provided rules.

## Usage

1. Set up the data
   
Modify `rules.txt`: This text file contains a set of rules in a specific format. Each rule is represented as follows:

```mathematica
R1 A & N => E
```

- R1 is the rule name.
- A & N are the premises connected by & (logical AND).
- E is the conclusion that can be derived if the premises are satisfied.

2. Execute

Run the following command to execute the project:

```bash
python main.py
```

The program will prompt you to enter a goal and known facts. Alternatively, you can uncomment and use the predefined known facts and goal in the code.

The program will perform backward chaining with backtracking to determine if the goal can be proven with the known facts and display the result.
