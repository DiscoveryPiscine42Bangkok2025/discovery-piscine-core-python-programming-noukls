import sys
def downcase_it() :
    
        if len(sys.argv) < 2 :
            print('none')
        else : 
            for i in range(len(sys.argv)) :
                i = i+1
                print(sys.argv[i].lower())
downcase_it()
 