# Test Cases for Gym Membership System

## normal tests
| test | input | expected result | status |
|------|--------|-----------------|---------|
| add member | name: ali, type: basic | member added | pass |
| view members | - | shows list | pass |
| search member | name: ali | shows ali | pass |
| delete member | id: 001 | removed message | pass |
| sort members | - | sorted list printed | pass |

## edge tests
| test | input | expected result | status |
|------|--------|-----------------|---------|
| view when empty | none | "no members yet" | pass |
| search missing person | "unknown" | "not found" | pass |
| delete wrong id | 999 | "id not found" | pass |
| large list | 100+ names | still works slow but ok | pass |
