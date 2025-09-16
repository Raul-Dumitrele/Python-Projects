# Python String Prefix Example

This project demonstrates the difference between `lstrip()` and `removeprefix()` when working with strings that have a common prefix like `www.`.

## Code Example

```python
links = {
     "www.chatgpt.ro",
     "www.facebook.com",
     "www.youtube.com",
     "www.wikipedia.com",
}

for link in links:
    print(link.lstrip("www."))
    # lstrip removes all characters in the set "w", ".", until it finds a different one.
    # This may result in "ikipedia.com" for "www.wikipedia.com".

    print(link.removeprefix("www."))
    # removeprefix removes exactly the specified prefix ("www.") if it exists.
```

## Key Points
- **`lstrip("www.")`** removes all leading `w` and `.` characters until a different character is found.
- **`removeprefix("www.")`** removes exactly the prefix `"www."` only if it's present.

### Example Output

For `www.wikipedia.com`:

- **Using `lstrip("www.")`** → `ikipedia.com` (may be missing letters)
- **Using `removeprefix("www.")`** → `wikipedia.com` (correct result)
