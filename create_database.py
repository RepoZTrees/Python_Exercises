import psycopg2
from faker import Faker

def main():
    conn = psycopg2.connect('dbname = customer')
    curr = conn.cursor()
    for i in range(1,11):
        fake = Faker()
        #print(fake.name())
        curr.execute("""INSERT INTO customer(id, name, address, email)
        VALUES(%s, %s, %s, %s);""",
                     (i, fake.name(), fake.address(), fake.email()))
        conn.commit()
        
    
if __name__ == "__main__":
    main()
