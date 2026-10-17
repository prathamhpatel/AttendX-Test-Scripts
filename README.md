# AttendX-Test-Scripts

Sample automation test scripts for **AttendX**, the student attendance application.
The QA team keeps all test scripts in this repository instead of sharing them by e-mail or pen drive.

> **Note:** AttendX is a demo scenario. The base URL, element IDs and test data in these scripts are
> placeholders, and the scripts have not been run against a real application.

## Test scripts

| File | What it tests |
|------|---------------|
| `test_login.py` | Valid login, wrong password, empty username/password, masked password field |
| `test_mark_attendance.py` | Marking students Present/Absent and saving; saving without selecting a class |
| `conftest.py` | Shared setup used by both test files (browser fixture, base URL, login helper) |

## Team workflow

1. `git pull` before you start work.
2. Make your change, then `git add` + `git commit -m "<clear message>"`.
3. `git push` so the rest of the team gets it.

