import sqlite3
import sys

#initialize sql database 'vote'
conn = sqlite3.connect('vote.sqlite')
#initialize cursor to communicate with database
cur = conn.cursor()

def get_winner_of_state(state):
	sql_fetch_query_bunty = "SELECT * FROM vote WHERE state=\'{state}\' and voted_for='Bunty'".format(state=state)
	bunty_record = select_query(sql_fetch_query_bunty)

	sql_fetch_query_bubli = "SELECT * FROM vote WHERE state=\'{state}\' and voted_for='Babli'".format(state=state)
	babli_record = select_query(sql_fetch_query_bubli)

	if(len(bunty_record) == 0 and len(babli_record) == 0):
		return "Invalid"

	winner_of_state = get_max_voted(len(bunty_record), len(babli_record))
	return winner_of_state

def get_winner_for_country():
	sql_get_states = "SELECT state FROM vote group by state"
	records = select_query(sql_get_states)

	winner_per_state = []

	for record in records:
		output = get_winner_of_state(record[0])
		winner_per_state.append(output)
	
	elect_president = get_max_voted(winner_per_state.count("Bunty"),winner_per_state.count("Babli"))
	# print(elect_president)
	return elect_president

#------------------------------------------HELPER FUNCTIONS-------------------------------------------------------
def select_query(query):
	cur.execute(query)
	record = cur.fetchall()
	return record

def get_max_voted(bunty_count, babli_count):
	if(bunty_count > babli_count):
		return 'Bunty'
	elif(bunty_count < babli_count):
		return 'Babli'
	else :
		return 'Draw'

# get_winner_of_state('Arizona')
# get_winner_for_country()