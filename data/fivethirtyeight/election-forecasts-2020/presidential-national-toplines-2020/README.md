# FiveThirtyEight - National Toplines 2020

This [dataset](https://projects.fivethirtyeight.com/2020-general-data/presidential_national_toplines_2020.csv) is pulled nightly from the [FiveThirtyEight GitHub repository on the 2020 U.S. Election Forecasts](https://github.com/fivethirtyeight/data/tree/master/election-forecasts-2020). We pull and process it nightly as a simple approach to ensure that we are up to date with the source data.


## Original National Toplines 2020 Structure:  

|Variable | Description | Type/Coding |
|---|----|--|
| cycle                      | The election cycle (2020) | Text |
| branch                     | The kind of race this forecast pertains to (presidential) | Text |
| model                      | The model type (polls-plus is the only model we are running for the 2020 presidential race) | Text |
| modeldate                  | Date of the model run | Date |
| candidate_inc              | Name of the incumbent | Text |
| candidate_chal             | Name of the challenger | Text |
| candidate_3rd              | Name of the third-party candidate | Text |
| ecwin_inc                  | Chance that the incumbent will win a majority of the electoral votes                              | Numeric |
| ecwin_chal                 | Chance that the challenger will win a majority of the electoral votes                              | Numeric |
| ecwin_3rd                  | Chance that the third-party candidate will win a majority of the electoral votes                              | Numeric |
| ec_nomajority              | Chance that no candidate will win a majority of the electoral votes                              | Numeric |
| popwin_inc                 | Chance that the incumbent will win the popular vote                             | Numeric |
| popwin_chal                | Chance that the challenger will win the popular vote                              | Numeric |
| popwin_3rd                 | Chance that a third-party candidate will win the popular vote                             | Numeric |
| ev_inc                     | Forecasted number of Electoral College votes for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| ev_chal                    | Forecasted number of Electoral College votes for the challenger, including the upper and lower bounds of an 80% confidence interval | Numeric |
| ev_3rd                     | Forecasted number of Electoral College votes for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | Numeric |
| ev_inc_lo                  | Forecasted number of Electoral College votes for the incumbent, including the upper and lower bounds of an 80% confidence interval | Int |
| ev_chal_lo                 | Forecasted number of Electoral College votes for the challenger, including the upper and lower bounds of an 80% confidence interval | Int |
| ev_3rd_lo                  | Forecasted number of Electoral College votes for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | Int |
| ev_inc_hi                  | Forecasted number of Electoral College votes for the incumbent, including the upper and lower bounds of an 80% confidence interval | Int |
| ev_chal_hi                 | Forecasted number of Electoral College votes for the challenger, including the upper and lower bounds of an 80% confidence interval | Int |
| ev_3rd_hi                  | Forecasted number of Electoral College votes for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | Int |
| national_voteshare_inc     | Forecasted national vote share for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| national_voteshare_chal    | Forecasted national vote share for the challenger, including the upper and lower bounds of an 80% confidence interval | Numeric |
| national_voteshare_3rd     | Forecasted national vote share for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | Numeric |
| nat_voteshare_other        | Forecasted national vote share for all the other candidates, including the upper and lower bounds of an 80% confidence interval | Numeric |
| national_voteshare_inc_lo  | Forecasted national vote share for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| national_voteshare_chal_lo |Forecasted national vote share for the challenger, including the upper and lower bounds of an 80% confidence interval | Numeric |
| national_voteshare_3rd_lo  | Forecasted national vote share for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | Numeric |
| nat_voteshare_other_lo     | Forecasted national vote share for all the other candidates, including the upper and lower bounds of an 80% confidence interval | Numeric |
| national_voteshare_inc_hi  | Forecasted national vote share for the incumbent, including the upper and lower bounds of an 80% confidence interval | Numeric |
| national_voteshare_chal_hi | Forecasted national vote share for the challenger, including the upper and lower bounds of an 80% confidence interval | Numeric |
| national_voteshare_3rd_hi  |Forecasted national vote share for the third-party candidate, including the upper and lower bounds of an 80% confidence interval | Numeric |
| nat_voteshare_other_hi     | Forecasted national vote share for all the other candidates, including the upper and lower bounds of an 80% confidence interval | Numeric |
| timestamp                  | Date and time the simulations were run | Timestamp |
| simulations                | Number of simulations run | Int |

## Data Curation & Transformation

The following operations have been performed on the source file:

- The following variables have been renamed to be more descriptive and unified by topic:

	- `cycle` -> `election_cycle`  
    - `branch` -> `race_type`  
	- `modeldate` -> `date_modeled`   
	- `candidate_inc` -> `name_incumbent`   
	- `candidate_chal` -> `name_challenger`   
	- `candidate_3rd` -> `name_third`   
	- `ecwin_inc`  -> `win_ec_incumbent`   
	- `ecwin_chal` -> `win_ec_challenger`  
	- `ecwin_3rd` -> `win_ec_third`  
	- `ec_nomajority` -> `win_ec_none`  
	- `popwin_inc` -> `win_pop_incumbent`  
	- `popwin_chal` -> `win_pop_challenger`  
	- `popwin_3rd` -> `win_pop_third`  
	- `ev_inc` -> `votes_ec_incumbent`  
	- `ev_chal` -> `votes_ec_challenger`  
	- `ev_3rd` -> `votes_ec_third`  
	- `ev_inc_lo` -> `votes_ec_lo_incumbent`  
	- `ev_chal_lo` -> `votes_ec_lo_challenger`  
	- `ev_3rd_lo` -> `votes_ec_lo_third`  
	- `ev_inc_hi` -> `votes_ec_hi_incumbent`  
	- `ev_chal_hi` -> `votes_ec_hi_challenger`  
	- `ev_3rd_hi` -> `votes_ec_hi_third`  
	- `national_voteshare_inc` -> `voteshare_nat_incumbent`  
	- `national_voteshare_chal` -> `voteshare_nat_challenger`  
	- `national_voteshare_3rd` -> `voteshare_nat_third`  
	- `nat_voteshare_other` -> `voteshare_nat_other`  
	- `national_voteshare_inc_lo` -> `voteshare_nat_lo_incumbent`  
	- `national_voteshare_chal_lo` -> `voteshare_nat_lo_challenger`  
	- `national_voteshare_3rd_lo` -> `voteshare_nat_lo_third`  
	- `nat_voteshare_other_lo` -> `voteshare_nat_lo_other`  
	- `national_voteshare_inc_hi` -> `voteshare_nat_hi_incumbent`  
	- `national_voteshare_chal_hi` -> `voteshare_nat_hi_challenger`  
	- `national_voteshare_3rd_hi` -> `voteshare_nat_hi_third`  
	- `nat_voteshare_other_hi` -> `voteshare_nat_hi_other`  
	- `timestamp` -> `simulation_timestamp`  
	- `simulations` -> `simulation_count`  
    
- The date_modeled variable has been reformatted to be an ISO 8601 date. 
- The model variable has been coded.
- The variables have be reorganized to have the modelling and simulation variables together at the end of the record.

## Transformed Structure 

|Variable | Description | Type/Coding |
|---|----|--|
| election_cycle              | The election cycle this forecast pertains to. | Text |
| race_type                   | The kind of race this forecast pertains to. | Text |
| name_incumbent              | Name of the incumbent candidate. | Text |
| name_challenger             | Name of the challenging candidate. | Text |
| name_third                  | Name of the third-party candidate. | Text |
| win_ec_incumbent            | The chance that the incumbent will win a majority of the Electoral College votes. | Numeric |
| win_ec_challenger           | The chance that the challenger will win a majority of the Electoral College votes. | Numeric |
| win_ec_third                | The chance that the third-party candidate will win a majority of the Electoral College votes. | Numeric |
| win_ec_none                 | The chance that no candidate will win a majority of the Electoral College votes. | Numeric |
| win_pop_incumbent           | The chance that the incumbent will win the popular vote. | Numeric |
| win_pop_challenger          | The chance that the challenger will win the popular vote. | Numeric |
| win_pop_third               | The chance that a third-party candidate will win the popular vote. | Numeric |
| votes_ec_incumbent          | The forecasted number of Electoral College votes for the incumbent. | Numeric |
| votes_ec_challenger         | The forecasted number of Electoral College votes for the challenger. | Numeric |
| votes_ec_third              | The forecasted number of Electoral College votes for the third-party candidate. | Numeric |
| votes_ec_lo_incumbent       | The forecasted number of Electoral College votes for the incumbent - lower bound of 80% confidence interval. | Int |
| votes_ec_lo_challenger      | The forecasted number of Electoral College votes for the challenger - lower bound of 80% confidence interval. | Int |
| votes_ec_lo_third           | The forecasted number of Electoral College votes for the third-party candidate - lower bound of 80% confidence interval. | Int |
| votes_ec_hi_incumbent       | The forecasted number of Electoral College votes for the incumbent - upper bound of 80% confidence interval. | Int |
| votes_ec_hi_challenger      | The forecasted number of Electoral College votes for the challenger - upper bound of 80% confidence interval. | Int |
| votes_ec_hi_third           | The forecasted number of Electoral College votes for the third-party candidate - upper bound of 80% confidence interval. | Int |
| voteshare_nat_incumbent     | The forecasted national vote share for the incumbent. | Numeric |
| voteshare_nat_challenger    | The forecasted national vote share for the challenger. | Numeric |
| voteshare_nat_third         | The forecasted national vote share for the third-party candidate. | Numeric |
| voteshare_nat_other         | The forecasted national vote share for all the other candidates. | Numeric |
| voteshare_nat_lo_incumbent  | The forecasted national vote share for the incumbent - lower bound of 80% confidence interval. | Numeric |
| voteshare_nat_lo_challenger | The forecasted national vote share for the challenger - lower bound of 80% confidence interval. | Numeric |
| voteshare_nat_lo_third      | The forecasted national vote share for the third-party candidate - lower bound of 80% confidence interval. | Numeric |
| voteshare_nat_lo_other      | The forecasted national vote share for all the other candidates - lower bound of 80% confidence interval. | Numeric |
| voteshare_nat_hi_incumbent  | The forecasted national vote share for the incumbent - upper bound of 80% confidence interval. | Numeric |
| voteshare_nat_hi_challenger | The forecasted national vote share for the challenger - upper bound of 80% confidence interval. | Numeric |
| voteshare_nat_hi_third      | The forecasted national vote share for the third-party candidate - upper bound of 80% confidence interval. | Numeric |
| voteshare_nat_hi_other      | The forecasted national vote share for all the other candidates - upper bound of 80% confidence interval. | Numeric |
| model                       | The model type. Polls-plus is the only model being run for the 2020 presidential race (as opposed to polls-only). The polls-only model relies only on polls from a particular state, while the polls-plus model is based on state polls, national polls and endorsements as described <a href="https://en.wikipedia.org/wiki/FiveThirtyEight" target="_blank">here</a>. | 0: polls-only, 1: polls-plus |
| date_modeled                | Date of the model run | Date |
| simulation_timestamp        | Date and time the simulations were run | Timestamp |
| simulation_count            | Number of simulations run | Int |
