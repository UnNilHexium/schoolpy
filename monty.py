import random as r

# Keep the original options safe
OPTIONS = ["a", "b", "c", "d"]


def mcq():
    # Work on a fresh copy every time
    options = OPTIONS.copy()

    correct_answer = r.choice(options)
    chosen_answer = r.choice(options)

    # Remove the correct answer from the pool of wrong answers to eliminate
    options.remove(correct_answer)

    # Eliminate two wrong answers
    remove_answer1 = r.choice(options)
    options.remove(remove_answer1)

    remove_answer2 = r.choice(options)
    options.remove(remove_answer2)

    # CASE 1: The host accidentally eliminated the player's chosen answer
    if chosen_answer in (remove_answer1, remove_answer2):
        return 2

    # CASE 2: The player switches to the remaining unopened option
    # Recreate the remaining pool to find the switched answer
    remaining = OPTIONS.copy()
    remaining.remove(remove_answer1)
    remaining.remove(remove_answer2)
    remaining.remove(chosen_answer)

    # There is only one element left in 'remaining'
    switched_answer = remaining[0]

    if switched_answer == correct_answer:
        return 1  # Win by switching
    else:
        return 0  # Lose by switching


pf = 0  
pc = 0  
ud = 0  


for _ in range(1000):
    x = mcq()
    if x == 0:
        pf += 1
    elif x == 1:
        pc += 1
    elif x == 2:
        ud += 1

print(f"Lost by switching: {pf}")
print(f"Won by switching: {pc}")
print(f"Invalid games (Host picked player's choice): {ud}")