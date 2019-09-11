from tabulate import tabulate

class BinaryRelation():
    
    def __init__(self, list_of_pairs):
        self.pairs = set(list_of_pairs)


    def table(self):
        '''
        Metoda koja ispisuje listu uređenih parova u tabličnom obliku.
        Koristi tabulate modul.
        '''
        
        print(tabulate(self.pairs, tablefmt="fancy_grid"))  
    
    def converse(self):
        '''
        Obrat (engl. converse, inverse). 
        Metoda koja vraća uređene parove tako da za svaki (a,b) 
        element iz relacije proslijeđene metodi, vraća par (b,a).
        '''
        
        converse = {(b, a) for (a, b) in self.pairs}
        return BinaryRelation(converse)
    
    def __add__(self, r2):
        '''
        Unija (engl. union). 
        Metoda vraća skup svih uređenih parova koji pripadaju 
        prvoj relaciji ili drugoj relaciji.
        '''
        
        union = set(self.pairs) | set(r2.pairs) 
        return BinaryRelation(union)
    
    def __or__(self, r2):
        '''
        Unija (engl. union). 
        Metoda koja poziva metodu __add__(self, r2)
        '''
        
        return r1 + r2
    
    def __and__(self, r2):
        '''
        Presjek (engl. intersection). 
        Metoda vraća skup svih uređenih parova koji su 
        zajednički objema relacijama.
        '''
        
        intersection = set(self.pairs) & set(r2.pairs)
        return BinaryRelation(intersection)
    
    def __sub__(self, r2):
        '''
        Razlika (engl. difference). 
        Vraća skup svih uređenih parova koji pripadaju prvoj relaciji, 
        ali ne pripadaju drugoj relaciji.
        '''
        
        return BinaryRelation(set(self.pairs) - set(r2.pairs))

    def compose(self, r2):
        '''
        Kompozicija relacija (engl. composition).  
        Metoda koja vraća novu relaciju dobivenu primjenom pravila 
        kompozicije dviju proslijeđenih relacija.
        '''
        
        composition = set()
        for a, b in self.pairs:
             for c, d in r2.pairs:
                    if b == c:
                        composition.add((a,d))
        return BinaryRelation(composition)
        
    def __mul__(self, r2):
        '''
        Kompozicija relacija (engl. composition). 
        Metoda koja poziva metodu compose(self, r2)
        '''
        
        return self.compose(r2)
    
    def __contains__(self, pair):
        '''
        Metoda koja vraća True ako postoji zadani uređeni par
        u relaciji, a False ako ne postoji
        '''
        
        return True if pair in self.pairs else False

    def __len__(self):
        '''
        Metoda koja vraća broj elemenata (uređenih parova) relacije.
        '''
        
        return len(self.pairs)
 
    def __eq__(self, r2):
        '''
        Jednakost relacija (engl. equality).
        '''
        
        return self.pairs == r2.pairs
    
    def __ne__(self, r2):
        '''
        Nejednakost relacija (engl. unequal, not equal).
        '''
        
        return self.pairs != r2.pairs
    
    def __lt__(self, r2):
        '''
        Operator "manje od".
        Provjerava sadrži li jedna operacija drugu.
        '''

        return self.pairs < r2.pairs
    
        
    def __le__(self, r2):
        '''
        Operator "manje od".
        Provjerava sadrži li jedna operacija drugu.
        Vraća True i u slučaju da su relacije jednake.
        '''
        
        return self.pairs <= r2.pairs
    
       
    def __gt__(self, r2):
        '''
        Operator "veće od".
        Provjerava sadrži li jedna operacija drugu.
        '''
        
        return self.pairs > r2.pairs
        
        
    def __ge__(self, r2):
        '''
        Operator "veće od".
        Provjerava sadrži li jedna operacija drugu.
        Vraća True i u slučaju da su relacije jednake.
        '''
        
        return self.pairs >= r2.pairs
    
    def is_function(self): 
        '''
        Svojstvo funkcionalnost.
        Metoda koja provjerava je li relacija funkcionalna te 
        vraća True ako je, a False ako nije.
        '''
        
        for a, b in self.pairs:
            for c, d in self.pairs:
                if(a == c) and (b != d):
                    return False
        return True
    
    def is_reflexive(self):
        '''
        Provjera je li relacija refleksivna.
        '''
        
        l = []
        for x,y in self.pairs:
            l.append(x)
            l.append(y)
        s = set(l)
        for x in list(s):
            if (x,x) not in self.pairs:
                return False
        return True
    
    def is_ireflexive(self):
        '''
        Provjera je li relacija irefleksivna.
        '''
        
        l = []
        for x,y in self.pairs:
            l.append(x)
            l.append(y)
        s = set(l)
        for x in list(s):
            if (x,x) in self.pairs:
                return False
        return True
    
    def is_symmetric(self):
        '''
        Provjera je li relacija simetrična.
        '''
        
        return self.converse() == self  
    
    def is_transitive(self):
        '''
        Provjera je li relacija tranzitivna.
        '''
        
        return self * self <= self
    
    def is_asymmetric(self):
        '''
        Provjera je li relacija asimetrična.
        '''
        
        r = self & self.converse()
        return bool(not(r.pairs))
        
    def is_antisymmetric(self):
        '''
        Provjera je li relacija antisimetrična.
        '''
        
        for x, y in self.pairs:
            if ((y, x) in self.pairs and x != y):
                return False
        return True
    
    
    def is_equivalence_relation(self):
        '''
        Provjera je li relacija ekvivalencije.
        '''
        
        r = self.is_reflexive()
        s = self.is_symmetric()
        t = self.is_transitive()
        return r and s and t 
    
    def is_partial_order(self):
        '''
        Provjera je li relacija parcijalnog uređaja.
        '''
        
        r = self.is_reflexive()
        a = self.is_antisymmetric()
        t = self.is_transitive()
        return r and a and t
    
    def __repr__(self):
        return f"BinaryRelation({self.pairs})"