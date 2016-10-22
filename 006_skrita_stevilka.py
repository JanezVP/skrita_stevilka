secret = 22

guess = int (raw_input ("Ugani skrito stevilko (med 1 in 30): "))

if guess == secret:
    print "Uganili ste. Cestitamo! Skrita stevilka je 22:)"
else:
    print "Odgovor je nepravilen. To ni skrita stevilka: " + str (guess)
