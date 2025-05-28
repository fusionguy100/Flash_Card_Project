🇫🇷 Flashy: French-English Flashcard App

Flashy is a simple, interactive flashcard app built with Python and Tkinter to help users learn French vocabulary efficiently using spaced repetition and self-assessment.
✨ Features

    🃏 Flip cards to see translations (French → English).

    ✅ Mark words as known to remove them from future sessions.

    🔁 Automatically saves progress in a CSV file.

    🧠 Shows a new flashcard every 3 seconds unless answered.

    💾 Handles missing files gracefully.

🖥️ GUI Preview

The app displays a front side of the flashcard with a French word, and flips to the English translation after 3 seconds.

Buttons:

    ✅ Known — Removes the current card from the learning list.

    ❌ Unknown — Keeps the word in the rotation and shows a new one.

📁 Folder Structure

Flashy/
├── data/
│   ├── french_words.csv          # Original vocabulary list (French + English)
│   └── words_to_learn.csv        # Progress-tracking file (auto-generated)
├── images/
│   ├── card_front.png            # Image for front of flashcard
│   ├── card_back.png             # Image for back of flashcard
│   ├── right.png                 # Checkmark icon
│   └── wrong.png                 # X icon
└── main.py                       # Main Python file

🛠️ Requirements

    Python 3.x

    pandas

    tkinter (included in standard Python library)

📦 How to Run

    Clone or download this repository.

    Ensure you have pandas installed:

pip install pandas

Make sure the images and data folders are in the same directory as main.py.

Run the app:

    python main.py

🧠 How It Works

    On first launch, it loads french_words.csv from /data.

    If words_to_learn.csv exists, it resumes where you left off.

    The flashcard flips to the English side after 3 seconds.

    Press ✅ to remove the word from your study list.

    The updated list is saved back to words_to_learn.csv.

📌 Notes

    To restart your learning progress, simply delete words_to_learn.csv.

    This app can be extended to support other languages by modifying the CSV data.
