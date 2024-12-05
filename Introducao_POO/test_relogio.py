import relogio

r2 = relogio.Relogio2(60)
assert r2.get_hora_formatada() == "00:01:00"
r2.adicionar_hora(2)
assert r2.get_hora_formatada() == "02:01:0?"