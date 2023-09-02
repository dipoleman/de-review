\c nc_sells_fridges_og

\echo '\n ------ items -------\n'
SELECT * FROM items;
\echo '\n ------ staff -------\n'
SELECT * FROM staff;
\echo '\n ------ sales -------\n'
SELECT * FROM sales;


\c nc_sells_fridges_new

\echo '\n\n\n ------ dim_features -------\n'
SELECT * FROM dim_features;
\echo '\n ------ stock feature juc -------\n'
SELECT * FROM stock_feature_junc;
\echo '\n ------ dim_stock -------\n'
SELECT * FROM dim_stock;


