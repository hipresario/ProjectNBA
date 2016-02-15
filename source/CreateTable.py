import sqlite3
import os
import csv
import DBConnection


currentpath = os.path.dirname(os.path.abspath(__file__))

def readCSVFile(url):
	infile = csv.DictReader(open(url,'rb'), delimiter=',')
	return infile;

def createPlayerProfile():
	sql = '''create table if not exists player_profile(
		Player,FromYear,ToYear,Pos,Ht,Wt,DOB,College
 	       )'''
	conn = DBConnection.getConnection()
	conn.execute(sql)
	print('player_profile table created...')
	conn.close()
	return

def loadPlayerProfileData():
	conn = DBConnection.getConnection()
	path = currentpath + '/data/player_since_2000_profile.csv'
	infile = readCSVFile(path)
	to_db = [(row['Player'],row['From'],row['To'], row['Pos'], row['Ht'],row['Wt'],row['DOB'],row['College']) for row in infile]
        cur = conn.cursor()
	cur.executemany("INSERT INTO player_profile (Player,FromYear,ToYear,Pos,Ht,Wt,DOB,College) VALUES (?,?,?,?,?,?,?,?);", to_db)
	conn.commit()
	print('Load Player_profile done.')
	conn.close()
	return

def createPlayerSalary():
	sql = '''CREATE TABLE IF NOT EXISTS PLAYER_SALARY(
		 Name,Season,Team,Lg,Salary
		)'''
	conn = DBConnection.getConnection()
	conn.execute(sql)
	print('PLAYER_SALARY table created...')
	conn.close()
	return 

def loadPlayerSalaryData():
	conn = DBConnection.getConnection()
	path = currentpath + '/data/player_since_2000_salary.csv'
	infile = readCSVFile(path)
	to_db = [(row['Name'],row['Season'],row['Team'], row['Lg'], row['Salary']) for row in infile]
        cur = conn.cursor()
	cur.executemany("INSERT INTO PLAYER_SALARY (Name,Season,Team,Lg,Salary) VALUES (?,?,?,?,?);", to_db)
	conn.commit()
	print('Load PLAYER_SALARY done.')
	conn.close()
	return

def createPlayerStats():
	sql = '''CREATE TABLE IF NOT EXISTS PLAYER_STATS(
		 Name,Season,Age,Tm,Lg,Pos,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,
		 BLK,TOV,PF,PTS
		)'''
	conn = DBConnection.getConnection()
	conn.execute(sql)
	print('PLAYER_STATS table created...')
	conn.close()
	return 

def loadPlayerStatsData():
	conn = DBConnection.getConnection()
	path = currentpath + '/data/player_since_2000_stats.csv'
	infile = readCSVFile(path)
	to_db = [(row['Name'],row['Season'],row['Team'], row['Lg'], row['Salary']) for row in infile]
        cur = conn.cursor()
	cur.executemany("INSERT INTO PLAYER_SALARY (Name,Season,Age,Tm,Lg,Pos,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,
		 BLK,TOV,PF,PTS) VALUES (?,?,?,?,?);", to_db)
	conn.commit()
	print('Load PLAYER_SALARY done.')
	conn.close()
	return


def createPlayerStatsFrom2011To12():
	sql = '''CREATE TABLE IF NOT EXISTS PLAYER_STATS_2011_12(
		 Name,Season,Age,Tm,Pos)'''
	conn = DBConnection.getConnection()
	conn.execute(sql)
	print('PLAYER_STATS_2011_12 table created...')
	conn.close()
	return 

def loadPlayerStatsDataFrom2011():
	conn = DBConnection.getConnection()
	cur.executemany("INSERT INTO PLAYER_STATS_2011_12 (Name,Season,Age,Tm,Lg,Pos,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS) VALUES ( ))
	conn.commit()
	print('Load PLAYER_SALARY done.')
	conn.close()
	return




def createTeamsProfile():
	sql = '''CREATE TABLE IF NOT EXISTS TEAMS_PROFILE(
		TEAM CHAR(20),
		FRANCHISE CHAR(50),
		LEAGUE CHAR(10),
		FROM_YEAR INT,
		TO_YEAR INT,
		YEARS INT,
		GAMES INT,
		WIN INT,
		LOSS INT,
		WIN_LOSS_RATIO REAL,
		PLAYOFFS INT,
		DIV_WINS INT,
		CONF_WINS INT,
		CHAMP_WINS INT
		)'''
	conn = DBConnection.getConnection()
	conn.execute(sql)
	print('TEAMS_PROFILE table created...')
	conn.close()
	return 
	
def loadTeamsProfileData():
	conn = DBConnection.getConnection()
	path = currentpath + '/data/teams_profile.csv'
	infile = readCSVFile(path)
	to_db = [(row['Team'],row['Franchise'],row['Lg'], row['From'], row['To'], row['Yrs'], row['G'], row['W'], row['L'], row['W/L%'],row['Plyfs'],row['Div'],row['Conf'],row['Champ'] ) for row in infile]
        cur = conn.cursor()
	cur.executemany("INSERT INTO TEAMS_PROFILE (TEAM, FRANCHISE,LEAGUE, FROM_YEAR,TO_YEAR,YEARS,GAMES,WIN,LOSS,WIN_LOSS_RATIO,PLAYOFFS,DIV_WINS,CONF_WINS,CHAMP_WINS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
	conn.commit()
	print('Load Teams Profile done.')
	conn.close()
	return

def createTeamStats():
	sql = '''CREATE TABLE IF NOT EXISTS TEAM_STATS(
		Name,Season,Lg,Team,W,L,W_L_Ratio,Finish,SRS,Pace,Rel_Pace,ORtg,Rel_ORtg,DRtg,Rel_DRtg,Playoffs,Coaches,Top_WS
		)'''
	conn = DBConnection.getConnection()
	conn.execute(sql)
	print('TEAM_STATS table created...')
	conn.close()
	return
	
def loadTeamStatsData():
	conn = DBConnection.getConnection()
	path = currentpath + '/data/team_season_stats.csv'
	infile = readCSVFile(path)
	to_db = [(row['Name'],row['Season'],row['Lg'], row['Team'], row['W'], row['L'], row['W/L%'], row['Finish'], row['SRS'], row['Pace'],row['Rel_Pace'],row['ORtg'],row['Rel_ORtg'],row['DRtg'],row['Rel_DRtg'],row['Playoffs'],row['Coaches'], row['Top WS'] ) for row in infile]
        cur = conn.cursor()
	cur.executemany("INSERT INTO TEAM_STATS (Name,Season,Lg,Team,W,L,W_L_Ratio,Finish,SRS,Pace,Rel_Pace,ORtg,Rel_ORtg, DRtg,Rel_DRtg,Playoffs,Coaches,Top_WS) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db)
	conn.commit()
	print('Load TEAM_STATS done.')
	conn.close()
	return
 
#testing
def readTeamsProfile():
	conn = DBConnection.getConnection()
	cursor = conn.execute("SELECT * from TEAMS_PROFILE")
	for row in cursor:
	   print "Team = ", row[0]
	   print "TO_YEAR = ", row[4]
	   print "CHAMP_WINS = ", row[13], "\n"

	print "Operation done successfully";
	conn.close()
	return
 
def readTeamStats():
	conn = DBConnection.getConnection()
	cursor = conn.execute("SELECT * from TEAM_STATS")
	for row in cursor:
	   print "Name = ", row[0]
	   print "W/L% = ", row[6]
	   print "Top WS = ", row[17], "\n"

	print "Operation done successfully";
	conn.close()
	return

def readPlayerSalary():
	conn = DBConnection.getConnection()
	cursor = conn.execute("SELECT * from PLAYER_SALARY")
	for row in cursor:
	   print "Name = ", row[0]
	   print "Season = ", row[1]
	   print "Salary = ", row[4], "\n"

	print "Operation done successfully";
	conn.close()
	return

#createTeamsProfile()
#loadTeamsProfile()
#readTeamsProfile()
#createTeamStats()
#loadTeamStatsData()
#readTeamStats()
#createPlayerSalary()
#loadPlayerSalaryData()
#readPlayerSalary()
#createPlayerProfile()
#loadPlayerProfileData()
#createPlayerFrom2011To2012();

