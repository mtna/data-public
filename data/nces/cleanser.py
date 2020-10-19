import addfips
import pandas as pd
import numpy as np

variables = {
    'NCES School ID': 'school_id_nces',
    'State School ID': 'school_id_state',
    'NCES District ID': 'district_id_nces',
    'State District ID': 'district_id_state',
    'Low Grade*': 'grade_low',
    'High Grade*': 'grade_high',
    'School Name': 'school_name',
    'District': 'district_name',
    'County Name*': 'county_name',
    'Street Address': 'street_address',
    'City': 'city',
    'State': 'state',
    'ZIP': 'zip',
    'ZIP 4-digit': 'zip_4_digit',
    'Phone': 'phone_number',
    'Locale Code*': 'locale',
    'Locale*': 'locale_name',
    'Charter': 'is_charter',
    'Magnet*': 'is_magnet',
    'Title I School*': 'is_title_1_school',
    'Title 1 School Wide*': 'is_title_1_school_wide',
    'Students*': 'cnt_students',
    'Teachers*': 'cnt_teachers',
    'Student Teacher Ratio*': 'student_teacher_ratio',
    'Free Lunch*': 'is_lunch_free',
    'Reduced Lunch*': 'is_lunch_reduced'
}


def recode_bool(df, col):
    for index, row in df.iterrows():
        value = row[col]
        if value == True:
            df.loc[index, col] = 1
        elif str(value) == '–' or str(value) == '†':
            df.loc[index, col] = None
        else:
            df.loc[index, col] = 0
    return df


if __name__ == "__main__":
    # read the combined raw file
    df = pd.read_csv('./data/nces/clean/combined_raw.csv', low_memory=False)

    # normalizing nces column names
    df.rename(variables, axis="columns", inplace=True)

    # creating nces county_fips column from state and county_name values
    af = addfips.AddFIPS()
    state_fips = []
    county_fips = []
    for key, value in df['county_name'].items():
        state = df['state'][key]
        if str(state) == "nan":
            state_fips.append(None)
        else:
            state_fips.append(af.get_state_fips(state))

        if str(value) == "nan":
            county_fips.append(None)
        else:
            county_fips.append(af.get_county_fips(value, state))
    df['us_state_fips'] = state_fips
    df['us_county_fips'] = county_fips

    # ensure locale has no decimals
    df['locale'] = df['locale'].astype(pd.Int32Dtype())
    df['grade_low'] = df['grade_low'].astype(str)
    df['grade_high'] = df['grade_high'].astype(str)
    df['grade_low'] = df['grade_low'].str.replace('nan','')
    df['grade_high'] = df['grade_high'].str.replace('nan','')

    # 0 pad any ids that do not match the NCES length
    df['school_id_nces'] = df['school_id_nces'].apply(lambda x: '{0:0>12}'.format(x))
    df['district_id_nces'] = df['district_id_nces'].apply(lambda x: '{0:0>7}'.format(x))
    df['zip'] = df['zip'].apply(lambda x: '{0:0>5}'.format(x))
    df['zip_4_digit'] = df['zip_4_digit'].apply(lambda x: '{0:0>4}'.format(x))
    df['grade_low'] = df['grade_low'].apply(lambda x: '{0:0>2}'.format(x))
    df['grade_high'] = df['grade_high'].apply(lambda x: '{0:0>2}'.format(x))

    # cleaning up boolean columns
    df['is_charter'] = df['is_charter'].map({'Yes': 1, 'No': 0}) 
    df['is_charter'] = df['is_charter'].astype(pd.Int32Dtype())
    df['is_magnet'] = df['is_magnet'].map({'Yes': 1, 'No': 0}) 
    df['is_magnet'] = df['is_magnet'].astype(pd.Int32Dtype())
    df['is_title_1_school'] = df['is_title_1_school'].map({'Yes': 1, 'No': 0}) 
    df['is_title_1_school'] = df['is_title_1_school'].astype(pd.Int32Dtype())
    df['is_title_1_school_wide'] = df['is_title_1_school_wide'].map({
                                                                    'Yes': 1, 'No': 0}) 
    df['is_title_1_school_wide'] = df['is_title_1_school_wide'].astype(pd.Int32Dtype())
    df['is_lunch_free'] = df['is_lunch_free'].map({'Yes': 1, 'No': 0}) 
    df['is_lunch_free'] = df['is_lunch_free'].astype(pd.Int32Dtype())
    df['is_lunch_reduced'] = df['is_lunch_reduced'].map({'Yes': 1, 'No': 0}) 
    df['is_lunch_reduced'] = df['is_lunch_reduced'].astype(pd.Int32Dtype())


    # order the variables
    df = df[['school_id_nces', 'school_id_state', 'district_id_nces', 'district_id_state', 'grade_low', 'grade_high', 'street_address', 'city', 'us_state_fips', 'us_county_fips',
                     'zip', 'zip_4_digit', 'phone_number', 'locale', 'cnt_students', 'cnt_teachers', 'student_teacher_ratio', 'is_charter', 'is_magnet', 'is_title_1_school', 'is_title_1_school_wide', 'is_lunch_free', 'is_lunch_reduced']]

    # create clean files
    df.to_csv(f'./data/nces/clean/nces_schools.csv', header=True, index=False)
