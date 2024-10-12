# RedBus
This project is a Bus Information System built using Streamlit, providing an easy-to-use interface to filter and view bus details from different states, routes, prices, star ratings, and bus types. The data is managed through a PostgreSQL database, allowing efficient searches across various bus routes.

Features
Filter by State and Route: Users can select a specific state and view all bus routes available for that state.
Price Filter: Easily filter buses by price to find one that fits your budget.
Star Rating Filter: Sort and filter buses based on customer ratings.
Bus Type Filter: View buses by different categories, such as Sleeper, AC, Non-AC, etc.
Dynamic Data Loading: The app uses real-time data from a PostgreSQL database, ensuring up-to-date information.
Project Structure
Streamlit App: A single-page application that provides a clean UI to search and filter bus data.
Database: PostgreSQL is used to store bus information, including states, routes, prices, ratings, and bus types.
Selenium for Data Scraping: Bus data was scraped from RedBus using Selenium and is processed into a usable format for the app.
Installation
To get started with the project, follow these steps:

Prerequisites
Python 3.x
PostgreSQL
Streamlit
Steps
Clone the Repository

bash
Copy code
git clone https://github.com/Raghul978/RedBus.git
cd RedBus
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Database Setup

Set up a PostgreSQL database and update the connection details in the application code.
Run the App

bash
Copy code
streamlit run app.py
Usage
Once the app is running, you can filter buses by state, price, star rating, or bus type. The interface is designed to be intuitive, so you can quickly find the desired bus route.

Future Improvements
Live Data Integration: Integrating with a live bus API to keep data updated in real-time.
User Authentication: Adding user authentication to provide personalized experiences.
Enhanced Filters: Introducing more advanced filtering options such as bus amenities, departure locations, and arrival times.



![Screenshot 2024-10-12 183326](https://github.com/user-attachments/assets/9d473a88-a96e-4739-9547-3a7af6ba66cd)
