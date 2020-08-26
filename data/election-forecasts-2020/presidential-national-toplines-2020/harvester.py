import os
import pandas as pd


variables = {
    'cycle': 'election_cycle',
    'branch': 'race_type',
    'modeldate': 'date_modeled',
    'candidate_inc': 'name_incumbent',
    'candidate_chal': 'name_challenger',
    'candidate_3rd': 'name_third',
    'ecwin_inc': 'win_ec_incumbent',
    'ecwin_chal': 'win_ec_challenger',
    'ecwin_3rd': 'win_ec_third',
    'ec_nomajority': 'win_ec_none',
    'popwin_inc': 'win_pop_incumbent',
    'popwin_chal': 'win_pop_challenger',
    'popwin_3rd': 'win_pop_third',
    'ev_inc': 'votes_ec_incumbent',
    'ev_chal': 'votes_ec_challenger',
    'ev_3rd': 'votes_ec_third',
    'ev_inc_lo': 'votes_ec_lo_incumbent',
    'ev_chal_lo': 'votes_ec_lo_challenger',
    'ev_3rd_lo': 'votes_ec_lo_third',
    'ev_inc_hi': 'votes_ec_hi_incumbent',
    'ev_chal_hi': 'votes_ec_hi_challenger',
    'ev_3rd_hi': 'votes_ec_hi_third',
    'national_voteshare_inc': 'voteshare_nat_incumbent',
    'national_voteshare_chal': 'voteshare_nat_challenger',
    'national_voteshare_3rd': 'voteshare_nat_third',
    'nat_voteshare_other': 'voteshare_nat_other',
    'national_voteshare_chal_lo': 'voteshare_nat_lo_incumbent',
    'national_voteshare_inc_lo': 'voteshare_nat_lo_challenger',
    'national_voteshare_3rd_lo': 'voteshare_nat_lo_third',
    'nat_voteshare_other_lo': 'voteshare_nat_lo_other',
    'national_voteshare_inc_hi': 'voteshare_nat_hi_incumbent',
    'national_voteshare_chal_hi': 'voteshare_nat_hi_challenger',
    'national_voteshare_3rd_hi': 'voteshare_nat_hi_third',
    'nat_voteshare_other_hi': 'voteshare_nat_hi_other',
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
    df = df[['election_cycle', 'race_type', 'name_incumbent', 'name_challenger', 'name_third', 'win_ec_incumbent',
             'win_ec_challenger', 'win_ec_third', 'win_ec_none', 'win_pop_incumbent', 'win_pop_challenger', 'win_pop_third',
             'votes_ec_incumbent', 'votes_ec_challenger', 'votes_ec_third', 'votes_ec_lo_incumbent', 'votes_ec_lo_challenger',
             'votes_ec_lo_third', 'votes_ec_hi_incumbent', 'votes_ec_hi_challenger', 'votes_ec_hi_third',
             'voteshare_nat_incumbent', 'voteshare_nat_challenger', 'voteshare_nat_third', 'voteshare_nat_other',
             'voteshare_nat_lo_incumbent', 'voteshare_nat_lo_challenger', 'voteshare_nat_lo_third', 'voteshare_nat_lo_other',
             'voteshare_nat_hi_incumbent', 'voteshare_nat_hi_challenger', 'voteshare_nat_hi_third', 'voteshare_nat_hi_other',
             'model', 'date_modeled', 'simulation_timestamp', 'simulation_count']]

    # order the records by date
    df = df.sort_values(by=['date_modeled'], ascending=False)

    return df


if __name__ == "__main__":
    path = os.path
   # Loop over the files within the raw folder
    for filename in sorted(os.listdir('./data/fivethirtyeight/election-forecasts-2020/presidential-national-toplines-2020/raw')):
        if filename.endswith('.csv') and path.exists(f'./data/fivethirtyeight/election-forecasts-2020/presidential-national-toplines-2020/{filename}') == False:
            print(filename)
            # For each csv file, map the transformed data to its respective file in the harvested folder
            data = pd.read_csv(f"./data/fivethirtyeight/election-forecasts-2020/presidential-national-toplines-2020/raw/{filename}", float_precision='round_trip')
            df = clean(data)
            df.to_csv(f"./data/fivethirtyeight/election-forecasts-2020/presidential-national-toplines-2020/clean/{filename}", index=False)
            #write to the latest file (clear and rewrite)
            if path.exists(f'./data/fivethirtyeight/election-forecasts-2020/presidential-national-toplines-2020/latest.csv'):
                open('./data/fivethirtyeight/election-forecasts-2020/presidential-national-toplines-2020/latest.csv', 'w').close()
                df.to_csv(f"./data/fivethirtyeight/election-forecasts-2020/presidential-national-toplines-2020/latest.csv", index=False)