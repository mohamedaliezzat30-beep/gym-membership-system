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
    
    def add_member(self, name, m_type):
        mid = str(self.next_id).zfill(3)   # creates ID like 001
        self.members[mid] = Member(mid, name, m_type)
        self.next_id += 1
        print("added member:", name)

    def view_members(self):
        if len(self.members) == 0:
            print("no members yet")
        else:
            for m in self.members.values():
                print(m.member_id, m.name, m.m_type, m.status)
                
    def search_member(self, name):
        # find member by name
        for m in self.members.values():
            if m.name.lower() == name.lower():
                print("found:", m.member_id, m.name, m.m_type, m.status)
                return
        print("not found")
