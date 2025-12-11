# Gym Membership System CW1

# Class to store information about each member
class Member:
    def __init__(self, member_id, name, m_type):
        self.member_id = member_id
        self.name = name
        self.m_type = m_type
        self.status = "Active"    # default status for everyone


# Main system class that controls everything
class GymSystem:
    def __init__(self):
        self.members = {}   # I am using a dictionary to store members
        self.next_id = 1    # This is for creating auto IDs like 001, 002...

    # Add a new member
    def add_member(self, name, m_type):
        member_id = str(self.next_id).zfill(3)   # makes 3-digit ID
        self.members[member_id] = Member(member_id, name, m_type)
        self.next_id += 1
        print("Member added:", name)

    # View all members
    def view_members(self):
        if len(self.members) == 0:
            print("No members yet")
        else:
            for m in self.members.values():
                print(m.member_id, m.name, m.m_type, m.status)

    # Search for a member by name (linear search)
    def search_member(self, name):
        for m in self.members.values():
            if m.name.lower() == name.lower():
                print("Found:", m.member_id, m.name, m.m_type, m.status)
                return
        print("Not found")

    # Delete a member using ID
    def delete_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print("Member deleted")
        else:
            print("ID not found")

    # Sort members by name using Bubble Sort
    def sort_members(self):
        if len(self.members) <= 1:
            print("Not enough members to sort")
            return

        # get list of the IDs so we can swap them
        keys = list(self.members.keys())

        # Bubble Sort (simple version)
        for i in range(len(keys)):
            for j in range(len(keys) - 1):
                name1 = self.members[keys[j]].name.lower()
                name2 = self.members[keys[j + 1]].name.lower()

                if name1 > name2:   # if wrong order, swap them
                    keys[j], keys[j + 1] = keys[j + 1], keys[j]

        # Make a new dictionary in this sorted order
        sorted_members = {}
        for k in keys:
            sorted_members[k] = self.members[k]

        self.members = sorted_members
        print("Members sorted by name")


# Function to choose membership type
def choose_membership_type():
    print("Choose membership type:")
    print("1 - Basic")
    print("2 - Premium")
    print("3 - VIP")
    choice = input("Enter choice: ")

    if choice == "1":
        return "Basic"
    elif choice == "2":
        return "Premium"
    elif choice == "3":
        return "VIP"
    else:
        print("Invalid choice, defaulting to Basic")
        return "Basic"


# Main menu loop
def main():
    system = GymSystem()

    while True:
        print("\n--- GYM MENU ---")
        print("1 - Add member")
        print("2 - View members")
        print("3 - Search member")
        print("4 - Delete member")
        print("5 - Sort members")
        print("6 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            m_type = choose_membership_type()
            system.add_member(name, m_type)

        elif choice == "2":
            system.view_members()

        elif choice == "3":
            name = input("Enter name to search: ")
            system.search_member(name)

        elif choice == "4":
            member_id = input("Enter ID to delete: ")
            system.delete_member(member_id)

        elif choice == "5":
            system.sort_members()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again")


# Run the program
main()
