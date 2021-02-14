import string
from math import sqrt
def count_words():
    d = dict()
    text = open("mockingjay.txt", "r") 
    for line in text:
        line = line.strip()
        line = line.lower()
        line = line.translate(line.maketrans("","",string.punctuation))#for removing the puntcation
        words = line.split(" ")
        for word in words:
            if word in d:
                d[word]= d[word]+1
            else:
                d[word] = 1
    text.close
    #for key in list(d.keys()): 
     #   print(key, ":", d[key])
    #print(new_d[-20:])
    new_d=list(dict(sorted(d.items(), key=lambda item: item[1])))
    return new_d[-20:]


    

def write_into_text():
    l = count_words()
    files = open("maximum_word.txt","w")
    files.write('\n'.join(l))
    files.close()
   # with open('your_file.txt', 'w') as f:
    #for item in my_list:
     #   f.write("%s\n" % item) #different way 

    
    
def euclidean_distance():
    x1 = int(input("enter x1: "))
    y1 = int(input("enter y1: "))
    x2 = int(input("enter x2: "))
    y2 = int(input("enter y2: "))
    result = (x1-x2)**2 + (y1-y2)**2
    print(int(sqrt(result)))


class Empte:
    pass

class vehcle:
    max_speed = 250
    mileage = 1000

def reverse_words():
    sentance = input("enter your sentence to reverse: ")
    words =sentance.split(" ")
    for i in range(len(words),0,-1):
        print(words[i-1])


class names_person():
    def __init__(self):
        self.name_person = ""

    def get_String(self):
        self.name_person = input("Enter your name: ")

    def print_String(self):
        print(self.name_person.upper())

class Circle:
    def __init__(self):
        self.radice = 3
    def area_of_circle(self):
        self.radice = int(input("enter the redice for area: "))
        print((self.radice)**2 * 3.14)
    def  perimeter_of_circle(self):
        self.radice = int(input("enter the redice: "))
        print(2*3.14*self.radice)    

#write_into_text()
#euclidean_distance()
#reverse_words()
#obj = names_person()
#obj.get_String()
#obj.print_String()
#c1 = Circle()
#c1.area_of_circle()
#c1.perimeter_of_circle()

