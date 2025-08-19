# FastAPI Cost Manager

A simple **FastAPI** project to manage costs **without a database**, storing data in memory using a Python dictionary. This is designed for **learning**.

## Features

* Create, read, update, and delete (CRUD) costs.
* Each cost contains:

  * `id` (int) – unique identifier
  * `description` (str) – cost description
  * `amount` (float) – cost amount
* RESTful endpoints for managing costs.
* In-memory storage (no database required).
* Automatic API documentation via **Swagger UI** and **ReDoc**.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

## Running the API

Start the server with **Uvicorn**:

```bash
uvicorn core.main:app --reload
```

* The API will be available at: `http://127.0.0.1:8000`
* Swagger UI: `http://127.0.0.1:8000/docs`
* ReDoc: `http://127.0.0.1:8000/redoc`

---

## Notes

* Data is stored **in memory**, so all costs will be **lost when the server restarts**.

---

## License

This project is licensed under the MIT License.

