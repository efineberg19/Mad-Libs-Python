#!/usr/bin/python
#MadLibs.py

''' Gets words from user and uses them to tell a Madlibs story. '''

__author__ = "Beth Fineberg"
__version__ = "1.0"

import time

name = input("What is your name? ")
time.sleep(1)

def welcome():
    print("Hello " + name + "! Welcome to Madlibs.")
    time.sleep(1)

def main():
    #allows user to pick mode
    print(name + ", please pick a story by typing in the",
          "corresponding number.")
    time.sleep(1)
    print("1. School Cafeteria \n2. Presidential facts \n3. The Arrest")
    mode = int(input("\n"))
    time.sleep(1)

    #makes user think game is loading
    print("Madlibs Loading...")
    time.sleep(1)
    print("...")
    time.sleep(1)

    ##################################################
    # Get all words from user and plays cafeteria mode
    ##################################################
    if mode == 1:
        print("Welcome to: School Cafeteria!")
        time.sleep(1)

        adj1    = input("Please enter an adjective: ")
        verb1   = input("Please enter a verb: ")
        adj2    = input("Please enter an adjective: ")
        noun1   = input("Please enter a noun: ")
        adj3    = input("Please enter an adjective: ")
        noun2   = input("Please enter a noun: ")
        adj4    = input("Please enter an adjective: ")
        noun3   = input("Please enter a noun: ")
        adj5    = input("Please enter an adjective: ")
        verb2   = input("Please enter a verb: ")
        noun4   = input("Please enter a noun: ")

        time.sleep(1)
        print("...")
        time.sleep(1)
        
        print("Our school cafteria has really", adj1, "food. Just thinking about it",
              "makes my stomach " + verb1 + ". The spaghetti is", adj2, "and",
              "tastles like" + noun1 + ". One day, I swear one of my meatballs",
              "started to " + verb2 + "! The turkey tacos are totally ", adj3,
              "and look kind of like old " + noun2 + ". My friend", name, "actually",
              "likes the meatloaf, even though it's", adj4, "and", adj5, ". I",
              "call it \"mystery meatloaf\" and think it's really made out of "
              + noun3 + ". My dad said he'd make my lunches, but the first day,",
              "he made me a sandwich out of", noun4, "and peanut butter! I think",
              "I'd rather take my changes with the cafeteria!")

    #####################################################
    # Get all words from user and plays presidential mode
    #####################################################
    elif mode == 2:
        print("Welcome to: Presidential Facts!")
        time.sleep(1)

        adj1            = input("Please enter an adjective: ")
        plural_noun1    = input("Please enter a plural noun: ")
        noun1           = input("Please enter a noun: ")
        adj2            = input("Please enter an adjective: ")
        last_name1      = input("Please enter a last name: ")
        adj3            = input("Please enter an adjective: ")
        noun2           = input("Please enter a noun: ")
        #save number as string, easier for integration into text
        num1            = input("Please enter a number: ")
        plural_noun2    = input("Please enter a plural noun: ")
        noun4           = input("Please enter a noun: ")
        adj4            = input("Please enter an adjective: ")
        noun5           = input("Please enter a noun: ")
        plural_noun3    = input("Please enter a plural noun: ")
        last_name2      = input("Please enter a last name: ")
        noun3           = input("Please enter a noun: ")

        time.sleep(1)
        print("...")
        time.sleep(1)
        
        print("1) Harvard is a/an", adj1, "university that has graduated the",
              "most American"  + plural_noun1 + ". Graduates include John Adams,",
              "Theodore Roosevelt, John E. " + last_name1 + ",", name, "W. Bush,",
              "and Barack " + last_name2 + ". \n2) In 1833, Andrew Jackson became",
              "the first", noun1, "to ride on a/an", adj2, "train. \n3)", name, "H.",
              "Taft was the largest president ever, weighting in at more than",
              "three hundred " + plural_noun2 + ". \n4)", name, "Madison was the",
              "shortest " + noun2 + ", at five feet", num1, "inches. He also",
              "weighed the least at just one hundred " + plural_noun3 + ". \n5)",
              "At 69, Ronald Reagen was the oldest " + noun3 + ". The most", adj3,
              "president was JFK at 43. Theodore Roosevelt was the youngest",
              noun4, "to become president, but that was only after the death",
              "of William McKinley. \n6) President Zachary Taylor claimed the term",
              "\"First" + noun5 + "\" in 1849 when he described", name, "Madison",
              "as America's", adj4, "Lady.")

    ###############################################
    # Get all words from user and plays arrest mode
    ###############################################

    elif mode == 3:
        print("Welcome to: The Arrest!")
        time.sleep(1)

        location            = input("Please enter a location: ")
        noun1               = input("Please enter a noun: ")
        verb_ed1            = input("Please enter a verb in the past tense: ")
        relative            = input("Please enter a type of family relative: ")
        verb1               = input("Please enter a verb: ")
        noun2               = input("Please enter a noun: ")
        adj3                = input("Please enter an adjective: ")
        verb_ed2            = input("Please enter a verb in the past tense: ")
        noun3               = input("Please enter a noun: ")
        verb2               = input("Please enter a verb: ")
        verb_ed3            = input("Please enter a verb in the past tense: ")
        noun4               = input("Please enter a noun: ")
        body_part           = input("Please enter a body part: ")
        verb4               = input("Please enter a verb: ")
        noun5               = input("Please enter a noun: ")
        adj1                = input("Please enter an adjective: ")
        noun6               = input("Please enter a noun: ")
        chain_restaurant    = input("Please enter the name of a chain restaurant: ")
        verb3               = input("Please enter a verb: ")
        noun7               = input("Please enter a noun: ")
        adj2                = input("Please enter an adjective: ")

        time.sleep(1)
        print("...")
        time.sleep(1)

        print("A man in", location, "was arrested this morning after he", verb_ed1,
              "a", noun1, "in front of " + noun2 + ". " + name + ", had a history",
              "of " + verb1 + ", but no one-not even his " + noun3 + "-ever imagined", 
              "he'd",  verb2, "with a", noun4, "stuck in his " + body_part +
              ". \"I always thought he was " + adj1 +", but I never thought he'd",
              "do something like this. Even his", relative, "was surprised.\"",
              "After a brief chase, cops followed him to a " + chain_restaurant
              + ", where he reportedly", verb_ed2, "in the fry machine. In",
              "January, a", noun5, "was charged with a similar crime. But rather",
              "than", verb3, "with a " + noun6 + ", she", verb_ed3, "with a", adj2,
              "dog. Either way, we imagine that after witnessing him", verb4,
              "with a " + noun7 + ", there are probably a whole lot of people",
              "who are " + adj3 + ".")

    else:
        #if mode input is not 1, 2, or 3, message displayed and game restarts
        print(mode, "is not a valid mode!")
        main()

welcome()

main()
