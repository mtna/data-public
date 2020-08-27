import os
import pandas as pd


variables = {
    'cycle': 'election_cycle',
    'branch': 'race_type',
    'modeldate': 'date_modeled',
    'candidate_inc': 'name_incumbent',
    'candidate_chal': 'name_challenger',
    'candidate_3rd': 'name_third',
    'indicator': 'indicator_name',
    'category': 'indicator_category',
    'current_zscore': 'zscore_current',
    'projected_zscore': 'zscore_projected',
    'projected_hi': 'zscore_projected_lo',
    'projected_lo': 'zscore_projected_hi',
    'timestamp': 'simulation_timestamp',
    'simulations': 'simulation_count'
}


def clean(data):
    df = pd.DataFrame(data)

    # Rename the file headers
    df.rename(variables, axis="columns", inplace=True)

    # Reformat dates
    df['date_modeled'] = pd.to_datetime(df['date_modeled'])

    # Code model type
    df['model'] = df['model'].map({'polls-only': '0', 'polls-plus': '1'})

    # Code indicator category
    df['indicator_category'] = df['indicator_category'].map({'stock market' : '0', 'spending' : '1', 'manufacturing' : '2', 'jobs' : '3', 'inflation' : '4', 'income' : '5', 'combined' : '6'})

    # reorder so that the cnt and new  are always next to each other in the same order
    df = df[['election_cycle', 'race_type', 'name_incumbent', 'name_challenger', 'name_third', 'indicator_name', 'indicator_category', 'zscore_current',
             'zscore_projected', 'zscore_projected_lo', 'zscore_projected_hi', 'model', 'date_modeled', 'simulation_timestamp', 'simulation_count']]

    # order the records by date
    df = df.sort_values(by=['date_modeled','indicator_category'], ascending=[False, True])

    return df


if __name__ == "__main__":
    path = os.path
   # Loop over the files within the raw folder
    for filename in sorted(os.listdir('./data/fivethirtyeight/election-forecasts-2020/economic-index/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/fivethirtyeight/election-forecasts-2020/economic-index/{filename}') == False:
            print(filename)
            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(
                f"./data/fivethirtyeight/election-forecasts-2020/economic-index/raw/{filename}", float_precision='round_trip')
            df = clean(data)
            df.to_csv(
                f"./data/fivethirtyeight/election-forecasts-2020/economic-index/clean/{filename}", index=False)
            # write to the latest file (clear and rewrite)
            if path.exists(f'./data/fivethirtyeight/election-forecasts-2020/economic-index/latest.csv'):
                open('./data/fivethirtyeight/election-forecasts-2020/economic-index/latest.csv', 'w').close()
                df.to_csv(
                    f"./data/fivethirtyeight/election-forecasts-2020/economic-index/latest.csv", index=False)
