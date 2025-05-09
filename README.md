# Setup the application
Execute the commands step by step to start the application
- Python 3.11 needs to be installed

## Create Virtual Environment
Open terminal:

```bash
python -m venv venv
cd /venv/Scripts
./activate
cd ..
cd ..
```

This will create and activate the environment to install packages

## Install Packages
In terminal:

```bash
pip install -r ./requirements.txt
```
This will install the required packages for the application

## Start the server
In terminal:

```bash
uvicorn app.main:app --reload
```
This will start the uvicorn server running on localhost and port 8000.

## Check if the application is running
Navigate to [Localhost:8000](http://localhost:8000)

## Try running the tests
Open the root folder in terminal and enter the following command:

```bash
pytest app/tests/test_main.py
```
This should run the tests and output if the tests passed or failed

## Usage
### Category API
API List:
### GET http://localhost:8000/api/categories
### POST http://localhost:8000/api/categories
### PUT http://localhost:8000/api/categories/1
### DELETE http://localhost:8000/api/categories/1
Create or update object payload
```json
{
    "name": "Sample Category",
    "description": "Description of a category"
}
```

### Product API
API List:
### GET http://localhost:8000/api/products
### POST http://localhost:8000/api/products
### PUT http://localhost:8000/api/products/1
### DELETE http://localhost:8000/api/products/1
Create or update object payload
```json
{
    "name": "Sample Product",
    "description": "Description of a product",
    "price": 100,
    "category_id": 1
}
```