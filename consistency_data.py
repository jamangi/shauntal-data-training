import util

SHAUNTAL_DATA = [
    {"date": "2023-09-30", "tasks_completed": 1},
    {"date": "2023-10-01", "tasks_completed": 1},
    {"date": "2023-10-02", "tasks_completed": 1},
    {"date": "2023-10-03", "tasks_completed": 1}
]

SHAUNTAL_CONSISTENCY_TUPLES = [(datum['tasks_completed'], util.to_date(datum['date'])) for datum in SHAUNTAL_DATA]
