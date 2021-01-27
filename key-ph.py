import RAKE
text1 = """Google quietly rolled out a new way for Android users to listen 
to podcasts and subscribe to shows they like, and it already works on 
your phone. Podcast production company Pacific Content got the exclusive 
on it.This text is taken from Google news."""
stop_words = 'SmartStoplist.txt'
rakeobj = RAKE.Rake(stop_words)
words = rakeobj.run(text1)
print(words)
for w in words:
    print(w[0])