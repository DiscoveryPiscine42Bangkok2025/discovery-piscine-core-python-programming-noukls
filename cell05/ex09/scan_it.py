import re
import sys
key_word = sys.argv[1]
text = sys.argv[2]
matches = re.findall(key_word,text)
print(matches)
if len(sys.argv) != 3 :
    print('none')
elif matches == [] :
    print('none')
else :
    print(len(matches)) 
    
