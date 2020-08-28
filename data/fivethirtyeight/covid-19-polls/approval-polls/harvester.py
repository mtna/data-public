import os
import pandas as pd

variables = {
    'subject': 'poll_subject',
    'tracking': 'poll_type',
    'sponsor': 'poll_sponsor',
    'text': 'question_text',
    'approve': 'pct_approve',
    'disapprove': 'pct_disapprove',
    'url': 'poll_url',
    'start_date': 'date_start',
    'end_date': 'date_end'
}


def clean(data):
    df = pd.DataFrame(data)

    # Rename the file headers
    df.rename(variables, axis="columns", inplace=True)

    # Reformat dates
    df['date_start'] = pd.to_datetime(df['date_start'])
    df['date_end'] = pd.to_datetime(df['date_end'])

    # Code poll type
    df['poll_type'] = df['poll_type'].map({False: '0', True: '1'})

    # reorder so that the cnt and new  are always next to each other in the same order
    df = df[['date_start', 'date_end', 'pollster', 'poll_sponsor', 'poll_type', 'poll_subject', 'question_text',  'population',
             'party', 'sample_size', 'pct_approve', 'pct_disapprove', 'poll_url']]

    # order the records by date
    df = df.sort_values(by=['date_end'], ascending=False)

    return df


if __name__ == "__main__":
    path = os.path
   # Loop over the files within the raw folder
    for filename in sorted(os.listdir('./data/fivethirtyeight/covid-19-polls/approval-polls/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/fivethirtyeight/covid-19-polls/approval-polls/{filename}') == False:
            print(filename)
            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(
                f"./data/fivethirtyeight/covid-19-polls/approval-polls/raw/{filename}", float_precision='round_trip')
            df = clean(data)
            df.to_csv(
                f"./data/fivethirtyeight/covid-19-polls/approval-polls/clean/{filename}", index=False)
            # write to the latest file (clear and rewrite)
            if path.exists(f'./data/fivethirtyeight/covid-19-polls/approval-polls/latest.csv'):
                open('./data/fivethirtyeight/covid-19-polls/approval-polls/latest.csv', 'w').close()
                df.to_csv(
                    f"./data/fivethirtyeight/covid-19-polls/approval-polls/latest.csv", index=False)
