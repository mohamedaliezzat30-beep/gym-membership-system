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

# menu system to run everything
def main():
    system = GymSystem()

    while True:
        print("\n-- gym menu --")
        print("1 - add member")
        print("2 - view members")
        print("3 - search member")
        print("4 - delete member")
        print("5 - sort members")
        print("6 - exit")

        choice = input("enter choice: ")

        if choice == "1":
            name = input("name: ")
            m_type = input("membership type: ")
            system.add_member(name, m_type)

        elif choice == "2":
            system.view_members()

        elif choice == "3":
            name = input("enter name: ")
            system.search_member(name)

        elif choice == "4":
            member_id = input("enter member id: ")
            system.delete_member(member_id)

        elif choice == "5":
            system.sort_members()

        elif choice == "6":
            print("bye")
            break

        else:
            print("wrong choice")


main()
