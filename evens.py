
evens = [even for even in range(0,10,2)]
print(evens)

start1 = ["fee","fie","foe"]
rhymes = [
    ('flop','get a mop'),
    ('fope','turn the rope'),
    ('fa','get your ma'),
    ('fudge','call the judge'),
    ('fat','pet the cat'),
    ('fog','walk the dog'),
    ('fun','say we\'re done')
]
start2 = 'Someone better'

def first_line(start1):
    for each in start1:
        print(each.capitalize()+'! ')
        
def second_line(rhymes,start1,start2):
    for first,second in rhymes:
        first_line(start1)
        print(first.capitalize()+'! \n')
        print(start2+' ')
        print(second+'.\n')
second_line(rhymes,start1,start2)