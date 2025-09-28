from dbhandler import DatabaseConnection
from logger import Logger
class DuplicateRegistrationError (Exception):
    pass
class InvalidCredentialsError (Exception):
    pass

class student:
    def __init__(self):
        self.db = DatabaseConnection()
        self.logger = Logger(self.__class__.__name__)   

    def Registration(self,name,email, password):
        print("Registration Initiated")
        self.logger.write_log("Registration Initiated", level="info")
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from students where email = %s"
            cursor.execute(query,(email,))
            rows = cursor.fetchall()
            if (len(rows))>0:
                print("Student email is not registered")
                self.logger.write_log("Duplicate registration attempt", level="warning")
                raise DuplicateRegistrationError("Email already registered")
            query = "Insert into students(name,email, password) values(%s,%s,%s)"
            cursor.execute(query,( name, email, password))
            conn.commit()
            print(f"Student '{name}' is registered successfully !!")
            self.logger.write_log(f"Student '{name}' is registered successfully !!", level="info")
        except Exception as e:
            print (f"Exception occured {e} exception type : {type(e)}")
            self.logger.write_log(f"Exception occured {e} exception type : {type(e)}", level="error")
            raise e
        finally:    
            cursor.close()
            self.db.close_connection()


    
    def Login(self, email, password): 
        print("Login Initiated")
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = "select * from students where email = %s"
            cursor.execute(query,(email,))
            rows = cursor.fetchall()
            return_value = False
            if (len(rows))==0:
                print("Student email is not registered")
                self.logger.write_log("Student email is not registered", level="warning")
                return_value = False
            else:
                if rows[0][3] == password:
                    print("Successfully logged in")
                    self.logger.write_log("Successfully logged in", level="info")
                    return_value = True
                else:
                    print("Credential doesn't match")
                    self.logger.write_log("Credential    doesn't match", level="warning")
                    return_value = False
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


    