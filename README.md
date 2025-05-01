
# 📦 Cadastro de Produtos

Aplicação web simples para cadastro e exibição de produtos, desenvolvida com [Streamlit](https://streamlit.io/). As imagens são armazenadas no **Azure Blob Storage** e os dados em um banco de dados **SQL Server**.

![Streamlit Badge](https://img.shields.io/badge/Streamlit-Enabled-FF4B4B?logo=streamlit) ![Python Badge](https://img.shields.io/badge/Python-3.8+-blue?logo=python) ![Azure Badge](https://img.shields.io/badge/Azure-Blob%20Storage-0078D4?logo=microsoftazure)

---

## ✨ Funcionalidades

- 📝 Cadastro de produtos (nome, descrição, preço e imagem)
- ☁️ Upload e armazenamento de imagens no Azure Blob Storage
- 📋 Listagem de produtos com imagens e detalhes
- 💻 Interface web amigável e responsiva com Streamlit

---

## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- Conta no [Microsoft Azure](https://azure.microsoft.com/) com Blob Storage configurado
- Banco de dados SQL Server acessível

---

## 🚀 Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **(Opcional) Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\ctivate         # Windows
   ```

3. **Crie um arquivo requirements.txt com as seguintes dependências**
   ```bash
   streamlit
   azure-storage-blob
   pymysql
   python-dotenv
   ```

4. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure o arquivo `.env`:**

   Crie um arquivo `.env` com as seguintes variáveis (exemplo abaixo):

   ```env
   BLOB_CONNECTION_STRINGG= sua_ConnectionString
   BLOB_CONTAINER_NAME = seu_container
   BLOB_ACCOUNT_NAME = sua_account
   SQL_SERVER = "seu_server"
   SQL_DATABASE = "seu_database"
   SQL_USERNAME = "seu_username"
   SQL_PASSWORD = "seu_password"
   ```

6. **Execute a aplicação:**

   ```bash
   streamlit run app.py
   ```

---

## 📁 Estrutura Sugerida do Projeto

```plaintext
├── app.py
├── requirements.txt
├── .env           # Adicione suas variáveis de ambiente aqui
├── .env.example   # Modelo de arquivo .env (não comite este arquivo)
├── utils/
│   ├── db.py
│   └── storage.py
├── assets/
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/)
- [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)
- [SQL Server](https://www.microsoft.com/en-us/sql-server)
- [Python](https://www.python.org/)

---

## 🧪 Testes

> Testes automatizados ainda não implementados.  
> Sugestão: utilizar `pytest` ou `unittest` para validação de funcionalidades.

---

## 📌 Roadmap (Próximos Passos)

- [ ] Autenticação de usuários
- [ ] Edição e exclusão de produtos
- [ ] Paginação na listagem
- [ ] Validações mais robustas nos formulários
- [ ] Testes unitários e de integração

---

## 📑 Script SQL para Criação das Tabelas

Execute o seguinte script SQL para criar as tabelas necessárias no seu banco de dados **SQL Server**:

```sql
 CREATE TABLE Produtos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255),
    descricao NVARCHAR(MAX),
    preco DECIMAL(18,2),
    imagem_url NVARCHAR(2083)
)
```

Este script cria a tabela `Produtos` com as colunas necessárias para armazenar o nome, descrição, preço e o caminho da imagem.

---

## 📝 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
