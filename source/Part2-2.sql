.mode csv
.import player_since_2000_stats.csv PLAYER_STATS
.import player_since_2000_profile.csv PLAYER_PROFILE
.import player_since_2000_salary.csv PLAYER_SALARY
.mode column

/* question 2 */
.output Q2.txt
/* How many active players are in 2011-2012 season */
select count(distinct(name))
from player_stats
where season = '2011-12';
/* ans 478 */

/* How many play in each position in 2011-2012 season */
select pos, count(*)
from player_stats
where season = '2011-12' group by pos;
/* ans
C           121       
C-PF        1         
PF          106       
PF-SF       1         
PG          114       
SF          105       
SF-PF       1         
SG          102      
Total 551 postion been played in season 11-12 
*/

/* What is the average age in 2011-2012 season */
select avg(age)
from (select name, age
      from player_stats
      where season = '2011-12' group by name);
/* ans 26.64 */

/* what is the average weight and average experience in 2011-2012 season */
select avg(wt), avg(2011-since)
from player_profile
where since <= '2011' and til >= '2012';
/* 223.300947867299  4.90995260663507 */

/* what is the average salary */
select avg(salary_view.sa_sum)
from (select sum(salary) sa_sum
      from player_salary
      where season = '2011-12' group by name) salary_view;
/* ans 4402734.65 */

/* average career salary */
select avg(player_salary_by_year.sa_sum)
from (select sum(salary) sa_sum
      from player_salary group by season, name) player_salary_by_year;
/* ans 3875105 */