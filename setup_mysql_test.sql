-- Set up the new database rentabike_test_db and add user rentabike_test
CREATE DATABASE IF NOT EXISTS rentabike_test_db;
CREATE USER IF NOT EXISTS 'rentabike_test'@'localhost' IDENTIFIED BY 'password';
-- Grant all privileges for rentabike_test on rentabike_test_db.
GRANT ALL ON rentabike_test_db.* TO 'rentabike_test'@'localhost';
-- Grant select privilege on performance_schema database to rentabike_test.
GRANT SELECT ON performance_schema.* TO 'rentabike_test'@'localhost';
