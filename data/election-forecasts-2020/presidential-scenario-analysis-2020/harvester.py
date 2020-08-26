import os
import pandas as pd

variables = {
    'cycle': 'election_cycle',
    'branch': 'race_type',
    'modeldate': 'date_modeled',
    'candidate_inc': 'name_incumbent',
    'candidate_chal': 'name_challenger',
    'candidate_3rd': 'name_third',
    'probability': 'scenario_probability',
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

    # reorder so that the cnt and new  are always next to each other in the same order
    df = df[['election_cycle', 'race_type', 'name_incumbent', 'name_challenger', 'name_third', 'scenario_id',
             'scenario_probability', 'scenario_description', 'model', 'date_modeled', 'simulation_timestamp', 'simulation_count']]

    df['scenario_id'] = df['scenario_id'].astype(pd.Int32Dtype())

    # order the records by date
    df = df.sort_values(
        by=['date_modeled', 'scenario_id'], ascending=[False, True])

    return df


if __name__ == "__main__":
    path = os.path
   # Loop over the files within the raw folder
    for filename in sorted(os.listdir('./data/fivethirtyeight/election-forecasts-2020/presidential-scenario-analysis-2020/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/fivethirtyeight/election-forecasts-2020/presidential-scenario-analysis-2020/{filename}') == False:
            print(filename)
            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(
                f"./data/fivethirtyeight/election-forecasts-2020/presidential-scenario-analysis-2020/raw/{filename}", float_precision='round_trip')
            df = clean(data)
            df.to_csv(
                f"./data/fivethirtyeight/election-forecasts-2020/presidential-scenario-analysis-2020/clean/{filename}", index=False)
            # write to the latest file (clear and rewrite)
            if path.exists(f'./data/fivethirtyeight/election-forecasts-2020/presidential-scenario-analysis-2020/latest.csv'):
                open('./data/fivethirtyeight/election-forecasts-2020/presidential-scenario-analysis-2020/latest.csv', 'w').close()
                df.to_csv(
                    f"./data/fivethirtyeight/election-forecasts-2020/presidential-scenario-analysis-2020/latest.csv", index=False)
