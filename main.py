import fire
from jira_issue_creator.jira_issue import JiraIssueCreator
from dotenv import load_dotenv
import os

load_dotenv()

JIRA_LOGIN = os.getenv("JIRA_LOGIN")
JIRA_PASSWORD = os.getenv("JIRA_PASSWORD")
JIRA_URL = os.getenv("JIRA_URL")


def jira_creator(
    start_date,
    end_date,
    first_period_start="08:00",
    first_period_end="12:00",
    second_period_start="13:00",
    second_period_end="17:00",
):
    jira = JiraIssueCreator(JIRA_LOGIN, JIRA_PASSWORD, JIRA_URL)
    jira.create_issues_by_date_range(
        start_date,
        end_date,
        first_period_start,
        first_period_end,
        second_period_start,
        second_period_end,
        debug=True,
    )


if __name__ == "__main__":
    fire.Fire(jira_creator)
