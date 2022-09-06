import sqlite3

con = sqlite3.connect('dbDEMO2.db')
cur = con.cursor()

class database():

    def sqlThick(self):
        sql = cur.execute("SELECT Thick From WoodSize")
        data_thick = []
        thick_set = set(sql)

        for i in thick_set:
            data_thick.append(i[0])
        data_thick.sort()
        return data_thick

    def sqlWide(self):
        sql = cur.execute("SELECT Wide From WoodSize")
        data_wide = []
        wide_set = set(sql)
        for i in wide_set:
            data_wide.append(i[0])
        data_wide.sort()
        return data_wide

    def sqlLong(self):
        sql = cur.execute("SELECT Long From WoodSize")
        data_long = []
        long_set = set(sql)
        for i in long_set:
            data_long.append(i[0])
        data_long.sort()
        return data_long

    def sqlType(self):
        sql = cur.execute("SELECT woodtype_name From WoodType").fetchall()
        data_type= []
        type_set = set(sql)
        for i in type_set:
            data_type.append(i[0])
        data_type.sort()
        return   data_type

    def dataTableHome(self):
        sql = cur.execute("SELECT Wood.Wood_id, Wood.Wood_code, Woodtype.Woodtype_name , "
                                " WoodSize.Thick , WoodSize.Wide , WoodSize.Long , Input.Quantity , volume  , activity  "
                                "FROM Wood "
                                "INNER JOIN WoodType ON Wood.WoodType = WoodType.Woodtype_id "
                                "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.Woodsize_id "
                                "INNER JOIN Input ON Wood.Input = Input.Input_id ")
        return  sql

    def dataTableInput(self):
        sql = cur.execute("SELECT Input.Input_date , Wood.Wood_id , Woodtype.Woodtype_name , "
                                 "WoodSize.Thick , WoodSize.Wide , WoodSize.Long , Input.Quantity , volume , Input.Supplier  "
                                 "FROM Wood "
                                 "INNER JOIN Input ON Wood.Input = Input.Input_id "
                                 "INNER JOIN WoodType ON Wood.WoodType = WoodType.Woodtype_id "
                                 "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.Woodsize_id "
                                 )

        return  sql

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
        sql =  cur.execute(("SELECT Wood_code FROM Wood where Wood_code LIKE ?"),('%'+value+'%')).fetchall()
        return sql


    def updateInputTable(self,check,date,id,type,thick,wide,long,quantity,volume,supplier):
        # sql = cur.execute(("Update Wood set  Wood_id=? , volume=? Where Wood_id=?"),(id,volume,check))
        # con.commit()\
        sql = cur.execute(("Update Wood "
                           "SET Wood_id=? ,"
                           "WoodType=(select WoodType.Woodtype_id  FROM WoodType Where Woodtype.Woodtype_name=?) ,"
                           "WoodSize=(Select WoodSize.Woodsize_id FROM WoodSize Where WoodSize.Thick=?  AND WoodSize.Wide=? AND WoodSize.Long=?) ,"
                           "Input=(select Input.Input_id FROM Input WHERE Input.Supplier=? AND Input.Input_date=? AND Input.Quantity=?) ,"
                           "volume=? "
                           "where Wood_id=?"
                           ), (id,type,thick,wide,long,supplier,date,quantity,volume,check))
        con.commit()

    def funcDisplayEidit(self,check,date,id,type,thick,wide,long,volume,supplier):
       pass
