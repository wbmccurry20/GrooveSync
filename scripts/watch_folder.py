import os
import shutil
import time

def is_analyzed(file_path, initial_mod_time):
    # Get the current modification time
    current_mod_time = os.path.getmtime(file_path)
    return current_mod_time != initial_mod_time

def watch_folder(source_folder, destination_folder, check_interval=120, analysis_wait_time=300):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    while True:
        for filename in os.listdir(source_folder):
            full_file_path = os.path.join(source_folder, filename)
            if os.path.isfile(full_file_path) and filename.endswith(".mp3"):
                print(f"Found new file: {filename}")
                
                # Get the initial modification time of the file
                initial_mod_time = os.path.getmtime(full_file_path)

                # Wait and check if the file has been analyzed
                start_time = time.time()
                while time.time() - start_time < analysis_wait_time:
                    if is_analyzed(full_file_path, initial_mod_time):
                        print(f"File {filename} appears to be analyzed.")
                        break
                    time.sleep(check_interval)
                else:
                    print(f"File {filename} did not appear to be analyzed within the wait time.")

                # Move the file to the destination folder
                dest_file_path = os.path.join(destination_folder, filename)
                shutil.move(full_file_path, dest_file_path)
                print(f"Moved {filename} to {destination_folder}")

        time.sleep(10)  # Check the folder every 10 seconds

source = "/Users/will/Desktop/Z2"
rekordbox_auto_import = "/Users/will/Desktop/Z2"  # Update with your desired folder name

watch_folder(source, rekordbox_auto_import)
