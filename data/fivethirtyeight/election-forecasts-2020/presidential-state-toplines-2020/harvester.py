import addfips
import os
import pandas as pd

variables = {
    'cycle': 'election_cycle',
    'branch': 'race_type',
    'modeldate': 'date_modeled',
    'candidate_inc': 'name_incumbent',
    'candidate_chal': 'name_challenger',
    'candidate_3rd': 'name_third',
    'winstate_inc': 'win_state_incumbent',
    'winstate_chal': 'win_state_challenger',
    'winstate_3rd': 'win_state_third',
    'voteshare_inc': 'voteshare_incumbent',
    'voteshare_inc_lo': 'voteshare_lo_incumbent',
    'voteshare_inc_hi': 'voteshare_hi_incumbent',
    'voteshare_chal': 'voteshare_challenger',
    'voteshare_chal_lo': 'voteshare_lo_challenger',
    'voteshare_chal_hi': 'voteshare_hi_challenger',
    'voteshare_3rd': 'voteshare_third',
    'voteshare_3rd_lo': 'voteshare_lo_third',
    'voteshare_3rd_hi': 'voteshare_hi_third',
    'voteshare_other': 'voteshare_other',
    'voteshare_other_lo': 'voteshare_lo_other',
    'voteshare_other_hi': 'voteshare_hi_other',
    'win_EC_if_win_state_inc': 'win_ec_if_win_state_incumbent',
    'win_EC_if_win_state_chal': 'win_ec_if_win_state_challenger',
    'win_state_if_win_EC_inc': 'win_state_if_win_ec_incumbent',
    'win_state_if_win_EC_chal': 'win_state_if_win_ec_challenger',
    'timestamp': 'simulation_timestamp',
    'simulations': 'simulation_count'
}


def clean(data):
    df = pd.DataFrame(data)

    # Rename the file headers
    df.rename(variables, axis="columns", inplace=True)

    # Reformat dates
    df['date_modeled'] = pd.to_datetime(df['date_modeled'])

    # Turn state names into fips code
    af = addfips.AddFIPS()
    fips = []
    for key, value in df['state'].items():
        fips.append(af.get_state_fips(value))
    df['us_state_fips'] = fips

    # Drop records where state fips is empty
    df = df.dropna(subset=['us_state_fips'])

    # Code model type
    df['model'] = df['model'].map({'polls-only': '0', 'polls-plus': '1'})

    # reorder so that the cnt and new  are always next to each other in the same order
    df = df[['election_cycle', 'race_type', 'name_incumbent', 'name_challenger', 'name_third', 'us_state_fips', 'tipping', 'vpi', 'win_state_incumbent', 'win_state_challenger', 'win_state_third', 'win_ec_if_win_state_incumbent', 'win_ec_if_win_state_challenger', 'win_state_if_win_ec_incumbent', 'win_state_if_win_ec_challenger', 'voteshare_incumbent',
             'voteshare_challenger', 'voteshare_third', 'voteshare_other', 'voteshare_lo_incumbent', 'voteshare_lo_challenger', 'voteshare_lo_third', 'voteshare_lo_other', 'voteshare_hi_incumbent', 'voteshare_hi_challenger', 'voteshare_hi_third', 'voteshare_hi_other', 'margin', 'margin_lo', 'margin_hi', 'model', 'date_modeled', 'simulation_timestamp', 'simulation_count']]

    # order the records by date
    df = df.sort_values(by=['date_modeled'], ascending=False)

    return df


if __name__ == "__main__":
    path = os.path
   # Loop over the files within the raw folder
    for filename in sorted(os.listdir('./data/fivethirtyeight/election-forecasts-2020/presidential-state-toplines-2020/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/fivethirtyeight/election-forecasts-2020/presidential-state-toplines-2020/{filename}') == False:
            print(filename)
            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(
                f"./data/fivethirtyeight/election-forecasts-2020/presidential-state-toplines-2020/raw/{filename}", float_precision='round_trip')
            df = clean(data)
            df.to_csv(
                f"./data/fivethirtyeight/election-forecasts-2020/presidential-state-toplines-2020/clean/{filename}", index=False)
            # write to the latest file (clear and rewrite)
            if path.exists(f'./data/fivethirtyeight/election-forecasts-2020/presidential-state-toplines-2020/latest.csv'):
                open('./data/fivethirtyeight/election-forecasts-2020/presidential-state-toplines-2020/latest.csv', 'w').close()
                df.to_csv(
                    f"./data/fivethirtyeight/election-forecasts-2020/presidential-state-toplines-2020/latest.csv", index=False)
