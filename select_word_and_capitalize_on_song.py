song="""When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
word='moray'

    #capitalize a word in a song, the song is registered in the ego-psyche injectively as a visual
    #a symbolic typing in first-person ((?):transmissible) cognate mind phenom co-ordered dually in the hypnoanalytic sense (objectably-oriented)),
    #here representing symbolic-associatively as i=cue and i2=harmony/disharmony/tonal tonality, as a gravitas accumulative currency with wish-fulfilled notion 

class capton():
    def __init__(self,song,words):
        self.words=words.capitalize()
        self.song=song
        self.songp=self.capitalize_words_on_it(self.song,self.words)
    def __str__(self):
        return str(self.songp)
    def __print__(self):
        print(self.__str__())
        return
    def capitalize_words_on_it(self,song,words):
        i=self.song.find(self.words.lower())
        i2=self.song.find(self.words.lower())+len(self.words.lower())
        self.song=self.song[:i]+self.words+self.song[i2:]
        return self.song
    
print(capton(song,word))