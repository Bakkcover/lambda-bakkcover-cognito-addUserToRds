import json
import sys
import logging
import psycopg2
import os

# rds settings
rds_host  = os.environ.get('RDS_HOST')
rds_username = os.environ.get('RDS_USERNAME')
rds_user_pwd = os.environ.get('RDS_USER_PWD')
rds_db_name = os.environ.get('RDS_DB_NAME')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn_string = "host=%s user=%s password=%s dbname=%s" % \
                    (rds_host, rds_username, rds_user_pwd, rds_db_name)
    print(conn_string)
    conn = psycopg2.connect(conn_string)
except:
    logger.error("ERROR: Could not connect to Postgres instance.")
    sys.exit()

def lambda_handler(event, context):
    username = event['userName']
    email = event['request']['userAttributes']['email']
    sub = event['request']['userAttributes']['sub']

    print(username)
    print(email)
    print(sub)

    query = """select count(*) from books"""

    with conn.cursor() as cur:
        rows = []
        cur.execute(query)
        for row in cur:
            rows.append(row)

    print(rows)

    # Return to Amazon Cognito
    return event

