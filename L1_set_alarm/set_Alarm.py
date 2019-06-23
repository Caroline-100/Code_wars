def set_alarm(employed, vacation):
    if employed == True and vacation == True:
        return False
    if employed == False and vacation == True:
        return False
    if employed == True and vacation == False:
        return True
    if employed == False and vacation == False:
        return False

assert set_alarm(True, True) == False, "Fails when input is True, True"
assert set_alarm(False, True) == False, "Fails when input is False, True"
assert set_alarm(False, False) == False, "Fails when input is False, False"
assert set_alarm(True, False) == True, "Fails when input is True, False"