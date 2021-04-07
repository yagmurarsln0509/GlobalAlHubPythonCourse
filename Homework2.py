d1 = {'user_name': 'Yagmur' , 'password': '12345'} 

user_name1 = input('Lütfen kullanıcı adınızı giriniz: ')
password1= input('Lütfen Parolanızı giriniz: ')

if (d1['user_name'] != user_name1 and d1['password'] == password1):
    print('Kullanıcı adınız hatalı ')
elif (d1['user_name'] == user_name1 and d1['password']  != password1):
    print('Parolanız hatalı')
elif ( d1['user_name'] != user_name1 and d1['password']  != password1):
    print('Kullanıcı adınız ve parolanız hatalı')
else:
    print('Başarılı giriş yaptınız')
