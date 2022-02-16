# Get users name
name = input("What is your name: ")

if name == 'Jake':
    print("\nWow! I absolutely love that name, nice to meet you Jake!")
else:
    print(f"\n... No offense, but that's a terrible name, I have always liked the name Jake for some "
          f"reason.\nAnyways, nice to meet you {name}.")

print(f"\n\nThe rules of the game are simple, answer all 3 questions correct, and you will win A NEW BLIMP!!!\n")
is_begin = input("Are you ready (Y/N):").lower()
if is_begin != 'n' and is_begin != 'y':
    print(f"Are you stupid is the head {name}, I asked for the letter Y for 'Yes', or N for 'No'... You gave me this "
          f"value: '{is_begin}'.\n Since you couldn't even get the pre-question correct, I'm terminating the game, "
          f"you would have failed anyways.")
    quit()

if is_begin.lower() == "y":
    print("Time to beginn, MUHAHAHA\n")
else:
    print("Fine, be that way... I'll just keep the blimp myself, I'll call it the 'Blimp-mo-beal'")
    quit()

# Question 1
print("QUESTION 1: How much gigabytes of memes should the typical person have on their computer?\nA) 70GB or more\nB) "
      "10GB to 70GB\nC) Less than 10GB, but more than 1 GB\nD) None, memes are free on Google...")
q1a = input("What is your answer: ").lower()

if q1a != "a" and q1a != "b" and q1a != "c" and q1a != "d":
    print("Seriously....SERIOUSLY! I ask you to give me the letter A, B, C, or D, and you somehow failed to follow "
          "the simplist of rules. I'm terminating myself, that's how much I don't want to be in your precense "
          "anymore.")

if q1a == 'a':
    if name.lower() != 'matt':
        print(f"I bet your real name is Matt, not {name}. Only Matt would think this is the right answer... Congrats "
              f"on losing on the first questions, no blimp for you. I'm shutting down now...")
    else:
        print(f"{name}, I knew you would pick this option, I am here to tell you no.... NOOOOOOOO. You lost, "
              f"better luck next time.")
    quit()
elif q1a == 'b':
    print('I feel bad for the gigabytes that have to hold and look at that data 24/7 just because you might need it 2 '
          'years from now. *Sigh, you lose. NEXT!')
    quit()
elif q1a == 'c':
    print('WRONG, did you try A or B? Better luck next time {name}.')
    quit()
elif q1a == 'd':
    print('YES, CORRECT! Obviously this was a freebie, no one would actually download memes to their hard drive.')

# Question 2
print("QUESTION 2: Who is the best Gears and Rainbow player in the entire universe?\nA) Jake\nB) JakePember\nC) "
      "Matt\nD) Zack")
q1a = input("What is your answer: ").lower()

if q1a != "a" and q1a != "b" and q1a != "c" and q1a != "d":
    print("Seriously....SERIOUSLY! I ask you to give me the letter A, B, C, or D, and you somehow failed to follow "
          "the simplist of rules. I'm terminating myself, that's how much I don't want to be in your precense "
          "anymore.")
    quit()

if q1a == 'a':
    print("WOW, amazing; Only a true fan knows the real name of JakePember! Since you know him in real life, "
          "pleassseee can you try to get me an autograph, have it made out to 'pie_eating_snake', that's my gamer "
          "tag.")
elif q1a == 'b':
    print("That's correct! This is common knowledge of coarse, nothing difficult about this question. No one is even "
          "close to his skill level.")
elif q1a == 'c':
    print("WRONG, I should ban you right now for such a terrible guess. In fact, I'm just going to end the quiz now, "
          "goodbye.")
    quit()
elif q1a == 'd':
    print("You must have misread the question, I asked who is the BEST player, not who is the equivelent of Robin to "
          "the best player. ZINNNNGGGG")
    quit()

print(f"I CANT BELIEVE IT! {name}, you have made it to the final question, congrats. Question 3 is... where did I put "
      f"it... nope, not there... oh no, I think I lost it :(  .")
print(f"{name}, can you help me? Someone must have deleted my 3rd question! Can you edit my code to add a 3rd "
      f"question for me to ask others to complete the game?")

end = input('Press the enter key to stop me from running, then proceed to operating on my code.')
