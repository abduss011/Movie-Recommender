# Movie Recommender System

## Overview

This project is a **full-stack movie recommendation engine** designed to suggest films based on user preferences. It uses a modern architecture with a Python API, ML backend to serve recommendations and a React frontend for a dynamic user interface.

* **Recommendation Method:** **Content-Based Filtering** (The system recommends movies that are similar in content—such as genre, cast, or director—to movies the user already likes.)
* **Architecture:** **Flask** API (Backend) and **React** (Frontend).


## Demo

![Screenshot 1](imgs/image11.png)
![Screenshot 2](imgs/image12.png)

---

## Key Features

* **Personalized Recommendations:** Generates suggestions based on movie attributes.
* **RESTful API:** Provides a clean interface for fetching recommendations.
* **Modern UI:** A fast and responsive interface built with React.

---

##  Prerequisites

Ensure you have the following installed on your system:

* **Python 3.x**
* **Node.js / npm**
* **Git**

---

##  Setup Instructions

The application requires the backend and frontend to run **concurrently** in two separate terminal sessions.

### 1. Initial Project Setup

1.  **Clone the repository:**
    ```bash
    git clone [Your-GitHub-Repository-URL]
    cd movie-recommender-system
    ```
2.  **Install Backend Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Backend (Python/Flask) Setup

This server hosts the similarity model and the recommendation API.

1.  **Navigate to the backend directory:**
    ```bash
    cd back
    ```
2.  **Process Data & Build the Model:**
    This step generates the necessary data structures (e.g., similarity matrix) used by the API.
    ```bash
    python process.py
    ```
3.  **Start the API Server:**
    ```bash
    python app.py
    ```
    *The API should now be running locally, typically at `http://127.0.0.1:5000`.*

### 3. Frontend (React) Setup

The user interface connects to the local Flask API.

1.  **Navigate to the frontend directory:**
    ```bash
    cd ../react
    ```
2.  **Install Frontend Dependencies:**
    ```bash
    npm install
    ```
3.  **Start the React Application:**
    ```bash
    npm start
    ```
    *The application will automatically open in your web browser, typically at `http://localhost:3000`.*
---