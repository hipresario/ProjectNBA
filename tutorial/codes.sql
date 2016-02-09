.mode csv
.import out.csv table1
.tables
.mode column
select * from table1 order by from_year desc;
select from_year , count(*), avg(champ), sum(champ) from table1 group by from_year;
delete from table1 where from_year<1990;
select * from table1;

.schema table1
.help
update table1 set champ=50 where from_year=2003;
select * from table1;
select Franchise, from_year, champ from table1 where yrs>=20;
select Franchise, from_year, champ from table1 where yrs>=20 and champ>0;
select Franchise, from_year, champ from table1 where yrs>=20 or champ>0;
select * from table1 where Franchise like "M%";

select avg(temp.total_yrs) from (select from_year,sum(yrs) as total_yrs from table1 group by from_year) temp;
select from_year,sum(yrs) as total_yrs from table1 group by from_year;

.mode csv
.import out_title.csv table2
select count(*) from table2;

create table table3(Franchise,yrs,champ);
insert into table3 select Franchise,yrs,champ from table2;

select * from table3 a , table1 b where a.Franchise=b.Franchise;
select * from table3 a left join table1 b on a.Franchise=b.Franchise;

create table table4 as select * from table3 a left join table1 b on a.Franchise=b.Franchise;
select * from table4;

.tables
.save demo.db
.exit

