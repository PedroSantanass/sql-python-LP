import time
import pandas as pd

df = pd.DataFrame({ 'Nome':   ['Pedro', 'João' ,'José'], 
                    'Celular':['+5581999272781', '+5518996847677', '+5577999321234'],
                    'CPF':    ['70576146404', '12345678910', '31235554501'],
                    'CNPJ':   ['36978520001007', '86132644000159', '22615315000186'],
                    'Saldo':  [0, 1500, 150]})
class Transacao():
    def __init__(self, valor_transacao = '', nome='', tipo_pix='', chave_pix='', pessoa_receb='', saldo_conta=''):
        self.nome         = nome
        self.valor        = valor_transacao
        self.tipo_pix     = tipo_pix
        self.chave_pix    = chave_pix
        self.pessoa_receb = pessoa_receb
        self.saldo_conta  = 0        
    def executar_transacao(self, df): 
        ########################################################CPF#############################################################
        self.nome                 = input('Qual o seu nome?\n')
        self.tipo_pix             = input('Qual o tipo da chave pix? EX: CPF, Celular, CNPJ\n')
        if self.tipo_pix == 'CPF':
            self.chave_pix        = str(input('Digite aqui a chave PIX:\n'))
            df_filtrada = df.loc[df['CPF'] == self.chave_pix]
            if len(df_filtrada.index) == 1:
                pass
            elif len(df_filtrada.index) == 0:
                print('CPF inválido/não encontrado.')
                exit()    
            elif len(self.chave_pix) < 11:
                self.chave_pix    = str(input('Quantidade de caracteres insuficiente, digite novamente seu cpf:\n'))   
            elif len(self.chave_pix) > 12:
                self.chave_pix    = str(input('Quantidade de caracteres excedentes, digite novamente seu cpf:\n'))                  
        #####################################################CELULAR###########################################################
        elif self.tipo_pix == 'Celular':
            self.chave_pix         = str(input('Digite aqui a chave PIX:\n'))
            df_filtrada = df.loc[df['Celular'] == self.chave_pix]
            if len(df_filtrada.index) == 1:
                pass
            elif len(df_filtrada.index) == 0:
                print('Número de telefone inválido/não encontrado.\n')
                exit() 
            elif len(self.chave_pix) < 14:
                self.chave_pix     = str(input('Quantidade de caracteres insuficiente, digite seu numero no formato +5581999272781:\n'))
            elif len(self.chave_pix) > 15:
                self.chave_pix    = str(input('Quantidade de caracteres excedentes, digite novamente seu Celular:\n'))            
        #######################################################CNPJ##############################################################
        elif self.tipo_pix == 'CNPJ':
            self.chave_pix        = str(input('Digite aqui a chave PIX:\n'))
            df_filtrada = df.loc[df['CNPJ'] == self.chave_pix]
            if len(df_filtrada.index) == 1:
                pass
            elif len(df_filtrada.index) == 0:
                print('Não encontramos seu CNPJ.')
                exit()
            elif len(self.chave_pix) < 14:
                self.chave_pix    = str(input('Quantidade de caracteres insuficiente, digite seu CPNJ no formato RRRRRRRSSSSDD:\n')) 
            elif len(self.chave_pix) < 13:
                self.chave_pix    = str(input('Quantidade de caracteres insuficiente, digite novamente seu CNPJ:\n'))
            else:
                print('Não encontramos seu CNPJ.')
                exit()
        ############################################################################################################################            
        resposta = input('Deseja confirmar sua transferência?\n')
        
        if resposta == 'sim':    
            print('OK, vamos processar a transferencia!')
            time.sleep(2)            
            self.valor_transacao      = int(input('Qual o valor da transação bancaria?\n'))
            print("Transição em execução...")
            time.sleep(3)
            self.saldo_conta          = self.valor_transacao
            print("Transação excutada com sucesso, seu saldo é: " + str(self.saldo_conta))        
        #####################################
        else:
            print('Oops, não encontramos este tipo de chave em nosso sistema')
            time.sleep(3)
            print('Operação cancelada...')
            exit()
        #####################################
t1 = Transacao()
t1.executar_transacao(df)
