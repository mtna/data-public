import os
import pandas as pd

variables = {
    'subject': 'poll_subject',
    'grade': 'poll_grade',
    'tracking': 'poll_type',
    'weight': 'poll_weight',
    'influence': 'poll_influence',
    'approve': 'pct_approve',
    'disapprove': 'pct_disapprove',
    'approve_adjusted': 'pct_approve_adjusted',
    'disapprove_adjusted': 'pct_disapprove_adjusted',
    'url': 'poll_url',
    'modeldate': 'date_modeled',
    'startdate': 'date_start',
    'enddate': 'date_end',
    'multiversions': 'poll_multi_version',
    'samplesize' :'sample_size'
}


def clean(data):
    df = pd.DataFrame(data)

    # Rename the file headers
    df.rename(variables, axis="columns", inplace=True)

    # Reformat dates
    df['date_modeled'] = pd.to_datetime(df['date_modeled'])
    df['date_start'] = pd.to_datetime(df['date_start'])
    df['date_end'] = pd.to_datetime(df['date_end'])

    # Code poll type
    df['poll_type'] = df['poll_type'].map({False: '0', True: '1'})

    # Make is multiversion boolean
    df['poll_multi_version'] = df['poll_multi_version'].map(lambda v: True if v == '*' else False)

    # reorder so that the cnt and new  are always next to each other in the same order
    df = df[['date_modeled', 'date_start', 'date_end', 'poll_subject', 'pollster', 'poll_grade', 'poll_type', 'poll_weight', 'poll_influence', 'poll_multi_version',
             'population', 'party', 'sample_size', 'pct_approve', 'pct_disapprove', 'pct_approve_adjusted', 'pct_disapprove_adjusted', 'timestamp', 'poll_url']]

    # order the records by date
    df = df.sort_values(by=['date_modeled', 'date_end'], ascending=False)

    return df


if __name__ == "__main__":
    path = os.path
   # Loop over the files within the raw folder
    for filename in sorted(os.listdir('./data/fivethirtyeight/covid-19-polls/approval-polls-adjusted/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/fivethirtyeight/covid-19-polls/approval-polls-adjusted/{filename}') == False:
            print(filename)
            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(
                f"./data/fivethirtyeight/covid-19-polls/approval-polls-adjusted/raw/{filename}", float_precision='round_trip')
            df = clean(data)
            df.to_csv(
                f"./data/fivethirtyeight/covid-19-polls/approval-polls-adjusted/clean/{filename}", index=False)
            # write to the latest file (clear and rewrite)
            if path.exists(f'./data/fivethirtyeight/covid-19-polls/approval-polls-adjusted/latest.csv'):
                open(
                    './data/fivethirtyeight/covid-19-polls/approval-polls-adjusted/latest.csv', 'w').close()
                df.to_csv(
                    f"./data/fivethirtyeight/covid-19-polls/approval-polls-adjusted/latest.csv", index=False)
