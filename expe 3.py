tpl1=(9, 0, 1, 3, 10, 23)
tpl2=(2, 4, 7, 8, 2, 11)
def juntaordenados(tpl1, tpl2):
    tplnew =()
    for i in tpl1 :
        tplnew = tplnew + (i,)
    for i in tpl2 :
        tplnew = tplnew + (i,)

    return tplnew
(juntaordenados(tpl1, tpl2)).sort(True)
print(juntaordenados(tpl1, tpl2))
	
