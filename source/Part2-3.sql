.mode csv
.import player_since_2000_stats.csv PLAYER_STATS
.import player_since_2000_profile.csv PLAYER_PROFILE
.import player_since_2000_salary.csv PLAYER_SALARY
.mode column

/* question 3 */
.output Q3.txt
/* create a table with correct schema */
create table player_salary_new (
"Name" text,
"Season" text,
"Team" text,
"Lg" text,
"Salary" integer
);
insert into player_salary_new select * from player_salary where season='2011-12';

/* who are the top 10% best paid players in the 2011-12 season? Which team did these players play for? */
/* order salary in desc order */
select name, team, sum(salary) sa_sum
from player_salary_new
group by name
order by sa_sum desc
limit (select count(distinct(name))
       from player_salary_new)/10;
/* ans:
Kobe Bryant  Los Angeles Lakers  25244493  
Vince Carte  Dallas Mavericks    21300000  
Kevin Garne  Boston Celtics      21247044  
Tim Duncan   San Antonio Spurs   21164619  
Rashard Lew  Washington Wizards  21136631  
Gilbert Are  Orlando Magic       19269307  
Dirk Nowitz  Dallas Mavericks    19092873  
Pau Gasol    Los Angeles Lakers  18714150  
Carmelo Ant  New York Knicks     18518574  
Amar'e Stou  New York Knicks     18217705  
Dwight Howa  Orlando Magic       18091770  
Joe Johnson  Atlanta Hawks       18038573  
Richard Ham  Chicago Bulls       17500000  
Elton Brand  Philadelphia 76ers  17059727  
Chris Paul   Los Angeles Clippe  16359805  
Deron Willi  New Jersey Nets     16359805  
Brandon Roy  Portland Trail Bla  16032144  
Chris Bosh   Miami Heat          16022500  
LeBron Jame  Miami Heat          16022500  
Dwyane Wade  Miami Heat          15691000  
Kevin Duran  Oklahoma City Thun  15506632  
Paul Pierce  Boston Celtics      15333334  
Baron Davis  New York Knicks     15252181  
Zach Randol  Memphis Grizzlies   15200000  
Antawn Jami  Cleveland Cavalier  15076715  
Rudy Gay     Memphis Grizzlies   15032144  
Andrew Bynu  Los Angeles Lakers  14900000  
Chauncey Bi  Los Angeles Clippe  14200000  
Chris Kaman  New Orleans Hornet  14030000  
Al Jefferso  Utah Jazz           14000000  
Andre Iguod  Philadelphia 76ers  13531750  
Carlos Booz  Chicago Bulls       13500000  
Tyson Chand  New York Knicks     13107837  
Nene         Denver Nuggets      13000000  
Manu Ginobi  San Antonio Spurs   12981038  
Marc Gasol   Memphis Grizzlies   12922194  
Emeka Okafo  New Orleans Hornet  12541812  
Tony Parker  San Antonio Spurs   12500000  
Josh Smith   Atlanta Hawks       12400000  
LaMarcus Al  Portland Trail Bla  12372000  
Luol Deng    Chicago Bulls       12325000  
Danny Grang  Indiana Pacers      12015904  
Al Horford   Atlanta Hawks       12000000  
Andrew Bogu  Milwaukee Bucks     12000000  
Joakim Noah  Chicago Bulls       12000000  
*/

/*b whare are the bottom 10% for 2011-2012 season, which team they play? */
select name, team, sum(salary) sa_sum
from player_salary_new
group by name order by sa_sum
limit (select count(distinct(name))
       from player_salary_new)/10;

/* ans
Eric Dawson  San Antonio Spurs  38172     
Courtney Fo  Los Angeles Clipp  42009     
Garret Sile  Phoenix Suns       51097     
Andre Emmet  New Jersey Nets    61433     
Ben Uzoh     Cleveland Cavalie  61433     
Ike Diogu    San Antonio Spurs  64028     
Brian Skinn  Memphis Grizzlies  65446     
Larry Owens  New Jersey Nets    86052     
Dennis Horn  New Jersey Nets    91642     
Malcolm Tho  San Antonio Spurs  103104    
Manny Harri  Cleveland Cavalie  122942    
Carldell Jo  New Orleans Horne  168035    
Mychel Thom  Cleveland Cavalie  168035    
Earl Barron  Golden State Warr  185588    
Donald Sloa  New Orleans Horne  198629    
Jeff Foote   New Orleans Horne  225341    
Darington H  Milwaukee Bucks    245884    
Mickell Gla  Miami Heat         248263    
Derrick Car  Los Angeles Laker  270427    
Hamady N'Di  Washington Wizard  270427    
Jeff Adrien  Houston Rockets    270427    
Mike James   Chicago Bulls      277566    
Greg Smith   Houston Rockets    301733    
DaJuan Summ  New Orleans Horne  303137    
Francisco E  Philadelphia 76er  305792    
Josh Davis   Memphis Grizzlies  314041    
Lance Thoma  New Orleans Horne  328444    
Walker Russ  Detroit Pistons    374289    
Larry Hughe  Orlando Magic      414443    
Solomon Jon  New Orleans Horne  440353    
Andrew Goud  Los Angeles Laker  473604    
Charles Jen  Golden State Warr  473604    
Chris Wrigh  Golden State Warr  473604    
Cory Higgin  Charlotte Bobcats  473604    
Darius Morr  Los Angeles Laker  473604    
DeAndre Lig  Orlando Magic      473604    
E'Twaun Moo  Boston Celtics     473604    
Isaiah Thom  Sacramento Kings   473604    
Ivan Johnso  Atlanta Hawks      473604    
Jerome Jord  New York Knicks    473604    
Jon Leuer    Milwaukee Bucks    473604    
Jordan Will  New Jersey Nets    473604    
Josh Harrel  New York Knicks    473604    
Julyan Ston  Denver Nuggets     473604    
Justin Harp  Orlando Magic      473604    
*/

/* who are the middle 50% by pay? which teams did they play for*/
select name, team, sum(salary) sa_sum from player_salary_new group by name order by sa_sum limit (select count(distinct(name)) from player_salary_new)/2 offset (select count(distinct(name)) from player_salary_new)/4;

/* ans in increasing order
Quincy Pondexter  Memphis Grizzlies  1153800   
Wayne Ellington   Minnesota Timberw  1154040   
Reggie Jackson    Oklahoma City Thu  1156320   
Earl Clark        Orlando Magic      1160000   
Dominique Jones   Dallas Mavericks   1193280   
Taj Gibson        Chicago Bulls      1195680   
Royal Ivey        Oklahoma City Thu  1200000   
Brian Cook        Los Angeles Clipp  1223166   
Jannero Pargo     Atlanta Hawks      1223166   
Jason Kapono      Los Angeles Laker  1223166   
Marquis Daniels   Boston Celtics     1223166   
Maurice Evans     Washington Wizard  1223166   
Sasha Pavlovic    Boston Celtics     1223166   
Willie Green      Atlanta Hawks      1223166   
Eddy Curry        Miami Heat         1229255   
Jared Jeffries    New York Knicks    1229255   
Rasual Butler     Toronto Raptors    1229255   
Reggie Evans      Los Angeles Clipp  1229255   
Rodrigue Beauboi  Dallas Mavericks   1236720   
Damion James      New Jersey Nets    1243080   
Kenneth Faried    Denver Nuggets     1254720   
Byron Mullens     Charlotte Bobcats  1288200   
Serge Ibaka       Oklahoma City Thu  1288200   
Trevor Booker     Washington Wizard  1294920   
Hamed Haddadi     Memphis Grizzlies  1300000   
Nolan Smith       Portland Trail Bl  1306920   
Michael Redd      Phoenix Suns       1308506   
Omri Casspi       Cleveland Cavalie  1341960   
Elliot Williams   Portland Trail Bl  1348800   
Anthony Carter    Toronto Raptors    1352181   
Brian Cardinal    Dallas Mavericks   1352181   
Brian Scalabrine  Chicago Bulls      1352181   
Jamaal Magloire   Toronto Raptors    1352181   
Jason Collins     Atlanta Hawks      1352181   
Jerry Stackhouse  Atlanta Hawks      1352181   
Juwan Howard      Miami Heat         1352181   
Mike Bibby        New York Knicks    1352181   
Tony Battie       Philadelphia 76er  1352181   
Tracy McGrady     Atlanta Hawks      1352181   
Troy Murphy       Los Angeles Laker  1352181   
Vladimir Radmano  Atlanta Hawks      1352181   
Craig Brackins    Philadelphia 76er  1404960   
Tobias Harris     Milwaukee Bucks    1418160   
Darren Collison   Indiana Pacers     1455960   
James Anderson    San Antonio Spurs  1463520   
Chris Singleton   Washington Wizard  1485000   
Gary Forbes       Toronto Raptors    1500000   
Greg Oden         Portland Trail Bl  1500000   
James Jones       Miami Heat         1500000   
Jeff Ayres        Indiana Pacers     1500000   
Sebastian Telfai  Phoenix Suns       1500000   
Eric Maynor       Oklahoma City Thu  1516680   
Avery Bradley     Boston Celtics     1524480   
Iman Shumpert     New York Knicks    1563120   
Gustavo Ayon      New Orleans Horne  1567500   
Jeff Teague       Atlanta Hawks      1579920   
Eric Bledsoe      Los Angeles Clipp  1596360   
Nikola Vucevic    Philadelphia 76er  1645400   
Ty Lawson         Denver Nuggets     1654440   
Renaldo Balkman   New York Knicks    1675000   
Kevin Seraphin    Washington Wizard  1680360   
Kawhi Leonard     San Antonio Spurs  1731960   
Jrue Holiday      Philadelphia 76er  1741440   
Luke Babbitt      Portland Trail Bl  1768800   
Marcus Morris     Houston Rockets    1823280   
James Johnson     Toronto Raptors    1833120   
Omer Asik         Chicago Bulls      1857500   
Larry Sanders     Milwaukee Bucks    1861920   
Matt Barnes       Los Angeles Laker  1906200   
Markieff Morris   Phoenix Suns       1919160   
Austin Daye       Detroit Pistons    1929600   
Patrick Patterso  Houston Rockets    1959960   
Dante Cunningham  Memphis Grizzlies  2000000   
Earl Watson       Utah Jazz          2000000   
D.J. White        Charlotte Bobcats  2001167   
Donte Greene      Sacramento Kings   2015896   
Alec Burks        Utah Jazz          2020200   
Darrell Arthur    Memphis Grizzlies  2027119   
Anthony Tolliver  Minnesota Timberw  2050000   
Ed Davis          Toronto Raptors    2063040   
George Hill       Indiana Pacers     2086360   
Goran Dragic      Houston Rockets    2108000   
Klay Thompson     Golden State Warr  2126520   
Tyler Hansbrough  Indiana Pacers     2138040   
Josh Howard       Utah Jazz          2150000   
Nicolas Batum     Portland Trail Bl  2155365   
Xavier Henry      New Orleans Horne  2171640   
Rudy Fernandez    Denver Nuggets     2180443   
Kosta Koufos      Denver Nuggets     2203792   
Courtney Lee      Houston Rockets    2225093   
Jimmer Fredette   Sacramento Kings   2238360   
Ryan Anderson     Orlando Magic      2244601   
Ben Wallace       Detroit Pistons    2246400   
Keyon Dooling     Boston Celtics     2246400   
Anthony Parker    Cleveland Cavalie  2250000   
Gerald Henderson  Charlotte Bobcats  2250600   
Cole Aldrich      Oklahoma City Thu  2286000   
J.J. Hickson      Sacramento Kings   2354537   
Kemba Walker      Charlotte Bobcats  2356320   
Terrence William  Houston Rockets    2369040   
J.R. Smith        New York Knicks    2382353   
Lou Amundson      Indiana Pacers     2403000   
Paul George       Indiana Pacers     2406240   
Quentin Richards  Orlando Magic      2446600   
JaVale McGee      Washington Wizard  2462400   
Ryan Hollins      Cleveland Cavalie  2483333   
Brandon Jennings  Milwaukee Bucks    2493720   
Aaron Gray        Toronto Raptors    2500000   
DeShawn Stevenso  New Jersey Nets    2500000   
Jason Smith       New Orleans Horne  2500000   
Kenyon Martin     Los Angeles Clipp  2500000   
Reggie Williams   Charlotte Bobcats  2500000   
Gordon Hayward    Utah Jazz          2532960   
Ersan Ilyasova    Milwaukee Bucks    2541000   
Brandon Knight    Detroit Pistons    2563320   
Roy Hibbert       Indiana Pacers     2588590   
DeMar DeRozan     Toronto Raptors    2625000   
Antonio McDyess   San Antonio Spurs  2640000   
Dahntay Jones     Indiana Pacers     2700000   
Marreese Speight  Memphis Grizzlies  2721255   
Eduardo Najera    Charlotte Bobcats  2750000   
Al-Farouq Aminu   New Orleans Horne  2755560   
Bismack Biyombo   Charlotte Bobcats  2798040   
Jordan Hill       Houston Rockets    2855760   
Robin Lopez       Phoenix Suns       2862602   
Anthony Randolph  Minnesota Timberw  2911231   
Brandon Rush      Golden State Warr  2956658   
Chris Wilcox      Boston Celtics     3000000   
Jeff Foster       Indiana Pacers     3000000   
Josh McRoberts    Los Angeles Laker  3000000   
Shane Battier     Miami Heat         3000000   
Shawne Williams   New Jersey Nets    3000000   
Jason Thompson    Sacramento Kings   3001284   
Greg Monroe       Detroit Pistons    3007920   
Jerryd Bayless    Toronto Raptors    3042280   
Corey Brewer      Denver Nuggets     3059000   
Jan Vesely        Washington Wizard  3065040   
Brook Lopez       New Jersey Nets    3076983   
Stephen Curry     Golden State Warr  3117120   
Tony Allen        Memphis Grizzlies  3150000   
D.J. Augustin     Charlotte Bobcats  3236470   
Raja Bell         Utah Jazz          3240000   
Johan Petro       New Jersey Nets    3250000   
Will Bynum        Detroit Pistons    3250000   
Nick Collison     Oklahoma City Thu  3272997   
Ekpe Udoh         Golden State Warr  3294960   
Thabo Sefolosha   Oklahoma City Thu  3300000   
Matt Bonner       San Antonio Spurs  3315000   
Daequan Cook      Oklahoma City Thu  3341558   
Timofey Mozgov    Denver Nuggets     3343896   
Marco Belinelli   New Orleans Horne  3377604   
C.J. Watson       Chicago Bulls      3400000   
Derek Fisher      Los Angeles Laker  3400000   
Jonny Flynn       Houston Rockets    3414720   
Ricky Rubio       Minnesota Timberw  3480120   
Carlos Delfino    Milwaukee Bucks    3500000   
Chris Duhon       Orlando Magic      3500000   
Shannon Brown     Phoenix Suns       3500000   
Shaun Livingston  Milwaukee Bucks    3500000   
Joel Anthony      Miami Heat         3600000   
DeMarcus Cousins  Sacramento Kings   3627720   
Tiago Splitter    San Antonio Spurs  3672000   
Luke Ridnour      Minnesota Timberw  3680000   
Nick Young        Washington Wizard  3695857   
C.J. Miles        Utah Jazz          3700000   
Tristan Thompson  Cleveland Cavalie  3726600   
Mike Dunleavy     Milwaukee Bucks    3750000   
Nazr Mohammed     Oklahoma City Thu  3750000   
Udonis Haslem     Miami Heat         3780000   
Dorell Wright     Golden State Warr  3823000   
Eric Gordon       New Orleans Horne  3831184   
Matt Carroll      Charlotte Bobcats  3900000   
Anthony Morrow    New Jersey Nets    4000000   
Hakim Warrick     Phoenix Suns       4000000   
Jordan Farmar     New Jersey Nets    4000000   
Mario Chalmers    Miami Heat         4000000   
Ryan Gomes        Los Angeles Clipp  4000000   
Steve Blake       Los Angeles Laker  4000000   
Wesley Johnson    Minnesota Timberw  4006080   
Spencer Hawes     Philadelphia 76er  4051024   
Charlie Bell      Golden State Warr  4099920   
Enes Kanter       Utah Jazz          4133280   
Tyreke Evans      Sacramento Kings   4151640   
Danilo Gallinari  Denver Nuggets     4190182   
Chris Andersen    Denver Nuggets     4234000   
Brandon Bass      Boston Celtics     4250000   
Jared Dudley      Phoenix Suns       4250000   
Randy Foye        Los Angeles Clipp  4250000   
Ramon Sessions    Cleveland Cavalie  4257973   
J.J. Barea        Minnesota Timberw  4300000   
Ronny Turiaf      Washington Wizard  4360000   
Daniel Gibson     Cleveland Cavalie  4403834   
Derrick Favors    Utah Jazz          4443360   
Jonas Jerebko     Detroit Pistons    4500000   
Nikola Pekovic    Minnesota Timberw  4503600   
Derrick Williams  Minnesota Timberw  4602720   
James Harden      Oklahoma City Thu  4604760   
Linas Kleiza      Toronto Raptors    4605000   
Kevin Love        Minnesota Timberw  4609701   
Ronnie Brewer     Chicago Bulls      4710000   
Zaza Pachulia     Atlanta Hawks      4750000   
Brad Miller       Minnesota Timberw  4752000   
Darko Milicic     Minnesota Timberw  4776500   
Evan Turner       Philadelphia 76er  4947840   
Jamal Crawford    Portland Trail Bl  5000000   
Jarrett Jack      New Orleans Horne  5000000   
Jason Maxiell     Detroit Pistons    5000000   
Kyle Korver       Chicago Bulls      5000000   
Luc Mbah a Moute  Milwaukee Bucks    5000000   
Russell Westbroo  Oklahoma City Thu  5082416   
Hasheem Thabeet   Houston Rockets    5127720   
Kyrie Irving      Cleveland Cavalie  5144280   
Lou Williams      Philadelphia 76er  5176000   
Chuck Hayes       Sacramento Kings   5250000   
Martell Webster   Minnesota Timberw  5256000   
Jason Richardson  Orlando Magic      5395000   
Mike Miller       Miami Heat         5400000   
Nate Robinson     Golden State Warr  5483307   
Amir Johnson      Toronto Raptors    5500000   
John Wall         Washington Wizard  5530080   
Channing Frye     Phoenix Suns       5600000   
O.J. Mayo         Memphis Grizzlies  5632637   
Luke Walton       Los Angeles Laker  5680000   
Blake Griffin     Los Angeles Clipp  5731080   
Kyle Lowry        Houston Rockets    5750000   
Francisco Garcia  Sacramento Kings   5800000   
Josh Childress    Phoenix Suns       6000000   
Wesley Matthews   Portland Trail Bl  6135160   
*/

/* over all seasons of the active players in the 2011-12 season, 
how much money was paid to all users by season? */
select old_t.season, sum(old_t.salary)
from player_salary old_t
join player_salary_new new_t on old_t.name=new_t.name
group by old_t.season;

/* The pay out for each season
1994-95     6829800          
1995-96     15162000         
1996-97     34700500         
1997-98     52221513         
1998-99     92629020         
1999-00     160490955        
2000-01     216279076        
2001-02     281863210        
2002-03     388799322        
2003-04     537043303        
2004-05     688610545        
2005-06     929776220        
2006-07     1132500943       
2007-08     1395337795       
2008-09     1641312045       
2009-10     1817092177       
2010-11     1922169145       
2011-12     2097534601       
2012-13     2007200712       
2013-14     1809716235       
2014-15     1861266806       
2015-16     1804407886       
2016-17     1419495479       
2017-18     980897169        
2018-19     639598951        
2019-20     199038930        
2020-21     2170000          
2021-22     2170000          
*/

/* How many players were active in each season */
select old_t.season, count(distinct(old_t.name)) from player_salary old_t join player_salary_new new_t on old_t.name=new_t.name group by old_t.season;

/* ans
1994-95     3                          
1995-96     6                          
1996-97     14                         
1997-98     19                         
1998-99     30                         
1999-00     42                         
2000-01     54                         
2001-02     79                         
2002-03     94                         
2003-04     127                        
2004-05     158                        
2005-06     190                        
2006-07     215                        
2007-08     240                        
2008-09     274                        
2009-10     317                        
2010-11     379                        
2011-12     456                        
2012-13     384                        
2013-14     302                        
2014-15     292                        
2015-16     236                        
2016-17     150                        
2017-18     78                         
2018-19     42                         
2019-20     11                         
2020-21     1                          
2021-22     1                          
*/

/* what is the average per player by season? assume average pay*/
select pay.t_season, pay.t_salary/num_player.num_p
from (select old_t.season t_season, sum(old_t.salary) t_salary
from player_salary old_t
join player_salary_new new_t on old_t.name=new_t.name
group by old_t.season) pay
join
(select old_t.season num_p_season, count(distinct(old_t.name)) num_p from player_salary old_t join player_salary_new new_t on old_t.name=new_t.name group by old_t.season) num_player
on pay.t_season = num_player.num_p_season;

/*ans
1994-95     2276600                      
1995-96     2527000                      
1996-97     2478607                      
1997-98     2748500                      
1998-99     3087634                      
1999-00     3821213                      
2000-01     4005168                      
2001-02     3567888                      
2002-03     4136163                      
2003-04     4228687                      
2004-05     4358294                      
2005-06     4893559                      
2006-07     5267446                      
2007-08     5813907                      
2008-09     5990189                      
2009-10     5732151                      
2010-11     5071686                      
2011-12     4599856                      
2012-13     5227085                      
2013-14     5992437                      
2014-15     6374201                      
2015-16     7645796                      
2016-17     9463303                      
2017-18     12575604                     
2018-19     15228546                     
2019-20     18094448                     
2020-21     2170000                      
2021-22     2170000                      
*/

.output stdout
.exit
