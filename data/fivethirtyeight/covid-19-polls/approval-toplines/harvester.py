import os
import pandas as pd

variables = {
    'subject': 'poll_subject',
    'modeldate': 'date_modeled',
    'approve_estimate': 'pct_approve_estimate',
    'disapprove_estimate': 'pct_disapprove_estimate'
}


def clean(data):
    df = pd.DataFrame(data)

    # Rename the file headers
    df.rename(variables, axis="columns", inplace=True)

    # Reformat dates
    df['date_modeled'] = pd.to_datetime(df['date_modeled'])

    # reorder so that the cnt and new  are always next to each other in the same order
    df = df[['date_modeled', 'poll_subject', 'party',
             'pct_approve_estimate', 'pct_disapprove_estimate',  'timestamp']]

    # order the records by date
    df = df.sort_values(by=['date_modeled'], ascending=False)

    return df


if __name__ == "__main__":
    path = os.path
   # Loop over the files within the raw folder
    for filename in sorted(os.listdir('./data/fivethirtyeight/covid-19-polls/approval-toplines/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/fivethirtyeight/covid-19-polls/approval-toplines/{filename}') == False:
            print(filename)
            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(
                f"./data/fivethirtyeight/covid-19-polls/approval-toplines/raw/{filename}", float_precision='round_trip')
            df = clean(data)
            df.to_csv(
                f"./data/fivethirtyeight/covid-19-polls/approval-toplines/clean/{filename}", index=False)
            # write to the latest file (clear and rewrite)
            if path.exists(f'./data/fivethirtyeight/covid-19-polls/approval-toplines/latest.csv'):
                open(
                    './data/fivethirtyeight/covid-19-polls/approval-toplines/latest.csv', 'w').close()
                df.to_csv(
                    f"./data/fivethirtyeight/covid-19-polls/approval-toplines/latest.csv", index=False)
