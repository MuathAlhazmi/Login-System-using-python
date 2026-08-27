# Login System (Python)

**Written March 2019.** A console registration and login flow — one of my first
programs.

---

## Why this is here

Kept as a dated record, not as a showcase. **March 2019** is nearly four years
before ChatGPT (November 2022) and predates any AI coding assistance. It came
from a book, the Python docs, and getting it wrong repeatedly.

## What it does

Asks whether you are already registered. If you are, it checks your credentials
against `Login.txt`. If you are not, it collects your name, age, username and
password, writes the credentials to `Login.txt` and the personal details to
`Details.txt`, then confirms.

Roughly 30 lines: `input`, `if`/`else`, file reading and appending, and string
handling.

## The part I would still defend

The original README carried this warning, written at the time:

> *"This project should only be experemental and should not be used in a real
> website because it will store passwords as a plain text."*

Typo included. I did not know how to hash a password in 2019 — but I knew that
storing one in plaintext was wrong, and I said so in the README instead of
quietly shipping it. **Knowing the limits of what you have built, and writing
them down, is the habit worth keeping.**

The same instinct is why the projects I write now ship with a *Known weaknesses*
section.

## What is wrong with it, precisely

- **Passwords stored in plaintext.** The fix is `hashlib.scrypt` or `bcrypt`
  with a per-user salt, comparing digests rather than strings.
- **Credentials compared by exact line match**, so a comma in a username breaks
  the format entirely.
- **No input validation** — age accepts any string.
- **Files opened without context managers** in the registration branch, so a
  crash mid-write leaves the file open. The login branch does use `with`.
- Duplicate usernames are never checked.

## Running it

```bash
python3 Login.py
```

Do not type a real password into it.
