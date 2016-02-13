.mode csv
.import player_stats.csv PLAYER_STATS
.tables
.mode column

/* question 2 */

/* How many active players are in 2011-2012 season */
select count(distinct(name)) from player_stats where season = '2011-12';
/* ans 353 */

/* How many play in each position in 2011-2012 season */
select pos, count(*) from player_stats where season = '2011-12' group by pos;
/* ans
C           87        
C-PF        1         
PF          85        
PG          76        
SF          74        
SF-PF       1         
SG          78   
Total 402 postion been played in season 11-12 
*/

/* What is the average age in 2011-2012 season */
select avg(age) from (select name, age from player_stats where season = '2011-12' group by name);
/* ans 25.64

/* what is the average weight in 2011-2012 season */
/* need to get from player profile page. Does not include player stats page */

/* what is the average salary */


/* average career salary */


/* question 3 */
