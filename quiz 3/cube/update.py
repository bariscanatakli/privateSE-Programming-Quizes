from states import *



def update(square,a = onyuz,b = sagyuz,c = arkayuz,d = solyuz,e = altyuz,f = ustyuz):
    onyuz.update({square: a.get(square) })
    sagyuz.update({square: b.get(square) })
    arkayuz.update({square: c.get(square) })
    solyuz.update({square: d.get(square) })
    altyuz.update({square: e.get(square) })
    ustyuz.update({square: f.get(square) })