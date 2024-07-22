import shutil
import os

source_folder = r"G:\\Musikvideos"
destination_folder = r"D:\Musikvideos"

source_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
destination_files = [f for f in os.listdir(destination_folder) if os.path.isfile(os.path.join(destination_folder, f))]

print(f"Quelldateien: {source_files}")
print(f"Zieldateien: {destination_files}")

for file in source_files:
    src = os.path.join(source_folder, file)
    dst = os.path.join(destination_folder, file)
    if os.path.isfile(src):
        if file not in destination_files:
            try:
                shutil.copy2(src, dst)
            except PermissionError as e:
                print(f"Permission denied: {e}")
            except Exception as e:
                print(f"Error occurred: {e}")
