## 2. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")

query_plan_one = conn.execute('EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 1000000 AND population_growth < 0.05;').fetchall()

## 3. Query plan for multi-column queries ##

conn = sqlite3.connect("factbook.db")

conn.execute('CREATE INDEX IF NOT EXISTS pop_idx ON facts(population);')
conn.execute('CREATE INDEX IF NOT EXISTS pop_growth_idx ON facts(population_growth);')

query_plan_two = conn.execute('EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population_growth < 0.05;').fetchall()


## 6. Creating a multi-column index ##

conn = sqlite3.connect("factbook.db")

conn.execute('CREATE INDEX IF NOT EXISTS pop_pop_growth_idx ON facts(population, population_growth);')

query_plan_three = conn.execute('EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 1000000 AND population_growth < 0.05;').fetchall()



## 7. Covering index ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")

query_plan_four = conn.execute('explain query plan select population,population_growth from facts where population > 1000000 and population_growth < 0.05;').fetchall()

## 8. Covering index for single column ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")

query_plan_five = conn.execute('explain query plan select population from facts where population > 1000000;').fetchall()