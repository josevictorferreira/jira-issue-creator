from jira import JIRA
from dotenv import load_dotenv
from jira_issue_creator.utils import JiraUtils
import os
import datetime

load_dotenv()

JIRA_LOGIN = os.getenv("JIRA_LOGIN")
JIRA_PASSWORD = os.getenv("JIRA_PASSWORD")
JIRA_URL = os.getenv("JIRA_URL")
PROJECT_KEY = os.getenv("PROJECT_KEY")
ISSUETYPE_ID = os.getenv("ISSUETYPE_ID")
SUMMARY = os.getenv("SUMMARY")
ACTIVITY_NAME = os.getenv("ACTIVITY_NAME")
ACTIVITY_TYPE = os.getenv("ACTIVITY_TYPE")


class JiraIssueCreator:
    def __init__(self, user, password, url):
        self.jira = JIRA(url, basic_auth=(user, password))

    def list_projects(self):
        return self.jira.projects()

    def list_issue_types(self):
        return self.jira.issue_types()

    def issue_type_by_name(self, name):
        return self.jira.issue_type_by_name(name)

    def create_issue(self, init_time, end_time):
        fields = {
            "project": {"key": PROJECT_KEY},
            "summary": SUMMARY,
            "issuetype": {"id": ISSUETYPE_ID},
            "customfield_11101": ACTIVITY_NAME,
            "customfield_11111": ACTIVITY_TYPE,
            "customfield_11103": init_time,
            "customfield_11104": end_time,
        }
        return self.jira.create_issue(fields=fields)

    def create_issues_by_date_range(
        self,
        init_date,
        end_date,
        start_period_hour,
        end_period_hour,
        start_second_period_hour=None,
        end_second_period_hour=None,
        debug=False,
    ):
        print("Criando issues das datas " + init_date + " até " + end_date)
        return False
        dates = JiraUtils.get_date_range_without_holidays(init_date, end_date)
        issue_dates = JiraUtils.get_all_issue_dates(
            dates,
            start_period_hour,
            end_period_hour,
            start_second_period_hour,
            end_second_period_hour,
        )
        for day_issues in issue_dates:
            self.create_issue(day_issues[0], day_issues[1])
            if debug:
                print("Criado issue para a data " + day_issues[0])
            if day_issues[2] is not None and day_issues[3] is not None:
                self.create_issue(day_issues[2], day_issues[3])
        return None

