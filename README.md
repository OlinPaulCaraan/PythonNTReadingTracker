# New Testament Reading Tracker by Olin Paul Caraan

---

### Description:

This is a simple command-line app built with Python that helps users track their progress as they read through the New Testament books of the Bible. It is designed to be lightweight, beginner-friendly, and functional without requiring any installation of Python on the user's machine. The app is compiled into a standalone executable for easy use.

---

### Main Features:

1. **Read and Track Chapters**
   Users can mark individual chapters as "read" from any New Testament book.

2. **Check Reading Progress**
   The app shows your current progress as a percentage, displaying how much of the New Testament you have read.

3. **View Specific Chapters Read**
   Users can view a list of all chapters they have already completed, book by book.

4. **Reset Reading Tracker**
   Users can clear all progress and start from scratch if they choose.

5. **Exit Option**
   Cleanly exits the application without saving any changes beyond what is already recorded.

---

### 📁 Technical Details:

* **Language:** Python 3.12
* **User Interface:** Command-line only (no graphical interface)
* **Storage:** The app uses a JSON file (`progress.json`) to save and load reading progress.
* **Language Support:** Book names are displayed in **Tagalog** for familiarity and accessibility to Filipino readers.
* **Standalone Build:** Packaged into a single `.exe` file using PyInstaller, which allows it to run on any Windows system without requiring Python installation.

---

### How to Use:

✅ Step 1: Open the App
Double-click the file main.exe inside the dist folder.

A black window (Command Prompt) will open with a welcome message.

✅ Step 2: Choose an Option
You'll see a menu like this:

```
New Testament Reading Tracker by Olin Paul Caraan

1. Mark a chapter as read  
2. Show reading progress  
3. View chapters read  
4. Reset reading progress  
5. Exit  
Enter your choice (1-5):
Type a number (1 to 5) and press Enter to choose what you want to do.
```

📖 Option 1: Mark a chapter as read
You will see a list of New Testament books in Tagalog.

Type the number of the book you want (for example, 1 for Mateo) and press Enter.

It will ask you to enter the chapter number you read. Type it (for example, 5) and press Enter.

The app will save it as "read" in the background.

📊 Option 2: Show reading progress
This will calculate the total number of chapters you have read and display your percentage.

For example, it might say: You have read 27 out of 260 chapters. Progress: 10.38%

📚 Option 3: View chapters read
Choose this to see a list of which chapters you already marked as read, organized by book.

If you read Juan chapter 1 and 3, it might show:

```
Juan: [1, 3]
```
🔄 Option 4: Reset reading progress
This will delete all saved progress.

It will ask: Are you sure you want to reset your progress? (y/n)

Type y to confirm, or n to cancel.

❌ Option 5: Exit
This will close the app.

💾 Where your progress is saved
A file named progress.json is automatically created in the same folder.

This file keeps track of your read chapters, so even after closing the app, your progress is saved.
