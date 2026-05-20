# terminal-based-snippet-manager
First time making non-game python codes :D
# DevDrop CLI

DevDrop CLI is a lightweight terminal-based code snippet manager built with Python.

Users can save, search, favorite, and manage code snippets directly from the command line.

---

## Features

- Save code snippets
- Search snippets by keyword
- View saved snippets
- Delete snippets
- Favorite important snippets
- Store data locally using JSON

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/devdrop-cli.git
cd devdrop-cli
```

Run the project:

```bash
python main.py
```

If `python` does not work, try:

```bash
python3 main.py
```

---

## Instructions

After starting the project, you will be asked to choose a number from `1-7`.

Each number corresponds to a function:

```text
1 -> Add a new snippet
2 -> List all saved snippets
3 -> View a specific snippet
4 -> Search snippets by keyword
5 -> Delete a snippet
6 -> Toggle favorite on/off
7 -> Exit the application
```

---

## Example

Example snippet:

```python
def hello():
    print("Hello World")
```

---

## Storage

All snippets are stored locally inside:

```text
snippets.json
```

---

## Future Improvements

- Syntax highlighting
- SQLite database support
- Terminal UI with Rich
- Cloud synchronization
- GitHub Gist integration

---

## License

MIT License
