import sys
import sqlite3

def get_avg_sal(family):
    connection = sqlite3.connect('survey.db')
    cursor = connection.cursor()
    
    sql = "SELECT avg(reading) \
           FROM Person JOIN Survey \
           ON Person.ident = Survey.person \
           WHERE Survey.quant = 'sal' \
           AND Person.family = ?"
           
    cursor.execute(sql, [family])
    results = cursor.fetchall()
    sal = results[0][0]
    
    connection.close()

    return sal

for line in sys.stdin:
    family = line.strip()
    sal = get_avg_sal(family)
    print sal, family

