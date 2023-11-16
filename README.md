# `jump2digital-hackato` Repository

Welcome to the `jump2digital-hackato` repository! This is the database component of an application dedicated to monitoring touristic activity in Barcelona. Our aim is to provide real-time information about high-concurrency tourist spots and monuments in the city, helping to enhance the experience for both visitors and local businesses.

## Overview

The `jump2digital-hackato` project uses Postgres on Supabase to manage and analyze data related to tourist movements and popular monument locations in Barcelona. This repository contains the initial data and scripts required for setting up and testing the database.

## Contents of the Data Folder

- `puntos_bnc.csv`: This CSV file contains the coordinates of the top 20 most popular monuments in Barcelona. It serves as a primary reference for identifying key areas of interest for tourists.

- `random_pos.py`: A Python script that generates random positions within a specified range of longitudes and latitudes in the Barcelona area. This script simulates user movement by generating mock data every 20 seconds, essential for proof of concept and testing.

- `database_users.ipynb`: A Jupyter notebook designed for local development. It allows for easy manipulation and testing of the database through Python scripts. This tool is particularly useful for developers who wish to experiment with or extend the capabilities of the database.

## Future Developments

For the later stages of deployment, the database will be configured to receive data from multiple sources that can provide real-time coordinates of users. This integration will significantly enhance the application’s ability to monitor and analyze tourist activity in Barcelona.

## How to Use

1. **Set Up Your Local Environment:**
   - Clone the repository.
   - Ensure you have Python and Jupyter Notebook installed.
   - Install PostgreSQL if not already installed.

2. **Initialize the Database:**
   - Use the `puntos_bnc.csv` file to populate the initial data on popular monuments.
   - Run `random_pos.py` to generate and insert mock user data into the database.

3. **Development and Testing:**
   - Utilize `database_users.ipynb` for experimenting with data manipulation and querying techniques.

## Contribution

Contributions to the `jump2digital-hackato` project are welcome! Whether it's improving the code, refining the database structure, or suggesting new data sources, your input is valuable. Please read the `CONTRIBUTING.md` file for guidelines on how to contribute.

## Contact

For any queries or suggestions, feel free to open an issue in this repository or contact the project maintainers directly.

Thank you for your interest in the `jump2digital-hackato` project. Together, we can make tourism in Barcelona a more enjoyable and sustainable experience!