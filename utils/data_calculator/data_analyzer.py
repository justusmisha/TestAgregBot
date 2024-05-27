import asyncio
from datetime import datetime, timedelta
from data.db_base import conn


class DataCalculator:
    def __init__(self, data):
        self.data = data
        self.dt_from = self.str_to_dict()["dt_from"]
        self.dt_upto = self.str_to_dict()["dt_upto"]
        self.group_type = self.str_to_dict()["group_type"]

    def str_to_dict(self):
        time_mapping = {
            'month': '%Y-%m',
            'day': '%Y-%m-%d',
            'hour': '%Y-%m-%d %H'
        }
        query = self.data.split('"')
        query = query[1::2]
        result_dict = {query[i]: query[i + 1] for i in range(0, len(query), 2)}
        result_dict["dt_from"] = datetime.strptime(result_dict["dt_from"], "%Y-%m-%dT%H:%M:%S")
        result_dict["dt_upto"] = datetime.strptime(result_dict["dt_upto"], "%Y-%m-%dT%H:%M:%S")
        result_dict["group_type"] = time_mapping.get(result_dict["group_type"])
        return result_dict

    async def data_calculation(self):
        result = {"dataset": [], "labels": []}
        current_date = self.dt_from
        while current_date <= self.dt_upto:
            end_date = self.calculate_end_date(current_date)
            data_sum = 0
            for i in await conn():
                i_date = i["dt"]
                if current_date <= i_date < end_date:
                    try:
                        data_sum += i['value']
                    except ValueError:
                        print('Values not correct')
            result["dataset"].append(data_sum)
            result["labels"].append(current_date.strftime("%Y-%m-%dT%H:%M:%S"))
            current_date = end_date
        return result

    def calculate_end_date(self, current_date):
        if self.group_type == "%Y-%m":
            return (current_date.replace(day=1) + timedelta(days=31)).replace(day=1)
        elif self.group_type == "%Y-%m-%d":
            return current_date + timedelta(days=1)
        elif self.group_type == "%Y-%m-%d %H":
            return current_date + timedelta(hours=1)
        else:
            raise ValueError("Invalid group_type")
