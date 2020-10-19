import os
import pandas as pd

if __name__ == "__main__":
    path = os.path
    df = None
    
    # Loop over the files within the folder
    for filename in os.listdir('./data/nces/raw'):
            if filename.endswith('.csv'):
                data = pd.read_csv(f"./data/nces/raw/{filename}")
                if df is None:
                    print("Initializing: "+filename)
                    df = data
                else:
                    print("Concat: "+filename)
                    df = pd.concat([df, data], axis=0)
            
    df = df.sort_values(by=['State School ID'])


    # ensure the 4 digit zip does not have decimals
    df['ZIP'] = df['ZIP'].astype(pd.Int32Dtype())
    df['ZIP'] = df['ZIP'].astype(str)
    df['ZIP 4-digit'] = df['ZIP 4-digit'].astype(pd.Int32Dtype())
    df['ZIP 4-digit'] = df['ZIP 4-digit'].astype(str)
    df['ZIP 4-digit'] = df['ZIP 4-digit'].str.replace('<NA>','')

    # 0 pad any ids that do not match the NCES length
    df['NCES School ID'] = df['NCES School ID'].apply(lambda x: '{0:0>12}'.format(x))
    df['NCES District ID'] = df['NCES District ID'].apply(lambda x: '{0:0>7}'.format(x))
    df['ZIP'] = df['ZIP'].apply(lambda x: '{0:0>5}'.format(x))
    df['ZIP 4-digit'] = df['ZIP 4-digit'].apply(lambda x: '{0:0>4}'.format(x))

    df.to_csv(f"./data/nces/clean/combined_raw.csv", header=True, index=False)

    # remove the special characters from the data
    # Read in the file
    with open('./data/nces/clean/combined_raw.csv', 'r') as file :
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('–', '')
    filedata = filedata.replace('†', '')

    # Write the file out again
    with open('./data/nces/clean/combined_raw.csv', 'w') as file:
        file.write(filedata)