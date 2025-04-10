This project contains Python scripts and setup instructions to automatically start and stop an AWS EC2 instance at specific times on weekdays (Monday to Friday) using Windows Task Scheduler.

📦 Contents
start_instance.py – Starts the EC2 instance

stop_instance.py – Stops the EC2 instance

Scheduled via Task Scheduler to run at any time. E.g.:

5:00 AM CST → Start

8:00 PM CST → Stop

⚙️ Prerequisites
Before you begin:

✅ Python installed on your Windows machine

✅ AWS CLI installed and configured with valid credentials

✅ EC2 instance with proper permissions to be started/stopped

🧩 Step-by-Step Setup
1. ✅ Install Python (if not already)
Download from: https://www.python.org/downloads/
python --version

2. ✅ Install AWS CLI
Download & install the AWS CLI from:
👉 https://awscli.amazonaws.com/AWSCLIV2.msi
After install, open Command Prompt and run:
aws --version

4. ✅ Configure AWS Credentials
Run this command:
aws configure
Enter your credentials:
AWS Access Key ID     : YOUR_ACCESS_KEY
AWS Secret Access Key : YOUR_SECRET_KEY
Default region name   : us-east-1
Default output format : json
Credentials will be saved in:
C:\Users\Administrator\.aws\credentials

4. ✅ Place Your Python Scripts
Create or download the following scripts into:
C:\Users\Administrator\Desktop\EC2_Auto_stop_start\

Copy and paste the 2 stop and start python code in this repo
start_instance.py
stop_instance.py

    
🗓️ Schedule the Tasks (Task Scheduler)
✅ Schedule Start Script (5:00 AM CST, Weekdays)

"C:\Users\Administrator\Desktop\EC2_Auto_stop_start\start_instance.py"
C:\Users\Administrator\Desktop\EC2_Auto_stop_start
"C:\Users\Administrator\Desktop\EC2_Auto_stop_start\stop_instance.py"

Manually run below commands for testing in CMD.
python "C:\Users\Administrator\Desktop\EC2_Auto_stop_start\start_instance.py"
python "C:\Users\Administrator\Desktop\EC2_Auto_stop_start\stop_instance.py"
If you see the messages:
Instance i-064c70326f14d183e started.
Instance i-064c70326f14d183e stopped.
✅ You're all set!

🔐 IAM Permissions Required
The IAM role or user must have this policy attached:

json
Copy
Edit
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    }
  ]
}


Scripts run only on weekdays – no unnecessary EC2 billing on weekends.

The instance ID used is: i-064c70326f14d183e (replace with yours if different).

You can expand this to support logging, email notifications, or EC2 health checks.
