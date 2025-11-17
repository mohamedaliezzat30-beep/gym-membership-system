# Gym Membership System CW1 start

# Member class, to store member details

class Member:
    def __init__(self, member_id, name, m_type):
        self.member_id = member_id
        self.name = name
        self.m_type = m_type
        self.status = "Active"   # default status


class GymSystem:
    def __init__(self):
        self.members = {}   # That's gonna store members here later
        self.next_id = 1    # That's for auto IDs
