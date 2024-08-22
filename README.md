# Talk To Your DB 🗃️

![image](https://github.com/user-attachments/assets/7e9406c3-25b9-43ff-b68d-83816eb1e51c)
<!-- Replace with the URL to your screenshot -->

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview
**Talk To Your DB** is a web-based application built using [Streamlit](https://streamlit.io/), designed to help users interact with their database using natural language. This tool uses Generative AI to transform user questions into SQL queries and fetches accurate results from the database.

## Features
- Converts natural language questions into SQL queries.
- Fetches data from your database and provides answers directly in the app.
- Uses **Google Generative AI** for natural language processing.
- Simple and intuitive interface built with Streamlit.

## Installation

### Prerequisites
Before you can run this tool, you need to have the following installed:
- Python 3.8 or above
- Streamlit
- Google Generative AI API access (Google Cloud setup)
- MySQL database

### Step-by-Step Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/talk-to-your-db.git
    cd talk-to-your-db
    ```

2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Google API key:
    - In your project directory, create a `.env` file or directly export it in your terminal:
      ```bash
      export GOOGLE_API_KEY='your-google-api-key'
      ```

## Usage

1. To run the Streamlit app, navigate to the project directory and run the following command:
    ```bash
    streamlit run main.py
    ```

2. Enter your question in the input box and press Enter.

3. The application will generate an SQL query, execute it, and display the results.

## Dependencies

The key dependencies for this project are:
- [Streamlit](https://streamlit.io/) for the user interface.
- [LangChain](https://github.com/hwchase17/langchain) for natural language processing.
- [Google Generative AI](https://cloud.google.com/genai) for embeddings.
- MySQL for database management.

You can find all the dependencies listed in the `requirements.txt` file.

## Configuration

Make sure to configure your **Google API key** as an environment variable:
```bash
export GOOGLE_API_KEY='your-google-api-key'
