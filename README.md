# AttendX-Test-Scripts

Selenium + pytest automation scripts for **AttendX**, the student attendance application.
All QA engineers now share test scripts through this repository instead of e-mail / pen drives.

## Test scripts

| File | What it tests |
|------|---------------|
| `test_login.py` | Valid login, wrong password, empty username/password |
| `test_mark_attendance.py` | Marking students Present/Absent and saving; saving without selecting a class |
| `conftest.py` | Shared Chrome `driver` fixture and `login()` helper |

## How to run

```bash
pip install -r requirements.txt
export ATTENDX_URL=http://localhost:8080   # AttendX server under test
pytest -v
```

## Team workflow

1. `git pull` before you start work.
2. Make your change, then `git add` + `git commit -m "<clear message>"`.
3. `git push` so the rest of the team gets it.
