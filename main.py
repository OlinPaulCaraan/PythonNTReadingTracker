# main.py

from books import new_testament
from progress import initialize_progress, load_progress, save_progress

print("========================================")
print("📖 New Testament Reading Tracker")
print("Made by Olin Paul Caraan")
print("========================================")

# make sure progress.json exists when the app starts
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

        # count how many chapters are in the New Testament total, and how many you've read
        total_chapters = 0
        total_read = 0

        print("\n📚 Reading Progress:")

        # goes through each book and its list of chapters.
        for book, chapters in progress.items():
            read_count = sum(chapters) # counts how many True values are in the list.
            chapter_count = len(chapters) # counts how many total chapters the book has.
            total_chapters += chapter_count # Adds this book’s chapter count to the total.
            total_read += read_count # Adds how many chapters you’ve read in this book to the total read

            # shows progress for the current book
            print(f"- {book}: {read_count}/{chapter_count} chapters read")

        # calculate overall percentage
        # (total_read / total_chapters) * 100 = your progress in percentage.
        # :.2f means "show only 2 decimal places"
        percent = (total_read / total_chapters) * 100
        print(f"\n✅ Overall progress: {total_read}/{total_chapters} chapters read ({percent:.2f}%)")

    # Option 2: Mark a chapter as read
    elif choice == "2":
        # Reads your current reading status from file
        progress = load_progress()

        # Show list of New Testament books (It loops through all books in your new_testament dictionary)
        print("\n📘 Books in the New Testament:\n")
        for i, book in enumerate(new_testament.keys(), 1): # enumerate(..., 1) gives you a number starting at 1 for each book
            print(f"{i}. {book}")

        # Prepare a list of book names
        book_names = list(new_testament.keys())

        # Ask user to choose a book
        try:
            book_choice = int(input("\nEnter the number of the book: "))
            if book_choice < 1 or book_choice > len(book_names): # This checks if the user's number is outside the valid range (like 0 or 100)
                print("❌ Invalid book number.")
                continue
            selected_book = book_names[book_choice - 1] # Save the selected book
            chapter_count = len(progress[selected_book]) # chapter_count is how many chapters that book has
        except ValueError: # If the user typed something that can’t be turned into a number, this handles the error 
            print("❌ Please enter a valid number for the book.")
            continue

        try:
            chapter = int(input(f"Enter chapter number to mark as read (1 to {chapter_count}): ")) # Prompts the user to enter a chapter number for the selected book
            if chapter < 1 or chapter > chapter_count: # Makes sure the number is valid for that book
                print("❌ Invalid chapter number.")
                continue

            # Check if chapter is already marked
            if progress[selected_book][chapter - 1]:
                print("✅ That chapter is already marked as read.")
            # Mark as read and save
            else:
                progress[selected_book][chapter - 1] = True
                save_progress(progress)
                print(f"✅ Marked {selected_book} chapter {chapter} as read.")

        # Handles errors like typing text instead of a number
        except ValueError:
            print("❌ Please enter a valid number for the chapter.")

    # Option 3: Unmark a chapter
    elif choice == "3":
        progress = load_progress()

        # Show list of books. This displays the numbered list of New Testament books
        print("\n📕 Books in the New Testament:\n")
        for i, book in enumerate(new_testament.keys(), 1):
            print(f"{i}. {book}")

        book_names = list(new_testament.keys())

        # Ask the user to choose a book
        try:
            book_choice = int(input("\nEnter the number of the book: "))
            if book_choice < 1 or book_choice > len(book_names):
                print("❌ Invalid book number.")
                continue
            selected_book = book_names[book_choice - 1]
            chapter_count = len(progress[selected_book])

        # If the user types letters or an invalid number, this prevents the program from crashing
        except ValueError:
            print("❌ Please enter a valid number for the book.")
            continue

        # Ask for the chapter to unmark
        try:
            chapter = int(input(f"Enter chapter number to unmark (1 to {chapter_count}): "))
            if chapter < 1 or chapter > chapter_count:
                print("❌ Invalid chapter number.")
                continue

            # Check if it's already unread
            if not progress[selected_book][chapter - 1]:
                print("ℹ️ That chapter is already not marked.")

            # Sets that chapter to False (meaning "not read")
            else:
                progress[selected_book][chapter - 1] = False
                save_progress(progress)
                print(f"🔁 Unmarked {selected_book} chapter {chapter} as unread.")

        # Catches problems like if the user typed letters or special characters instead of a number
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
        progress = load_progress() # 	Loads saved progress from JSON file

        print("\n📑 Detailed Chapters Read:\n")
        for book, chapters in progress.items(): # This goes through every book in your progress
            read_chapters = [str(i + 1) for i, read in enumerate(chapters) if read]
            # Filters only the chapters marked as read. It is for the list of chapter numbers that have been read. If you’ve read something in that book, show the chapter numbers.
            if read_chapters:
                chapters_str = ", ".join(read_chapters)
                print(f"- {book}: Chapters {chapters_str}")
            else:
                # If not, say: "No chapters read yet."
                print(f"- {book}: No chapters read yet.")

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 6.")
