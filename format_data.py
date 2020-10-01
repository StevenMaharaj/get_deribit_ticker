import json
from pprint import pprint

import pandas as pd

def format(path):
    print('formating into a csv')
    with open(path, "r") as f:
            rows = f.readlines()


    res_small = []
    for i in range(len(rows)):
        res = json.loads(rows[i])
        res_small += [res['params']['data']]

        for key,value in res_small[i]["stats"].items():
            res_small[i][key] = value

        del res_small[i]["stats"]



    df = pd.DataFrame(res_small)

    df.to_csv(f"{path[:-3]}csv",index=False)
    print('All done')
    print(f"You will find the file here {path[:-3]}csv")
