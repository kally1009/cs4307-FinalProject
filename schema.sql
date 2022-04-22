CREATE TABLE PEOPLE(
id int PRIMARY KEY,
f_name text,
last_name text,
status text,
real_salary int,
hours int,
job_title text
);

CREATE TABLE AGENCY(
id int PRIMARY KEY,
agency text,
location text
);

CREATE TABLE JOBS(
job_title text PRIMARY KEY,
base_salary int
);


CREATE TABLE HOUSING(
burrow text,
avg_rent int,
avg_buy int,
bedroooms int
);
