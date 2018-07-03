init_code = """
if not "Army" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Army'?")

Army = USER_GLOBAL['Army']

if not "Warrior" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Warrior'?")

Warrior = USER_GLOBAL['Warrior']

if not "Defender" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Defender'?")

Defender = USER_GLOBAL['Defender']

if not issubclass(Defender, Warrior):
    raise Warning("Defender should be the subclass of the Warrior")

if not "Vampire" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Vampire'?")

Vampire = USER_GLOBAL['Vampire']

if not issubclass(Vampire, Warrior):
    raise Warning("Vampire should be the subclass of the Warrior")

fight = USER_GLOBAL['fight']

battle = USER_GLOBAL['battle']
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "1. Fight": [
        prepare_test(middle_code='''carl = Warrior()
jim = Warrior()''',
                     test="fight(carl, jim)",
                     answer=True)
                ],

    "2. Fight": [
        prepare_test(middle_code='''ramon = Warrior()
slevin = Warrior()''',
                     test="fight(ramon, slevin)",
                     answer=True)
                ],
    "3. Fight": [
        prepare_test(middle_code='''bob = Warrior()
mars = Warrior()
fight(bob, mars)''',
                     test="bob.is_alive",
                     answer=True)
                ],
    "4. Fight": [
        prepare_test(middle_code='''zeus = Warrior()
godkiller = Warrior()
fight(zeus, godkiller)''',
                     test="zeus.is_alive",
                     answer=True)
                ],
    "5. Fight": [
        prepare_test(middle_code='''husband = Warrior()
wife = Warrior()
fight(husband, wife)''',
                     test="wife.is_alive",
                     answer=False)
                ],
    "6. Fight": [
        prepare_test(middle_code='''dragon = Warrior()
knight = Warrior()
fight(dragon, knight)''',
                     test="knight.is_alive",
                     answer=False)
                ],
    "1. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 1)
army_2.add_units(Warrior, 2)''',
                     test="battle(army_1, army_2)",
                     answer=False)
                ],

    "2. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_2.add_units(Warrior, 3)''',
                     test="battle(army_1, army_2)",
                     answer=False)
                ],
    "3. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 5)
army_2.add_units(Warrior, 7)''',
                     test="battle(army_1, army_2)",
                     answer=False)
                ],
    "4. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)''',
                     test="battle(army_1, army_2)",
                     answer=True)
                ],
    "5. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 10)
army_2.add_units(Warrior, 11)''',
                     test="battle(army_1, army_2)",
                     answer=True)
                ],
    "6. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 11)
army_2.add_units(Warrior, 7)''',
                     test="battle(army_1, army_2)",
                     answer=True)
                ],
    "7. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 5)
army_1.add_units(Defender, 4)
army_1.add_units(Defender, 5)
army_2.add_units(Warrior, 4)''',
                     test="battle(army_1, army_2)",
                     answer=True)
                ],
    "8. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 5)
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
army_1.add_units(Defender, 4)''',
                     test="battle(army_1, army_2)",
                     answer=True)
                ],
    "9. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 10)
army_1.add_units(Defender, 5)
army_2.add_units(Warrior, 5)
army_1.add_units(Defender, 10)''',
                     test="battle(army_1, army_2)",
                     answer=True)
                ],
    "10. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 2)
army_1.add_units(Warrior, 1)
army_1.add_units(Defender, 1)
army_2.add_units(Warrior, 5)''',
                     test="battle(army_1, army_2)",
                     answer=False)
                ],
    "11. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 5)
army_1.add_units(Vampire, 6)
army_1.add_units(Warrior, 7)
army_2.add_units(Warrior, 6)
army_2.add_units(Defender, 6)
army_2.add_units(Vampire, 6)''',
                     test="battle(army_1, army_2)",
                     answer=True)
                ],
    "12. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 2)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 3)''',
                     test="battle(army_1, army_2)",
                     answer=False)
                ],
    "13. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 11)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 13)''',
                     test="battle(army_1, army_2)",
                     answer=False)
                ],
    "14. Battle": [
        prepare_test(middle_code='''army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 9)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 8)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 13)''',
                     test="battle(army_1, army_2)",
                     answer=True)
                ]
}
