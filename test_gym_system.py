import unittest
from src.gym_membership import GymSystem

class TestGymSystem(unittest.TestCase):

    def test_empty_start(self):
        system = GymSystem()
        self.assertEqual(len(system.members), 0)

    def test_add_member(self):
        system = GymSystem()
        system.add_member("Ali", "Basic")
        self.assertEqual(len(system.members), 1)

    def test_search_member(self):
        system = GymSystem()
        system.add_member("Ali", "Basic")
        found = False
        for m in system.members.values():
            if m.name == "Ali":
                found = True
        self.assertTrue(found)

    def test_delete_member(self):
        system = GymSystem()
        system.add_member("Ali", "Basic")
        member_id = list(system.members.keys())[0]
        system.delete_member(member_id)
        self.assertEqual(len(system.members), 0)

if __name__ == "__main__":
    unittest.main()
