# Gym Membership System CW1

# Class to store each member's information
class Member:
    def __init__(self, member_id, name, m_type):
        self.member_id = member_id
        self.name = name
        self.m_type = m_type
        self.status = "Active"  # default status

# Main system class
class GymSystem:
    def __init__(self):
        self.members = {}  # dictionary to store members
        self.next_id = 1   # auto ID counter

    # Add new member
    def add_member(self, name, m_type):
        member_id = str(self.next_id).zfill(3)
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

    # Search by name
    def search_member(self, name):
        for m in self.members.values():
            if m.name.lower() == name.lower():
                print("Found:", m.member_id, m.name, m.m_type, m.status)
                return
        print("Not found")

    # Delete a member
    def delete_member(self, member_id):
        if member_id in self.members:
            del self.members[member_id]
            print("Member deleted")
        else:
            print("ID not found")

    # Sort members (very simple method)
    def sort_members(self):
        sorted_members = dict(sorted(self.members.items(), key=lambda item: item[1].name.lower()))
        self.members = sorted_members
        print("Members sorted by name")

# Let the user choose membership type
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
        print("Invalid choice, default = Basic")
        return "Basic"

# Main menu
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
if __name__ == "__main__":
    main()
