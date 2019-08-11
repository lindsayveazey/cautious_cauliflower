def question(prompt, hint, answer):
    '''
    prompt - string
    hint - string
    answer - string
    '''
    while True: 
        response = input(prompt)
        if response is "?":
            print(hint)
        elif response is not None:
            print(answer)
            break

##### Quiz: SQL edition #####

print("For each question, type your response, then press ENTER to proceed; this triggers the answer to each open-ended quesiton. Type '?' to trigger a hint.\n\n")

q1 = question("[SQL] Name and define the six query clauses.", "SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY", "SELECT: determines which columns to include in the query's result set\n\n FROM: identifies the tables from which to draw data and how the tables should be joined\n\n WHERE: filters out unwanted data\n\n GROUP BY: used to group rows together by common column values\n\n HAVING: filters out unwanted groups\n\n ORDER BY: sorts the rows of the final result set by >=1 columns")

q2 = question("[SQL] Name and define the seven logical operators.", "LIKE, IN, BETWEEN, IS NULL, AND, OR, NOT, ORDER BY", "LIKE allows you to match similar values, instead of exact values.\n\nIN allows you to specify a list of values you’d like to include.\n\nBETWEEN allows you to select only rows within a certain range.\n\nIS NULL allows you to select rows that contain no data in a given column.\n\nAND allows you to select only rows that satisfy two conditions.\n\nOR allows you to select rows that satisfy either of two conditions.\n\nNOT allows you to select rows that do not match a certain condition.")

q3 = question("[SQL- BigQuery] Write a description for the command: WHERE ...", "What are you targeting with the WHERE command? Consider the formatting.", "WHERE Filtering_column_name = 'Name123'")

q4 = question("[SQL- BigQuery] Step # 1: Use Python to import the package bigquery to use Google's API, BigQuery:", "from ______ import _____", "from google.cloud import bigquery")

q5 = question("[SQL- BigQuery] Step # 2) Create 'client' object to retrieve information from BigQuery datasets:", "client = ________", "client = bigquery.Client()")

q6 = question("[SQL- BigQuery] In BigQuery, each dataset is contained in a corresponding project. Step # 3a) Construct a reference to the dataset:", "dataset_ref = _____", "dataset_ref = client.dataset('hacker_news', project = 'bigquery-public-data')")

q7 = question("[SQL- BigQuery] Step # 3b) API request to fetch the dataset:", "dataset = ________", "dataset = client.get_dataset(dataset_ref)")

q8 = question("[SQL- BigQuery] Step # 4) Print a list of all tables in the dataset:", "Define your tables list and write a for loop.", "tables = list(client.list_tables(dataset))\n\n for table in tables:\n\n ....print(table.table_id)")

q9 = question("[SQL- BigQuery] Step # 5a) Construct a reference to a particular table by name:", "table_ref = ____", "table_ref = dataset_ref.table('table_1234')")


q10 = question("[SQL- BigQuery] Step # 5b) API request to fetch the table:", "table = ____", "table = client.get_table(table_ref)")

q11 = question("[SQL- BigQuery] Step # 6) Print the table schema. ", "This is one line of code.", "table.schema")

q12 = question("[SQL- BigQuery] Step # 7) Examine the table head for the first column and simultaneously convert to a pandas DataFrame using to_dataframe():", "client.____(_____, selected_fields = table.schema[:1], _____).to_dataframe()", "client.list_rows(table, selected_fields = table.schema[:1], max_results = 5).to_dataframe()")

q13 = question("[SQL] Write a description for the command: ORDER BY ...", "What would you want to accomplish with this command?", "Sequential ordering based on the column name in ORDER BY column name")

q14 = question("[SQL] Write a command using the following commands: SELECT, FROM, ORDER BY.", "Specify where the columns and tables are named.", "SELECT col1, col2, ... \n\n FROM table_name \n\n ORDER BY col1, col2, ...")

q15 = question("[SQL] How would you change the order (ascending/descending) of the selection clled by the ORDER BY command?", "What two words could change the order here?", "ORDER BY col1, col2, ... ASC DESC")

q16 = question("[SQL] How would you group a selection called from col1?", "Think of the word 'group'...", "GROUP BY col2")

q17 = question("[SQL] Write a description for each command: SELECT ... FROM ...", "Remember the formatting for FROM", "SELECT Target_column_name # The column I'm targeting ... FROM `project.database.table` # Note the backticks ``")


