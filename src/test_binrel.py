import unittest

from binrel import BinaryRelation

class TestBinaryRelation(unittest.TestCase):
    def setUp(self):
        self.r1 = BinaryRelation({(1, 2), (3, 4), (2, 3)})
        self.r2 = BinaryRelation({(2,4), (3,6), (1,2)})
        self.r3 = BinaryRelation({(1,2),(1,3)})
        
        self.r4 = BinaryRelation({(1,2),(2,3),(3,4)})
        self.r5 = BinaryRelation({(1,2),(2,3),(3,4),(1,8)})
        
        self.reflexiveRelation = BinaryRelation({(1,1),(2,2),(3,3)})
        self.ireflexiveRelation = BinaryRelation({(1,3),(2,4),(1,4)})
        self.symmetricRelation = BinaryRelation({(1,1),(2,1), (1,2)})
        self.transitiveRelation = BinaryRelation({(1,1),(2,2),(1,2),(2,1)})
        self.antisymmetricRelation = BinaryRelation({(1,1),(2,2),(1,3)})
        
        self.equivalenceRelation = BinaryRelation({(1,1), (2,2), (3,3), (1,2), (2,1)})
        self.patialOrder = BinaryRelation({(1,1), (2,2), (3,3), (1,2)})
    
    def test_converse(self):
        self.assertEqual(self.r1.converse(), BinaryRelation({(3, 2), (4, 3), (2, 1)})) 
        
    def test_add(self):
        self.assertEqual(self.r1 + self.r2, (BinaryRelation({(1, 2), (2, 3), (3, 6), (3, 4), (2, 4)})))
        
    def test_sub(self):
        self.assertEqual(self.r1 - self.r2, (BinaryRelation({(3, 4),(2, 3)})))
        
    def test_mul(self):
        self.assertEqual(self.r1 * self.r2, (BinaryRelation({(2, 6), (1, 4)})))
        
    def test_is_function1(self):
        self.assertTrue(self.r1.is_function())
        
    def test_is_function2(self):
        self.assertFalse(self.r3.is_function())
        
    def test_and(self):
        self.assertEqual(self.r1 & self.r2,BinaryRelation({(1, 2)}))
        
    def test_contains1(self):
        self.assertTrue((1,2) in self.r1)
        
    def test_contains2(self):
        self.assertFalse((1,8) in self.r1)
        
    def test_len(self):
        self.assertEqual(len(self.r1), 3)
        
    def test_eq1(self):
        self.assertTrue(self.r1 == self.r1)
        
    def test_eq2(self):
        self.assertFalse(self.r1 == self.r2)
        
    def test_ne1(self):
        self.assertTrue(self.r1 != self.r2)
        
    def test_ne1(self):
        self.assertFalse(self.r1 != self.r1)
        
    def test_lt1(self):
        self.assertTrue(self.r4 < self.r5)
        
    def test_lt2(self):
        self.assertFalse(self.r1 < self.r2)
    
    def test_lt2(self):
        self.assertFalse(self.r1 < self.r1)
        
    def test_gt1(self):
        self.assertTrue(self.r5 > self.r4)
        
    def test_gt2(self):
        self.assertFalse(self.r5 > self.r5)
        
    def test_gt3(self):
        self.assertFalse(self.r1 > self.r2)
    
    def test_le1(self):
        self.assertTrue(self.r1 <= self.r1)
        
    def test_le1(self):
        self.assertTrue(self.r4 <= self.r5)
 
    def test_le1(self):
        self.assertFalse(self.r1 <= self.r2)
        
    def test_ge1(self):
        self.assertTrue(self.r1 >= self.r1)
        
    def test_ge2(self):
        self.assertTrue(self.r5 >= self.r4)
        
    def test_ge3(self):
        self.assertFalse(self.r1 >= self.r2)
        
    def test_is_reflexive1(self):
        self.assertTrue(self.reflexiveRelation.is_reflexive())
        
    def test_is_reflexive2(self):
        self.assertFalse(self.r1.is_reflexive())
        
    def test_is_ireflexive1(self):
        self.assertTrue(self.ireflexiveRelation.is_ireflexive())
        
    def test_is_ireflexive2(self):
        self.assertFalse(self.reflexiveRelation.is_ireflexive())
        
    def test_is_symmetric1(self):
        self.assertTrue(self.symmetricRelation.is_symmetric())
        
    def test_is_symmetric2(self):
        self.assertFalse(self.r1.is_symmetric())
        
    def test_is_transitive1(self):
        self.assertTrue(self.transitiveRelation.is_transitive())
        
    def test_is_transitive2(self):
        self.assertFalse(self.r1.is_transitive())
        
    def test_is_antisymmetric1(self):
        self.assertTrue(self.antisymmetricRelation.is_antisymmetric())
        
    def test_is_antisymmetric2(self):
        self.assertFalse(self.symmetricRelation.is_antisymmetric())
        
    def test_is_equivalence_relation1(self):
        self.assertTrue(self.equivalenceRelation.is_equivalence_relation())
        
    def test_is_equivalence_relation2(self):
        self.assertFalse(self.r1.is_equivalence_relation())
        
    def test_is_partial_order1(self):
        self.assertTrue(self.patialOrder.is_partial_order())
    
    def test_is_partial_order2(self):
        self.assertFalse(self.equivalenceRelation.is_partial_order())
    
        
unittest.main(argv=[''], verbosity=2, exit=False)