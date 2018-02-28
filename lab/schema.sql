DROP TABLE if exists business;

CREATE TABLE business (
  id INTEGER PRIMARY KEY autoincrement,
  business_name varchar(127),
  business_type varchar(127),
  market_type   varchar(127),
  job_to_be_done varchar(255),
  revenue_model varchar(127)
);

INSERT INTO business VALUES
(0, 'Amazon' ,'for-profit', 'B2B and some B2C','products with as little wait time as possible','disintermediation (fulfilled by Amazon), freemium (Amazon Prime), and Brokerage (sellers on Amazon) model'),
(1, 'Apple'  ,'for-profit', 'B2C', "a product that is secure with a friendly UX and UI that improves one\'s self image", 'growth model'),
(2, 'Netflix','for-profit', 'B2C', 'an easy service to stream shows','subscription model'),
(3, 'Tesla'  ,'for-profit', 'B2C', 'a vehicle that is safe, unique, ecofriendly, and sophisticated','disintermediation model');