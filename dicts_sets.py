e2f={'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f['walrus'])
f2e={e2f[animal]:animal for animal in e2f}
print(f2e.get('chien'))
cats=['Henri','Grumpy','Lucy']
octopi={}
emus={}
strng={'cats':cats,'octopi':{},'emus':{}}
life={'animals':strng,'plants':{},'other':{}}
print(life)
print(life['animals'])
print(life['animals']['cats'])
squares={range(10): i**i for i in range(10)}
odd={i for i in range(1,10,2)}
st=['Got  ' + str(i) for i in range(10)]
for i in st:
    print(i)
b=('optimist','pessimist','troll')
a=('The glass is half full','The glass is half empty','How did you get a cup?')
a_dict1=dict(zip(b,a))
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks on a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop','Check your exits']
a_dict=dict(zip(titles,plots))
