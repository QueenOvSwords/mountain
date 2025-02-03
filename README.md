# **Python Flashcard Quiz**

This is a simple Python script that helps users study concepts to prepare for tests or certifications using a flashcard-style quiz.

## **How It Works**

1. The script reads a `sections.txt` file, which contains section titles in the format:

```
1.1: Secure Network Design
1.2: Wireless Security
```

2. The user selects a section (e.g., `1.1`) and the script loads the corresponding terms file, e.g., **`1.1.txt`**, which contains definitions in format **`term:optional acronym:definition`**.

```
Firewall:A security device that filters network traffic 
Intrusion Detection System:IDS:A system that monitors network activity
```

3. The quiz begins by showing **definitions**, and the user must type the correct **term** or **acronym**.

4. The script keeps track of correct answers and displays the final score.
