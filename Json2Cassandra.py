import argparse
from cassandra.cluster import Cluster
import json







def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("-host", help="insert host")
    parser.add_argument("-port", help="insert port")
    parser.add_argument("-keyspace", help="name base")
    parser.add_argument("-table", help="table name")
    parser.add_argument("-file", help="file name")
    arg = parser.parse_args()
    cluster = Cluster([arg.host],port=int(arg.port)) 
    session = cluster.connect()
    session.execute("USE {}".format(arg.keyspace))
    with open(arg.file) as f:
        for document in f:
            document = document.replace("'","''")
            session.execute("""
                            insert into {} JSON '{}'
                            """.format(arg.table,document))


    print("JSON inserted succefully on {} table".format(arg.table))
if __name__ == '__main__':
    run()
