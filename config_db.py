
#######################################################################################
#Configurações com banco de dados MySQL
#######################################################################################

SECRET_KEY = 'univesp_ti'

#CONSTANTE#
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}@{servidor}/{database}'.format(
        SGBD = 'mysql',
        usuario = 'root',
        servidor = 'localhost',
        database = 'satelite_prd'
    )



    #######################################################################################