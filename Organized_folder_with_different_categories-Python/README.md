# File Organizer Script

A Python script that automatically organizes files in a directory into categorized folders based on file types.

## 📋 Description

This script helps you organize cluttered directories by automatically sorting files into appropriate folders based on their extensions. It's particularly useful for organizing download folders, desktop files, or any directory with mixed file types.

## 🚀 Features

- Automatically categorizes files into predefined categories
- Creates destination folders if they don't exist
- Handles files that don't match any category (places them in "others" folder)
- Prevents overwriting existing files
- Easy to customize with your own categories

## 📁 File Categories

The script organizes files into these categories:

| Category      | File Extensions                                   |
| ------------- | ------------------------------------------------- |
| **Images**    | .jpg, .png, .jpeg, .gif                           |
| **Videos**    | .mp4, .mkv                                        |
| **Music**     | .mp3, .wav                                        |
| **Archives**  | .zip, .tgz, .rar, .tar                            |
| **Documents** | .pdf, .docx, .csv, .xlsx, .pptx, .doc, .ppt, .xls |
| **Setups**    | .msi, .exe                                        |
| **Programs**  | .py, .c, .cpp, .php, .C, .CPP                     |
| **Design**    | .xd, .psd                                         |
| **Others**    | Any other extension                               |

## ⚙️ Requirements

- Python 3.x
- Standard Python libraries: `os`, `shutil`

## 📦 Installation

1. Download the script file: `file_organizer.py`
2. Save it to your desired location

## 🎯 Usage

1. Open the script in a text editor
2. Modify the directory path in the `os.chdir()` line to point to the folder you want to organize:

   ```python
   os.chdir(r"C:\path\to\your\folder")

   Run the script:
   python file_organizer.py
   ```

## 🔧 Customization

You can easily customize the categories by modifying the extentions dictionary in the script:

python
extentions = {
"images": [".jpg", ".png", ".jpeg", ".gif"],
"videos": [".mp4", ".mkv"], # Add your own categories and extensions here
}

## 📂 Folder Structure After Organization

After running the script, your files will be organized into this structure:

Your Folder/
├── sorted/
│ ├── images/
│ ├── videos/
│ ├── musics/
│ ├── zip/
│ ├── documents/
│ ├── setup/
│ ├── programs/
│ ├── design/
│ └── others/

⚠️ Important Notes
The script moves files rather than copying them

Always back up important files before running the script

Make sure you have appropriate permissions to modify files in the target directory

The script will skip files that already exist in the destination folders

## 🐛 Troubleshooting

If you encounter issues:

Check that the directory path is correct and accessible

Ensure you have write permissions in the target directory

Verify that Python is properly installed on your system

## Authon Name:

[Raul Dumitrele](https://github.com/Raul-Dumitrele)
