
def printDetails(queries):
	view_created='''"create view article_log_join as create view article_log_join as select title,author,slug,path from log join articles on log.path like concat('%',articles.slug,'%')"'''
	print('-------- Starting Execution ----------------')
	print('--------- List of Tables in database -------------')
	print('\n\n\n')
	print('''          List of relations
	 Schema |   Name   | Type  |  Owner
	--------+----------+-------+---------
	 public | articles | table | vagrant
	 public | authors  | table | vagrant
	 public | log      | table | vagrant''')
	print('\n\n\n')
	print('---------- Table 1 : Articles-------------------------')
	print('''                                  Table "public.articles"
	 Column |           Type           |                       Modifiers
	--------+--------------------------+-------------------------------------------------------
	 author | integer                  | not null
	 title  | text                     | not null
	 slug   | text                     | not null
	 lead   | text                     |
	 body   | text                     |
	 time   | timestamp with time zone | default now()
	 id     | integer                  | not null default nextval('articles_id_seq'::regclass)
	Indexes:
	    "articles_pkey" PRIMARY KEY, btree (id)
	    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
	Foreign-key constraints:
	    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)''')
	print('\n\n\n')

	print('---------- Table 2 : Author-------------------------')
	print('''                         Table "public.authors"
	 Column |  Type   |                      Modifiers
	--------+---------+------------------------------------------------------
	 name   | text    | not null
	 bio    | text    |
	 id     | integer | not null default nextval('authors_id_seq'::regclass)
	Indexes:
	    "authors_pkey" PRIMARY KEY, btree (id)
	Referenced by:
	    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)''')
	print('\n\n\n')

	print('---------- Table 3 : Log-------------------------')
	print('''                                  Table "public.log"
	 Column |           Type           |                    Modifiers
	--------+--------------------------+--------------------------------------------------
	 path   | text                     |
	 ip     | inet                     |
	 method | text                     |
	 status | text                     |
	 time   | timestamp with time zone | default now()
	 id     | integer                  | not null default nextval('log_id_seq'::regclass)
	Indexes:
	    "log_pkey" PRIMARY KEY, btree (id)''')

	print('\n\n\n')
	print('Query 1 : What are the most popular three articles of all time?')
	print('Query 2 :  Who are the most popular article authors of all time? ')
	print('Query 3	 : On which days did more than 1 percent of requests lead to errors? ')
	print('\n\n\n')
