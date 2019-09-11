from tabulate import tabulate
from collections import namedtuple

class Relation():
    
    def __init__(self, list_of_tuples):
        self.tuples = set(list_of_tuples) 

    def projection(self, columns):
        '''
        Projekcija (eng. projection). 
        Metoda koja vraća sve retke zadanih stupaca.
        '''
        
        rows = list(set([tuple(getattr(row, column) 
                        for column in columns.split())
                        for row in self.tuples]))
        
        # novi namedtuple
        named = []
        new_namedtuple = namedtuple(self.name(), columns.split())
        for t in rows:
            named.append(new_namedtuple._make(t))
        return Relation(named)
        
    def selection(self, column, rel_operator, x):
        '''
        Selekcija (eng. selection).
        Metoda koja vraća samo one retke 
        koji zadovoljavaju zadani uvjet.
        '''
        
        selection = []
        if(rel_operator == "=="):
            for row in self.tuples:
                if row[column-1] == x:
                    selection.append(row)
        elif(rel_operator == "<"):
            for row in self.tuples:
                if row[column-1] < x:
                    selection.append(row)  
        elif(rel_operator == "<="):
            for row in self.tuples:
                if row[column-1] <= x:
                    selection.append(row)     
        elif(rel_operator == ">"):
            for row in self.tuples:
                if row[column-1] > x:
                    selection.append(row)
        elif(rel_operator == ">="):
            for row in self.tuples:
                if row[column-1] >= x:
                    selection.append(row)
        return Relation(selection) 

    def cartesian_product(self, r2):
        '''
        Kartezijev produkt (eng. cartesian product).
        Vraća novu relaciju koja se dobije spajajući svaki red 
        iz prve relacije sa svakim redom iz druge relacije.
        '''
        
        rows = set(x+y for x in self.tuples for y in r2.tuples)
           
        # nova relacijska shema    
        new_schema = []
        for el in self.relational_schema():
            if el in r2.relational_schema():
                new_schema.append(self.name()+"_"+el)
            else:
                new_schema.append(el)
        
        for el in r2.relational_schema():
            if el in self.relational_schema():
                new_schema.append(r2.name()+"_"+el)
            else:
                new_schema.append(el)

        # novi namedtuple
        named = []
        new_name = self.name()+"_cartesian_"+r2.name() # novo ime relacije
        new_namedtuple = namedtuple(new_name, new_schema)
        for t in rows:
            named.append(new_namedtuple._make(t))
        return Relation(named)
    
    def natural_join(self, r2):
        '''
        Prirodni spoj (eng. natural join)
        Redci rezultirajuće relacije su dobiveni na način da 
        se spajaju svi redci iz prve relacije sa svim redcima iz 
        druge relacije koji se podudaraju na zajedničkim atributima
        '''
        
        # (presjek) lista zajedničkih atributa za dvije relacije
        schema1 = self.relational_schema()
        schema2 = r2.relational_schema()
        common_fields = list(set(schema1) & set(schema2))
        
        # nova relacijska shema
        new_schema = self.relational_schema()
        for el in r2.relational_schema():
            if el not in common_fields:
                new_schema.append(el)
          
        # novo ime relacije
        new_name = self.name()+"_join_"+r2.name()
                
        new_relation = [] # nova relacija koja se dobije iz prve dvije
        
        # ako su relacijske sheme disjunktne, prirodni spoj je isto što i Kartezijev produkt
        if len(common_fields) == 0: 
            return self.cartesian_product(r2)
        else:
            indexes1 = [self.relational_schema().index(el) 
                        for el in self.relational_schema() if el in common_fields]
            indexes2 = [r2.relational_schema().index(self.relational_schema()[i]) 
                        for i in indexes1]
            
            for row1 in self.tuples:
                for row2 in r2.tuples:
                    matching = True
                    for i in range(0,len(indexes1)):
                        if row1[indexes1[i]] != row2[indexes2[i]]:
                            matching = False
                            break
                    if matching:
                        new_row = list(row1)
                        for i in range(0,len(r2.relational_schema())):
                            if i not in indexes2:
                                new_row.append(row2[i])
                        new_relation.append(tuple(new_row))
        # novi namedtuple             
        named = []
        new_namedtuple = namedtuple(new_name, new_schema)
        for t in new_relation:
            named.append(new_namedtuple._make(t))
        return Relation(named)
    


    def rename(self, current_name, new_name):
            '''
            Preimenovanje (engl. rename)
            Metoda koja omogućava promjenu imena atributa 
            u nekoj relacijskoj shemi
            '''
                             
            schema = self.relational_schema()
            
            if current_name in self.relational_schema():
                if new_name not in self.relational_schema():
                    for el in self.relational_schema():
                        if el == current_name:
                            new_index = self.relational_schema().index(el)
            
            # novi namedtuple
            named = []
            schema[new_index] = new_name
            new_namedtuple = namedtuple(self.name(), schema)
            for t in self.tuples:
                named.append(new_namedtuple._make(t))
            
            return Relation(named)
        
    def __and__(self, r2):
        '''
        Presjek (eng. intersection). 
        Metoda vraća skup svih uređenih parova 
        koji su zajednički objema relacijama.
        '''
        
        intersection = set(self.tuples) & set(r2.tuples)
                             
        # novi namedtuple             
        named = []
        new_name = self.name() + "_intersection_" + r2.name()
        new_schema = Relation(intersection).relational_schema()
        new_namedtuple = namedtuple(new_name, new_schema)
        for t in intersection:
            named.append(new_namedtuple._make(t))
        return Relation(named)

    
    def __add__(self, r2):
        '''
        Unija (eng. union). 
        Metoda vraća skup svih uređenih parova 
        koji pripadaju prvoj relaciji ili drugoj relaciji.
        '''
        
        union = set(self.tuples) | set(r2.tuples)
        return union
    
    def __or__(self, r2):
        '''
        Unija (eng. union). 
        Metoda koja poziva metodu __add__(self, r2)
        '''
        union = self + r2
        
        # novi namedtuple  
        named = []
        new_name = self.name() + "_union_" + r2.name()
        new_schema = Relation(union).relational_schema()
        new_namedtuple = namedtuple(new_name, new_schema)
        for t in union:
            named.append(new_namedtuple._make(t))
        return Relation(named)
    
    def __sub__(self, r2):
        '''
        Razlika (eng. difference). 
        Vraća skup svih uređenih parova koji pripadaju 
        prvoj relaciji, ali ne pripadaju drugoj relaciji.
        '''
        
        difference = set(self.tuples) - set(r2.tuples)
        
        # novi namedtuple  
        named = []
        new_name = self.name() + "_difference_" + r2.name()
        new_schema = Relation(difference).relational_schema()
        new_namedtuple = namedtuple(new_name, new_schema)
        for t in difference:
            named.append(new_namedtuple._make(t))
        return Relation(named)
        
    def relational_schema(self):
        columns = ""
        for column in list(self.tuples)[0]._fields:
            columns += column + " "
        columns = columns.split()
        return columns
    
    def name(self):
        return str(list(self.tuples)[0]).split('(')[0]  

    def table(self):
        print(self.name()+"\n")
        t = self.tuples
        s = self.relational_schema()
        print(tabulate(t, s, tablefmt="github"))
        
    def __eq__(self, r2):
        tuples = self.tuples == r2.tuples
        schema = self.relational_schema() == r2.relational_schema()
        name = self.name() == r2.name()
        return tuples and schema and name
        
    def __repr__(self):
        return f"Relation({self.tuples})"
        