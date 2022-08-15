def arithmetic_arranger(problems,TFBool=False):
  line1 = ''
  line2 = ''
  line3 = ''
  line4 =''
  if len(problems)>5:
    return "Error: Too many problems."
  else:
    for i in problems:
      string = i.split()
      if (string[1] == '+') or (string[1] == '-'):
        if string[0].isnumeric() and string[2].isnumeric():
          if len(string[0])>4 or len(string[2])>4:
            return "Error: Numbers cannot be more than four digits."
          else:
            if len(string[0])>len(string[2]):
              barlength = len(string[0]) + 2
            else:
              barlength = len(string[2]) + 2
            line1+=((barlength-len(string[0]))*" "+string[0]+"    ")
            line2+=string[1]+((barlength-len(string[2])-1)*" "+string[2]+"    ")
            line3+=barlength*'-'+"    "
            if TFBool == True:
              if string[1]=='+':
                number=int(string[0])+int(string[2])
              else:
                number = int(string[0])-int(string[2])
              line4 +=((barlength-len(str(number)))*" "+str(number)+"    ")
        else:
          return "Error: Numbers must only contain digits."
      else:
        return "Error: Operator must be '+' or '-'."
    
    arranged_problems= (line1.rstrip()+"\n"+line2.rstrip()+"\n"+line3.rstrip())
    if TFBool is True:
      arranged_problems += "\n"+line4.rstrip()
    return arranged_problems
