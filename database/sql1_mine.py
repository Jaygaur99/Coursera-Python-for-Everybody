import sqlite3 as S
conn = S.connect('emaildb-sqlite')
con = conn.cursor()

con.execute('DROP TABLE IF EXISTS Counts')
con.execute('CREATE TABLE Counts(org TEXT,count INTEGER)')

fhand = input('Enter file name')
if len(fhand)<1:fhand = 'mbox.txt'
fh = open(fhand)
for line in fh:
    if not line.startswith('From: '):continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    print(org)

    con.execute('SELECT count FROM Counts WHERE org = ?',(org,))
    row = con.fetchone()
    if row is None:
        con.execute('INSERT INTO Counts(org , count) VALUES( ? , 1)',(org,))
    else:
        con.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in con.execute(sqlstr) :
    print (str(row[0]), row[1])

con.close()
