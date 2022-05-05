CREATE TABLE IF NOT EXISTS AGENCIES(
id integer PRIMARY KEY,
agency_name text,
borough text,

UNIQUE (agency_name, borough)
);

CREATE TABLE IF NOT EXISTS HOUSING(
borough text,
avg_rent integer,
avg_buy integer,
bedrooms integer
);

CREATE TABLE IF NOT EXISTS JOBS(
job_title text,
agency_id integer,
base_salary integer,

FOREIGN KEY (agency_id) REFERENCES AGENCIES(id),
PRIMARY KEY (job_title, agency_id)
);

CREATE TABLE IF NOT EXISTS PEOPLE(
id integer PRIMARY KEY,
last_name text,
f_name text,
a_status text,
title text,
real_salary integer,
hours_w integer,
agency_id integer,

FOREIGN KEY (title) references JOBS(job_title),
FOREIGN KEY (agency_id) REFERENCES AGENCIES(id) ON UPDATE CASCADE
);


