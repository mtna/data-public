# FiveThirtyEight - COVID Concern Toplines

This [dataset](https://raw.githubusercontent.com/fivethirtyeight/covid-19-polls/master/covid_concern_toplines.csv) is pulled nightly from the [FiveThirtyEight GitHub repository on the COVID-19 Polls](https://github.com/fivethirtyeight/covid-19-polls). We pull and process them nightly as a simple approach to ensure that we are up to date with the source data.

## Original Covid Concern Toplines Structure:  

|Variable | Description | Type/Coding |
|---|----|--|
| subject             | For concern polls, this column identifies which subject the poll is asking Americans about (for example, concern-infected vs concern-economy). | Text |
| modeldate           | Date of model run | Date |
| party               | Party of respondents | Text |
| very_estimate       | Very concerned estimate | Numeric |
| somewhat_estimate   | Somewhat concerned estimate | Numeric |
| not_very_estimate   | Not very concerned estimate | Numeric |
| not_at_all_estimate | Not at all concerned estimate | Numeric |
| timestamp           |  | Timestamp |

## Data Curation & Transformation

The following operations have been performed on the source file:

- The following variables have been renamed to be more descriptive and unified by topic:

	- `subject` -> `poll_subject`
	- `modeldate` -> `date_modeled` 
	- `very_estimate` -> `pct_concern_very_estimate`,
	- `somewhat_estimate` -> `pct_concern_some_estimate` 
	- `not_very_estimate` -> `pct_concern_not_very_estimate`,
	- `not_at_all_estimate` -> `pct_concern_none_estimate`
    
- The date_modeled variable has been reformatted to be an ISO 8601 date. 
- The poll_subject variable has been coded.
- The party variable has been coded.

## Transformed Structure 

|Variable | Description | Type/Coding |
|---|----|--|
| date_modeled            | Date of the model run. | Date |
| poll_subject            | The subject of the poll. | Text |
| party                   | The party affiliation of the respondents. | all: All Parties, D: Democrat, I: Independent, R: Republican ||
| pct_concern_very_estimate    | The estimated percent of respondents who are very concerned about the effects of COVID-19.. FiveThirtyEight averages are calculated similarly to how they handle presidential approval ratings, which means they <a href="https://fivethirtyeight.com/features/how-were-tracking-donald-trumps-approval-ratings/" target= "_blank">account for the quality of the pollster and each pollster’s house effects</a> (whether they seem to yield unusually high or low numbers for each question compared with the polling consensus), in addition to a poll’s recency and sample size. In cases where the pollster did not provide sample sizes by party, they were calculated based on the percentage of total respondents who identified with each party. | Numeric |
| pct_concern_some_estimate | The estimated percent of respondents who are somewhat concerned about the effects of COVID-19.. FiveThirtyEight averages are calculated similarly to how they handle presidential approval ratings, which means they <a href="https://fivethirtyeight.com/features/how-were-tracking-donald-trumps-approval-ratings/" target= "_blank">account for the quality of the pollster and each pollster’s house effects</a> (whether they seem to yield unusually high or low numbers for each question compared with the polling consensus), in addition to a poll’s recency and sample size. In cases where the pollster did not provide sample sizes by party, they were calculated based on the percentage of total respondents who identified with each party. | Numeric |
| pct_concern_not_very_estimate    | The estimated percent of respondents who are not very concerned about the effects of COVID-19.. FiveThirtyEight averages are calculated similarly to how they handle presidential approval ratings, which means they <a href="https://fivethirtyeight.com/features/how-were-tracking-donald-trumps-approval-ratings/" target= "_blank">account for the quality of the pollster and each pollster’s house effects</a> (whether they seem to yield unusually high or low numbers for each question compared with the polling consensus), in addition to a poll’s recency and sample size. In cases where the pollster did not provide sample sizes by party, they were calculated based on the percentage of total respondents who identified with each party. | Numeric |
| pct_concern_none_estimate | The estimated percent of respondents who are not concerned at all about the effects of COVID-19. FiveThirtyEight averages are calculated similarly to how they handle presidential approval ratings, which means they <a href="https://fivethirtyeight.com/features/how-were-tracking-donald-trumps-approval-ratings/" target= "_blank">account for the quality of the pollster and each pollster’s house effects</a> (whether they seem to yield unusually high or low numbers for each question compared with the polling consensus), in addition to a poll’s recency and sample size. In cases where the pollster did not provide sample sizes by party, they were calculated based on the percentage of total respondents who identified with each party. | Numeric |
| timestamp               | A timestamp indicating when the adjusted record was created. | Timestamp |
