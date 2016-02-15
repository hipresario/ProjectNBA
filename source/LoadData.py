.mode csv
.import player_stats.csv PLAYER_STATS
.tables
.mode column

select count(distinct(name)) from player_stats where season = '2011-12';
 
