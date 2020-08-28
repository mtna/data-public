import os
import pandas as pd

variables = {
    'subject': 'poll_subject',
    'modeldate': 'date_modeled',
    'very_estimate': 'pct_concern_very_estimate',
    'somewhat_estimate': 'pct_concern_some_estimate',
    'not_very_estimate': 'pct_concern_not_very_estimate',
    'not_at_all_estimate': 'pct_concern_none_estimate'
}


def clean(data):
    df = pd.DataFrame(data)

    # Rename the file headers
    df.rename(variables, axis="columns", inplace=True)

    # Reformat dates
    df['date_modeled'] = pd.to_datetime(df['date_modeled'])

    # Code subject
    df['poll_subject'] = df['poll_subject'].map(
        {'concern-economy': '0', 'concern-infected': '1'})

    # reorder so that the cnt and new  are always next to each other in the same order
    df = df[['date_modeled', 'poll_subject', 'party', 'pct_concern_very_estimate',
             'pct_concern_some_estimate', 'pct_concern_not_very_estimate', 'pct_concern_none_estimate', 'timestamp']]

    # order the records by date
    df = df.sort_values(by=['date_modeled'], ascending=False)

    return df


if __name__ == "__main__":
    path = os.path
   # Loop over the files within the raw folder
    for filename in sorted(os.listdir('./data/fivethirtyeight/covid-19-polls/concern-toplines/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/fivethirtyeight/covid-19-polls/concern-toplines/{filename}') == False:
            print(filename)
            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(
                f"./data/fivethirtyeight/covid-19-polls/concern-toplines/raw/{filename}", float_precision='round_trip')
            df = clean(data)
            df.to_csv(
                f"./data/fivethirtyeight/covid-19-polls/concern-toplines/clean/{filename}", index=False)
            # write to the latest file (clear and rewrite)
            if path.exists(f'./data/fivethirtyeight/covid-19-polls/concern-toplines/latest.csv'):
                open(
                    './data/fivethirtyeight/covid-19-polls/concern-toplines/latest.csv', 'w').close()
                df.to_csv(
                    f"./data/fivethirtyeight/covid-19-polls/concern-toplines/latest.csv", index=False)
