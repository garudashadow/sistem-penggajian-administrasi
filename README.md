
Built by https://www.blackbox.ai

---

# Sistem Penggajian & Administrasi

## Project Overview
**Sistem Penggajian & Administrasi** is a web-based application designed for managing employee payroll and administrative tasks. The application includes a user-friendly login interface, an admin dashboard with various statistics, and is built using Tailwind CSS for styling and Flask as the backend framework.

## Installation

To get started with the project, follow these steps to set it up on your local environment:

### Prerequisites
- Python 3.6 or higher
- Flask
- A web browser

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/sistem-penggajian-administrasi.git
    cd sistem-penggajian-administrasi
    ```

2. **Install the required Python packages**:
    You may want to set up a virtual environment for this project:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install Flask
    ```

3. **Run the application**:
    ```bash
    python server.py
    ```

4. **Open your browser** and navigate to http://localhost:8000 to access the application.

## Usage

Once the server is running, you can access the login page. Enter the following credentials to log in:
- **Username**: admin
- **Password**: admin

After a successful login, you'll be directed to the dashboard where you can view various statistics related to employees and payroll activities.

## Features

- User authentication with feedback on login success/failure.
- Dashboard displaying:
  - Total number of employees.
  - Total payroll processed.
  - Today's attendance record.
  - Pending tasks.
- Recent activity log for employee actions.
- Responsive design using Tailwind CSS.

## Dependencies

The following dependencies are used in the project:

- Flask

**CSS and JS Libraries**:
- Tailwind CSS for styling (via CDN)
- Font Awesome for icons (via CDN)
- Google Fonts for typography (Inter font)

## Project Structure

```plaintext
sistem-penggajian-administrasi/
├── index.html           # Main HTML file for the application interface.
├── server.py            # Flask server script handling API requests and serving static files.
```

### index.html
Contains:
- Login form with username/password fields and a submit button.
- Dashboard layout with statistics cards and a table for recent activities.
- Integrated CSS from Tailwind and JavaScript for handling the login submission.

### server.py
Sets up the Flask application with:
- Routes for serving the main HTML file and handling login requests.
- Security headers to enhance application security.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.