# FiveThirtyEight - Presidential Scenario Analysis 2020

This [dataset](https://projects.fivethirtyeight.com/2020-general-data/presidential_scenario_analysis_2020.csv) is pulled nightly from the [FiveThirtyEight GitHub repository on the 2020 U.S. Election Forecasts](https://github.com/fivethirtyeight/data/tree/master/election-forecasts-2020). We pull and process it nightly as a simple approach to ensure that we are up to date with the source data.

## Original Presidential Scenario Analysis 2020 Structure:  

|Variable | Description | Type/Coding |
|---|----|--|
| cycle                | The election cycle (2020) | Text |
| branch               | The kind of race this forecast pertains to (presidential) | Text |
| model                | The model type (polls-plus is the only model we are running for the 2020 presidential race) | Text |
| modeldate            | Date of the model run | Date |
| candidate_inc        | Name of the incumbent | Text |
| candidate_chal       | Name of the challenger | Text |
| candidate_3rd        | Name of the third-party candidate | Text |
| scenario_id          | A unique identifier for each scenario | Int |
| probability          | The forecasted chance that the scenario will happen | Numeric |
| scenario_description | A description of the scenario in question | Numeric |
| timestamp            | Date and time the simulations were run | Timestamp |
| simulations          | Number of simulations run | Int |

## Data Curation & Transformation

The following operations have been performed on the source file:

- The following variables have been renamed to be more descriptive and unified by topic:

	- `cycle` -> `election_cycle`  
    - `branch` -> `race_type`  
	- `modeldate` -> `date_modeled`   
	- `candidate_inc` -> `name_incumbent`   
	- `candidate_chal` -> `name_challenger`   
	- `candidate_3rd` -> `name_third`   
	- `probability` -> `scenario_probability`
	- `timestamp` -> `simulation_timestamp`  
	- `simulations` -> `simulation_count`  
    
- The date_modeled variable has been reformatted to be an ISO 8601 date. 
- The model variable has been coded.
- The variables have be reorganized to have the modeling and simulation variables together at the end of the record.

## Transformed Structure 

|Variable | Description | Type/Coding |
|---|----|--|
| election_cycle       | The election cycle this forecast pertains to. | Text |
| race_type            | The kind of race this forecast pertains to. | Text |
| name_incumbent       | Name of the incumbent candidate. | Text |
| name_challenger      | Name of the challenging candidate. | Text |
| name_third           | Name of the third-party candidate. | Text |
| scenario_id          | A unique identifier for the scenario within the date this was modeled. | Text |
| scenario_probability | The forecasted chance that the scenario will happen. | Int |
| scenario_description | A description of the scenario in question. | Numeric |
| model                | The model type. Polls-plus is the only model being run for the 2020 presidential race (as opposed to polls-only). The polls-only model relies only on polls from a particular state, while the polls-plus model is based on state polls, national polls and endorsements as described <a href="https://en.wikipedia.org/wiki/FiveThirtyEight" target="_blank">here</a>. | 0: polls-only, 1: polls-plus |
| date_modeled         | Date of the model run | Date |
| simulation_timestamp | Date and time the simulations were run | Timestamp |
| simulation_count     | Number of simulations run | Int |
