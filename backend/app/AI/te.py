import time
from dataclasses import dataclass
from typing import List, Set, Dict
from keyword_scanner import scan_keywords

# Import your main scanning function here
# from your_main_file import scan_keywords_aho

# Sample realistic email text to test actual output
sample_email = """
Dear User,
We detected suspicious login attempts on your account. 
Please review this urgent security alert immediately and update your password 
to avoid account suspension. Click the link below to verify your identity.
"""

print("--- 1. RUNNING SCAN ON SAMPLE EMAIL ---")
start_time = time.perf_counter()

# Execute the actual scanner
result = scan_keywords(sample_email)

end_time = time.perf_counter()
execution_time_ms = (end_time - start_time) * 1000

print("\n--- 2. ACTUAL OUTPUT PRODUCED ---")
print(f"Detected Categories : {result.detected_categories}")
print(f"Matched Keywords    : {result.matched_keywords}")
print(f"Calculated Score    : {result.score}")

print("\n--- 3. EFFICIENCY & PERFORMANCE METRICS ---")
print(f"Time Taken          : {execution_time_ms:.4f} milliseconds")
print("Memory Footprint    : O(N + M + Z) where N is text length, M is total keywords, Z is matches.")
print("Algorithm Scale     : Single-pass linear scan (O(N)). Does not re-scan text per keyword.")