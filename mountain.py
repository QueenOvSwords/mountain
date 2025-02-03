#! /usr/bin/env python3

import random
import pyfiglet

ascii_description = pyfiglet.figlet_format("FLASHCARDS")
ascii_banner = pyfiglet.figlet_format("mountain.py", font='digital')

print(ascii_description)
print(ascii_banner)

def load_terms(filename):

    terms_dict = {}
    acronyms_dict = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(":", 2)
            if len(parts) == 2:
                term, definition = parts
                terms_dict[term.strip()] = definition.strip()
            elif len(parts) == 3:
                term, acronym, definition = parts
                term, acronym, definition = term.strip(), acronym.strip(), definition.strip()

                terms_dict[term] = (acronym, definition)
                acronyms_dict[acronym] = (term, definition)

    return terms_dict, acronyms_dict

def quiz(terms):
    shuffled_terms = list(terms.items())
    random.shuffle(shuffled_terms)

    correct = 0

    for term, definition in shuffled_terms:
        if isinstance(definition, tuple):
            acronym, full_definition = definition
        else:
            acronym, full_definition = None, definition

        print(f"\n* {full_definition}")
        user_input = input("Enter the term or acronym: ").strip()

        if user_input.lower() == term.lower():
            if acronym:
                print(f"Correct. Acroynm: {acronym}")
            else:
                print("Correct.")
            correct += 1
        elif acronym and user_input.lower() == acronym.lower():
            print(f"Correct. The full term is: {term}")
            correct += 1
        else:
            if acronym:
                print(f"Incorrect. Answer is {term} ({acronym})")
            else:
                print(f"Incorrect. Answer is {term}")

    print(f"\nScore: {correct}/{len(terms)}\n")
    main_menu()

def choose_file():
    options = []

    with open("sections.txt", "r", encoding="utf-8") as file:
        for line in file:
            options.append(line)
    
    section = input("Choose section to study:\n\n"  + "".join(options) + "\nEnter section number (x.x)\n")

    return section + ".txt"

def main_menu():
    file_name = choose_file()
    terms, acronyms = load_terms(file_name)
    quiz(terms)

main_menu()

