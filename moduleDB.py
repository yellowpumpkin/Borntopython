import sqlite3
con = sqlite3.connect('dbDEMO.db')
cur = con.cursor()

class database():

    def dataThick(self):
        Thick = cur.execute("SELECT Thick From WoodSize")
        data_thick = []
        thick_set = set(Thick)
        for i in thick_set:
            data_thick.append(i[0])
        data_thick.sort()
        return data_thick

    def dataWide(self):
        Wide = cur.execute("SELECT Wide From WoodSize")
        data_wide = []
        wide_set = set(Wide)
        for i in wide_set:
            data_wide.append(i[0])
        data_wide.sort()
        return data_wide

    def dataLong(self):
        Long = cur.execute("SELECT Long From WoodSize")
        data_long = []
        long_set = set(Long)
        for i in long_set:
            data_long.append(i[0])
        data_long.sort()
        return data_long

    def dataType(self):
        Type = cur.execute("SELECT woodtype_name From WoodType")
        data_type= []
        for i in Type:
            data_type.append(i[0])
        return data_type

    def dataTableInput(self):
        tableInput = cur.execute("SELECT Input.Input_date , Wood.Wood_id , Woodtype.Woodtype_name , "
                                 "WoodSize.Thick , WoodSize.Wide , WoodSize.Long , volume , Input.Supplier  "
                                 "FROM Wood "
                                 "INNER JOIN Input ON Wood.Input = Input.Input_id "
                                 "INNER JOIN WoodType ON Wood.WoodType = WoodType.Woodtype_id "
                                 "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.Woodsize_id "
                                 )

        return  tableInput

    def dataTableHome(self):
        tableHome = cur.execute("SELECT Wood.Wood_id,Wood.Wood_code, Woodtype.Woodtype_name , "
                                "WoodSize.Thick , WoodSize.Wide , WoodSize.Long , Quantity , volume  , activity  "
                                "FROM Wood "
                                "INNER JOIN WoodType ON Wood.WoodType = WoodType.Woodtype_id "
                                "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.Woodsize_id ")
        return  tableHome

    def search(self, value):
        query = ("SELECT Wood.Wood_id,Wood.Wood_code, Woodtype.Woodtype_name , "
                "WoodSize.Thick , WoodSize.Wide , WoodSize.Long , Quantity , volume  , activity  "
                "FROM Wood "
                "INNER JOIN WoodType ON Wood.WoodType = WoodType.Woodtype_id "
                "INNER JOIN WoodSize ON Wood.WoodSize = WoodSize.Woodsize_id "
                )
        results=cur.execute(query)
        print(value)
        return results

    def updateInputTable(self,date):
        # global prog
       print(date)

    def funcDisplayEidit(self):
        pass
