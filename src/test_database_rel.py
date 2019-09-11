import unittest
from collections import namedtuple

Osoba = namedtuple('Osoba', 'JMBAG ime spol godine')
Smjer = namedtuple('Smjer', 'JMBAG ime smjer')

R1 = namedtuple('R1', 'A B')
S1 = namedtuple('S1', 'C D E')

R2 = namedtuple('R2', 'A B C D')
S2 = namedtuple('S2', 'B C E')

N1 = namedtuple('r', 'A B C')
N2 = namedtuple('s', 'A B C')
N3 = namedtuple('k', 'A B C')


from database_rel import Relation

class TestRelation(unittest.TestCase):    
    def setUp(self):    
        studenti = set([
        Osoba('0178982471', 'Ana', 'žensko', 19),
        Osoba('0137829897', 'Luka', 'muško', 19),
        Osoba('0198274011', 'Marko', 'muško', 20),
        Osoba('0066719843','Mate', 'muško', 23),
        Osoba('0678124712', 'Sabina', 'žensko', 23),
        Osoba('0177023974', 'Sabina', 'žensko', 22),
        ])
        
        self.rel1 = Relation(studenti)
        
        smjerovi = set([
        Smjer('0172885615', 'Antonija', 'Informacijsko i programsko inženjerstvo'),
        Smjer('0178982471', 'Ana', 'Informacijsko i programsko inženjerstvo'),
        Smjer('0137829897', 'Luka', 'Organizacija poslovnih sustava'),
        Smjer('0198274011', 'Marko', 'Baze podataka i baze znanja'),
        Smjer('0066719843', 'Mate', 'Informatika u obrazovanju'),
        Smjer('0678124712', 'Sabina', 'Baze podataka i baze znanja'),
        Smjer('0177023974', 'Sabina', 'Organizacija poslovnih sustava'),
        ])
        
        self.rel2 = Relation(smjerovi)
        
        r1 = set([R1(4,1), R1(3,2),])
        self.rel3 = Relation(r1)
        
        s1 = set([S1(3,2,1), S1(3,3,5),])
        self.rel4 = Relation(s1)
        
        r2 = set([R2('a', 'b','c','d'), R2('a','b','a','a'),])
        self.rel5 = Relation(r2)
        
        s2 = set([S2('b','c','a'), S2('c','c','a'),])
        self.rel6 = Relation(s2)
        
        
        r1 = set([N1(2,3,1), N1(1,1,1),N1(0,1,0),])
        self.r = Relation(r1)
        
        s1 = set([N2(1,0,1), N2(2,3,1),])
        self.s = Relation(s1)
        
        k1 = set([N3(0,1,0), N3(1,2,3),])
        self.k = Relation(k1)
        
    
    def test_selection_1(self):
        a = self.rel1.selection(2, "==", "Sabina")
        b = Relation({Osoba(JMBAG='0678124712', ime='Sabina', spol='žensko', godine=23), 
                      Osoba(JMBAG='0177023974', ime='Sabina', spol='žensko', godine=22)})
        self.assertEqual(a,b)
        
    def test_selection_2(self):
        a = self.rel1.selection(1, "==", "0178982471")
        b = Relation({Osoba(JMBAG='0178982471', ime='Ana', spol='žensko', godine=19)})
        self.assertEqual(a,b)
        
    def test_selection_3(self):
        a = self.rel1.selection(4, "==", 23)
        b = Relation({Osoba(JMBAG='0066719843', ime='Mate', spol='muško', godine=23), 
                      Osoba(JMBAG='0678124712', ime='Sabina', spol='žensko', godine=23)})
        self.assertEqual(a,b)   
        
    def test_selection_4(self):
        a = self.rel1.selection(4, "<", 20)
        b = Relation({Osoba(JMBAG='0137829897', ime='Luka', spol='muško', godine=19), 
                      Osoba(JMBAG='0178982471', ime='Ana', spol='žensko', godine=19)})
        self.assertEqual(a,b)
        
    def test_selection_5(self):
        a = self.rel1.selection(4, "<=", 20)
        b = Relation({Osoba(JMBAG='0198274011', ime='Marko', spol='muško', godine=20), 
                      Osoba(JMBAG='0178982471', ime='Ana', spol='žensko', godine=19), 
                      Osoba(JMBAG='0137829897', ime='Luka', spol='muško', godine=19)})
        self.assertEqual(a,b)
        
    def test_selection_6(self):
        a = self.rel1.selection(4, ">", 20)
        b = Relation({Osoba(JMBAG='0177023974', ime='Sabina', spol='žensko', godine=22), 
                      Osoba(JMBAG='0066719843', ime='Mate', spol='muško', godine=23), 
                      Osoba(JMBAG='0678124712', ime='Sabina', spol='žensko', godine=23)})
        self.assertEqual(a,b)
    
    def test_selection_7(self):
        a = self.rel1.selection(4, ">=", 20) 
        b = Relation({Osoba(JMBAG='0177023974', ime='Sabina', spol='žensko', godine=22), 
                      Osoba(JMBAG='0198274011', ime='Marko', spol='muško', godine=20), 
                      Osoba(JMBAG='0066719843', ime='Mate', spol='muško', godine=23), 
                      Osoba(JMBAG='0678124712', ime='Sabina', spol='žensko', godine=23)})
        self.assertEqual(a,b)
        
    def test_projection_1(self):
        a = self.rel1.projection('ime godine').tuples
        a_tuples = [tuple(t) for t in a]
        b = [('Sabina', 23),('Sabina', 22), ('Ana', 19),('Luka', 19), ('Marko', 20),('Mate', 23)]
        self.assertEqual(set(a_tuples), set(b))
        
    def test_projection_2(self):
        a = self.rel1.projection('ime').tuples
        a_tuples = [tuple(t) for t in a]
        b = [('Sabina',), ('Luka',), ('Marko',), ('Mate',), ('Ana',)]
        self.assertEqual(set(a_tuples), set(b))
        
    def test_rename(self):
        a = self.rel1.rename("ime", "Smjer_ime")
        s = a.relational_schema()
        b = ['JMBAG', 'Smjer_ime', 'spol', 'godine']
        self.assertEqual(s, b)
        
    def test_natural_join1(self):
        a = self.rel1.natural_join(self.rel2).tuples
        a_tuples = [tuple(t) for t in a]
        b = [('0066719843', 'Mate', 'muško', 23, 'Informatika u obrazovanju'),
             ('0198274011', 'Marko', 'muško', 20, 'Baze podataka i baze znanja'),
             ('0177023974', 'Sabina', 'žensko', 22, 'Organizacija poslovnih sustava'),
             ('0137829897', 'Luka', 'muško', 19, 'Organizacija poslovnih sustava'),
             ('0178982471','Ana','žensko', 19, 'Informacijsko i programsko inženjerstvo'),
             ('0678124712', 'Sabina', 'žensko', 23, 'Baze podataka i baze znanja')]
        self.assertEqual(set(a_tuples),set(b))
        
    def test_natural_join2(self):
        # za disjunktne sheme
        
        a = self.rel3.natural_join(self.rel4).tuples
        a_tuples = [tuple(t) for t in a]
        b = [(3, 2, 3, 2, 1), (3, 2, 3, 3, 5), (4, 1, 3, 2, 1), (4, 1, 3, 3, 5)]
        self.assertEqual(set(a_tuples),set(b))
        
    def test_cartesian_product1(self):
        a = self.rel3.cartesian_product(self.rel4).tuples
        a_tuples = [tuple(t) for t in a]
        b = [(3, 2, 3, 2, 1), (3, 2, 3, 3, 5), (4, 1, 3, 2, 1), (4, 1, 3, 3, 5)]
        self.assertEqual(set(a_tuples),set(b))
        
    def test_cartesian_product2(self):    
        a = self.rel5.cartesian_product(self.rel6).tuples
        a_tuples = [tuple(t) for t in a]
        b = [('a', 'b', 'c', 'd', 'c', 'c', 'a'),
             ('a', 'b', 'a', 'a', 'b', 'c', 'a'),
             ('a', 'b', 'a', 'a', 'c', 'c', 'a'),
             ('a', 'b', 'c', 'd', 'b', 'c', 'a')]
        self.assertEqual(set(a_tuples),set(b))
    
    def test_cartesian_product_schema2(self):
        a = (self.rel5.cartesian_product(self.rel6)).relational_schema()
        b = ['A', 'R2_B', 'R2_C', 'D', 'S2_B', 'S2_C', 'E']
        
        self.assertEqual(a,b)
        
    def test_intersection(self):
        a = (self.r | self.s).tuples
        a_tuples = [tuple(t) for t in a]
        b = [(1, 1, 1), (0, 1, 0), (2, 3, 1), (1, 0, 1)]
        self.assertEqual(set(a_tuples), set(b))
        
    def test_union(self):
        a = (self.r & self.s).tuples
        a_tuples = [tuple(t) for t in a]
        b = [(2, 3, 1)]
        self.assertEqual(set(a_tuples), set(b))
        
    def test_difference(self):
        a = (self.r - self.s).tuples
        a_tuples = [tuple(t) for t in a]
        b = [(1, 1, 1), (0, 1, 0)]
        self.assertEqual(set(a_tuples), set(b))

    
unittest.main(argv=[''], verbosity=2, exit=False)