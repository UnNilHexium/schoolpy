import random as r


options=["a",'b','c','d']
def mcq():
    correct_answer=r.choice(options)
    chosen_answer=r.choice(options)
    l=options.remove(correct_answer)
    wrong_answer1=r.choice(l)
    l=options.remove()
    wrong_answer2=r.choice(l)
    chosen_answer=