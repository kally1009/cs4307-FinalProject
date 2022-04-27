CREATE TABLE AGENCIES(
id integer PRIMARY KEY,
agency_name text,
borough text
);

CREATE TABLE HOUSING(
borough text,
avg_rent integer,
avg_buy integer,
bedroooms integer
);

CREATE TABLE JOBS(
job_title text PRIMARY KEY,
agency_id integer,
base_salary integer,

FOREIGN KEY (agency_id) REFERENCES AGENCIES(id)
);

CREATE TABLE PEOPLE(
id integer PRIMARY KEY,
last_name text,
f_name text,
status text,
title text,
real_salary integer,
hours integer,
agency_id integer,

FOREIGN KEY (title) references JOBS(job_title),
FOREIGN KEY (agency_id) REFERENCES AGENCIES(id) ON UPDATE CASCADE
);


