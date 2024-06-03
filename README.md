### README for ZipProcessorApp

---

## ZipProcessorApp

ZipProcessorApp is a GUI application built with Python and Tkinter that processes zip files to generate a file structure JSON and content JSON files. The application extracts files from a zip archive, creates a JSON representation of the file structure, and splits the contents into multiple JSON files if necessary.

### Features
- Extract zip files and create a JSON representation of the file structure.
- Split file contents into multiple JSON files with a maximum of 175 files each.
- User-friendly GUI built with Tkinter.
- Create standalone executables for both macOS and Windows.

### Table of Contents
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
  - [Windows](#windows)
  - [macOS](#macos)
- [Creating Standalone Executables](#creating-standalone-executables)
  - [Windows](#creating-standalone-executables-windows)
  - [macOS](#creating-standalone-executables-macos)
- [Usage](#usage)
- [Example Project Structure](#example-project-structure)
- [License](#license)

### Requirements
- Python 3.x
- Tkinter
- PyInstaller
- Pillow (for image conversion on macOS)

### Setup Instructions

#### Windows

1. **Download and Install Python**:
   - Download Python from the [official website](https://www.python.org/downloads/).
   - Ensure you select "Add Python to PATH" during installation.

2. **Install Required Python Packages**:
   ```sh
   pip install pyinstaller
   ```

#### macOS

1. **Install Homebrew**:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install Python and Tkinter**:
   ```sh
   brew install python-tk
   ```

3. **Install pyenv**:
   ```sh
   curl https://pyenv.run | bash
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
   echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
   echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
   echo 'eval "$(pyenv init -)"' >> ~/.zshrc
   echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
   source ~/.zshrc
   ```

4. **Install Python with Tkinter Support**:
   ```sh
   env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.12.3
   pyenv global 3.12.3
   ```

5. **Install Required Python Packages**:
   ```sh
   pip install pyinstaller pillow
   ```

### Creating Standalone Executables

#### Windows

1. **Prepare the Project**:
   Ensure your project folder contains the script and an icon file (if desired).
   ```
   project-folder/
   ├── zip_processor_app.py
   └── icon.ico
   ```

2. **Create the Executable**:
   ```sh
   pyinstaller --name ZipProcessorApp --onefile --windowed --icon=icon.ico zip_processor_app.py
   ```

#### macOS

1. **Prepare the Project**:
   Ensure your project folder contains the script and an icon file (if desired).
   ```
   project-folder/
   ├── zip_processor_app.py
   └── icon.ico
   ```

2. **Create the Executable**:
   ```sh
   pyinstaller --name ZipProcessorApp --onefile --windowed --icon=icon.ico zip_processor_app.py
   ```

### Usage

1. **Open the Application**:
   Run the executable (`ZipProcessorApp` on macOS or `ZipProcessorApp.exe` on Windows).

2. **Select a Zip File**:
   Click the "Browse" button to select a zip file for processing.

3. **Process the Zip File**:
   Click the "Process" button to extract the zip file and generate the JSON files.

4. **View Results**:
   The JSON files will be created in the same directory as the extracted files.

### Example Project Structure

```
project-folder/
├── zip_processor_app.py
├── icon.ico  # Icon for macOS and Windows
```

### License

Permission is hereby granted, free of charge, to any person obtaining a copy of this Python script and associated documentation files (the "Script"), to deal in the Script without restriction, including without limitation the rights to use, copy, modify, merge, publish, and distribute the Script, and to permit persons to whom the Script is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Script.

The Script shall not be used, modified, merged, published, distributed, or sublicensed for any commercial purpose without the express permission of the copyright holder. This includes selling copies of the Script or offering paid services utilizing the Script.

THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SCRIPT OR THE USE OR OTHER DEALINGS IN THE SCRIPT.

