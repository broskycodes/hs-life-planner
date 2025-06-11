import json
import os
from DataManager import DataManager
# Tester method for classes


def main():
    # Open existing files
    os.makedirs("save_files", exist_ok=True)
    if not os.path.exists(os.path.join("save_files", "init.json")):
        with open("save_files/init.json", "w") as file:
            json.dump(True, file)
    data_manager = DataManager("save_files")
    schedules = []
    associations = []
    user_profile = []
    items = []
    other_data = {}
    for file_name, file_contents in data_manager.load_all():
        if file_name == "schedules":
            schedules = file_contents
        elif file_name == "associations":
            associations = file_contents
        elif file_name == "user_profile":
            user_profile = file_contents
        elif file_name == "items":
            items = file_contents
        else:
            other_data[file_name] = file_contents

    # Save data when program is closed
    data_manager.save("schedules.json", schedules)
    data_manager.save("associations.json", associations)
    data_manager.save("user_profile.json", user_profile)
    data_manager.save("items.json", items)
    for file_name, file_contents in other_data.items():
        file_json_name = file_name + ".json"
        data_manager.save(file_json_name, file_contents)


if __name__ == "__main__":
    main()
