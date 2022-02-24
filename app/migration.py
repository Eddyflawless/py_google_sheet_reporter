import sys
import os
from mysql.connector import Error
from app import db

DBConnector = db.DBConnector

def run_migration():

    db_connection = None

    try:
       pass

    except Exception as e:
        print("Migration failed \n")
        raise e
    finally:
        db_connection.close()

if __name__ == '__main__':
    run_migration()