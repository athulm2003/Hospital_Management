from mysql import connector
from datetime import datetime

class dbconnect:
    def get_connected(self):
        try:
            self.con = connector.connect(
                host="localhost",
                user="root",
                password="Athul@2003",
                database="hsptl_db"
            )
            return self.con
        except Exception as e:
            return None

class HsptlManager(dbconnect):
    def post(self,**kwargs):
        try:
            self.connect=super().get_connected()
            self.cursor=self.con.cursor()
            query="""
                        insert into patient(name,place,mobile,dr_name,admission_date)
                        values(%s,%s,%s,%s,%s)
                    """
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.con.commit()
            print("New Patient Added Successfully...!")
        except Exception as e:
            print(e)

    def get_object(self,id=None):

        self.connect=super().get_connected()
        self.cursor=self.con.cursor()
        query="select * from patient where id=%s"
        values=(id,)
        self.cursor.execute(query,values)
        record=self.cursor.fetchone()
        return record

    def retrieve(self,id=None):
        try:
            self.connect=super().get_connected()
            record=self.get_object(id=id)
            print(record)
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect=super().get_connected()
            self.cursor=self.con.cursor()
            query="select * from patient"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            return records
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            self.connect=super().get_connected()
            record=self.get_object(id=id)
            values=(id,)
            if record!=None:
                query="delete from patient where id=%s"
                self.cursor.execute(query,values)
                self.con.commit()
                print("Patient Deleted Successfully.")
            else:
                print("Patient Not Found..")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            self.connect=super().get_connected()
            record=self.get_object(id=id)
            if record!=None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k + "=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update patient set {placeholder} where id =%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.con.commit()
                print("Patient Details Updated..")
            else:
                print("Patient Not Found...")
        except Exception as e:
            print(e)






# obj=HsptlManager()
# #obj.post(name="Aswin",place="Kochi",mobile="2387863433",dr_name="Arun",admission_date=datetime.today())
# obj.put(id=2,name="Athul")