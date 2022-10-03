import mysql.connector

class BD:
    """Classe para conexão ao banco de dados"""

    connectionDict = {"host": "localhost",
                      "database": "BoTiago", "user": "root", "password": "*******"}

    def conectar():
        """Estabelece a conexão com o banco de dados"""

        conn = mysql.connector.connect(
            host=BD.connectionDict["host"],
            database=BD.connectionDict["database"],
            user=BD.connectionDict["user"],
            password=BD.connectionDict["password"]
        )
        return conn

    def selecionar(comando):
        """Executa comando SELECT no banco de dados"""

        try:
            conn = BD.conectar()
            cursor = conn.cursor()
            cursor.execute(comando)
        except Exception as e:
            tipo_erro = type(e).__name__
            print("Erro do tipo: {}\n Mensagem de erro: {}.".format(tipo_erro, e))
        else:
            resultado = cursor.fetchall()
            conn.close()
            return resultado
