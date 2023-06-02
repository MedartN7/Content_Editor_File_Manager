# Content Editor File Manager

Content Editor File Manager is a Python application designed to automatically organize files based on their types. It monitors a specified directory for any changes and moves the files to appropriate destination folders.

## Features

- Automatic file organization: The application monitors a source directory for any changes and automatically moves files to destination folders based on their types.
- Supported file types: The application supports organizing audio, video, image, document, and archive/compressed files.
- Customizable destination folders: Destination folders for each file type can be easily customized to match your specific requirements.
- Timeout functionality: If no file is moved within a specified timeout period, the application will exit.
- Logging: The application logs all file movements and errors for easy tracking and debugging.

## Planned Features

- Interactive mode: Add an interactive mode where the user can choose specific files to move or skip.
- Configuration file: Introduce a configuration file to easily manage and update the source directory and destination folders.
- File exclusion: Allow excluding specific files or file patterns from being moved.
- File renaming: Add an option to rename files during the move process.
- GUI interface: Develop a graphical user interface for easier configuration and control.

## Install the required dependencies

-pip install watchdog

## Usage
1. Modify the source_dir and destination folder paths in main.py according to your setup.

2. Run the application: main.py

3. The application will start monitoring the source directory for any file changes and automatically move them to the corresponding destination folders.

## Code Description

1. main.py

- `Observer` and `FileMover` classes from the Watchdog library: These classes are used to monitor a specified directory (`source_dir`) for any file modifications and perform actions accordingly.
- `start_timer` method: This method of the `FileMover` class is responsible for starting a timer to check for activity timeout.
- `check_activity_timeout` method: This method of the `FileMover` class is called when the activity timeout is reached, and it performs the necessary actions or exits the program.
- Threading: The code utilizes the `threading` module to run the file monitoring and moving functionality concurrently with the timer and activity timeout.
To use the code, follow these steps:
- Set the `source_dir` variable to the directory you want to monitor for file changes.
- Execute the script.
- The script will start monitoring the `source_dir` for any modifications and move files to the appropriate destination directories based on their extensions.
- It will also start a timer to check for activity timeout. If no file movement occurs within the specified timeout, the program will exit.

2. filemover.py

- `FileMover` class: This class extends the `FileSystemEventHandler` from the Watchdog library and handles file events such as modifications. It contains methods to check the file type and move it to the appropriate destination folder.
- Destination Folders: The code defines several destination folders (`dest_dir_sfx`, `dest_dir_music`, etc.) where files of specific types will be moved.
- File Type Checks: The code checks the file extension against predefined lists (`audio_extensions`, `video_extensions`, etc.) to determine the file type.
- File Movement: When a file of a specific type is detected, it is moved to the corresponding destination folder using the `shutil.move` function.
- Logging: The code utilizes the Python `logging` module to log file movements and other relevant information.
- Timer and Timeout: The code includes a timer functionality that triggers a timeout if no files are moved within a specified period. This helps in gracefully exiting the program.

2. utils.py

- `start_timer` function: This function takes a `file_mover` object as an argument and calls its `start_timer` method. It is used to start a timer that triggers a specified function after a certain duration.
- `check_activity_timeout` function: This function takes a `file_mover` object as an argument and calls its `check_activity_timeout` method. It is used to check if any activity has occurred within a specific timeframe and take appropriate action.

These functions can be integrated into a larger application or program where timing and activity tracking are required. They provide a way to execute certain actions asynchronously and handle timeouts effectively.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please submit a pull request. Make sure to follow the existing code style and provide a clear description of the changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.