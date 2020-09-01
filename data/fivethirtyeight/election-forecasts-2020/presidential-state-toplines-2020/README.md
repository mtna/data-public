# FiveThirtyEight - State Toplines 2020

This [dataset](https://projects.fivethirtyeight.com/2020-general-data/presidential_state_toplines_2020.csv) is pulled nightly from the [FiveThirtyEight GitHub repository on the 2020 U.S. Election Forecasts](https://github.com/fivethirtyeight/data/tree/master/election-forecasts-2020). We pull and process it nightly as a simple approach to ensure that we are up to date with the source data.


## Original State Toplines 2020 Structure:  

|Variable | Description | Type/Coding |
|---|----|--|
| cycle                    | The election cycle (2020) | Text |
| branch                   | The kind of race this forecast pertains to (presidential) | Text |
| model                    | The model type (polls-plus is the only model we are running for the 2020 presidential race) | Text |
| modeldate                | Date of the model run | Date |
| candidate_inc            | Name of the incumbent | Text |
| candidate_chal           | Name of the challenger | Text |
| candidate_3rd            | Name of the third-party candidate | Text |
| state                    | Name of the state | Numeric |
| tipping                  | Tipping-point chance, the chance the state will deliver the decisive vote in the Electoral College | Numeric |
| vpi                      | Voter power index, the relative likelihood that an individual voter in the state will determine the Electoral College winner | Numeric |
| winstate_inc             | Chance the incumbent will win the state | Numeric |
| winstate_chal            | Chance the challenger will win the state | Numeric |
| winstate_3rd             | Chance the third-party candidate will win the state | Numeric |
| voteshare_inc            | Forecasted vote share for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_inc_lo         | Forecasted vote share for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_inc_hi         | Forecasted vote share for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_chal           | Forecasted vote share for the challenger, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_chal_lo        | Forecasted vote share for the challenger, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_chal_hi        | Forecasted vote share for the challenger, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_3rd            | Forecasted vote share for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_3rd_lo         | Forecasted vote share for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_3rd_hi         | Forecasted vote share for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | InNumerict |
| voteshare_other          | Forecasted vote share for other candidates, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_other_lo       | Forecasted vote share for other candidates, including the upper and lower bounds of an 80% confidence interval | Numeric |
| voteshare_other_hi       | Forecasted vote share for other candidates, including the upper and lower bounds of an 80% confidence interval | Numeric |
| margin                   | Forecasted margin for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| margin_lo                | Forecasted margin for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| margin_hi                | Forecasted margin for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| win_EC_if_win_state_inc  | Chance that the incumbent will win the Electoral College if they win this state | Numeric |
| win_EC_if_win_state_chal | Chance that the challenger will win the Electoral College if they win this state | Numeric |
| win_state_if_win_EC_inc  | Chance that the incumbent will win this state if they win the Electoral College | Numeric |
| win_state_if_win_EC_inc  | Chance that the challenger will win this state if they win the Electoral College | Numeric |
| timestamp                | Date and time the simulations were run | Timestamp |
| simulations              | Number of simulations run | Int |

## Data Curation & Transformation

The following operations have been performed on the source file:

- The following variables have been renamed to be more descriptive and unified by topic:

	- `cycle` -> `election_cycle`  
    - `branch` -> `race_type`  
	- `modeldate` -> `date_modeled`   
	- `candidate_inc` -> `name_incumbent`   
	- `candidate_chal` -> `name_challenger`   
	- `candidate_3rd` -> `name_third`   
	- `winstate_inc` -> `win_state_incumbent`
    - `winstate_chal` -> `win_state_challenger`
    - `winstate_3rd` -> `win_state_third`
    - `voteshare_inc` -> `voteshare_incumbent`
    - `voteshare_inc_lo` -> `voteshare_lo_incumbent`
    - `voteshare_inc_hi` -> `voteshare_hi_incumbent`
    - `voteshare_chal` -> `voteshare_challenger`
    - `voteshare_chal_lo` -> `voteshare_lo_challenger`
    - `voteshare_chal_hi` -> `voteshare_hi_challenger`
    - `voteshare_3rd` -> `voteshare_third`
    - `voteshare_3rd_lo` -> `voteshare_lo_third`
    - `voteshare_3rd_hi` -> `voteshare_hi_third`
    - `voteshare_other` -> `voteshare_other`
    - `voteshare_other_lo` -> `voteshare_lo_other`
    - `voteshare_other_hi` -> `voteshare_hi_other`
    - `win_EC_if_win_state_inc` -> `win_ec_if_win_state_incumbent`
    - `win_EC_if_win_state_chal` -> `win_ec_if_win_state_challenger`
    - `win_state_if_win_EC_inc` -> `win_state_if_win_ec_incumbent`
    - `win_state_if_win_EC_chal` -> `win_state_if_win_ec_challenger`
	- `timestamp` -> `simulation_timestamp`  
	- `simulations` -> `simulation_count`  
    
- The date_modeled variable has been reformatted to be an ISO 8601 date. 
- The model variable has been coded.
- The state variable has been replaced with us_state_fips which has FIPS codes instead of state names.
- There were several records whose states were congressional districts, these have been dropped. 
- The variables have be reorganized to have variables about the chance to win the Electoral College based on a state victory (and vice versa) grouped near the chances of state victory.
- The variables have be reorganized to have the modeling and simulation variables together at the end of the record.

## Transformed Structure 

|Variable | Description | Type/Coding |
|---|----|--|
| election_cycle                 | The election cycle this forecast pertains to. | Text |
| race_type                      | The kind of race this forecast pertains to. | Text |
| name_incumbent                 | Name of the incumbent candidate. | Text |
| name_challenger                | Name of the challenging candidate. | Text |
| name_third                     | Name of the third-party candidate. | Text |
| us_state_fips                  | The U.S. FIPS 5-2 state code. | Text |
| tipping                        | The chance this state will deliver the decisive vote in the Electoral College. | Numeric |
| vpi                            | The relative likelihood that an individual voter in the state will determine the Electoral College winner. | Numeric |
| win_state_incumbent            | The chance that the incumbent will win the state. | Numeric |
| win_state_challenger           | The chance that the challenger will win the state. | Numeric |
| win_state_third                | The chance that the third-party candidate will win the state. | Numeric |
| win_ec_if_win_state_incumbent  | The chance that the incumbent will win the Electoral College if they win this state. | Numeric |
| win_ec_if_win_state_challenger | The chance that the challenger will win the Electoral College if they win this state. | Numeric |
| win_state_if_win_ec_incumbent  | The chance that the incumbent will win this state if they win the Electoral College. | Numeric |
| win_state_if_win_ec_challenger | The chance that the challenger will win this state if they win the Electoral College. | Numeric |
| voteshare_incumbent            | The forecasted vote share for the incumbent. | Numeric |
| voteshare_challenger           | The forecasted vote share for the challenger. | Numeric |
| voteshare_third                | The forecasted vote share for the third-party candidate. | Numeric |
| voteshare_other                | The forecasted vote share for all the other candidates. | Numeric |
| voteshare_lo_incumbent         | The forecasted vote share for the incumbent - lower bound of 80% confidence interval. | Numeric |
| voteshare_lo_challenger        | The forecasted vote share for the challenger - lower bound of 80% confidence interval. | Numeric |
| voteshare_lo_third             | The forecasted vote share for the third-party candidate - lower bound of 80% confidence interval. | Numeric |
| voteshare_lo_other             | The forecasted vote share for all the other candidates - lower bound of 80% confidence interval. | Numeric |
| voteshare_hi_incumbent         | The forecasted vote share for the incumbent - upper bound of 80% confidence interval. | Numeric |
| voteshare_hi_challenger        | The forecasted vote share for the challenger - upper bound of 80% confidence interval. | Numeric |
| voteshare_hi_third             | The forecasted vote share for the third-party candidate - upper bound of 80% confidence interval. | Numeric |
| voteshare_hi_other             | The forecasted vote share for all the other candidates - upper bound of 80% confidence interval. | Numeric |
| margin                         | The forecasted margin for the incumbent. | Numeric |
| margin_lo                      | The forecasted margin for the incumbent - lower bound of 80% confidence interval. | Numeric |
| margin_hi                      | The forecasted margin for the incumbent - upper bound of 80% confidence interval. | Numeric |
| model                          | The model type. Polls-plus is the only model being run for the 2020 presidential race (as opposed to polls-only). The polls-only model relies only on polls from a particular state, while the polls-plus model is based on state polls, national polls and endorsements as described <a href="https://en.wikipedia.org/wiki/FiveThirtyEight" target="_blank">here</a>. | 0: polls-only, 1: polls-plus |
| date_modeled                   | Date of the model run | Date |
| simulation_timestamp           | Date and time the simulations were run | Timestamp |
| simulation_count               | Number of simulations run | Int |
