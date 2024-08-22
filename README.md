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
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview
**Talk To Your DB** is a web-based application designed to bridge the gap between natural language and SQL queries. With this tool, users can interact with their databases simply by asking questions in plain English. This application is particularly useful for non-technical users who need to extract specific data from databases without writing SQL queries.

## Features
- **Natural Language to SQL**: Converts natural language questions into SQL queries automatically.
- **Real-time Data Access**: Fetches and displays data from your database based on the generated SQL queries.
- **Powered by AI**: Utilizes **Google Generative AI** for natural language understanding and processing.
- **User-Friendly Interface**: Built with **Streamlit**, offering a clean and easy-to-use interface.
- **Few-Shot Learning**: Includes a set of predefined examples to improve query generation accuracy.

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

4. You can also modify and run the predefined few-shot examples to better understand the tool's capabilities.

## Dependencies

The key dependencies for this project are:
- [Streamlit](https://streamlit.io/) for the user interface.
- [LangChain](https://github.com/hwchase17/langchain) for natural language processing.
- [Google Generative AI](https://cloud.google.com/genai) for embeddings.
- MySQL for database management.
- [Chroma](https://www.trychroma.com/) for vector storage and retrieval.
- [HuggingFace Embeddings](https://huggingface.co/) for semantic similarity matching.

You can find all the dependencies listed in the `requirements.txt` file.

## Configuration

Make sure to configure your **Google API key** as an environment variable:
```bash
export GOOGLE_API_KEY='your-google-api-key'
```

## Examples
Here are a few example questions you can ask:

    1. "How many t-shirts do we have left for Nike in XS size and white color?"
    2. "How much is the total price of the inventory for all S-size t-shirts?"
    3. "If we have to sell all the Levi’s T-shirts today with discounts applied, how much revenue will our store generate?"

These examples will demonstrate how the application transforms questions into SQL queries and fetches results from the database.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please feel free to submit a pull request or open an issue.
