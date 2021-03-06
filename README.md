A lambda function to add a user's details to the "User" table in RDS PostgreSQL after confirmation

# Deployment Notes
## Importing `psycopg2` package in lambda function
`psycopg2` is a Python package used to interact with PostgreSQL databases.

As it is not available by default, a Layer has to be added to the lambda function that provides this package:
* Layer ARN: `arn:aws:lambda:ap-southeast-1:898466741470:layer:psycopg2-py38:1`

## Accessing RDS PostgreSQL instance from lambda function
To allow the lambda function to access the RDS database, the following steps need to be done:

### Grant EC2 Network Interface permissions to the lambda function's IAM Role
**Step 1: Create a policy with the following permissions:**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface",
                "ec2:DescribeInstances",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface",
                "ec2:AttachNetworkInterface"
            ],
            "Resource": "*"
        }
    ]
}
```
note: for our project, this policy has already been created
* Policy name: `AWS-Lambda-EC2-Network-Interface-Permissions`

**Step 2: Attach this policy to the function's IAM Role**

### Add the lambda function to a VPC and a Security Group
Now that the lambda function has the necessary permissions, it can be added to a VPC, and to a Security Group within the VPC.

### Add the lambda function's Security-Group to the Inbound Rules of the RDS instance's Security-Group
This allows the lambda function to access the RDS instance.

Done.