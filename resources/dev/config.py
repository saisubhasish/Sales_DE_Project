import os

key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"

#AWS Access And Secret key
aws_access_key = "PrbxNbhZyJ+jtjTlqgt+9uolS9qyd3T78zMT7B1XJaU="
aws_secret_key = "DKKoGzZHX/S8s9AStvcnPSXbcvR2td3kDSzORc7j715qJqkbpOUeMn/JH8A/E97H"
bucket_name = "de-sai-project-1"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


#Database credential
# MySQL database connection properties
database_name = "youtube_project"
url = f"jdbc:mysql://localhost:3306/{database_name}"
properties = {
    "user": "root",
    "password": "password",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "D:\\FSDS-iNeuron\\10.Projects-DS\\DataEngineerProject\\spark_data\\file_from_s3\\"
customer_data_mart_local_file = "D:\\FSDS-iNeuron\\10.Projects-DS\\DataEngineerProject\\spark_data\\customer_data_mart\\"
sales_team_data_mart_local_file = "D:\\FSDS-iNeuron\\10.Projects-DS\\DataEngineerProject\\spark_data\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "D:\\FSDS-iNeuron\\10.Projects-DS\\DataEngineerProject\\spark_data\\sales_partition_data\\"
error_folder_path_local = "D:\\FSDS-iNeuron\\10.Projects-DS\\DataEngineerProject\\spark_data\\error_files\\"
