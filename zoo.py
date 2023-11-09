from pprint import pprint
from collections import OrderedDict,defaultdict
def hours():
    print('Open 9-5 daily')
    return
plain = {'a' : 1, 'b' : 2, 'c' : 3}

pprint(plain)

fancy = OrderedDict(plain)
print(fancy)
dict_of_lists = defaultdict(list)
dict_of_lists['a'] = 'something for a'
print(dict_of_lists)