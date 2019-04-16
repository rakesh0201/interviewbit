def anagram(input):
        
        words = input.split(",")
        c = []
        
            
           
        for i in range(0 ,len(words)):
            b=[]
            if(words[i] == None):
                continue
            flag = 0   
            for j in range(i+1,len(words)):
                if(words[j]==None):
                    continue
                if(sorted(words[i]) == sorted(words[j])):
                    words[j] = '0'
                    flag = 1
                    
            if(flag==1):
                words[i] = '0'
            for k in range(0,len(words)):
                if(words[k] == '0'):
                    
                    b.append(k)
                    words[k] = None
            c.append(b)
       
                    
        print(c)

input = input("Enter string : ")
anagram(input)
