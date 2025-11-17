# Gym Membership System CW1 start

# Member class, to store member details
class Member: 
    def __init__(self, member_id, name, m_type):
        self.member_id = member_id   # save the ID number
        self.name = name   # save name
        self.m_type = m_type   # save membership type
        self.status = "Active"  # default status (Active)

# main system class (controls everything), and tracks all members
class GymSystem:
    def __init__(self):
        self.members = {}   # That's gonna store members here later
        self.next_id = 1    # That's for auto IDs

    # add a new member
    def add_member(self, name, m_type):
        mid = str(self.next_id).zfill(3)   # creates ID like 001
        self.members[mid] = Member(mid, name, m_type)  # Save member
        self.next_id += 1    # increase next ID number for the next new member
        print("added member:", name)

    # show all members
    def view_members(self):
        if len(self.members) == 0:
            print("no members yet")
        else:
            for m in self.members.values():  # loop through everyone
                print(m.member_id, m.name, m.m_type, m.status)

    # search member by name (check one by one)
    def search_member(self, name):
        # find member by name
        for m in self.members.values():
            if m.name.lower() == name.lower():  # match name
                print("found:", m.member_id, m.name, m.m_type, m.status)
                return
        print("not found")


    # delete member using ID
    def delete_member(self, member_id):
        # delete a member by id
        if member_id in self.members:
            del self.members[member_id]  # remove
            print("member deleted")
        else:
            print("id not found")


    # sort members alphabetically by name (Bubble Sort)
    def sort_members(self):
        # bubble sort by name
        keys = list(self.members.keys())   # get the IDs


        # bubble sort loop
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
    system = GymSystem()  # make system object

    # loop forever until exit
    while True:
        print("\n-- gym menu --")
        print("1 - add member")
        print("2 - view members")
        print("3 - search member")
        print("4 - delete member")
        print("5 - sort members")
        print("6 - exit")

        choice = input("enter choice: ") # ask user to choose one option

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
            print("See yaaa")  # exit program
            break

        else:
            print("wrong choice mate, go again") # wrong input


main() # Run the program
