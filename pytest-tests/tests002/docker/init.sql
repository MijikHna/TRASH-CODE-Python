CREATE USER test_user WITH PASSWORD 'password';

CREATE DATABASE test_db;
-- SELECT 'CREATE DATABASE test_db' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'test_db')\gexec

GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;

-- ALTER USER test_user CREATEDB; -- erlaubt Tabellen zu erstellen


--ALTER ROLE test_user SET DEFAULT_TRANSACTION_ISOLATION TO 'read committed';
ALTER ROLE test_user SET CLIENT_ENCODING TO 'utf8';
ALTER ROLE test_user SET TIMEZONE TO 'UTC';

ALTER DATABASE test_db SET TIMEZONE TO 'Europe/Berlin';

\c test_db -- connect to DB test_db

CREATE TABLE IF NOT EXISTS cars (
  id SERIAL PRIMARY KEY, 
  internal_name VARCHAR(30),
  modified TIMESTAMP NOT NULL DEFAULT NOW(),
  models INT,
  -- FOREIGN KEY(model) REFERENCES ref_cars_to_models(id) ON DELETE CASCADE
  users INT
  -- FOREIGN KEY(car) REFERENCES ref_cars_to_users(id) ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY, 
  full_name VARCHAR(30) NOT  NULL,
  first_name VARCHAR(30) NULL, 
  last_name VARCHAR(30) NULL, 
  created TIMESTAMP NOT NULL DEFAULT NOW(),
  cars INT
  -- FOREIGN KEY(car) REFERENCES ref_cars_to_users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS models (
  id SERIAL PRIMARY KEY,
  internal_name varchar(30) NOT NULL,
  cars INT
  -- FOREIGN KEY(car) REFERENCES ref_cars_to_models(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ref_cars_to_models (
  id SERIAL PRIMARY KEY,
  car_id INT,
  FOREIGN KEY(car_id) REFERENCES cars(id),
  model_id INT,
  FOREIGN KEY(model_id) REFERENCES models(id)
);

CREATE TABLE IF NOT EXISTS ref_cars_to_users (
  id SERIAL PRIMARY KEY,
  car_id INT,
  FOREIGN KEY(car_id) REFERENCES cars(id),
  user_id INT,
  FOREIGN KEY(user_id) REFERENCES users(id)
  -- CONSTRAINT PRIMARY KEY(car_id, user_id)
);

ALTER TABLE cars
ADD FOREIGN KEY(models) REFERENCES ref_cars_to_models(id) ON DELETE CASCADE;

ALTER TABLE cars
ADD FOREIGN KEY(users) REFERENCES ref_cars_to_users(id) ON DELETE CASCADE;

ALTER TABLE models
ADD FOREIGN KEY(cars) REFERENCES ref_cars_to_users(id) ON DELETE CASCADE;

ALTER TABLE users
ADD FOREIGN KEY(cars) REFERENCES ref_cars_to_models(id) ON DELETE CASCADE;

-- GRANT ALL PRIVILEGES ON DATABASE test_db TO postgres;
-- GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;

GRANT ALL ON ALL TABLES IN SCHEMA public to test_user;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to test_user;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to test_user;             