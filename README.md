# The All Image Background Remover

The All Image Background Remover is a Python project that automates the process of removing backgrounds from images in a selected folder. It utilizes the GrabCut algorithm implemented in OpenCV to separate the foreground and background of each image and save the results in a new directory.

## Features

- Removes backgrounds from images in a selected folder
- Saves the background-removed images in a separate directory
- Utilizes the GrabCut algorithm for accurate foreground extraction
- Supports multiple image formats (e.g., JPEG, PNG)
- Saves Bunch of times

## Usage

1. Install the required dependencies by running the following command:
        $ pip install opencv-python numpy tkinter

2. Clone this repository to your local machine or download the project files.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run the `main.py` script using the following command:
        $ python main.py

5. A file dialog will appear. Select the folder containing the images from which you want to remove the backgrounds.

6. The script will process each image in the selected folder, remove the background, and save the background-removed images in a new directory called "Background_Removed" within the source folder.

7. Once the script completes, you will see the paths of the saved background-removed images printed in the terminal.

## Contributing

Contributions to the Background Remover project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch with a descriptive name for your feature or improvement.

3. Make your changes to the codebase.

4. Write tests, if applicable, to ensure the correctness of your changes.

5. Commit your changes and push them to your forked repository.

6. Submit a pull request, providing a detailed description of your changes and the rationale behind them.

Please note that all contributions are subject to review and may require some modifications before being merged into the main project.

## License

This project is licensed under the [MIT License](LICENSE).