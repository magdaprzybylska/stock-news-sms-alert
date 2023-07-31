from datetime import datetime, timedelta


class CheckDate:
    def __init__(self):
        self.last_day = ''
        self.before_last_day = ''
        self.today = datetime.today()
        self.check_day()

    def check_day(self):

        if datetime.weekday(self.today) == 6:
            last_day_raw = datetime.now() - timedelta(2)
            self.last_day = datetime.strftime(last_day_raw, '%Y-%m-%d')

            before_last_day_raw = datetime.now() - timedelta(3)
            self.before_last_day = datetime.strftime(before_last_day_raw, '%Y-%m-%d')

        elif datetime.weekday(self.today) == 0:
            last_day_raw = datetime.now() - timedelta(3)
            self.last_day = datetime.strftime(last_day_raw, '%Y-%m-%d')

            before_last_day_raw = datetime.now() - timedelta(4)
            self.before_last_day = datetime.strftime(before_last_day_raw, '%Y-%m-%d')

        elif datetime.weekday(self.today) == 1:
            last_day_raw = datetime.now() - timedelta(1)
            self.last_day = datetime.strftime(last_day_raw, '%Y-%m-%d')

            before_last_day_raw = datetime.now() - timedelta(4)
            self.before_last_day = datetime.strftime(before_last_day_raw, '%Y-%m-%d')

        else:
            last_day_raw = datetime.now() - timedelta(1)
            self.last_day = datetime.strftime(last_day_raw, '%Y-%m-%d')

            before_last_day_raw = datetime.now() - timedelta(2)
            self.before_last_day = datetime.strftime(before_last_day_raw, '%Y-%m-%d')