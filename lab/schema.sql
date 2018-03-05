DROP TABLE if exists dht;
DROP TABLE if exists sound;
DROP TABLE if exists photo;


CREATE TABLE dht (
  date varchar(30),
  temp int,
  hum int,
);

CREATE TABLE sound (
  date varchar(30),
  audio int,
  env int,
  gate int
);

CREATE TABLE photo (
  date varchar(30),
  light int,
);

