## Stock Tracker

A stock tracking email service that sends stock drops relative to a specific reference percentage from the previous day. The data is retrieved from www.finanzen.net. This service can be deployed on AWS (see *setup* section).

---
**Setup**

1. create a virtual environment and install required packages: `pip install requirements.txt`
2. install aws CLI tool: `https://aws.amazon.com/cli/`
3. create aws credentials file using aws CLI tool by running `aws configure` and entering required information.
4. create a `config.yaml` file in `config/config.yaml` with the following structure:
    ```
    appName: stock_tracker

    aws:
        region: <REGION>

    mailing:
        sender: <SENDER@SAMPLE.com>
        recipients:
            - RECIPIENT1@SAMPLE.com
            - RECIPIENT2@SAMPLE.com
    ```
5. specifiy the percentage drop in `src/consts.py`
6. you can execute the program manually via `python src/main.py`
7. deployment on AWS:
    - step 1
    - step 2
    - step 3

---
**License**

Apache Software License 2.0