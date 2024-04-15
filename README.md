# Pixela API Interaction

Pixela API Interaction CLI is a command-line tool that allows users to interact with the Pixela API, enabling them to manage their [Pixela](https://pixe.la/) accounts, create users, graphs, post and update pixels, and more.

## Features

- **Login:** Simulates login by performing a profile update.
- **Create User:** Users can create a Pixela account.
- **Create Graph:** Users can create a new graph to track activity of a certain.
- **Post Pixel:** Add a new data point to a specific graph.
- **Update Pixel:** Modify an existing data point.
- **Delete Pixel:** Remove a data point from a graph.
- **Get User Graphs:** Retrieve a list of user's graphs.

## Usage

1. Run `main.py`.
2. Choose from the menu options to perform desired actions.

## Project Structure

- `main.py`: Contains the main program loop and user interface.
- `pixela.py`: Handles Pixela API interactions (e.g., login, graph management).
- `utils.py`: Provides utility functions (e.g., token hashing, screen clearing).

## Improvements to Consider

- **Input Validation:** Implement validation for user inputs to ensure data integrity.
- **Error Handling:** Enhance error handling to gracefully handle API errors and user mistakes.
- **Code Formatting:** Use a consistent code formatting style throughout the project.
- **Unit Tests:** Add unit tests to ensure the correctness of functions and improve code reliability.
- **Enhanced User Interface:** Improve user experience with better prompts, error messages, and feedback.
- **Colorized Output:** Enhance readability by adding color to console output for better distinction.
- **Documentation:** Provide inline documentation for functions and modules to improve code readability and maintainability.

## Acknowledgements

This project was inspired by [Dr. Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) course and the [Pixela API](https://docs.pixe.la/).

