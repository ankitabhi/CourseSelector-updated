drop table if exists majors_lookup;
drop table if exists course_lookup;
drop table if exists student_account_details;
drop table if exists student_academic_details;
drop table if exists student_course_details;
drop table if exists course_tags;
drop table if exists student_interests;

create table course_tags(
  course_code interger not null,
  tag_name VARCHAR not null,
  FOREIGN KEY (course_code) REFERENCES course_lookup(id)
);


create table student_interests(
  s_id integer not null,
  tag_name VARCHAR not null
);


create table student_course_details(
  id integer not null,
  course_name varchar not null,
  course_code varchar not null,
  semester varchar not null

);

create table student_account_details(
  id integer primary key AUTOINCREMENT,
  title varchar not null,
  first_name varchar not null,
  middle_name varchar,
  last_name varchar not null,
  street varchar,
  city varchar ,
  state varchar ,
  country varchar ,
  birth_date date not null,
  email varchar not null,
  password varchar not null
);

create table student_academic_details(
  id integer primary key AUTOINCREMENT,
  degree varchar not null,
  major varchar,
  semester integer not null
);


create table majors_lookup (
  id integer primary key AUTOINCREMENT,
  major_code varchar not null,
  major_name varchar not null,
  add_column1 varchar ,
  add_column2 varchar
  );

create table course_lookup (
  id integer primary key AUTOINCREMENT,
  course_code varchar not null,
  course_name varchar not null,
  major_code varchar,
  course_rating integer,
  prerequisite VARCHAR,
  credits integer not null
  );

insert into majors_lookup(major_code,major_name) values ("INFM","Information Management");
insert into majors_lookup(major_code,major_name) values ("CMSC","Computer Science");
insert into majors_lookup(major_code,major_name) values ("ENTS","Telecommunication");
insert into majors_lookup(major_code,major_name) values ("ENEE","Electrical and Computer Engineering");



insert into student_account_details(title,first_name,middle_name,last_name,email,birth_date,password) values ("Miss","Prajakta","Sanjeev","Arolker","admin","24-AUG-1990","admin");


insert into student_academic_details(degree,major,semester) values ("Masters","Information Management","Fall 2014");

insert into student_course_details(id, course_name, course_code, semester) values (1,"INFM600 - Information Environments","INFM600","Fall 2014");
insert into student_course_details(id, course_name, course_code, semester) values (1,"INFM603 - Information Technology","INFM603","Fall 2014");

insert into student_interests(s_id, tag_name) VALUES (1,"programming");
insert into student_interests(s_id, tag_name) VALUES (1,"web development");

select c.course_code from course_lookup c where c.course_code in (
  SELECT t.course_code from course_tags t where t.tag_name IN (
  SELECT s.tag_name from student_interests s where s.s_id = 1)
) and c.course_code not in (SELECT cc.course_code from student_course_details cc where cc.id = 1);



insert into course_lookup(course_code,course_name,major_code,course_rating,credits) values ("INFM600","INFM600 - Information Environments","INFM",1,3);
insert into course_lookup(course_code,course_name,major_code,course_rating,credits) values ("INFM603","INFM603 - Information Technology and Organizational Context","INFM",2,3);
insert into course_lookup(course_code,course_name,major_code,course_rating,credits) values ("INFM605","INFM605 - Users and Use Context","INFM",4,3);
insert into course_lookup(course_code,course_name,major_code,course_rating,credits) values ("INFM612","INFM612 - Management of Information Program and Services","INFM",5,3);

insert into course_lookup(course_code,course_name,major_code,course_rating,credits,prerequisite) values ("INFM620","INFM620 - Introduction to Strategic Informatino Management","INFM",2,3,"INFM612");
insert into course_lookup(course_code,course_name,major_code,course_rating,credits,prerequisite) values ("INFM700","INFM700 - Information Technology and Organizational Context","INFM",4,3,"INFM603");
insert into course_lookup(course_code,course_name,major_code,course_rating,credits,prerequisite) values ("INFM743","INFM743 - Development of Internet Applications","INFM",1,3,"INFM603");

/*
Programming
Web Development
Data Analytics
Strategic Management
Database
Information Systems*/

insert into course_tags(course_code, tag_name) VALUES ("INFM600","core");
insert into course_tags(course_code, tag_name) VALUES ("INFM603","core");
insert into course_tags(course_code, tag_name) VALUES ("INFM605","core");
insert into course_tags(course_code, tag_name) VALUES ("INFM612","core");

insert into course_tags(course_code, tag_name) VALUES ("INFM612","strategic management");
insert into course_tags(course_code, tag_name) VALUES ("INFM620","strategic management");
insert into course_tags(course_code, tag_name) VALUES ("INFM700","web development");
insert into course_tags(course_code, tag_name) VALUES ("INFM743","programming");
insert into course_tags(course_code, tag_name) VALUES ("INFM743","python");


select cc.course_code,cc.course_name,cc.prerequisite from course_lookup cc,course_tags tt where cc.course_code = tt.course_code and tt.tag_name in (select t.tag_name from course_tags t where t.course_code in (SELECT c.course_code from student_course_details c where c.id = 1)) and cc.course_code not in (SELECT c.course_code from student_course_details c where c.id = 1);