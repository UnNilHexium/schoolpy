import random as r


options=["a",'b','c','d']


def mcq():
    correct_answer=r.choice(options)
    chosen_answer=r.choice(options)
    l=options.remove(correct_answer)
    remove_answer1=r.choice(options)
    l=options.remove(remove_answer1)
    remove_answer2=r.choice(options)
    if chosen_answer in (remove_answer1,remove_answer2):
        return 2
    else:
        switch=options.remove(remove_answer1)
        switch=options.remove(remove_answer2)
        switch=options.remove(chosen_answer)
        check_answer=switch[0]
        if check_answer==correct_answer:
            return 1
        else:
            return 0

pf=0
pc=0
ud=0
while range(1000):
    x=mcq()
    if x==0:
        pf+=1
    elif x==1:
        pc+=1
    elif x==2:
        ud+=1

print(pf,pc,pd)
