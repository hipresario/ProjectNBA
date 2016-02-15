/*.mode csv
.import player_since_2000_stats.csv PLAYER_STATS
.import player_since_2000_profile.csv PLAYER_PROFILE
.import player_since_2000_salary.csv PLAYER_SALARY
.import seasons.csv SEASONS
.tables
.mode column*/
.headers on

/* question 4a */

/*What is the average salary of each team by season of each team
starting in 2002 and finishing 2012 season?*/
/* What is the variance of the salaries?*/
CREATE VIEW team_salary AS
SELECT season, team, avg(salary) av_salary 
	from PLAYER_SALARY
	where season IN ('2002-03', '2003-04', '2004-05', '2005-06', '2006-07', '2007-08', '2008-09', '2009-10', '2010-11', '2011-12')
	group by team, season
	order by season;

.mode csv
.output q4a1.csv
SELECT * FROM team_salary;
.output stdout

.mode column
CREATE VIEW team_salary_var AS
SELECT ps.season, ps.team, avg((ps.salary - ts.av_salary) * (ps.salary - ts.av_salary)) as var_salary
	from PLAYER_SALARY ps, team_salary ts
	where ps.team = ts.team and ps.season = ts.season
	group by ps.team, ps.season
	order by ps.season;

.mode csv
.output q4a2.csv
SELECT * FROM team_salary_var;
.output stdout

/*result: please see q4a1.csv and q4a2.csv*/

/* question 4b */
/*What is the average age of the players by season?*/

.output q4b1.csv
SELECT season, tm, avg(age) 
	from PLAYER_STATS
	group by tm, season
	order by season;
.output stdout
	
/*result: please see q4b1.csv*/

.mode column

/* Average and variance of experience by season of each team?*/

CREATE VIEW team_exp AS
SELECT s.SeasonName season, ps.tm team, avg(s.SeasonStart-p.since) av_exp
	from seasons s, player_profile p, player_stats ps
	where p.player = ps.name and s.SeasonName = ps.Season
	group by s.SeasonName, ps.tm;

.mode csv
.output q4b2.csv
SELECT * FROM team_exp;
.output stdout

/*result: please see q4b2.csv*/

.mode column
CREATE VIEW team_exp_var AS
SELECT s.SeasonName season, ps.tm team, avg((s.SeasonStart - p.since - te.av_exp) * (s.SeasonStart - p.since - te.av_exp)) as var_exp
	from seasons s, player_profile p, player_stats ps, team_exp te
	where p.player = ps.name and ps.tm = te.team 
	  and s.SeasonName = te.season and s.SeasonName = ps.Season
	group by s.SeasonName, ps.tm
	order by s.SeasonName;

.mode csv
.output q4b3.csv
SELECT * FROM team_exp_var;
.output stdout

.mode column

/*result: please see q4b3.csv*/

/* question 4c */
/*Can you provide the above in a “cross tabulation” format? That is,
teams are on each row, each column is a year, and the values are
the metrics above?*/

CREATE VIEW [PivotTeam_salary] AS
SELECT team AS 'Team\Season',
AVG(CASE WHEN season = '2002-03' THEN av_salary END) AS '2002-03',
AVG(CASE WHEN season = '2003-04' THEN av_salary END) AS '2003-04',
AVG(CASE WHEN season = '2004-05' THEN av_salary END) AS '2004-05',
AVG(CASE WHEN season = '2005-06' THEN av_salary END) AS '2005-06',
AVG(CASE WHEN season = '2006-07' THEN av_salary END) AS '2006-07',
AVG(CASE WHEN season = '2007-08' THEN av_salary END) AS '2007-08',
AVG(CASE WHEN season = '2008-09' THEN av_salary END) AS '2008-09',
AVG(CASE WHEN season = '2009-10' THEN av_salary END) AS '2009-10',
AVG(CASE WHEN season = '2010-11' THEN av_salary END) AS '2010-11',
AVG(CASE WHEN season = '2011-12' THEN av_salary END) AS '2011-12',
AVG(CASE WHEN season = '2012-13' THEN av_salary END) AS '2012-13',
AVG(CASE WHEN season = '2013-14' THEN av_salary END) AS '2013-14',
AVG(CASE WHEN season = '2014-15' THEN av_salary END) AS '2014-15',
AVG(CASE WHEN season = '2015-16' THEN av_salary END) AS '2015-16'
FROM team_salary
GROUP BY team;

.mode csv
.output q4c1.csv
SELECT * FROM [PivotTeam_salary];
.output stdout

CREATE VIEW [PivotTeam_salary_var] AS
SELECT team AS 'Team\Season',
AVG(CASE WHEN season = '2002-03' THEN var_salary END) AS '2002-03',
AVG(CASE WHEN season = '2003-04' THEN var_salary END) AS '2003-04',
AVG(CASE WHEN season = '2004-05' THEN var_salary END) AS '2004-05',
AVG(CASE WHEN season = '2005-06' THEN var_salary END) AS '2005-06',
AVG(CASE WHEN season = '2006-07' THEN var_salary END) AS '2006-07',
AVG(CASE WHEN season = '2007-08' THEN var_salary END) AS '2007-08',
AVG(CASE WHEN season = '2008-09' THEN var_salary END) AS '2008-09',
AVG(CASE WHEN season = '2009-10' THEN var_salary END) AS '2009-10',
AVG(CASE WHEN season = '2010-11' THEN var_salary END) AS '2010-11',
AVG(CASE WHEN season = '2011-12' THEN var_salary END) AS '2011-12',
AVG(CASE WHEN season = '2012-13' THEN var_salary END) AS '2012-13',
AVG(CASE WHEN season = '2013-14' THEN av_salary END) AS '2013-14',
AVG(CASE WHEN season = '2014-15' THEN var_salary END) AS '2014-15',
AVG(CASE WHEN season = '2015-16' THEN var_salary END) AS '2015-16'
FROM team_salary_var
GROUP BY team;

.mode csv
.output q4c2.csv
SELECT * FROM [PivotTeam_salary];
.output stdout

CREATE VIEW [PivotTeam_age] AS
SELECT tm AS 'Team\Season',
AVG(CASE WHEN season = '2002-03' THEN age END) AS '2002-03',
AVG(CASE WHEN season = '2003-04' THEN age END) AS '2003-04',
AVG(CASE WHEN season = '2004-05' THEN age END) AS '2004-05',
AVG(CASE WHEN season = '2005-06' THEN age END) AS '2005-06',
AVG(CASE WHEN season = '2006-07' THEN age END) AS '2006-07',
AVG(CASE WHEN season = '2007-08' THEN age END) AS '2007-08',
AVG(CASE WHEN season = '2008-09' THEN age END) AS '2008-09',
AVG(CASE WHEN season = '2009-10' THEN age END) AS '2009-10',
AVG(CASE WHEN season = '2010-11' THEN age END) AS '2010-11',
AVG(CASE WHEN season = '2011-12' THEN age END) AS '2011-12',
AVG(CASE WHEN season = '2012-13' THEN age END) AS '2012-13',
AVG(CASE WHEN season = '2013-14' THEN age END) AS '2013-14',
AVG(CASE WHEN season = '2014-15' THEN age END) AS '2014-15',
AVG(CASE WHEN season = '2015-16' THEN age END) AS '2015-16'
FROM PLAYER_STATS
GROUP BY tm;

.mode csv
.output q4c3.csv
SELECT * FROM [PivotTeam_age];
.output stdout

CREATE VIEW [PivotTeam_exp] AS
SELECT team AS 'Team\Season',
AVG(CASE WHEN season = '2002-03' THEN av_exp END) AS '2002-03',
AVG(CASE WHEN season = '2003-04' THEN av_exp END) AS '2003-04',
AVG(CASE WHEN season = '2004-05' THEN av_exp END) AS '2004-05',
AVG(CASE WHEN season = '2005-06' THEN av_exp END) AS '2005-06',
AVG(CASE WHEN season = '2006-07' THEN av_exp END) AS '2006-07',
AVG(CASE WHEN season = '2007-08' THEN av_exp END) AS '2007-08',
AVG(CASE WHEN season = '2008-09' THEN av_exp END) AS '2008-09',
AVG(CASE WHEN season = '2009-10' THEN av_exp END) AS '2009-10',
AVG(CASE WHEN season = '2010-11' THEN av_exp END) AS '2010-11',
AVG(CASE WHEN season = '2011-12' THEN av_exp END) AS '2011-12',
AVG(CASE WHEN season = '2012-13' THEN av_exp END) AS '2012-13',
AVG(CASE WHEN season = '2013-14' THEN av_exp END) AS '2013-14',
AVG(CASE WHEN season = '2014-15' THEN av_exp END) AS '2014-15',
AVG(CASE WHEN season = '2015-16' THEN av_exp END) AS '2015-16'
FROM team_exp
GROUP BY team;

.mode csv
.output q4c4.csv
SELECT * FROM [PivotTeam_exp];
.output stdout

CREATE VIEW [PivotTeam_exp_var] AS
SELECT team AS 'Team\Season',
AVG(CASE WHEN season = '2002-03' THEN var_exp END) AS '2002-03',
AVG(CASE WHEN season = '2003-04' THEN var_exp END) AS '2003-04',
AVG(CASE WHEN season = '2004-05' THEN var_exp END) AS '2004-05',
AVG(CASE WHEN season = '2005-06' THEN var_exp END) AS '2005-06',
AVG(CASE WHEN season = '2006-07' THEN var_exp END) AS '2006-07',
AVG(CASE WHEN season = '2007-08' THEN var_exp END) AS '2007-08',
AVG(CASE WHEN season = '2008-09' THEN var_exp END) AS '2008-09',
AVG(CASE WHEN season = '2009-10' THEN var_exp END) AS '2009-10',
AVG(CASE WHEN season = '2010-11' THEN var_exp END) AS '2010-11',
AVG(CASE WHEN season = '2011-12' THEN var_exp END) AS '2011-12',
AVG(CASE WHEN season = '2012-13' THEN var_exp END) AS '2012-13',
AVG(CASE WHEN season = '2013-14' THEN var_exp END) AS '2013-14',
AVG(CASE WHEN season = '2014-15' THEN var_exp END) AS '2014-15',
AVG(CASE WHEN season = '2015-16' THEN var_exp END) AS '2015-16'
FROM team_exp_var
GROUP BY team;

.mode csv
.output q4c5.csv
SELECT * FROM [PivotTeam_exp_var];
.output stdout

/*REFER TO REPORT*/

DROP VIEW team_salary;
DROP VIEW team_salary_var;
DROP VIEW team_exp;
DROP VIEW team_exp_var;
DROP VIEW [PivotTeam_salary];
DROP VIEW [PivotTeam_salary_var];
DROP VIEW [PivotTeam_age];
DROP VIEW [PivotTeam_exp];
DROP VIEW [PivotTeam_exp_var];