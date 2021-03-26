
#concectar no sftp 
transport = paramiko.Transport((host, port))
transport.connect(hostkey=None, username=user, password=pssw)
sf = paramiko.SFTPClient.from_transport(transport)

#upload file
sf.put(n, '/path/'+nome)

#download file
sf.chdir('/pasta')
for n in sf.listdir():
    if '.csv' in n: #verfica extensão do arquivo
        try:
            hj = datetime.strftime(datetime.now(), '%d-%m-%Y_%H%M%S')
            try:
                sf.get(f'/pasta/{n}', f'arquivos/logs/{n}')
                c += 1
                print(n+'baixado')
            except:
                pass
            try:
                #print('ok')
                sf.rename(n, f'/pasta/backup_log/{n}_{hj}.csv') #move para a pasta de backup apos download renomeando com a data do download 
            except:
                pass
        except Exception as erro:
            print(erro)
