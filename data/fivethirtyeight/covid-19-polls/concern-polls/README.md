# FiveThirtyEight - COVID Concern Polls

This [dataset](https://raw.githubusercontent.com/fivethirtyeight/covid-19-polls/master/covid_concern_polls.csv) is pulled nightly from the [FiveThirtyEight github repository on the COVID-19 Polls](https://github.com/fivethirtyeight/covid-19-polls). We pull and process it nightly as a simple approach to ensure that we are up to date with the source data.

## Original Covid Concern Polls Structure:  

|Variable | Description | Type/Coding |
|---|----|--|
| start_date  | Start date of poll | Date |
| end_date    | End date of poll | Date |
| pollster    | Organization that conducted the poll | Text |
| sponsor     | Organization that sponsored the poll | Text |
| sample_size | Size of polling sample | Int |
| population  | A for adults, RV for registered voters, LV for likely voters | Text |
| party       | Party of respondents | Text |
| subject     | For concern polls, this column identifies which subject the poll is asking Americans about (for example, concern-infected vs concern-economy) | Text |
| tracking    | TRUE if the poll is a tracking poll, meaning that the pollster is releasing data with overlapping samples | Boolean |
| text        | Text of the question the pollster asked | Text |
| very        |  | Numeric |
| somewhat    |  | Numeric |
| not_very    |  | Numeric |
| not_at_all  |  | Numeric |
| url         | Link to the poll | Text |

## Data Curation & Transformation

The following operations have been performed on the source file:

- The following variables have been renamed to be more descriptive and unified by topic:

	- `start_date` -> `date_start`  
    - `end_date` -> `date_end`  
	- `sponsor` -> `poll_sponsor`   
	- `subject` -> `poll_subject`   
	- `tracking` -> `poll_type`   
	- `text` -> `question_text`   
	- `very` -> `pct_concern_very`
	- `somewhat` -> `pct_concern_some`
	- `not_very` -> `pct_concern_not_very`
	- `not_at_all` -> `pct_concern_none`
	- `url` -> `poll_url`
    
- The date_start and date_end variables have been reformatted to be ISO 8601 dates. 
- The poll_subject variable has been coded.
- The tracking variable has been coded rather than using a boolean.
- The party variable has been coded.

## Transformed Structure 

|Variable | Description | Type/Coding |
|---|----|--|
| date_start     | The start date of the poll. | Date |
| date_end       | The end date of the poll. | Date |
| pollster       | The organization that conducted the poll. | Text |
| poll_sponsor   | The organization that sponsored the poll. | Text |
| poll_type      | The type of poll; tracking or non-tracking. Tracking polls are polls where the pollster is releasing data with overlapping samples. | 0: Non-Tracking Poll, 1: Tracking Poll |
| poll_subject   | The chance that the incumbent wins the electoral votes (votes_ec_total). | Text |
| question_text  | The text of the question the pollster asked. |Text |
| population     | The population being measured. | a: Adults, rv: Registered Voters, lv: Likely Voters |
| party          | The party affiliation of the respondents. | all: All Parties, D: Democrat, I: Independent, R: Republican |
| sample_size    | The size of the polling sample. | Int |
| pct_approve    | The percent of approving respondents. | Numeric |
| pct_disapprove | The percent of disapproving respondents. | Numeric |
| poll_url       | The URL to the poll. | Text |