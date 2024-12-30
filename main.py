import os

def search_multiple_texts_in_files(start_dir, search_texts):
    matches = []

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    for line_number, line in enumerate(f, start=1):
                        for text in search_texts:
                            if text in line:
                                matches.append((file_path, text, line_number, line.strip()))
            except Exception:
                pass

    if matches:
        print(f"\nSearch Results for {', '.join(search_texts)}:")
        for match in matches:
            print(f"Found '{match[1]}' in {match[0]} on line {match[2]}: {match[3]}")
    else:
        print(f"No matches found for {', '.join(search_texts)} in {start_dir}.")

directory_to_search = "/Users/Downloads"
search_strings = ["sun", "moon"]

search_multiple_texts_in_files(directory_to_search, search_strings)
