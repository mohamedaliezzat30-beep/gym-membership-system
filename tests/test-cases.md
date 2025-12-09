# Manual Test Cases – Gym Membership System

These tests were done by running the program using the menu in the terminal.

| Test No. | What I Tested | Input / Action | Expected Result | Actual Result | Status |
|----------|--------------|----------------|-----------------|---------------|--------|
| 1 | Empty system | View Members with no data | Show “No members yet” | Message shown | PASS |
| 2 | Add normal member | Add **Ali**, Type **Basic** | Member is added | Added successfully | PASS |
| 3 | Display members | View Members after adding | Ali should appear with an ID | Appears with ID | PASS |
| 4 | Search for existing member | Search “Ali” | System shows details | Found correctly | PASS |
| 5 | Search for missing member | Search “Unknown” | Show “Not found” | Message shown | PASS |
| 6 | Delete a member | Delete Ali using his ID | Member is removed | Deleted correctly | PASS |
| 7 | View after deleting | View members again | System empty message | Shown correctly | PASS |
| 8 | Sort members | Add Zed + Sara, then sort | Names ordered alphabetically | Sorted correctly | PASS |
| 9 | Wrong menu choice | Enter 10 or letter | Show error message | Error shown | PASS |
| 10 | Membership type | Choose Basic, Premium, VIP | Correct type saved | Works correctly | PASS |
| 11 | Many values | Add 20–50 random names | Program should still work | Works fine | PASS |


### Notes
- The program does not crash with empty or wrong input.
- Sorting is correct for small datasets.
- Search and deletion work properly because of dictionary storage.
