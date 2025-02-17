The program for calculating entropy and password cracking time.

Added calculation of password entropy in bits, which is an important indicator of password strength. Entropy is calculated using the formula:
Entropy (bits) = log₂(number of possible characters ^ password length)
Entropy indicates how difficult it is to crack a password using brute force. The higher the entropy, the stronger the password.

How to Use the Program
1. Save the code to a file, for example, password_cracker.py.

2. Make the file executable:
  chmod +x password_cracker.py
  
3. Run the program in the terminal:
  python3 password_cracker.py

4. Select a language:
  Mode 1: Русский / Russian
  Mode 2: English

5. Choose a mode:
   
  Mode 1: Estimate the time for a password of a given length and complexity.
  
  Mode 2: Estimate the time for an entered password.

Notes:

It is assumed that a millennium consists of 1000 years, a century consists of 100 years, a year consists of 365 days, and a month consists of approximately 30 days. This is a simplified assumption, as in reality, the number of days in months and years can vary.

The calculation time is estimated and depends on the assumption that the system can check 1 million combinations per second. For a more accurate estimate, the combinations_per_second value can be adjusted.

Entropy indicates how difficult it is to crack a password using a brute-force method. The higher the value, the stronger the password.

Entropy is calculated using the formula: log2(number of characters ^ password length).

The program supports two languages: Russian and English.

Depending on the selected language, all text messages will change.

Comments in the code are provided in both languages for ease of understanding.
