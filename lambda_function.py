import json
import sys
import logging
import psycopg2
import os

# RDS settings
rds_host  = os.environ.get('RDS_HOST')
rds_username = os.environ.get('RDS_USERNAME')
rds_user_pwd = os.environ.get('RDS_USER_PWD')
rds_db_name = os.environ.get('RDS_DB_NAME')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize a connection to the RDS PostgreSQL database
try:
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
                    (rds_host, rds_username, rds_user_pwd, rds_db_name)
    print(conn_string)
    conn = psycopg2.connect(conn_string)
except:
    logger.error("ERROR: Could not connect to Postgres instance.")
    sys.exit()

def lambda_handler(event, context):
    # Get user attributes from Cognito event
    username = event['userName']
    email = event['request']['userAttributes']['email']
    sub = event['request']['userAttributes']['sub']

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute the command
    cur.execute(
        "INSERT INTO users (sub, username, email) VALUES (%s, %s, %s);",
        (sub, username, email));

    # Make the changes to the database persistent
    conn.commit();

    # Close communication with the database
    cur.close()
    conn.close()

    # Return to Amazon Cognito
    return event