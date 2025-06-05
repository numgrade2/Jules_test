# Jules News

Jules News is a simple landing page application built with Python and the Flet framework. It displays a logo and the top three major news headlines of the day (currently using placeholder data).

## Prerequisites

- Python 3.7 or higher

## Setup and Running

1.  **Clone the repository (or download the `jules_news` directory).**

2.  **Navigate to the project directory:**
    ```bash
    cd path/to/jules_news
    ```

3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4.  **Install dependencies:**
    Make sure you have `pip` installed. The dependencies are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**
    ```bash
    flet run main.py
    ```
    If you encounter a "command not found" error for `flet`, you can try:
    ```bash
    python -m flet run main.py
    ```
    (This can happen if the directory containing Flet's scripts, often `~/.local/bin` on Linux/macOS, is not in your system's PATH.)

    Alternatively, you can run it as a standard Python script (though `flet run` is preferred for development features like hot reload):
    ```bash
    python main.py
    ```

    The application will open in a new window.

## Project Structure

-   `main.py`: The main Flet application code.
-   `requirements.txt`: Lists the Python dependencies for the project.
-   `README.md`: This file.
