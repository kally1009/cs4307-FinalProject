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
CONSTRAINT agency_id FOREIGN KEY (id) REFERENCES AGENCIES(id),
base_salary integer
);

CREATE TABLE PEOPLE(
id integer PRIMARY KEY,
last_name text,
f_name text,
status text,
CONSTRAINT title FOREIGN KEY (job_title) references JOBS(job_title),
real_salary integer,
hours integer,
CONSTRAINT agency_id FOREIGN KEY (id) REFERENCES AGENCIES(id)
);


