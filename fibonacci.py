#!/usr/bin/env python3
"""
Simple script to compute Fibonacci numbers.
Demonstrates basic Python script for HPC submission.
"""

import sys
import time

def fibonacci(n):
    """Compute the nth Fibonacci number."""
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def fibonacci_sequence(n):
    """Compute the first n Fibonacci numbers."""
    sequence = []
    for i in range(n):
        sequence.append(fibonacci(i))
    return sequence

if __name__ == "__main__":
    # Check if argument provided
    if len(sys.argv) < 2:
        print("Usage: python fibonacci.py <n>")
        print("Computing first 20 Fibonacci numbers by default...")
        n = 20
    else:
        n = int(sys.argv[1])

    print(f"Computing first {n} Fibonacci numbers...")
    start_time = time.time()

    # Compute the sequence
    sequence = fibonacci_sequence(n)

    elapsed_time = time.time() - start_time

    # Print results
    print(f"\nFirst {n} Fibonacci numbers:")
    for i, fib in enumerate(sequence):
        print(f"F({i}) = {fib}")

    print(f"\nComputation completed in {elapsed_time:.4f} seconds")
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")