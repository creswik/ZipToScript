import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import os
import json
from pathlib import Path

class ZipProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zip Processor App")
        
        self.label = tk.Label(root, text="Select a Zip File to Process:")
        self.label.pack(pady=10)
        
        self.button = tk.Button(root, text="Browse", command=self.browse_file)
        self.button.pack(pady=10)
        
        self.process_button = tk.Button(root, text="Process", command=self.process_zip, state=tk.DISABLED)
        self.process_button.pack(pady=10)
        
        self.file_path = ""
    
    def browse_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
        if self.file_path:
            self.label.config(text=f"Selected: {self.file_path}")
            self.process_button.config(state=tk.NORMAL)
    
    def process_zip(self):
        if not self.file_path:
            messagebox.showerror("Error", "No zip file selected.")
            return
        
        extract_dir = os.path.splitext(self.file_path)[0]
        os.makedirs(extract_dir, exist_ok=True)
        
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        
        root_files, dirs = self.list_files_and_dirs(extract_dir)
        
        # Create file structure JSON
        file_structure = self.generate_file_structure(extract_dir)
        file_structure_path = os.path.join(extract_dir, 'file_structure.json')
        with open(file_structure_path, 'w', encoding='utf-8') as f:
            json.dump(file_structure, f, ensure_ascii=False, indent=4)
        
        # Create content JSON files
        self.create_content_jsons(extract_dir, root_files, dirs)
        
        messagebox.showinfo("Success", f"Files processed and JSONs created in {extract_dir}")
    
    def list_files_and_dirs(self, directory):
        root_files = []
        dirs = []
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)):
                root_files.append(item)
            else:
                dirs.append(item)
        return root_files, dirs
    
    def generate_file_structure(self, directory):
        file_structure = {}
        for root, dirs, files in os.walk(directory):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                parts = relative_path.split(os.sep)
                d = file_structure
                for part in parts[:-1]:
                    d = d.setdefault(part, {})
                d[parts[-1]] = None
        return file_structure
    
    def create_content_jsons(self, base_dir, root_files, dirs):
        all_files = root_files + [os.path.join(d, f) for d in dirs for f in os.listdir(os.path.join(base_dir, d))]
        chunk_size = 175
        
        # Create JSON for root files
        for i in range(0, len(root_files), chunk_size):
            chunk = root_files[i:i+chunk_size]
            root_json = {file: self.read_file(os.path.join(base_dir, file)) for file in chunk}
            root_json_path = os.path.join(base_dir, f'root_{i//chunk_size + 1}.json')
            with open(root_json_path, 'w', encoding='utf-8') as f:
                json.dump(root_json, f, ensure_ascii=False, indent=4)
        
        # Create JSON for directory files
        for directory in dirs:
            dir_path = os.path.join(base_dir, directory)
            dir_files = os.listdir(dir_path)
            for i in range(0, len(dir_files), chunk_size):
                chunk = dir_files[i:i+chunk_size]
                dir_json = {file: self.read_file(os.path.join(dir_path, file)) for file in chunk}
                dir_json_path = os.path.join(base_dir, f'{directory}_{i//chunk_size + 1}.json')
                with open(dir_json_path, 'w', encoding='utf-8') as f:
                    json.dump(dir_json, f, ensure_ascii=False, indent=4)
    
    def read_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return "Error reading file"

if __name__ == "__main__":
    root = tk.Tk()
    app = ZipProcessorApp(root)
    root.mainloop()
