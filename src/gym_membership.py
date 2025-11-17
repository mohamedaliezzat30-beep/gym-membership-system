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

    def delete_member(self, member_id):
        # delete a member by id
        if member_id in self.members:
            del self.members[member_id]
            print("member deleted")
        else:
            print("id not found")

    def sort_members(self):
        # bubble sort by name
        keys = list(self.members.keys())

        # basic bubble sort
        for i in range(len(keys)):
            for j in range(len(keys) - 1):
                if self.members[keys[j]].name.lower() > self.members[keys[j+1]].name.lower():
                    keys[j], keys[j+1] = keys[j+1], keys[j]

        # rebuild dictionary in sorted order
        sorted_members = {}
        for k in keys:
            sorted_members[k] = self.members[k]

        self.members = sorted_members
        print("members sorted by name")

