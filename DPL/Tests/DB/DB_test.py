from DPLSystem.DB.dbHandler import dbHandler
from Tests.InitializeDb import User, Deliveries, DPLstations

class DbTest():
    def __init__(self):
        self.dbHandler = dbHandler('dbTest')
    def insert_user(self, newUser):
        self.dbHandler.insert_user(newUser)
        pass
    def get_all(self, table, condition=None, value=None):
        if not condition:
            return Session.query(table).all()
        else:
            return Session.query(table).filter_by(condition=value).all()

    def user_test(self):
        users = []
        users.append( User(email = '1@1.com', first_name='Bob', last_name='Bob', password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y",
                    postal_code = "V3E3B5") )
        users.append( User(email = '2@1.com', first_name='Sina', last_name='Bob', password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y",
                    postal_code = "V3E3B5") )
        users.append( User(email = '3@1.com', first_name='Mike', last_name='Bob', password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y",
                    postal_code = "V3E3B5") )
        users.append( User(email = '4@1.com', first_name='John', last_name='Bob', password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y",
                    postal_code = "V3E3B5") )
        a = self.dbHandler.test_insert_users(users)
        assert(a)
        users = []
        users.append( User(email = '1@2.com', first_name='Bob', last_name='Bob', password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y",
                    postal_code = "V3E3B5") )
        users.append( User(email = '1@3.com', first_name='Asa', last_name='Bob', password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y",
                    postal_code = "V3E3B5") )
        users.append( User(email = '1@4.com', first_name='Johnny', last_name='Bob', password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y",
                    postal_code = "V3E3B5") )
        users.append( User(email = '1@1.com', first_name='Bob', last_name='Bob', password="$2b$12$ppAg.mOnlIo15d0m7gPYr.1LZaUvuO29JVVBkv6bkQzQz6zK.f66y",
                    postal_code = "V3E3B5") )
        a = self.dbHandler.test_insert_users(users)
        assert(a)
        return True
    def delivery_test(self):
        deliveries = []
        deliveries.append( Deliveries(to_customer = 1) )
        deliveries.append( Deliveries(to_customer = 2) )
        deliveries.append( Deliveries(to_customer = 3) )
        deliveries.append( Deliveries(to_customer = 4) )
        assert ( self.dbHandler.test_insert_deliveries(deliveries) )
        deliveries = []
        deliveries.append( Deliveries(to_customer = 100) )
        assert ( not self.dbHandler.test_insert_deliveries(deliveries) )
        deliveries = []
        deliveries.append( Deliveries(to_customer = 3) )
        assert ( not self.dbHandler.test_insert_deliveries(deliveries) )
        return True
    def Cascade_delete_testing(self):
        self.dbHandler.delete_user(self)
        deliveries = self.dbHandler.get_all_deliveries()
        for d in deliveries:
            assert(not d.owner_id == 1)
        return True

    def run_all_tests(self):
        assert(self.user_test )
        assert(self.delivery_test )
        assert(self.Cascade_delete_testing )
        return True

dbT = DbTest()
if dbT.run_all_tests():
    print("All Db test passed succesfully")
else:
    print("Failuer some DB tests failed")
