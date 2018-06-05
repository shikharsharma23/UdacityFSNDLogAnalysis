#!/usr/bin/python3

import psycopg2
from print_details import printDetails


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.DatabaseError, e:
        print("<error message>")

def executeQuery(query):
    db, cursor = connect()
    cursor.execute(query)
    output=cursor.fetchall()
    db.close()
    return output

def return_sql_queries():
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

  return [sql_query_1,sql_query_2,sql_query_3]



def main():
  queries = return_sql_queries() # concatenate queries
  printDetails(queries)  # print task details
  query_counter = 0
  for query in queries:
      query_counter = query_counter + 1
      print('\t\t----------- Executing Query Number : ' +
            str(query_counter) + '-------------')
      print('\n')
      print(query)
      print('\n')
      result_query=executeQuery(query)
      print('\t\t------------- Result of Query Number : ' +
            str(query_counter) + '---------')
      print('\n')
      for result in result_query:
          out_str = '{:>40}  {:>40}'.format(str(result[0]),str(result[1]))
          print(out_str)
      print('\n\n')

main()