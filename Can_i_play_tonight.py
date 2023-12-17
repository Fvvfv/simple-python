#根据对象的心情指数判断今天能否打游戏
mood_index=int(input("今天对象的心情指数是"))
if mood_index >= 60:
    print("恭喜你，今晚可以打游戏")
else:
    print("今晚最好别打游戏")