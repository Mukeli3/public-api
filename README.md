# Public API using Flask-

This is a simple public API built with Flask that returns JSON data containing a registered email, the current UTC datetime as an ISO 8601 formatted timestamp, and a project's codebase GitHub URL.

## Project Structure

```
public_api/
├── venv/
├── app/
│   ├── __init__.py
│   ├── route.py  
├── README.md
├── run.py 
└── requirements.txt
```

## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- `pip` (Python package manager) installed.
- Virtual environment (recommended for dependency management).

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Mukeli3/public-api.git
   cd public_api
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt

   ```
4. Open the `.env.sample` file in a text editor. Copy all the contents of the file.

5. In the same project directory, create a new file named `.env`.

6. Paste the contents you copied from `.env.sample` into your newly created `.env` file.

7. Replace the placeholder values with your own information. For example:
```env
   EMAIL=your-email@example.com
   GITHUB_URL=https://github.com/yourusername/your-repo
```
4. Run the API:
   ```sh
   python run.py
   ```

## API Documentation

### Endpoint
```
GET /api/info
```

### Response Format (200 OK)
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Backlink
https://hng.tech/hire/python-developers
