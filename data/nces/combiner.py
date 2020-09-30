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