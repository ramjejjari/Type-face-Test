pip install pyphonetics -q 
from pyphonetics import Soundex
n=input()
snd = Soundex()
res=snd.phonetics(n)
final=[]
for i in range(text):
    a=snd.phonetics(i)
    if a==res:
        final.append(i)
print(*final)        