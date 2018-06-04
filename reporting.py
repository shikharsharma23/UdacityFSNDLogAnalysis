#!/usr/bin/python3

import psycopg2
from print_details import printDetails

# Three Postgres SQL queries for Analysis
sql_query_1 = '''select title,count(*) from article_log_join group by title
 order by count desc limit 3;'''
sql_query_2 = '''select name, count(*) from article_log_join join
 authors on  article_log_join.author=authors.id
  group by name order by count desc;'''
sql_query_3 = '''select date, percent_error from (select part1.date,
100*CAST(error_requests AS FLOAT)/total_requests as percent_error from
 (select date(time),count(*) as error_requests from log where
  status like concat('%',404,'%') group by date(time)) part1
join
(select date(time),count(*) as total_requests
 from  log group by date(time)) part2
on part1.date=part2.date) part3 where percent_error>1;'''

queries = [sql_query_1, sql_query_2, sql_query_3]  # concatenate queries

printDetails(queries)  # print task details

db = psycopg2.connect("dbname=news")  # connect to DB
cursor = db.cursor()  # get cursor

query_counter = 0
for query in queries:
	query_counter = query_counter + 1
	print('----------- Executing Query Number : ' + str(query_counter) + '-------------')
	print('\n')
	print(query)
	print('\n')
	cursor.execute(query)
	print('------------- Result of Query Number : ' + str(query_counter) + '---------')
	for result in cursor.fetchall():
		print(result)
	print('\n\n')

db.close()  # close db connection
