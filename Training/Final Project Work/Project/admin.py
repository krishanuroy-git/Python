from dbhandler import DatabaseConnection
from logger import Logger
class DuplicateRegistrationError (Exception):
    pass
class InvalidCredentialsError (Exception):
    pass

class admin:
    def __init__(self):
        self.db = DatabaseConnection()
        self.logger = Logger(self.__class__.__name__)

    def Registration(self,name, password):
        print("Registration Initiated")
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from admins where username = %s"
            cursor.execute(query,(name,))
            rows = cursor.fetchall()
            if (len(rows))>0:
                print("Admin name is already registered")
                self.logger.write_log("Duplicate registration attempt", level="warning")
                raise DuplicateRegistrationError("Name already registered")
            query = "Insert into admins(username, password) values(%s,%s)"
            cursor.execute(query,( name, password))
            conn.commit()
            print(f"Admin '{name}' is registered successfully !!")
            self.logger.write_log(f"Admin '{name}' is registered successfully !!", level="info")
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.write_log(f"Exception occured {e} exception type : {type(e)}", level="error")
            raise e
        finally:
            cursor.close()
            self.db.close_connection()      

    def Login(self, user, password): 
        print("Admin Login Initiated")
        self.logger.write_log("Admin Login Initiated", level="info")
        return_value = False
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from admins where username = %s"
            cursor.execute(query,(user,))
            rows = cursor.fetchall()
            if (len(rows))==0:
                print("The User is not admin")
                self.logger.write_log("The User is not admin", level="warning")
                return_value = False
            else:
                if rows[0][2] == password:
                    print("Successfully logged in as admin")
                    self.logger.write_log("Successfully logged in as admin", level="info")  
                    return_value = True
                else:
                    print("Admin Credential doesn't match")
                    self.logger.write_log("Admin Credential doesn't match", level="warning")
                    raise InvalidCredentialsError("Invalid admin credentials")
        except InvalidCredentialsError as e:
            print(f"Exception occurred: {e}")
            self.logger.write_log(f"Exception occurred: {e} type: {type(e)}", level="error")
            return_value = False
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.write_log(f"Exception occured {e} exception type : {type(e)}", level="error")
            return_value = False
        finally:    
            cursor.close()
            self.db.close_connection()
        return return_value
