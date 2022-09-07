import mysql.connector

class database():

    def generate_conn_singleton(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root1516",
            database="warehouse"
        )
        # cur = con.cursor()
        return con

    def sqlThick(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT Thick From WoodSize')
        data = cur.fetchall()
        data_thick = []
        thick_set = set(data)
        for i in thick_set:
            data_thick.append(i[0])
        data_thick.sort()
        conn.close()
        return data_thick

    def sqlWide(self):
        # pass
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute('SELECT Wide From WoodSize')
        data = cur.fetchall()
        data_wide = []
        wide_set = set(data)
        for i in wide_set:
            data_wide.append(i[0])
        data_wide.sort()
        conn.close()
        return data_wide

    def sqlLong(self):
        # pass
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        cur.execute('SELECT Longs From WoodSize')
        data = cur.fetchall()
        data_long = []
        long_set = set(data)
        for i in long_set:
            data_long.append(i[0])
        data_long.sort()
        conn.close()
        return data_long

    def sqlType(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        cur.execute("SELECT WoodType_name From WoodType")

        data = cur.fetchall()
        data_type= []
        type_set = set(data)
        for i in type_set:
            data_type.append(i[0])
        data_type.sort()

        conn.close()
        return   data_type

    def dataTableHome(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        cur.execute('SELECT Wood_id, Wood_code  , WoodType.WoodType_name  , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , Inputs.Quantity , Volume , Activity '
                    'FROM Wood '
                    'INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id '
                    'INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id '
                    'INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id '
                         )
        data = cur.fetchall()
        conn.close()
        return  data

    def dataTableInput(self):
        conn = self.generate_conn_singleton()
        cur = conn.cursor()

        cur.execute('SELECT Inputs.Date , Wood_id , WoodType.WoodType_name , WoodSize.Thick ,WoodSize.Wide , WoodSize.Longs , Inputs.Quantity , Volume , Inputs.Supplier '
                    'FROM Wood '
                    'INNER JOIN WoodType ON Wood.WoodType = WoodType.WoodType_id '
                    'INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.WoodSize_id '
                    'INNER JOIN Inputs ON Wood.Inputs = Inputs.Input_id '
                   )
        data = cur.fetchall()
        conn.close()
        return  data

    def dataTableHeat(self):
        pass
        # sql = cur.execute("SELECT Wood.Wood_code , WoodSize.Thick , WoodSize.Wide , WoodSize.Long ,  "
        #                   "volume , Quantity , Input.Input_date , activity "
        #                   "FROM Wood "
        #                   "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.Woodsize_id  "
        #                   "INNER JOIN Input ON Wood.Input = Input.Input_id"
        #                   )

    def search(self, value):
        print('%'+value+'%')
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql =  cur.execute(("SELECT Wood_code FROM Wood where Wood_code LIKE ?"),('%'+value+'%'))
        conn.commit()

    def updateInputTable(self,check,date,id,type,thick,wide,long,quantity,volume,supplier):
        # sql = cur.execute(("Update Wood set  Wood_id=? , volume=? Where Wood_id=?"),(id,volume,check))
        # con.commit()\
        conn = self.generate_conn_singleton()
        cur = conn.cursor()
        sql = cur.execute(("Update Wood "
                           "SET Wood_id=? ,"
                           "WoodType=(select WoodType.Woodtype_id  FROM WoodType Where Woodtype.Woodtype_name=?) ,"
                           "WoodSize=(Select WoodSize.Woodsize_id FROM WoodSize Where WoodSize.Thick=?  AND WoodSize.Wide=? AND WoodSize.Long=?) ,"
                           "Input=(select Input.Input_id FROM Input WHERE Input.Supplier=? AND Input.Input_date=? AND Input.Quantity=?) ,"
                           "volume=? "
                           "where Wood_id=?"
                           ), (id,type,thick,wide,long,supplier,date,quantity,volume,check))
        conn.commit()

    def funcDisplayEidit(self,check,date,id,type,thick,wide,long,volume,supplier):
       pass


# mycursor.execute("CREATE TABLE WoodType(woodtype_name varchar(50) ,Woodtype_id	int PRIMARY KEY)")
# mycursor.execute("CREATE TABLE User(user_id	int PRIMARY KEY,password varchar(16) , activity int )")
# mycursor.execute("CREATE TABLE Customer(customer_id	int PRIMARY KEY, customer_name varchar(50) )")
# mycursor.execute("CREATE TABLE WithdrawType(WithdrawType_id	int PRIMARY KEY,WithdrawType_name varchar(50) )")
# mycursor.execute("CREATE TABLE WoodQuality(WoodQuality_id	int PRIMARY KEY,WoodQuality_name varchar(50) )")



