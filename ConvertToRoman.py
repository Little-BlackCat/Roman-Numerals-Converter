#function convert unit numbert to roman
def mainUnit(strNum):
  return {
    "1" : "I",
    "2" : "II",
    "3" : "III",
    "4" : "IV",
    "5" : "V",
    "6" : "VI",
    "7" : "VII",
    "8" : "VIII",
    "9" : "IX"
  }.get(strNum, "0")

def tenUnit(strNum):
  return {
    "1" : "X",
    "2" : "XX",
    "3" : "XXX",
    "4" : "XL",
    "5" : "L",
    "6" : "LX",
    "7" : "LXX",
     "8" : "LXXX",
     "9" : "XC"
  }.get(strNum, "0")
        
def hundrenUnit(strNum):
  return {
    "1" : "C",
    "2" : "CC",
    "3" : "CCC",
    "4" : "CD",
    "5" : "D",
    "6" : "DC",
    "7" : "DCC",
    "8" : "DCCC",
    "9" : "CM"
  }.get(strNum, "0")

def thousonUnit(strNum):
  return {
    "1" : "M",
    "2" : "MM",
    "3" : "MMM",
  }.get(strNum, "0")
        
def toRoman(strNum):
  if (len(strNum) == 1): 
    return mainUnit(strNum[0])
  elif (len(strNum) == 2): 
    return tenUnit(strNum[1]) + mainUnit(strNum[0])
  elif (len(strNum) == 3):
    return hundrenUnit(strNum[2]) + tenUnit(strNum[1]) + mainUnit(strNum[0])
  elif (len(strNum) == 4):
    return thousonUnit(strNum[3]) + hundrenUnit(strNum[2]) + tenUnit(strNum[1]) + mainUnit(strNum[0])
  else :
    return "0"  

def convertToRoman(num):
  if num > 3999:
    return "Too many"
  else: 
    strNum = str(num)[::-1]; # num to string and reverse ---> ['3','2','1']
  
  romanNumber = toRoman(strNum).replace('0','')
  return romanNumber

