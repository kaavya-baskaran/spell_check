from textblob import TextBlob,Word

def spell(word):
    options=[]
    temp = []
    spl_char=['!','@','#','$','%','^','&','*','(',')','{','}','[',']','|','?','\\','/',',','.','<','>','_','-',';',':','~',"\'",'"']
    string_lis=list(word)
    if string_lis[-1] in spl_char:
        temp=string_lis[-1]
        string_lis.remove(string_lis[-1])
        word=''.join(string_lis)
    print('word=',word)

        
    sentence=Word(word)
    options=sentence.spellcheck()
    print(options[0])
    

    if options[0][1]==1.0:
        result=options[0][0]
        if temp:
            result+=temp
        
        return result
    
    elif(word==options[0][0]):
        result=word
        if temp:
            result+=temp
        
        return result
    
        
    else:
        selection=[]
        print("choose word instead of",word)
        for tuple in options[:5]:
            print(options.index(tuple)+1,"-",tuple[0])
            selection.append(tuple[0])
        option_num=int(input("num"))
        result=selection[option_num-1]
        
        if temp:
            result.append(temp)
            result=''.join(result)
        
        return result

sentence_to_check='Dhe feethers knnck eech others.'
words_in_sent=sentence_to_check.split()
senten=spell(words_in_sent[0])
for word in words_in_sent[1:]:
    senten+=' '+(spell(word))
print(senten)

    
    
    
