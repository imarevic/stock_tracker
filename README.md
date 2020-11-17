## Stock Tracker

A stock tracking email service that sends stock drops relative to a specific reference percentage from the previous day. The data is retrieved from www.finanzen.net. This service can be deployed on any on-premise or cloud infrastructure.

---
**Setup**

1. install aws CLI tool: `https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html`
2. create an aws credentials file using aws CLI tool by running `aws configure` and entering required information.
3. create a `config.yaml` file in `config/config.yaml` with the following structure:
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
6. create a virtual environment and install required packages: `pip install requirements.txt`
7. you can execute the program manually via `python src/main.py`
8. the service can also be deployed on any cloud infrastructure (AWS, GCP, Azure)

---
**License**

Apache Software License 2.0