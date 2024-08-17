import os
import time

def generate_rekordbox_xml(track_paths, xml_file_path):
    # Ensure the directory for the XML file exists
    os.makedirs(os.path.dirname(xml_file_path), exist_ok=True)

    with open(xml_file_path, 'w') as xml_file:
        xml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        xml_file.write('<DJ_PLAYLISTS Version="1.0">\n')
        xml_file.write('<PRODUCT Name="GrooveSync Rekordbox XML" Version="1.0"/>\n')
        xml_file.write('<COLLECTION Entries="{}">\n'.format(len(track_paths)))

        for i, track_path in enumerate(track_paths):
            track_name = os.path.basename(track_path)
            xml_file.write('<TRACK TrackID="{}" Name="{}" Location="file://localhost{}"/>\n'.format(i + 1, track_name, track_path.replace(" ", "%20")))

        xml_file.write('</COLLECTION>\n')
        xml_file.write('</DJ_PLAYLISTS>\n')

def main():
    source_folder = "/Users/will/Desktop/Z2"
    xml_file_path = "/Users/will/Desktop/rekordbox_auto_import/rekordbox_import.xml"
    destination_folder = "/Users/will/Desktop/Z2/testPlaylist"

    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Get the list of MP3 files in the source folder
    track_paths = [os.path.join(source_folder, f) for f in os.listdir(source_folder) if f.endswith('.mp3')]

    # Generate the Rekordbox XML file
    generate_rekordbox_xml(track_paths, xml_file_path)

    # Simulate waiting for Rekordbox to analyze the files
    print("Waiting for Rekordbox to analyze the files...")
    time.sleep(30)  # Adjust the wait time as necessary

    # Move the files to the destination folder after analysis
    for track_path in track_paths:
        dest_path = os.path.join(destination_folder, os.path.basename(track_path))
        if os.path.exists(track_path):
            os.rename(track_path, dest_path)
            print(f"Moved {os.path.basename(track_path)} to {destination_folder}")
        else:
            print(f"{os.path.basename(track_path)} was not found in {source_folder}")

    print("Process complete. All analyzed files have been moved.")

if __name__ == "__main__":
    main()
