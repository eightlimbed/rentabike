-- Set up the new database rentabike_dev_db and add user rentabike_dev
CREATE DATABASE IF NOT EXISTS rentabike_dev_db;
CREATE USER IF NOT EXISTS 'rentabike_dev'@'localhost' IDENTIFIED BY 'password';
-- Grant all privileges for rentabike_dev on rentabike_dev_db.
GRANT ALL ON rentabike_dev_db.* TO 'rentabike_dev'@'localhost';
-- Grant select privilege on performance_schema database to rentabike_dev.
GRANT SELECT ON performance_schema.* TO 'rentabike_dev'@'localhost';
