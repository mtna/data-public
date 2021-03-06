# FiveThirtyEight - COVID Approval Toplines

This [dataset](https://raw.githubusercontent.com/fivethirtyeight/covid-19-polls/master/covid_approval_toplines.csv) is pulled nightly from the [FiveThirtyEight github repository on the COVID-19 Polls](https://github.com/fivethirtyeight/covid-19-polls). We pull and process it nightly as a simple approach to ensure that we are up to date with the source data.

## Original Covid Approval Toplines Structure:  

|Variable | Description | Type/Coding |
|---|----|--|
| subject             | For approval polls, this column marks whose handling of covid-19 the approval poll is about (e.g. Trump). | Text |
| modeldate           | Date of model run | Date |
| party               | Party of respondents | Text |
| approve_estimate    | Approval estimate | Numeric |
| disapprove_estimate | Disapproval estimate | Numeric |
| timestamp           |  | Timestamp |

## Data Curation & Transformation

The following operations have been performed on the source file:

- The following variables have been renamed to be more descriptive and unified by topic:

	- `subject` -> `poll_subject`
	- `modeldate` -> `date_modeled` 
	- `approve_estimate` -> `pct_approve_estimate`,
	- `disapprove_estimate` -> `pct_disapprove_estimate` 
    
- The date_modeled variable has been reformatted to be an ISO 8601 date. 
- The party variable has been coded.

## Transformed Structure 

|Variable | Description | Type/Coding |
|---|----|--|
| date_modeled            | Date of the model run. | Date |
| poll_subject            | The subject of the poll. | Text |
| party                   | The party affiliation of the respondents. | all: All Parties, D: Democrat, I: Independent, R: Republican ||
| pct_approve_estimate    | The estimated percent of approval on the date modeled by party. FiveThirtyEight averages are calculated similarly to how they handle presidential approval ratings, which means they <a href="https://fivethirtyeight.com/features/how-were-tracking-donald-trumps-approval-ratings/" target= "_blank">account for the quality of the pollster and each pollster’s house effects</a> (whether they seem to yield unusually high or low numbers for each question compared with the polling consensus), in addition to a poll’s recency and sample size. In cases where the pollster did not provide sample sizes by party, they were calculated based on the percentage of total respondents who identified with each party. | Numeric |
| pct_disapprove_estimate | The estimated percent of disapproval on the date modeled by party. FiveThirtyEight averages are calculated similarly to how they handle presidential approval ratings, which means they <a href="https://fivethirtyeight.com/features/how-were-tracking-donald-trumps-approval-ratings/" target= "_blank">account for the quality of the pollster and each pollster’s house effects</a> (whether they seem to yield unusually high or low numbers for each question compared with the polling consensus), in addition to a poll’s recency and sample size. In cases where the pollster did not provide sample sizes by party, they were calculated based on the percentage of total respondents who identified with each party. | Numeric |
| timestamp               | A timestamp indicating when the adjusted record was created. | Timestamp |
