import os
import shutil
from pathlib import Path

def orginize_folder(folder_path:str):
    extensions ={
        "Images":[".jpg",".jpeg",".png",".gif"],
        "Documents":[".pdf",".docx",".txt",".csv"],
        "Videos":[".mp4",".avi"],
        "Music":[".mp3",".wav"],
        "Executables":[".exe",".msi"],
        "Others":[]
    }
    folder=Path(folder_path)
    for file in folder.iterdir():
        if file.is_file():
            moved = False
            for category, exts in extensions.items():
                if file.suffix.lower() in exts:
                    target = folder/category
                    target.mkdir(exist_ok=True)
                    shutil.move(str(file),str(target/file.name))
                    moved = True
                    break
            if not moved:
                target = folder / "others"
                target.mkdir(exist_ok=True)
                shutil.move(str(file),str(target/file.name))
if __name__ == "__main__":
    path= str(input("type the folde path to organize: "))
    orginize_folder(path)
    print("Files organized.")