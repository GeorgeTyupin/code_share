import pickle

class Database:
    def create_db(self , name = "data.db"):
        self.Codes = []
        with open(name , 'wb') as f:
            pickle.dump(self , f)

    def load_db(self , name = "data.db"):
        self.Codes = []
        with open(name , 'rb') as f:
            temp_obj = pickle.load(f)
            self.Codes = temp_obj.Codes[:]
    
    def save_code(self, code):
        new_id = len(self.Codes) + 1
        code.id = new_id
        code.href = code.id
        self.Codes.append(code)
        self.update()
        
    def update(self , name="data.db"):     
        with open(name , 'wb') as f:
            pickle.dump(self , f)

class Code:
    data = ""
    #уникальных параметр
    id = 0
    #уникальных параметр
    href = ""
    
    