import csv
import sys
import psycopg2

def main(fname):
    conn = psycopg2.connect('dbname = customer')
    curr = conn.cursor()
    data = curr.execute("""SELECT * from customer;"""),
    customer_info = curr.fetchall()
    
    with open(fname, 'wt') as f:
        writer = csv.writer(f)
        writer.writerow(('name','address','email'))
        for i in customer_info:
            writer.writerow(i)

if __name__ == "__main__":
    main(sys.argv[1])
