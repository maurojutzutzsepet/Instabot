from instabot import Bot
mau = Bot()
mau.login(username="snt_boot", password="Hol1s*")
pediruser = input('ingrese el usuario')
listaFotos = mau.get_total_user_medias(pediruser)
mau.download_photos(listaFotos, folder="persona1", save_description=True)