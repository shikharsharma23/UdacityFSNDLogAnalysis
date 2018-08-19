# Log-Analysis
## Project Overview

In this project, we work with data that could have come from a real-world web application,
with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

## How to Run?

## PreRequisites:
### Python3
### Vagrant
### Git
### VirtualBox

## Setup Project:
- Install Vagrant and VirtualBox
- Download or Clone fullstack-nanodegree-vm repository.
- Download the data (newsdata.sql) from udacity.
- Unzip this file after downloading it. The file inside is called newsdata.sql.
- Copy the newsdata.sql file and content of this current repository, by either downloading or cloning it from Here
- Launching the Virtual Machine:
- Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  `$ vagrant up`
- Then Log into this using command: (via git bash)
  `$ vagrant ssh`
- Change directory to /vagrant and look around with ls.
- Setting up the database and Creating Views:
= Load the data in local database using the command:
  `psql -d news -f newsdata.sql`

## The database includes three tables:

- The authors table includes information about the authors of articles.
- The articles table includes the articles themselves.
- The log table includes one entry for each time a user has accessed the site.
- Use psql -d news to connect to database.

## Task is to make a reporting tool that updates on real time basis

- Query 1 : What are the most popular three articles of all time?
- Query 2 :  Who are the most popular article authors of all time? 
- Query 3   : On which days did more than 1 percent of requests lead to errors? 
  


See the table details and programs output in output.txt


View Created for query 1 and query 2 :


`create view article_log_join as  select title,author,slug,path from log join articles on log.path like concat('%',articles.slug);`


Running the queries:
From the vagrant directory inside the virtual machine,run logs.py using:
  $ python3 reporting.py
