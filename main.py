# main.py

from books import new_testament
from progress import initialize_progress, load_progress, save_progress

print("========================================")
print("📖 New Testament Reading Tracker")
print("Made by Olin Paul Caraan")
print("========================================")

# Make sure progress.json exists when the app starts
initialize_progress()

def show_menu():
    print("\n📖 New Testament Reading Tracker")
    print("1. View progress")
    print("2. Mark a chapter as read")
    print("3. Unmark a chapter")
    print("4. Exit")
    print("5. Reset all progress")
    print("6. Show detailed chapters read")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    # Option 1: View progress
    if choice == "1":
        progress = load_progress()

        total_chapters = 0
        total_read = 0

        print("\n📚 Reading Progress:")

        for book, chapters in progress.items():
            read_count = sum(chapters)
            chapter_count = len(chapters)
            total_chapters += chapter_count
            total_read += read_count

            print(f"- {book}: {read_count}/{chapter_count} chapters read")

        percent = (total_read / total_chapters) * 100
        print(f"\n✅ Overall progress: {total_read}/{total_chapters} chapters read ({percent:.2f}%)")

    # Option 2: Mark a chapter as read
    elif choice == "2":
        progress = load_progress()

        print("\n📘 Books in the New Testament:\n")
        for i, book in enumerate(new_testament.keys(), 1):
            print(f"{i}. {book}")

        book_names = list(new_testament.keys())

        try:
            book_choice = int(input("\nEnter the number of the book: "))
            if book_choice < 1 or book_choice > len(book_names):
                print("❌ Invalid book number.")
                continue
            selected_book = book_names[book_choice - 1]
            chapter_count = len(progress[selected_book])
        except ValueError:
            print("❌ Please enter a valid number for the book.")
            continue

        try:
            chapter = int(input(f"Enter chapter number to mark as read (1 to {chapter_count}): "))
            if chapter < 1 or chapter > chapter_count:
                print("❌ Invalid chapter number.")
                continue

            if progress[selected_book][chapter - 1]:
                print("✅ That chapter is already marked as read.")
            else:
                progress[selected_book][chapter - 1] = True
                save_progress(progress)
                print(f"✅ Marked {selected_book} chapter {chapter} as read.")

        except ValueError:
            print("❌ Please enter a valid number for the chapter.")

    # Option 3: Unmark a chapter
    elif choice == "3":
        progress = load_progress()

        print("\n📕 Books in the New Testament:\n")
        for i, book in enumerate(new_testament.keys(), 1):
            print(f"{i}. {book}")

        book_names = list(new_testament.keys())

        try:
            book_choice = int(input("\nEnter the number of the book: "))
            if book_choice < 1 or book_choice > len(book_names):
                print("❌ Invalid book number.")
                continue
            selected_book = book_names[book_choice - 1]
            chapter_count = len(progress[selected_book])
        except ValueError:
            print("❌ Please enter a valid number for the book.")
            continue

        try:
            chapter = int(input(f"Enter chapter number to unmark (1 to {chapter_count}): "))
            if chapter < 1 or chapter > chapter_count:
                print("❌ Invalid chapter number.")
                continue

            if not progress[selected_book][chapter - 1]:
                print("ℹ️ That chapter is already not marked.")
            else:
                progress[selected_book][chapter - 1] = False
                save_progress(progress)
                print(f"🔁 Unmarked {selected_book} chapter {chapter} as unread.")

        except ValueError:
            print("❌ Please enter a valid number for the chapter.")

    # Option 4: Exit
    elif choice == "4":
        print("👋 Goodbye! Keep reading the Word!")
        break

    # Option 5: Reset all progress
    elif choice == "5":
        confirm = input("⚠️ This will reset all your reading progress. Type 'YES' to confirm: ")
        if confirm.strip().upper() == "YES":
            initialize_progress()
            print("🔄 All progress has been reset.")
        else:
            print("❌ Reset canceled.")

    # Option 6: Show detailed chapters read
    elif choice == "6":
        progress = load_progress()

        print("\n📑 Detailed Chapters Read:\n")
        for book, chapters in progress.items():
            read_chapters = [str(i + 1) for i, read in enumerate(chapters) if read]
            if read_chapters:
                chapters_str = ", ".join(read_chapters)
                print(f"- {book}: Chapters {chapters_str}")
            else:
                print(f"- {book}: No chapters read yet.")

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 6.")
