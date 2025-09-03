import os
import pandas as pd

# Path to the parent directory containing all folders
base_path = "C:/Users/moham/datasets/kaggle/fake-or-real-the-impostor-hunt/data/test"

data = []
# os.listdir() returns a list of all files and directories in the specified path
# os.path.join() join n no of pathts as arguments e.g., ("C:/Users", "Vikaas", "Documents")
# os.path.isdir(path) gives True if path is a directory else False

# Loop through all folder
for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        text_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
        if len(text_files) == 2:
            file1_path = os.path.join(folder_path, text_files[0])
            file2_path = os.path.join(folder_path, text_files[1])
            with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
                text1 = f1.read().strip()  # f1.read() reads from where the pointer is till the end to move pointer to start use f1.seek(0)
                text2 = f2.read().strip()
                
                data.append({
                    "folder_name": folder,
                    "article_a_text": text1,
                    "article_b_text": text2
                })
        else:
            print(f"Skipping {folder}: expected 2 .txt files, found {len(text_files)}")

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("test_article_pairs2.csv", index=False)
print("CSV file created: article_in_csv2.csv")
