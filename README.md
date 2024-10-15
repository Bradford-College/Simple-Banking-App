# A simple Application to Show streamlit

## Setup the Project

1. Install the dependencies in the project folder:
    ```sh
    pip install -r requirements.txt
    ```

2. Start the app:
    ```sh
    streamlit run app.py
    ```
    or
    ```sh
    python -m streamlit run app.py
    ```

### Project Structure

```
root directory
├── Classes
│   ├── accounts.py : Class to handle account
│   ├── demousers.py : Class containing sample users
│   ├── operations.py : Class to handle account operations
│   └── users.py : Class to create the user
├── pages
│   ├── balance.py : Page to show account balance
│   ├── dashboard.py : Page to show user transactions and balance
│   ├── login.py : The login page
│   ├── logout.py : The logout page
│   └── transfer.py : The transfer page
├── app.py : The entry point for the app
├── README.md
└── requirements.txt
```
