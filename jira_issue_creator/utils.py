import datetime
import holidays
from dotenv import load_dotenv
import os

load_dotenv()

COUNTRY = os.getenv("COUNTRY")
STATE = os.getenv("STATE")
TIMEZONE = os.getenv("TIMEZONE")


class JiraUtils:
    @staticmethod
    def get_date_range(init_date, end_date):
        """
        Return a list of dates between a date range without weekends.
        """
        start = datetime.datetime.strptime(init_date, "%d/%m/%Y")
        end = datetime.datetime.strptime(end_date, "%d/%m/%Y")
        weekdays = [6, 7]
        dates = [
            start + datetime.timedelta(days=x)
            for x in range(0, (end - start).days)
        ]
        return list(filter(lambda day: day.isoweekday() not in weekdays, dates))

    @staticmethod
    def get_date_range_without_holidays(init_date, end_date):
        """
        Return a list of dates between a date range without weekends and
        holidays.
        """
        all_hollidays = JiraUtils.get_hollidays()
        return list(
            filter(
                lambda day: day not in all_hollidays,
                JiraUtils.get_date_range(init_date, end_date),
            )
        )

    @staticmethod
    def get_all_issue_dates(
        dates,
        first_period_start="08:00",
        first_period_end="12:00",
        second_period_start=None,
        second_period_end=None,
    ):
        """ Add all period dates to a given range of dates. """
        return list(
            map(
                lambda date: list(
                    filter(
                        lambda x: x is not None,
                        [
                            JiraUtils.format_date_to_string(
                                date, first_period_start
                            ),
                            JiraUtils.format_date_to_string(
                                date, first_period_end
                            ),
                            JiraUtils.format_date_to_string(
                                date, second_period_start
                            ),
                            JiraUtils.format_date_to_string(
                                date, second_period_end
                            ),
                        ],
                    )
                ),
                dates,
            )
        )

    @staticmethod
    def format_date_to_string(date, hour):
        """ Format a date to string, in the required JIRA format. """
        if hour is None:
            return None
        return (
            date.strftime("%Y-%m-%d") + "T" + hour + ":00.000" + TIMEZONE + "00"
        )

    @staticmethod
    def get_hollidays():
        """ Return all holidays in the current country and state."""
        return holidays.CountryHoliday(COUNTRY, prov=None, state=STATE)

