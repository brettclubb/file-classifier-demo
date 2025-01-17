# File Classifier

This project is a simple file classification web application built using Flask and pandas. It allows users to upload files and classifies them based on their content.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your computer. You can download it from [here](https://www.python.org/downloads/).

## Setting Up the Project

Follow these steps to set up and run the project on your computer:

### 1. Clone the Repository

Clone the project repository to your local machine using the following command:

```sh
git clone https://github.com/your-username/file-classifier.git
```

Navigate to the project directory:

```sh
cd file-classifier
```

### 2. Create a Virtual Environment

Create a virtual environment to manage the project dependencies:

```sh
python -m venv venv
```

Activate the virtual environment:

- On Windows:

    ```sh
    venv\Scripts\activate
    ```

- On macOS/Linux:

    ```sh
    source venv/bin/activate
    ```

### 3. Install Dependencies

Install the required Python dependencies using `pip`:

```sh
pip install -r requirements.txt
```

### 4. Run the Application

Run the Flask application using the following command:

```sh
python file-classifier.py
```

### 5. Access the Application

Open your web browser and navigate to `http://localhost:5000`. You should see the file upload interface.

## Project Structure

Here is an overview of the project structure and the purpose of each folder:

- `uploads/`: This folder is used to store the uploaded files.
- `templates/`: This folder contains the HTML templates for the web application.
    - `upload.html`: The file upload interface.
    - `result.html`: The result page that displays the classification and file preview.
- `file-classifier.py`: The main Flask application file that handles file uploads and classification.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Usage

1. Upload a file using the file upload interface.
2. The application will classify the file and display the classification result along with a preview of the file content.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
