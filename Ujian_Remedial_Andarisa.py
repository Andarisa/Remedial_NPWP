def cekNPWP(nomor):
    
    
    syarat_hur_awal = ['01','02','03','04','05','06','07','08','09']

    syarat_huruf = '1234567890-.'
    
    
    status = True
    
    
    if '-' not in nomor and '.' not in nomor:
        status = False
        
        
    if '-'  in nomor and '.' in nomor:
        
        pisah = nomor.split('.')

        if len(pisah[0]) == 2 and len(pisah[1]) == 3 and len(pisah[2]) == 3 and len(pisah[3]) == 5 and len(pisah[4]) == 3 :
            status

        else:
            status = False


        pisah_2 = pisah[3].split('-')

        if len(pisah_2[0]) == 1 and len(pisah_2[1]) ==  3:
            status
        else:
            status = False
    
    
    
    if nomor[:2] not in syarat_hur_awal:
        status = False

    for i in nomor:
        if i not in syarat_huruf:
            status = False
    
    if '-' not in nomor and '.' not in nomor:
        status = False
        
    
    
    if status:
        print('Kode seri NPWP valid!')
        
        if nomor[:2] == '01' or nomor[:2] == '02' or nomor[:2] == '03':
            print(f'Identitas Wajib Pajak: {nomor[:2]} Wajib Pajak Badan')
        elif nomor[:2] == '04' or nomor[:2] == '06':
            print(f'Identitas Wajib Pajak: {nomor[:2]} Wajib Pajak Pengusaha')
        elif nomor[:2] == '05':
            print(f'Identitas Wajib Pajak: {nomor[:2]} Wajib Pajak Karyawan')
        elif nomor[:2] == '07' or nomor[:2] == '08' or nomor[:2] == '09':
            print(f'Identitas Wajib Pajak: {nomor[:2]} Wajib Pajak Orang Pribadi')
                
                
        print(f'Nomor Registrasi: {nomor[3:10]}')
                  
                  
        print(f'Alat pengaman: {nomor[11]}')
                  
            
        print(f'Kode KPP: {nomor[13:16]}')      
                  
                  
        print(f'Status Wajib Pajak: {nomor[17:]}')      
            
            
    else:
        print('Kode seri NPWP tidak valid!')
                

cekNPWP('99.999.999.9-999.999')

cekNPWP('091234560123123')

cekNPWP('09.123.456.A-123.123')

cekNPWP('02.123.456.0-212.191')


