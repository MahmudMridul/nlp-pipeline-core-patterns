# A Playground Project

The main purpose of this project is to experiment with a few Python features. This project implements the following features:

1. File reading and writing. 
2. Reading large files in batches using generators. 
3. Simple exception handling. 
4. Building and consuming custom decorators. 
5. Building and consuming custom context managers. 

## Setup

This project uses **uv** for fast Python package and environment management. 

### Prerequisites

Ensure you have `uv` installed on your system.

### Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <project-directory-name>
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   uv sync
   ```

3. **Activate the environment:**
   * **macOS/Linux:** `source .venv/bin/activate`
   * **Windows:** `.venv\Scripts\activate`

4. **Run the project:**
   ```bash
   uv run main.py
   ```
