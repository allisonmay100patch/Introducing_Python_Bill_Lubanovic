def good():
	return ['Harry','Ron','Hermione']
def get_odds():
    odds = [range(1,10,2)]
    thirdness = 0
    for i in odds:
        thirdness += 1
        if thirdness == 3:
            return i
def test(func):
    def new_function(func):
        print('start')
        func()
        print('end')
    return new_function(func)
def OopsException():
    pass
try:
    raise OopsException()
except:
    print('caught an oops')
get_odds()
test(good)