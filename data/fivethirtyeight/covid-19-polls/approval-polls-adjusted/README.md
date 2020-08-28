# FiveThirtyEight - COVID Approval Polls Adjusted

This [dataset](https://raw.githubusercontent.com/fivethirtyeight/covid-19-polls/master/covid_approval_polls_adjusted.csv) is pulled nightly from the [FiveThirtyEight GitHub repository on the COVID-19 Polls](https://github.com/fivethirtyeight/covid-19-polls). We pull and process it nightly as a simple approach to ensure that we are up to date with the source data.


## Original COVID Approval Polls Structure:  

|Variable | Description | Type/Coding |
|---|----|--|
| subject             | For approval polls, this column marks whose handling of covid-19 the approval poll is about (e.g. Trump). | Text |
| modeldate           | Date of model run | Date |
| party               | Party of respondents | Text |
| startdate           | Start date of poll | Date |
| enddate             | End date of poll | Date |
| pollster            | Organization that conducted the poll | Text |
| grade               | Grade given to the pollster in our Pollster Ratings | Text |
| samplesize          | Size of polling sample | Int |
| population          | A for adults, RV for registered voters, LV for likely voters | Text |
| weight              | Weight given to each poll in the model | Numeric |
| influence           | Weight given to each poll, adjusted for recency | Numeric |
| multiversions       | * denotes that multiple versions of a poll in the raw data file were combined (see note below) | Text |
| tracking            | TRUE if the poll is a tracking poll, meaning that the pollster is releasing data with overlapping samples | Boolean |
| approve             |  | Numeric |
| disapprove          |  | Numeric |
| approve_adjusted    |  | Numeric |
| disapprove_adjusted |  | Numeric |
| timestamp           |  | Numeric |
| url                 | Link to the poll | Text |

## Data Curation & Transformation

The following operations have been performed on the source file:

- The following variables have been renamed to be more descriptive and unified by topic:

	- `subject` -> `poll_subject`
	- `modeldate` -> `date_modeled` 
	- `startdate` -> `date_start`  
    - `enddate` -> `date_end`  
	- `grade` -> `poll_grade` 
	- `samplesize` -> `sample_size`  
	- `grade` -> `poll_grade` 
	- `weight` -> `poll_weight`           
	- `influence` -> `poll_influence`    
	- `multiversions` -> `poll_multi_version`   
	- `text` -> `question_text`   
	- `approve` -> `pct_approve`
	- `disapprove` -> `pct_disapprove`
	- `approve_adjusted` -> `pct_approve_adjusted`
	- `disapprove_adjusted` -> `pct_disapprove_adjusted`
	- `url` -> `poll_url`
    
- The date_modeled, date_start, and date_end variable have been reformatted to be an ISO 8601 date. 
- The tracking variable has been coded rather than using a boolean.
- The party variable has been coded.
- The variables have be reorganized.

## Transformed Structure 

|Variable | Description | Type/Coding |
|---|----|--|
| date_modeled            | Date of the model run. | Date |
| date_start              | The start date of the poll. | Date |
| date_end                | The end date of the poll. | Date |
| poll_subject            | The subject of the poll. | Text |
| pollster                | The organization that conducted the poll. | Text |
| poll_grade              | Grade given to the pollster in the FiveThirtyEight Pollster Ratings. | Text |
| poll_type               | The type of poll; tracking or non-tracking. Tracking polls are polls where the pollster is releasing data with overlapping samples. | 0: Non-Tracking Poll, 1: Tracking Poll |
| poll_weight             | The weight given to each poll in the model. | Numeric |
| poll_influence          | The weight given to each poll, adjusted for recency. | Numeric |
| poll_multi_version      | A boolean flag indicating if there were multiple versions of a poll in the raw data that were combined. If the same poll asked more than one relevant question (using different wording), both questions were included, but the results of those questions were averaged together, then input into the model, so the poll was not double counted. | Boolean |
| population              | The population being measured. | a: Adults, rv: Registered Voters, lv: Likely Voters |
| party                   | The party affiliation of the respondents. | all: All Parties, D: Democrat, I: Independent, R: Republican |
| sample_size             | The size of the polling sample. | Int |
| pct_approve             | The percent of approving respondents. | Numeric |
| pct_disapprove          | The percent of disapproving respondents. | Numeric |
| pct_approve_adjusted    | The adjusted percent of approving respondents. | Numeric |
| pct_disapprove_adjusted | The adjusted percent of disapproving respondents. | Numeric |
| timestamp               | A timestamp indicated whent the adjusted record was created. | Timestamp |
| poll_url                | The URL to the poll. | Text |