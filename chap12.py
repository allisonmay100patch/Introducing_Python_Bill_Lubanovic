import unicodedata
import re
import binascii
mystery = '\U0001f984'
print(mystery, unicodedata.name(mystery))

pop_bytes = mystery.encode('UTF-8')
print(pop_bytes)

pop_string = pop_bytes.decode()
print(pop_string)

mammoth = '''We have seen the Queen of cheese,
Laying quietly at your ease,
Gently fanned by evening breeze --
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial Show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees --
Or as the leaves upon the trees --
It did require to make thee please,
And stand unrivalled Queen of Cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great World's show at Paris.

Of the youth -- beware of these --
For some of them might rudely squeeze
And bite your cheek; then songs or glees
We could not sing o' Queen of Cheese.

We'rt thou suspended from baloon,
You'd cast a shade, even at noon;
Folks would think it was the moon
About to fall and crush them soon.'''

c_words = re.findall('\sc[\w]+', mammoth)
curdle = []
for curd in c_words:
    curdle += [curd[1:]]
print(curdle)

four_words = []
for four_letter_word in curdle:
    if len(four_letter_word) == 4:
        four_words += [four_letter_word]
print(four_words)

r_tailed_words = re.findall('\s[\w]+r[\s]',mammoth)

strs = []
for stripped in r_tailed_words:
    strs += [stripped.strip(' ')]
print(strs)

three_vowels = re.findall('[\w]*[aeiou]{3}[\w]*',mammoth)
print(three_vowels)
 
g = b'474946383961010001008000000000000ffffff21f9040100000002c000000000100010000020144003b'
gif = binascii.unhexlify(g)
print(gif)
print(gif[6])
print(gif[8])