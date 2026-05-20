# DevDrop CLI — A Terminal Snippet Manager
# Upload this as a clean beginner/intermediate Python project.
# Features:
# - Save snippets
# - Search snippets
# - Delete snippets
# - Favorites system
# - JSON storage
#
# Instructions:
# After starting the project, you will be asked to choose
# a number from 1-7. Each number corresponds to a function:
#
# 1 -> Add a new snippet
# 2 -> List all saved snippets
# 3 -> View a specific snippet
# 4 -> Search snippets by keyword
# 5 -> Delete a snippet
# 6 -> Toggle favorite on/off
# 7 -> Exit the application

import json
import os
from datetime import datetime

FILE_NAME = "snippets.json"


def load_snippets():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)



def save_snippets(snippets):
    with open(FILE_NAME, "w") as file:
        json.dump(snippets, file, indent=4)



def add_snippet(snippets):
    title = input("Snippet title: ")
    language = input("Language: ")
    tags = input("Tags (comma separated): ").split(",")

    print("Enter your code. Type END on a new line to finish:\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)

    code = "\n".join(lines)

    snippet = {
        "id": len(snippets) + 1,
        "title": title,
        "language": language,
        "tags": [tag.strip() for tag in tags],
        "code": code,
        "favorite": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    snippets.append(snippet)
    save_snippets(snippets)

    print("\nSnippet saved successfully.\n")



def list_snippets(snippets):
    if not snippets:
        print("\nNo snippets found.\n")
        return

    print("\nYour Snippets:\n")

    for snippet in snippets:
        star = "⭐" if snippet["favorite"] else ""

        print(f"[{snippet['id']}] {snippet['title']} {star}")
        print(f"Language: {snippet['language']}")
        print(f"Tags: {', '.join(snippet['tags'])}")
        print(f"Created: {snippet['created_at']}")
        print("-" * 50)



def view_snippet(snippets):
    snippet_id = input("Enter snippet ID: ")

    for snippet in snippets:
        if str(snippet["id"]) == snippet_id:
            print(f"\nTitle: {snippet['title']}")
            print(f"Language: {snippet['language']}")
            print(f"Tags: {', '.join(snippet['tags'])}")
            print("\nCode:\n")
            print(snippet["code"])
            print()
            return

    print("Snippet not found.\n")



def search_snippets(snippets):
    keyword = input("Search keyword: ").lower()

    results = []

    for snippet in snippets:
        if (
            keyword in snippet["title"].lower()
            or keyword in snippet["language"].lower()
            or any(keyword in tag.lower() for tag in snippet["tags"])
        ):
            results.append(snippet)

    if not results:
        print("\nNo matching snippets found.\n")
        return

    print("\nSearch Results:\n")

    for snippet in results:
        print(f"[{snippet['id']}] {snippet['title']} ({snippet['language']})")

    print()



def delete_snippet(snippets):
    snippet_id = input("Enter snippet ID to delete: ")

    for snippet in snippets:
        if str(snippet["id"]) == snippet_id:
            snippets.remove(snippet)
            save_snippets(snippets)
            print("Snippet deleted.\n")
            return

    print("Snippet not found.\n")



def toggle_favorite(snippets):
    snippet_id = input("Enter snippet ID: ")

    for snippet in snippets:
        if str(snippet["id"]) == snippet_id:
            snippet["favorite"] = not snippet["favorite"]
            save_snippets(snippets)

            status = "favorited" if snippet["favorite"] else "unfavorited"
            print(f"Snippet {status}.\n")
            return

    print("Snippet not found.\n")



def menu():
    snippets = load_snippets()

    print("""
Instructions:
After starting the project, choose a number from 1-7.
Each number corresponds to a function:

1 -> Add a new snippet
2 -> List all saved snippets
3 -> View a specific snippet
4 -> Search snippets by keyword
5 -> Delete a snippet
6 -> Toggle favorite on/off
7 -> Exit the application
""")

    while True:
        print("=" * 50)
        print(" DevDrop CLI ")
        print("=" * 50)
        print("1. Add snippet")
        print("2. List snippets")
        print("3. View snippet")
        print("4. Search snippets")
        print("5. Delete snippet")
        print("6. Toggle favorite")
        print("7. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            add_snippet(snippets)
        elif choice == "2":
            list_snippets(snippets)
        elif choice == "3":
            view_snippet(snippets)
        elif choice == "4":
            search_snippets(snippets)
        elif choice == "5":
            delete_snippet(snippets)
        elif choice == "6":
            toggle_favorite(snippets)
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    menu()
