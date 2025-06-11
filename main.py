import json
import os
import DataManager
# Tester method for classes


def main():
    # Open existing files
    if not os.path.exists(os.path.join("save_files", "init.json")):
        os.makedirs("save_files", exist_ok=True)
        with open("save_files/init.json", "w") as file:
            json.dump(True, file)
    data_manager = DataManager("save_files")
    schedules = []
    associations = []
    user_profile = []
    other_data = {}
    for file_name, file_contents in data_manager.load_all():
        if file_name == "schedules":
            schedules = file_contents
        elif file_name == "associations":
            associations = file_contents
        elif file_name == "user_profile":
            user_profile = file_contents
        else:
            other_data[file_name] = file_contents


if __name__ == "__main__":
    main()
