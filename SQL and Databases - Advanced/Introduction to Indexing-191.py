## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")

schema = conn.execute('pragma table_info(facts);').fetchall()
for s in schema:
    print(s)


## 3. Explain query plan ##

query_plan_one = conn.execute('EXPLAIN QUERY PLAN SELECT * FROM facts WHERE area>40000;').fetchall()
query_plan_two = conn.execute('EXPLAIN QUERY PLAN SELECT area FROM facts WHERE area > 40000;').fetchall()
query_plan_three = conn.execute('EXPLAIN QUERY PLAN SELECT * FROM facts WHERE name = "Czech Republic";').fetchall()

## 5. Time complexity ##

query_plan_four = conn.execute('EXPLAIN QUERY PLAN SELECT * from facts WHERE id = 20;').fetchall()

## 9. All together now ##

query_plan_six = conn.execute('EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 10000;').fetchall()

conn.execute('CREATE INDEX IF NOT EXISTS pop_idx ON facts(population);')

query_plan_seven = conn.execute('EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 10000;').fetchall()
