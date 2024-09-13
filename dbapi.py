import pymysql

class dbprocess():
    def __init__(self) -> None:
        pass

    def dbconnect(self):
        connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456syy',
        db='goods',
        charset='utf8mb4', # 字符集  
        cursorclass=pymysql.cursors.DictCursor  # 返回字典类型的结果  
    )
        return connection

    def dbtablecreate(self,connection):
        
        try:  
            with connection.cursor() as cursor:  
                # 创建goods数据库  
                create_db_sql = "CREATE DATABASE IF NOT EXISTS goods"  
                cursor.execute(create_db_sql)  
                
                # 选择goods数据库  
                use_db_sql = "USE goods"  
                cursor.execute(use_db_sql)  
                
                # 创建数据表goods_items  
                create_table_sql = """  
                CREATE TABLE Goods (  
                    id INT AUTO_INCREMENT PRIMARY KEY,  
                    category VARCHAR(50) NOT NULL,  -- 大类名称：螺类、蟹钳、扇贝  
                    name VARCHAR(255) NOT NULL,     -- 商品名称  
                    price DECIMAL(10, 2) NOT NULL,  -- 商品价格  
                    remarks TEXT,                    -- 备注  
                    modified_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- 修改日期  
                    previous_price DECIMAL(10, 2),  -- 之前价格  
                    image_url VARCHAR(255)          -- 图片URL  
                );
                """  
                cursor.execute(create_table_sql)  
                
            # 提交事务  
            connection.commit()  
            print("Database and table created successfully.")  
        
        except pymysql.MySQLError as e:  
            print(f"Error: {e}")  
        
        finally:  
            # 关闭连接  
            connection.close()

    def adddata(self,connection,category,name, price, spec, remarks,  previous_price, image_url):
        try:  
            with connection.cursor() as cursor:  
                # 插入数据示例  
                insert_sql = """  
                INSERT INTO goods (category, name, price, spec, remarks,  previous_price, image_url)  
                VALUES (%s, %s, %s, %s, %s, %s, %s)  
                """  
                data = (  
                    category,  
                    name, 
                    price,
                    spec,  
                    remarks,  
                    previous_price,  
                    image_url 
                )  
                cursor.execute(insert_sql, data)  
        
            # 提交事务  
            connection.commit()  
            print("Data inserted successfully.")  
        
        except pymysql.MySQLError as e:  
            print(f"Error: {e}")  
        
        finally:  
            # 关闭连接  
            connection.close()
    def deletedata(self,connection,id):
        try:  
            with connection.cursor() as cursor:  
                # 插入数据示例  
                insert_sql = "DELETE FROM goods WHERE id = %s;" 
                cursor.execute(insert_sql, id)  
        
            # 提交事务  
            connection.commit()  
            print("Data deleted successfully.")  
        
        except pymysql.MySQLError as e:  
            print(f"Error: {e}")  
        
        finally:  
            # 关闭连接  
            connection.close()






