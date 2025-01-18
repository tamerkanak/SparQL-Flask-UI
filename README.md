# SPARQL Query Interface

The **SPARQL Query Interface** is a web-based application designed to facilitate the execution of SPARQL queries on RDF data. Built using the Flask framework, this tool provides an intuitive interface for users to query RDF datasets and visualize the results in a structured tabular format.

---

## Features

- **Execute SPARQL Queries**: Run SPARQL queries on RDF data and view results in a clean, tabular format.
- **Predefined Example Queries**: Access a set of example queries to quickly explore common use cases.
- **Interactive Query Editor**: A user-friendly code editor with syntax highlighting and auto-completion for SPARQL.
- **Error Handling**: Clear error messages for invalid queries or runtime issues.
- **Responsive Design**: A modern, mobile-friendly interface built with Tailwind CSS.

---

## Installation

To set up the SPARQL Query Interface locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tamerkanak/SparQL-Flask-UI.git
   cd SparQL-Flask-UI
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```

4. **Access the Interface**:
   Open your browser and navigate to `http://localhost:5001` to access the SPARQL Query Interface.

---

## Usage

### Running SPARQL Queries

1. **Enter Your Query**:
   Use the interactive query editor to write or paste your SPARQL query.

   ![image](https://github.com/user-attachments/assets/09ec2fe2-3063-498d-9103-bf76a60e08ae)

2. **Execute the Query**:
   Click the **Run Query** button to execute the query. The results will be displayed in a table below the editor.

3. **View Results**:
   The query results are presented in a structured table, with each row representing a result and each column corresponding to a variable in the query.

   ![image](https://github.com/user-attachments/assets/53bd84ca-b3db-4a96-8b46-3a68c4b7f47d)

### Example Queries

To help users get started, the interface includes a dropdown menu with predefined example queries. These examples cover common scenarios, such as:

- **List VMs Belonging to Users**: Displays the relationship between users and their virtual machines.
- **List VMs Hosted by Servers**: Shows which virtual machines are hosted by specific servers.
- **List Database Servers and Services**: Retrieves database servers and the services they provide.
- **List Resources Used by Windows VMs**: Displays resources utilized by Windows virtual machines.
- **List Servers Managed by Administrators**: Shows servers managed by administrators.

   ![image](https://github.com/user-attachments/assets/cc1bf55e-c2d3-474a-b0b0-9eadab7e4744)

To load an example query, click the **Examples** button and select the desired query from the dropdown menu.


## Contributing

We welcome contributions to improve the SPARQL Query Interface! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

For major changes, please open an issue first to discuss the proposed changes.

---

## License

This project is licensed under the **MIT License**. For more details, see the [LICENSE](LICENSE) file.

---

## Contact

For questions, feedback, or collaboration opportunities, feel free to reach out:

- **Tamer Kanak**  
  Email: [tamerkanak75@gmail.com](mailto:tamerkanak75@gmail.com)  
  GitHub: [tamerkanak](https://github.com/tamerkanak)
