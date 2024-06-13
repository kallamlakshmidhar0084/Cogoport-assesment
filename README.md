# Cogoport-assesment

#setting up environment 
run the following code

pip install virtualenv
virtualenv env 
cd .\env
.\Scripts\activate

#intalling dependencies 
 pip install fastapi uvicorn  sqlalchemy psycopg2-binary

#running the fastAPI application
 uvicorn main:app --reload

#in database.py file change URL of database accordingly
# redirect to http://127.0.0.1:8000/docs to test the CURD operations
 
