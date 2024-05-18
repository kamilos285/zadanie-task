


class Task:
    def __init__(self, nazwa,opis,priorytet,termin):
        self.nazwa = nazwa
        self.opis = opis
        self.priorytet = priorytet
        self.termin = termin


    #def __str__(self): # nadpisujemy print(przyslaniamy,przeciazamy printa, dander method)
        #return f"{self.nazwa,self.opis,self.priorytet,self.termin}"
        

    def __repr__(self):
        return f"{self.nazwa,self.opis,self.priorytet,self.termin}"


class TaskM:
    def __init__(self):
        
        self.listaZadan = []
        



    def dodaj(self,zadanie):
        
        #nazwa = str(input("podaj nazwe: "))
        #opis = str(input("podaj opis: "))
        #priorytet = str(input("podaj priorytet: "))
        #termin = str(input("podaj termin: "))
        
        self.listaZadan.append(zadanie)


    def usun(self,usun_index):
        
        
        #usun_zadanie = int(input("wybierz zadanie ktore usunac: "))-1
        taskManager.listaZadan.pop(usun_index)
        

    def wyswietl(self,index = None):

        if index == None:
            print(self.listaZadan)
        
        else:
            print(self.listaZadan[index])
            


zadanie1 = Task("zadanie","zadanie domowe","wazne","nakiedys") # zadanie 1 to obiekt task


taskManager = TaskM()

print(taskManager.listaZadan)

taskManager.dodaj(zadanie1) # zadanie 1 to obiekt ale tez argument metody dodaj

taskManager.dodaj(Task("zadanie2","zadanie domowe","bardzo wazne","na jutro")) # drugi sposob tworzenia obiektu task ale juz bez nazwy

taskManager.wyswietl()

taskManager.wyswietl(1)

#taskManager.usun(1)

#print(taskManager.listaZadan[0].nazwa)

zadanie2 = taskManager.listaZadan[1]  # sposob dostania sie do 2 indexu w liscie zadan i nadania mu nazwy

#print(zadanie2)
