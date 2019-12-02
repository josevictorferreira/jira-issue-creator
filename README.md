
## Jira Issue Creator

    A Jira tool for helping creating a bunch of issues on Jira, each one corresponding a timesheet.

### Installation and Setup

    * Install poetry `pip install poetry --user`.
    * Enter the poetry virtual environment `poetry shell`.
    * Create a `.env` file in the root path of the project `touch .env`.
        * Fill the .env file with corresponding variables needed:
            ```
            JIRA_LOGIN=youruser
            JIRA_PASSWORD=yourjirapassword
            JIRA_URL=http://jira.lanet.accorservices.net/
            PROJECT_KEY=TSITEC
            ISSUETYPE_ID=10800
            SUMMARY=Desenvolvimento
            ACTIVITY_NAME=TKT-1785 - Ticket Conecte
            ACTIVITY_TYPE=Desenvolvimento de Software
            COUNTRY=BR
            STATE=PR
            TIMEZONE=-03
            ```
    * Run the command line tool:
        * Example: Create a all issues needed for 01/11/2019 to 30/11/2019:
            `python main.py --start_date=01/11/2019 --end_date=30/11/2019 --first_period_start=08:00 --first_period_end=12:00 --second_period_start=13:00 --second_period_end=17:00`
        * Example 2: Create all issues needed for 01/11/2019 to 30/11/2019 but with only one period:
            `python main.py --start_date=01/11/2019 --end_date=30/11/2019 --first_period_start=08:00 --first_period_end=12:00`
