-- column and filter information 
select 
	distinct(id), 
	date_time, 
	ip_address,
	product,
	query_type,
	format,
	"column",
	filter_column,
	filter_operator,
	filter_value
from 
	DBA.rds_statistics_v1 
order by 
	date_time  DESC;
	
-- IPs hitting the api, exclude null and internal ip
select distinct(ip_address), count(*) from 
	DBA.rds_statistics_v1 where ip_address is not NULL AND ip_address not like '10.%' group by ip_address order by 2 desc ;

-- IPs hitting the api and the products they hit, exclude null and internal ip
select distinct(ip_address), "product", count(*) as "count" from 
	DBA.rds_statistics_v1 where ip_address is not NULL AND ip_address not like '10.%'  group by ip_address order by 3 desc ;
	
-- IPs hitting the api and the products, query type, and columns they use, exclude null and internal ip
select distinct(ip_address), "product", query_type, format, "column", count(*) as "count" from 
	DBA.rds_statistics_v1 where ip_address is not NULL AND ip_address not like '10.%' group by ip_address order by 6 desc ;
	
	
	