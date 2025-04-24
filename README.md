# Python Coding Challenge

This project implements an ETL (Extract, Transform, Load) pipeline to interact with an Animals API. It fetches animal data, transforms specific fields, and sends the data to a designated endpoint.

## Repository

The source code for this project is available at:  
[https://github.com/py-saad/uforio](https://github.com/py-saad/uforio)

## Setup

### Prerequisites
- **Docker**: To run the provided container.
- **Python**: A modern version (3.8+ recommended).
- **Development Tools**: Your preferred IDE or tools.

### Steps to Get Started
1. **Download the Docker Image**  
   Download the image from:  
   [https://storage.googleapis.com/lp-dev-hiring/images/lp-programming-challenge-1-1625758668.tar.gz](https://storage.googleapis.com/lp-dev-hiring/images/lp-programming-challenge-1-1625758668.tar.gz)

2. **Load the Docker Container**  
   Run the following command to load the container:  
   ```
   docker load -i lp-programming-challenge-1-1625610904.tar.gz
   ```

3. **Run the Container**  
   Start the container and expose port 3123:  
   ```
   docker run --rm -p 3123:3123 -ti lp-programming-challenge-1
   ```

4. **Verify the API**  
   Open [http://localhost:3123/](http://localhost:3123/) to confirm the API is running.

## Project Setup

1. **Clone the Repository**  
   Clone this repository to your local machine:  
   ```
   git clone https://github.com/py-saad/uforio.git
   cd uforio
   ```

2. **Create and Activate a Virtual Environment**  
   Create a virtual environment named `venv`:  
   ```
   python -m venv venv
   ```  
   Activate the virtual environment:  
   - On Windows:  
     ```
     venv\Scripts\activate
     ```  
   - On macOS/Linux:  
     ```
     source venv/bin/activate
     ```

3. **Install Dependencies**  
   With the virtual environment activated, install the required packages:  
   ```
   pip install -r requirements.txt
   ```

4. **Run the Script**  
   Execute the main script to start the ETL process:  
   ```
   python main.py
   ```

## Project Structure

- **`main.py`**: The main script that orchestrates the ETL process (fetching, transforming, and loading animal data).
- **`requirements.txt`**: Lists the Python dependencies required for the project.
- **`/api`**: Contains API interaction logic (e.g., fetching animal data).
- **`/services`**: Includes transformation logic for fields like `friends` and `born_at`.
- **`/utils`**: Utility functions for handling retries and other helper tasks.
- **`/venv`**: Virtual environment directory (not tracked in Git; see `.gitignore`).

## The API

The Animals API is available on `http://localhost:3123/` and provides the following endpoints:
- **GET /animals/v1/animals**: Lists animals (paginated, use `page` param to fetch all).
- **GET /animals/v1/animals/<id>**: Fetches details for a specific animal by ID.
- **POST /animals/v1/home**: Accepts a JSON array of animal details (max 100 at a time). Requires transformed `friends` and `born_at` fields.
- **/docs**: OpenAPI documentation for schema details.

## The Exercise

This project:
1. Fetches all animal details from `/animals/v1/animals` and `/animals/v1/animals/<id>`.
2. Transforms the data:
   - Converts the `friends` field from a comma-delimited string to an array.
   - Converts the `born_at` field (if present) to an ISO8601 UTC timestamp.
3. Sends batches of up to 100 animals to `/animals/v1/home`.

### Challenges Handled
- The server may pause for 5-15 seconds.
- The server may return HTTP 500, 502, 503, or 504 errors.  
The script includes retry logic to handle these issues reliably.

## Design Notes

- The project is structured as a foundation for a maintainable repository.
- It uses the `requests` library for HTTP requests with retry logic.
- The code is modular, with separate functions for fetching, transforming, and loading data.
- Commit messages document the development process.

## Submitting

Submit your code to a public Git repository and share the link with the recruiting team via email.

If you have questions, feel free to reach out to the recruiting team.
