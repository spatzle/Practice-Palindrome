'''
Created on 2011-03-26

@author: joyce
'''
class Palindrome(str):
    
    def __init__(self, value):
        self.value = value
    
    def lenIsOdd(self):
        if len(self.value)%2 !=0:
            return True
        return False
    
    def update(self,newPalin):
        if(len(newPalin)-len(self.value) == 2):
            self.value = newPalin
        return len(self.value)


class PalindromeRunner():
    SPECIAL_CHAR = "x"
    def __init__(self,p):
        self.p = self.SPECIAL_CHAR+self.SPECIAL_CHAR+p+self.SPECIAL_CHAR+self.SPECIAL_CHAR
        self.evenPalins = {}
        self.oddPalins ={}
        self.palins = {1:self.oddPalins,2:self.evenPalins}
        self.initFindPalin() #init
        self.findPalin()
        
    def compare(self,pos,offset):
        if len(self.p)> pos+offset and pos-offset >0 and self.p[pos-offset]==self.p[pos+offset]:
            if pos not in self.oddPalins:
                self.oddPalins[pos] = Palindrome(self.p[pos-offset:pos+offset+1])
                return len(self.oddPalins[pos].value)
            else:
                return self.oddPalins[pos].update(self.p[pos-offset:pos+offset+1])

    def compareEven(self,pos,offset):
        if len(self.p)> pos+offset+1 and pos-offset >0 and self.p[pos-offset]==self.p[pos+offset+1]:
            return self.evenPalins[pos].update(self.p[pos-offset:pos+offset+2])    
            
    def initFindPalin(self):
        for x in range(1,len(self.p)-1):
            self.compare(x, 1)
        for x in range(0,len(self.p)-2):
            if(self.p[x]==self.p[x+1]):
                self.evenPalins[x] = Palindrome(self.p[x:x+2])

    def findPalin(self):
        for k,_ in self.oddPalins.items():
            for y in range (1,len(self.p)-1):
                self.compare(k,y)
        
        for k,_ in self.evenPalins.items():
            for y in range (1,len(self.p)-1):
                self.compareEven(k,y)      
    
    def __str__(self):
        printout = ""
        for x,_ in self.palins.items():
            for k,v in self.palins[x].items():
                printout +=str(k)+" "+v.value+"\n"
        return printout
    
    def longest(self):
        longestLen=0
        longest=""
        for x,_ in self.palins.items():
            for _,v in self.palins[x].items():
                if (len(v.value) > longestLen):
                    longestLen = len(v.value)
                    longest = v.value
        return longest.strip(self.SPECIAL_CHAR)

if __name__ == '__main__':
    p = PalindromeRunner("amanaplanacanalpanama")
    print ("result")
    print (p.longest())

    