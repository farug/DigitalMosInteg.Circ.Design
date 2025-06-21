#!/usr/bin/env python3
"""
Truth Table Generator for Boolean Expression: ~(A.~(~(B.C).D)+C)

This script generates a complete truth table showing the step-by-step evaluation
of the Boolean expression ~(A.~(~(B.C).D)+C) for all possible input combinations.
"""

def evaluate_expression(A, B, C, D):
    """
    Evaluate the Boolean expression ~(A.~(~(B.C).D)+C) step by step.
    
    Args:
        A, B, C, D: Boolean inputs (True/False)
    
    Returns:
        dict: Dictionary containing all intermediate steps and final result
    """
    # Step 1: B.C (B AND C)
    step1 = B and C
    
    # Step 2: ~(B.C) (NOT of B.C)
    step2 = not step1
    
    # Step 3: ~(B.C).D (NOT(B.C) AND D)
    step3 = step2 and D
    
    # Step 4: ~(~(B.C).D) (NOT of step 3)
    step4 = not step3
    
    # Step 5: A.~(~(B.C).D) (A AND step 4)
    step5 = A and step4
    
    # Step 6: A.~(~(B.C).D)+C (step 5 OR C)
    step6 = step5 or C
    
    # Step 7: ~(A.~(~(B.C).D)+C) (NOT of step 6) - Final result
    final_result = not step6
    
    return {
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        'B.C': step1,
        '~(B.C)': step2,
        '~(B.C).D': step3,
        '~(~(B.C).D)': step4,
        'A.~(~(B.C).D)': step5,
        'A.~(~(B.C).D)+C': step6,
        '~(A.~(~(B.C).D)+C)': final_result
    }

def print_truth_table():
    """Print the complete truth table with all intermediate steps."""
    
    # Header
    print("=" * 120)
    print("TRUTH TABLE FOR: ~(A.~(~(B.C).D)+C)")
    print("=" * 120)
    print("A | B | C | D | B.C | ~(B.C) | ~(B.C).D | ~(~(B.C).D) | A.~(~(B.C).D) | A.~(~(B.C).D)+C | ~(A.~(~(B.C).D)+C)")
    print("-" * 120)
    
    # Generate all possible combinations
    results = []
    for A in [False, True]:
        for B in [False, True]:
            for C in [False, True]:
                for D in [False, True]:
                    result = evaluate_expression(A, B, C, D)
                    results.append(result)
    
    # Print each row
    for result in results:
        print(f"{int(result['A'])} | {int(result['B'])} | {int(result['C'])} | {int(result['D'])} | "
              f"{int(result['B.C'])} | {int(result['~(B.C)'])} | {int(result['~(B.C).D'])} | "
              f"{int(result['~(~(B.C).D)'])} | {int(result['A.~(~(B.C).D)'])} | "
              f"{int(result['A.~(~(B.C).D)+C'])} | {int(result['~(A.~(~(B.C).D)+C)'])}")
    
    print("-" * 120)
    print("Legend: 0 = False, 1 = True")
    print("=" * 120)
    
    return results

def analyze_results(results):
    """Analyze the truth table results and provide insights."""
    
    print("\n" + "=" * 60)
    print("ANALYSIS")
    print("=" * 60)
    
    # Count when final result is True
    true_count = sum(1 for r in results if r['~(A.~(~(B.C).D)+C)'])
    false_count = len(results) - true_count
    
    print(f"Final result is TRUE in {true_count} out of {len(results)} cases")
    print(f"Final result is FALSE in {false_count} out of {len(results)} cases")
    
    print("\nCases where the expression evaluates to TRUE:")
    print("-" * 40)
    true_cases = [r for r in results if r['~(A.~(~(B.C).D)+C)']]
    for i, case in enumerate(true_cases, 1):
        print(f"{i}. A={int(case['A'])}, B={int(case['B'])}, C={int(case['C'])}, D={int(case['D'])}")
    
    print("\nCases where the expression evaluates to FALSE:")
    print("-" * 40)
    false_cases = [r for r in results if not r['~(A.~(~(B.C).D)+C)']]
    for i, case in enumerate(false_cases, 1):
        print(f"{i}. A={int(case['A'])}, B={int(case['B'])}, C={int(case['C'])}, D={int(case['D'])}")

def save_to_csv(results):
    """Save the truth table to a CSV file."""
    import csv
    
    filename = "truth_table_results.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['A', 'B', 'C', 'D', 'B.C', '~(B.C)', '~(B.C).D', '~(~(B.C).D)', 
                     'A.~(~(B.C).D)', 'A.~(~(B.C).D)+C', '~(A.~(~(B.C).D)+C)']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            # Convert boolean to int for CSV
            row = {key: int(value) for key, value in result.items()}
            writer.writerow(row)
    
    print(f"\nTruth table saved to {filename}")

if __name__ == "__main__":
    # Generate and display the truth table
    results = print_truth_table()
    
    # Analyze the results
    analyze_results(results)
    
    # Save to CSV
    save_to_csv(results) 