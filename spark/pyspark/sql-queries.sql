-- show tables
select * from taxi_rides_cache;
-- INSERT INTO `taxi_rides` VALUES ('at');
-- CACHE TABLE taxi_rides_cache AS SELECT * FROM taxi_rides;
-- SELECT * from taxi_rides;
-- LOAD DATA LOCAL INPATH 'data.csv' OVERWRITE INTO TABLE taxi_rides;
-- delete table taxi_rides
-- CREATE TABLE taxi_rides (
--   VendorID STRING, tpep_pickup_datetime STRING,
--   tpep_dropoff_datetime STRING, passenger_count STRING,
--   trip_distance STRING, RatecodeID STRING,
--   store_and_fwd_flag STRING, PULocationID STRING,
--   DOLocationID STRING, payment_type STRING,
--   fare_amount STRING, extra STRING, mta_tax STRING,
--   tip_amount STRING, tolls_amount STRING,
--   improvement_surcharge STRING, total_amount STRING
-- )
-- ROW FORMAT DELIMITED
-- FIELDS TERMINATED BY ",";
-- SHOW TABLES;
-- SELECT count(*) FROM taxi_rides;
-- CACHE TABLE taxi_rides_cache AS SELECT * FROM taxi_rides;
