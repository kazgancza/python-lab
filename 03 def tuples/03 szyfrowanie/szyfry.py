def koduj(public):
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""

    for char in public:
        if char.isupper():
            result+=char
        if char.islower() and char in letters.lower():
            result+=char.upper()
        if char.isdigit():
            char=int(char)
            if char==0:
                result+="ZERO"
            if char==1:
                result+="ONE"
            if char==2:
                result+="TWO"
            if char==3:
                result+="THREE"
            if char==4:
                result+="FOUR"
            if char==5:
                result+="FIVE"
            if char==6:
                result+="SIX"
            if char==7:
                result+="SEVEN"
            if char==8:
                result+="EIGHT"
            if char==9:
                result+="NINE"
        elif char==".":
            result+="STOP"

    return result

def cezar(text, key, enc):
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    
    if bool(enc) is True:

        for char in text:
            pos=letters.find(char.upper())
            pos+=int(key)
            pos%=26
            result+=letters[pos]
    else:

        for char in text:
            pos=letters.find(char.upper())
            pos-=int(key)
            pos%=26
            result+=letters[pos]
        
    return result

def vigener(text, key, enc):
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=""
    key_pos=0

    for char in text:

        current_key=letters.find(key[key_pos])
        result+=cezar(char, current_key, enc)
        key_pos+=1

        if key_pos==len(key):
            key_pos=0
    
    return result

def plotek(text, key, enc):
    result=""
    lines=[]

    for i in range(int(key)):
        lines+=" "
    
    if bool(enc)==True:
        
        pos=0
        vector=1 # 1 - up; 0 - down
        
        
        for i in range(len(text)):
            lines[pos]+=(text[i])
            if pos+1<key and vector==1:
                pos+=1
            elif pos+1==key:
                pos-=1
                vector=0
            elif pos==0:
                pos+=1
                vector=1
            elif pos<key and vector==0:
                pos-=1
        
        for i in range(key-1, -1, -1):
            result+=lines[i].strip()
    else:

        """
        for pos in range(0, key):
            i=key-1-pos
            while(i<len(text)):
                if pos==0 or pos==key-1:
                    lines[pos]+=text[i]
                    
                else: 
                    lines[pos]+=text[i-pos-1]
                    lines[pos]+=text[i-pos+1]
                i+=2*key-2
        """

    return result

   
