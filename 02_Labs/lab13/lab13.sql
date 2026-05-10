.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) from inventory group by item;

CREATE TABLE list as
  select name, Min(MSRP / rating) from products group by category; 

CREATE TABLE shopping_list AS
  SELECT name, store from list, lowest_prices where item = name;


CREATE TABLE total_bandwidth AS
  SELECT sum(b.Mbs) from shopping_list as a, stores as b where a.store = b.store;

