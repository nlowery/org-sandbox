from organism import Organism
import unittest
import settings

class OrganismTests(unittest.TestCase):

    def setUp(self):
        self.org = Organism(id=1)

    def test_organism_init(self):
        self.assertGreaterEqual(self.org.pos_x, 0)
        self.assertGreaterEqual(self.org.pos_y, 0)
        self.assertEqual(self.org.age, 0)
        self.assertEqual(self.org.distance_from_food, 0)
        self.assertEqual(self.org.energy, settings.STARTING_ENERGY)
        self.assertNotEqual(self.org.brain, None)

    def test_organism_move(self):
        pos_x = self.org.pos_x
        pos_y = self.org.pos_y
        self.org.move(5,5)
        self.assertEqual(pos_x, self.org.pos_x-5)
        self.assertEqual(pos_y, self.org.pos_y-5)

    def test_organism_brain(self):
        self.assertNotEqual(self.org.brain.process_input([0,0,0,0,0,0,0,0,0]), (0,0))
        self.assertNotEqual(self.org.brain.process_input([0,1,0,1,0,1,0,1,0]), (0,0))
        self.assertNotEqual(self.org.brain.process_input([1,1,1,1,1,1,1,1,1]), (0,0))