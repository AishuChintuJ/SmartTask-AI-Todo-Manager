import pandas as pd

from database.db import get_tasks


def export_csv(user_id):

    tasks = get_tasks(user_id)

    data = []


    for t in tasks:

        data.append(

            {
                "Task": t[2],

                "Category": t[3],

                "Priority": t[4],

                "Due Date": t[5],

                "Status": t[6]
            }

        )


    df = pd.DataFrame(data)


    df.to_csv(

        "tasks_export.csv",

        index=False

    )


    return True