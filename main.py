import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
import json
from dotenv import load_dotenv

load_dotenv()
blobConnectionString = os.getenv("BLOB_CONNECTION_STRING")
blobContainerName = os.getenv("BLOB_CONTAINER_NAME")
blobAccountName = os.getenv("BLOB_ACCOUNT_NAME")

SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USERNAME = os.getenv("SQL_USERNAME")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

st.title("Cadastro de produtos")

#formulario de cadastro de produtos
product_name = st.text_input("Nome do produto")
product_price = st.number_input("Preço do produto", min_value=0.0, format="%.2f")
product_description = st.text_area("Descrição do produto")
product_image = st.file_uploader("Imagem do produto", type=["jpg", "jpeg", "png"])

#save image to blob storage
def save_image_to_blob(image_file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobContainerName)
    blob_name = str(uuid.uuid4()) + "_" + image_file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(image_file.read(), overwrite=True)
    image_url = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
    return image_url

def insert_product_to_db(name, price, description, image_url):
    try:
        connection = pymssql.connect(
            host=SQL_SERVER,
            user=SQL_USERNAME,
            password=SQL_PASSWORD,
            database=SQL_DATABASE
        )
        cursor = connection.cursor()
        sql = "INSERT INTO Produtos (nome, descricao, preco, imagem_url) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, description, price, image_url))
        connection.commit()
        cursor.close()
        connection.close()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir produto no banco de dados: {e}")
        return False
    

if st.button("Cadastrar produto"):
    insert_product_to_db(product_name, product_price, product_description, save_image_to_blob(product_image))
    return_message = 'Produto cadastrado com sucesso!'

st.header('Produtos cadastrados')

if st.button("Listar produtos"):
    return_message = 'Produtos listados com sucesso!'