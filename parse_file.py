import sqlite3
import csv

#initialize sql database 'vote'
conn = sqlite3.connect('vote.sqlite')
#initialize cursor to communicate with database
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS vote')
cur.execute('''CREATE TABLE "vote"(
	"voter_id" TEXT,
	"state" TEXT,
	"voted_for" TEXT	
)
''')

with open("input.csv") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		print(row)
		voter_id = row[0]
		state = row[1]
		voted_for = row[2]
		cur.execute('''INSERT INTO vote(voter_id,state,voted_for)
			VALUES (?,?,?)''',(voter_id,state,voted_for))
		conn.commit()