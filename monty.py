import random as r


OPTIONS = ["a", "b", "c", "d"]


def mcq():
   
    options = OPTIONS.copy()

    correct_answer = r.choice(options)
    chosen_answer = r.choice(options)

    
    options.remove(correct_answer)

   
    remove_answer1 = r.choice(options)
    options.remove(remove_answer1)

    remove_answer2 = r.choice(options)
    options.remove(remove_answer2)

   
    if chosen_answer in (remove_answer1, remove_answer2):
        return 2

    remaining = OPTIONS.copy()
    remaining.remove(remove_answer1)
    remaining.remove(remove_answer2)
    remaining.remove(chosen_answer)
    switched_answer = remaining[0]

    if switched_answer == correct_answer:
        return 1  
    else:
        return 0  


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