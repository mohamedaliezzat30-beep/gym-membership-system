# Manual Test Cases – Gym Membership System

These are my own manual tests done by running the program from the menu.

| Test No. | Action / Input | Expected Result | Actual Result | Status |
|----------|----------------|----------------|---------------|--------|
| 1 | Start program and choose **View members** with no data | System shows “No members yet” | Shows message | PASS |
| 2 | Add member: Name: Ali, Type: Basic | Member should be added and message shown | Member added | PASS |
| 3 | View members after adding Ali | Ali should appear in the list with ID | Ali displayed in list | PASS |
| 4 | Search for **Ali** | System should show Ali’s details | Details shown | PASS |
| 5 | Search for **Unknown Name** | System should show “Not found” | Shows “Not found” | PASS |
| 6 | Delete member using Ali’s ID | Member should be deleted | Member deleted | PASS |
| 7 | View members after deleting | List should be empty again | Shows “No members yet” | PASS |
| 8 | Add multiple members then choose **Sort members** | List should appear in alphabetical order | Sorted correctly | PASS |
| 9 | Enter wrong menu value (e.g. 10) | System should display error message | Shows “Invalid choice” | PASS |
| 10 | Choose membership type (Basic/Premium/VIP) | System should store correct type | Type saved correctly | PASS |
