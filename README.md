## Backend Developer Assessment (AHAM Capital Asset Management Berhad)

This repository is created solely for the submission of Backend Developer Assessment prepared by AHAM Capital Asset Management Berhad.

## Project Summary
This backend project is developed using a framework written in Python which is called **FastAPI**, alongside with other Python libraries such as SQLALchemy (for ORM), Pydantic (for data validation), Alembic (for database migration), and Pytest (for testing). Plus, the project uses postgres as its db.

The structure of the folder is actually the implementation of an architecture design called the **Onion Architecture**. Since, this project is following the Onion Architecture, it will heavily depends on the concept of dependency injection and for this case, the project will make use of the dependency injection system provided by the FastAPI itself.

This project implements mixin pattern, where we can inject a certain method into a class. Other than that, the project will heavily depend on type hinting/type checking with the help of mypy. Hence, you will see the concept of generic typing is being implemented here. 

I will not go through the whole folder structure, but I will start with the important components/folders of the project. 

**Presentation**: Presentation folder focusses on anything related to the UI (in our case, the swagger UI). Changes here, will affect the swagger ui/openapi.

**application/services**: Services folder focusses on the business logic. Any business logic that we like to add, we will have to write it in this folder.

**persistence**: Persistence folder/layer serves as the query layer. Query to database should only be created here, in the persistence folder.

**domain/entities**: Entities folder serves as the schema representation of our database. If we have a table called sample_table, then inside Entities folder will have python script that have a python class represent that table.

It will be too long to explain one by one on each component of the code. Do contact me, if more explanation is required. 

## Running the project
To make it easy, I've created a yaml file named docker-compose. So, make sure you have docker installed in your machine. Follow the steps below to run the project:

*Step 1*
```bash
# assumed you have cloned the project
docker-compose up --build
```

*Step 2*
```bash
# in your machine's terminal
pip install ./src/requirements.txt
```

*Step 3*
```bash
# migrate database
alembic revision --autogenerate
alembic upgrade head
```

Once you have run all the steps, you can now open http://localhost:8080/docs to access the **swagger ui**.

If error related to database raises, please try to check if the aham_capital_db_service has these two databases:

1. fund_management_db
2. fund_management_db_test
 
You can add these databases if it does not exist. Refer the following variable.

username=admin <br/>
password=Admin2023! <br/>
host=localhost <br/>
port=5432

Note that, once you added those two database, you run this command again `alembic upgrade head`

## Testing
To run test for this project simply run the following command
```bash
# make sure you are in the project folder (not in src folder)
pytest
```
## Screenshots
![image](https://github.com/muhdamir/amiba/assets/62650104/b7860cde-358d-4e90-aeb2-bf0f180c87de)
