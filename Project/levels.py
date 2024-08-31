from sources import *
from Terminal import *


def A(game, terminal):
    QR = QR_A
    foundtexts = foundtexts_A

    A1(game, terminal)

    game.add_prompt("Gaining sight after the blinding flash of light you find yourself in a majestic greek temple. You realize that you've just explored the first level of the temple, and now you see ahead of you 6 more levels to surpass.")
    game.elohim(elohim_messages[11]+elohim_messages[12])
    game.add_prompt("You go ahead and enter the second circle of light that should bring you to the next level.")

    A2(game, terminal)
    A3(game, terminal)
    A4(game, terminal)
    A5(game, terminal)
    A6(game, terminal)
    A7(game, terminal)

    game.A_ = True

    game.add_prompt("You find yourself again and for the last time in the now explored temple. You've completed all 7 levels and got all 10 sigils.")
    game.elohim(elohim_messages[28])
    game.add_prompt("As the voice speaks, the closed gates of the temple finally opens.")
    game.elohim(elohim_messages[27])


    terminal.start(game, foundtexts)

    game.display_messages(QR)

    game.add_prompt("Exiting the temple you find yourself on a big artic isle, with everything covered in ice and snow. Only now you see the exterior of the complex A in which was the temple. Not too far you can see two more complexes to explore, B and C, and a infinitelly high tower that stands touching the black clouds above you.")

    game.elohim(elohim_messages[56])
    
    chosen_option = game.choose_option(["Proceed by going to plexus B.", "Enter the tower."])

    with open('A.txt', 'w') as f:
        f.write(game.output)

    if chosen_option == "Enter the tower.":
        game.tower_ = True
        T(game, terminal)

def B(game, terminal):
    QR = QR_B
    foundtexts = foundtexts_B

    game.add_prompt("You enter the complex B and find yourself inside an ancient egiptian tomb. You see a lot of sand on the ground and lit torches on the walls, everything looking like the insides of a pyramid.")

    game.elohim(elohim_messages[29])

    game.add_prompt("You see the same circles of the previous temple emitting light from the ground. You go ahead and enter the first circle of light that should bring you to the first level.")

    B1(game, terminal)
    B2(game, terminal)
    B3(game, terminal)
    B4(game, terminal)
    B5(game, terminal)
    B6(game, terminal)
    B7(game, terminal)

    game.add_prompt("You find yourself again and for the last time in the now explored tomb. You've completed all 7 levels and got all 9 sigils.")

    game.elohim(elohim_messages[30])

    game.B_ = True

    terminal.start(game, foundtexts)

    game.display_messages(QR)

    game.elohim(elohim_messages[57])

    chosen_option = game.choose_option(["Proceed by going to plexus C.", "Enter the tower."])

    with open('B.txt', 'w') as f:
        f.write(game.output)

    if chosen_option == "Enter the tower.":
        game.tower_ = True
        T(game, terminal)



def C(game, terminal):
    QR = QR_C
    foundtexts = foundtexts_C

    game.add_prompt("You enter the complex C and find yourself inside a huge christian cathedral. You see a huge hall with very high sealing and big windows full of colored glass.")

    game.elohim(elohim_messages[31])

    game.add_prompt("You see a big gate at the end of the hall made of some sort of metal. A bright light seems to pierce the gaps escaping trought the gate.")

    game.elohim(elohim_messages[32])

    game.add_prompt("You see the same circles of the previous temple emitting light from the ground. You go ahead and enter the first circle of light that should bring you to the first level, C1.")

    C1(game, terminal)
    C2(game, terminal)
    C3(game, terminal)
    C4(game, terminal)
    C5(game, terminal)
    C6(game, terminal)
    C7(game, terminal)

    game.C_ = True

    game.add_prompt("You find yourself again and for the last time in the now explored cathedral. You've completed all 7 levels and got all 9 sigils.")

    game.elohim(elohim_messages[82])

    terminal.start(game, foundtexts)

    game.display_messages(QR)

    chosen_option = game.choose_option(["Enter heaven.", "Enter the tower."])

    with open('C.txt', 'w') as f:
        f.write(game.output)

    if chosen_option == "Enter the tower.":
        T(game, terminal)
    else:
        H(game, terminal)




def T(game, terminal):

    game.add_prompt("You stand at the foot of the tower, it appears infinitelly high, reaching the black clouds above you. As soon as you take the elevator you hear the emotionless and robotic voice of EL0HIM")

    game.climb_tower += 1

    if game.climb_tower == 1:
        game.elohim(elohim_messages[51])

    if game.climb_tower == 2:
        game.elohim(elohim_messages[52])

    if game.climb_tower >= 3:
        game.elohim(elohim_messages[53])

    if game.A_ and not game.T1_:
        T1(game, terminal)

    if not game.B_:
        game.add_prompt("The elevator has floors 2,3,4,5 locked. You have to figure out a way to unlock the next floor if you want to proceed.")
        game.elohim(elohim_messages[55])
        return

    if game.B_ and not game.T2_:
        T2(game, terminal)

    if game.B_ and not game.T3_:
        T3(game, terminal)
    
    if not game.C_:
        game.add_prompt("The elevator has floors 4,5 locked. You have to figure out a way to unlock the next floor if you want to proceed.")
        game.elohim(elohim_messages[54])
        return

    if game.C_ and not game.T4_:
        T4(game, terminal)

    if game.C_ and not game.T5_:
        T5(game, terminal)
    
    if game.T5_:
        game.elohim(elohim_messages[64])
        game.got_sigils = game.do_enigma(enigma_list[1])
        chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
        if chosen_option == "Exit the tower and go to heaven.":
            H(game, terminal)
        else:
            game.elohim(elohim_messages[65])
            game.got_sigils = game.do_enigma(enigma_list[1])
            chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
            if chosen_option == "Exit the tower and go to heaven.":
                H(game, terminal)
            else:
                game.elohim(elohim_messages[66])
                game.got_sigils = game.do_enigma(enigma_list[1])
                chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                if chosen_option == "Exit the tower and go to heaven.":
                    H(game, terminal)
                else:
                    game.elohim(elohim_messages[67])
                    game.got_sigils = game.do_enigma(enigma_list[1])
                    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                    if chosen_option == "Exit the tower and go to heaven.":
                        H(game, terminal)
                    else:
                        game.elohim(elohim_messages[68])
                        game.got_sigils = game.do_enigma(enigma_list[1])
                        chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                        if chosen_option == "Exit the tower and go to heaven.":
                            H(game, terminal)
                        else:
                            game.elohim(elohim_messages[69])
                            game.got_sigils = game.do_enigma(enigma_list[1])
                            chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                            if chosen_option == "Exit the tower and go to heaven.":
                                H(game, terminal)
                            else:
                                game.elohim(elohim_messages[70])
                                game.got_sigils = game.do_enigma(enigma_list[1])
                                chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                                if chosen_option == "Exit the tower and go to heaven.":
                                    H(game, terminal)
                                else:
                                    game.elohim(elohim_messages[72])
                                    game.got_sigils = game.do_enigma(enigma_list[1])
                                    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                                    if chosen_option == "Exit the tower and go to heaven.":
                                        H(game, terminal)
                                    else:
                                        game.elohim(elohim_messages[73])
                                        game.got_sigils = game.do_enigma(enigma_list[1])
                                        chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                                        if chosen_option == "Exit the tower and go to heaven.":
                                            H(game, terminal)
                                        else:
                                            game.elohim(elohim_messages[74])
                                            game.got_sigils = game.do_enigma(enigma_list[1])
                                            chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                                            if chosen_option == "Exit the tower and go to heaven.":
                                                H(game, terminal)
                                            else:
                                                game.elohim(elohim_messages[75])
                                                game.got_sigils = game.do_enigma(enigma_list[1])
                                                chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                                                if chosen_option == "Exit the tower and go to heaven.":
                                                    H(game, terminal)
                                                else:
                                                    game.elohim(elohim_messages[77])
                                                    game.got_sigils = game.do_enigma(enigma_list[1])
                                                    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
                                                    if chosen_option == "Exit the tower and go to heaven.":
                                                        H(game, terminal)
                                                    else:
                                                        game.elohim(elohim_messages[78])
                                                        game.add_prompt("Passed the last puzzle you see at the end a majestic stand made out of gold. On it awaits you the last terminal you'll ever interact with.")
                                                        game.T_ = True
                                                        terminal.start(game, {})
                                                        game.elohim(elohim_messages[76])
                                                        print("ENDING TOWER")
                                                        with open('output.txt', 'w') as f:
                                                            f.write(game.output)
                                                        exit()
    



    

def H(game, terminal):

    if game.C_:

        game.add_prompt("The gates of heaven open to you emitting a blinding bright flash of light.")

        game.elohim(elohim_messages[83])



        if not game.H1_:
            H1(game, terminal)
        
        if not game.H2_:
            H2(game, terminal)

        if not game.H3_:
            H3(game, terminal)
            game.add_prompt("Passed the last sector you see the end of the garden. A majestic stand made out of gold awaits you, it has on it the last terminal you'll ever interact with.")
            game.H_ = True
            terminal.start(game, {})

            game.elohim(elohim_messages[84])

            print("ENDING HEAVEN")

            with open('output.txt', 'w') as f:
                f.write(game.output)
            exit()

    else:
        game.add_prompt(f"You can't enter heaven yet. You still have {game.got_sigils} seals, out of a total of {game.tot_sigils}.")








def A1(game, terminal):
    game.A1_ = True
    QR = QR_A1
    foundtexts = foundtexts_A1
    time_capsule = time_capsule_A1

    game.add_prompt("You wake up lookig at the sky. You don't remember anything, you do not know who you are, where you are, or how did you got here. You see ancient ruins resembling rome or greek culture immerse in a mediterranean enviroment.")

    game.elohim(elohim_messages[1]+elohim_messages[2])
    
    game.got_sigils = game.do_enigma(enigma_list[1])

    game.elohim(elohim_messages[3])

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.elohim(elohim_messages[4])

    game.got_sigils = game.do_enigma(enigma_list[1])

    terminal.start(game, foundtexts)

    game.elohim(elohim_messages[5])

    game.add_prompt("Next to the wall you see a circle on the ground emitting bright light.")

    game.elohim(elohim_messages[10])

    game.add_prompt("You step on the circle and enter the blinding bright flash of light.")

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

def A2(game, terminal):
    game.A2_ = True
    QR = QR_A2
    foundtexts = foundtexts_A2
    time_capsule = time_capsule_A2

    game.add_prompt(enter_A)

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.elohim(elohim_messages[13])

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_A)

def A3(game, terminal):
    game.A3_ = True
    QR = QR_A3
    foundtexts = foundtexts_A3
    time_capsule = time_capsule_A3

    game.add_prompt(enter_A)

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.elohim(elohim_messages[25])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_A)

def A4(game, terminal):
    game.A4_ = True
    QR = QR_A4
    foundtexts = foundtexts_A4
    time_capsule = time_capsule_A4

    game.add_prompt(enter_A)

    game.elohim(elohim_messages[14])

    game.add_prompt("You can suddenly see the world glitching, the trees disappearing and the sky getting darker. everything stops as soon as the thundering voice from the skys roars")

    game.elohim(elohim_messages[48]+elohim_messages[49])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_A)

def A5(game, terminal):
    game.A5_ = True
    QR = QR_A5
    foundtexts = foundtexts_A5
    time_capsule = time_capsule_A5

    game.add_prompt(enter_A)

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_A)

def A6(game, terminal):
    game.A6_ = True
    QR = QR_A6
    foundtexts = foundtexts_A6
    time_capsule = time_capsule_A6

    game.add_prompt(enter_A)

    terminal.start(game, foundtexts)

    game.elohim(elohim_messages[15])

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_A)

def A7(game, terminal):
    game.A7_ = True
    QR = QR_A7
    foundtexts = foundtexts_A7
    time_capsule = time_capsule_A7

    game.add_prompt(enter_A)

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt("You step on the circle and enter the blinding bright flash of light.")

def B1(game, terminal):
    game.B1_ = True
    QR = QR_B1
    foundtexts = foundtexts_B1
    time_capsule = time_capsule_B1

    game.add_prompt("As the light dissipates, you find yourself in a desert, surrounded by sand. You see some palms and some egiptian structures.")

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.add_prompt("A shadow appears in the distance, running and screaming quickly approaching you. The shadow suddenly dissapears before making contact with you as soon as the voice from the sky thunders.")

    game.elohim(elohim_messages[46]+elohim_messages[47])

    game.display_messages(QR)

    game.add_prompt(exit_B)

def B2(game, terminal):
    game.B2_ = True
    QR = QR_B2
    foundtexts = foundtexts_B2
    time_capsule = time_capsule_B2

    game.add_prompt(enter_B)

    game.elohim(elohim_messages[17])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_B)

def B3(game, terminal):
    game.B3_ = True
    QR = QR_B3
    foundtexts = foundtexts_B3
    time_capsule = time_capsule_B3

    game.add_prompt(enter_B)

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_B)

def B4(game, terminal):
    game.B4_ = True
    QR = QR_B4
    foundtexts = foundtexts_B4
    time_capsule = time_capsule_B4

    game.add_prompt(enter_B)

    game.elohim(elohim_messages[18])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.add_prompt("Suddenly the world starts glitching, the piramids start disappearing and the palms start trembling. Everythig stops when the voice from the sky roars in anger.")

    game.elohim(elohim_messages[50])

    game.display_messages(QR)

    game.add_prompt(exit_B)

def B5(game, terminal):
    game.B5_ = True
    QR = QR_B5
    foundtexts = foundtexts_B5
    time_capsule = time_capsule_B5

    game.add_prompt(enter_B)

    game.elohim(elohim_messages[19])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_B)

def B6(game, terminal):
    game.B6_ = True
    QR = QR_B6
    foundtexts = foundtexts_B6
    time_capsule = time_capsule_B6

    game.add_prompt(enter_B)

    game.elohim(elohim_messages[20])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_B)

def B7(game, terminal):
    game.B7_ = True
    QR = QR_B7
    foundtexts = foundtexts_B7
    time_capsule = time_capsule_B7

    game.add_prompt(enter_B)

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.display_messages(QR)

    game.add_prompt("You step on the circle and enter the blinding bright flash of light.")

def C1(game, terminal):
    game.C1_ = True
    QR = QR_C1
    foundtexts = foundtexts_C1
    time_capsule = time_capsule_C1

    game.add_prompt("As the light dissipates, you find yourself in a beautiful garden surrounded by ruins of walls made of stone blocks resembling medieval castles.")

    game.elohim(elohim_messages[21])
    
    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.add_prompt("After solving the puzzle you take the sigil, and as you do a piece of the terreain beneath you dissapears making you fall into darkness. Here nothing exists, nothing can be seen, you just hear the cold and emotionless voice of EL0HIM repeating to himself in circle.")

    game.elohim(elohim_messages[45])

    game.add_prompt("After some seconds that seemed to have lasted minutes, you dissapear from the darkness and reappear on the surface of the level.")

    game.display_messages(QR)

    game.add_prompt(exit_C)

def C2(game, terminal):
    game.C2_ = True
    QR = QR_C2
    foundtexts = foundtexts_C2
    time_capsule = time_capsule_C2

    game.add_prompt(enter_C)

    game.elohim(elohim_messages[26])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.elohim(elohim_messages[37])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_C)

def C3(game, terminal):
    game.C3_ = True
    QR = QR_C3
    foundtexts = foundtexts_C3
    time_capsule = time_capsule_C3

    game.add_prompt(enter_C)

    game.elohim(elohim_messages[22])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_C)

def C4(game, terminal):
    game.C4_ = True
    QR = QR_C4
    foundtexts = foundtexts_C4
    time_capsule = time_capsule_C4

    game.add_prompt(enter_C)

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_C)

def C5(game, terminal):
    game.C5_ = True
    QR = QR_C5
    foundtexts = foundtexts_C5
    time_capsule = time_capsule_C5

    game.add_prompt(enter_C)

    game.elohim(elohim_messages[23])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_C)

def C6(game, terminal):
    game.C6_ = True
    QR = QR_C6
    foundtexts = foundtexts_C6
    time_capsule = time_capsule_C6

    game.add_prompt(enter_C)

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    game.add_prompt(exit_C)

def C7(game, terminal):
    game.C7_ = True
    QR = QR_C7
    foundtexts = foundtexts_C7
    time_capsule = time_capsule_C7

    game.add_prompt(enter_C)

    game.elohim(elohim_messages[24])

    terminal.start(game, foundtexts)

    game.got_sigils = game.do_enigma(enigma_list[1])

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.display_messages(QR)

    game.add_prompt("You step on the circle and enter the blinding bright flash of light.")


def T1(game, terminal):
    QR = QR_T1
    foundtexts = foundtexts_T1
    time_capsule = time_capsule_T1

    game.T1_ = True

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    terminal.start(game, foundtexts)

    game.display_messages(QR)


    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)


def T2(game, terminal):

    game.T2_ = True

    QR = QR_T2
    foundtexts = foundtexts_T2
    time_capsule = time_capsule_T2

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    terminal.start(game, foundtexts)


    game.display_messages(QR)

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)



def T3(game, terminal):

    game.T3_ = True

    QR = QR_T3
    foundtexts = foundtexts_T3
    time_capsule = time_capsule_T3

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    terminal.start(game, foundtexts)


    game.display_messages(QR)

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)


def T4(game, terminal):

    game.T4_ = True

    QR = QR_T4
    foundtexts = foundtexts_T4
    time_capsule = time_capsule_T4

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    terminal.start(game, foundtexts)


    game.display_messages(QR)

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)


def T5(game, terminal):
    QR = QR_T5
    time_capsule = time_capsule_T5

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.got_sigils = game.do_enigma(enigma_list[1])

    game.display_messages(QR)

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)
    
    game.add_prompt("This is the last floor reachable with the elevator. You see a long set of stairs covered by foggy clouds, and as you go forward to uncover this mistery EL0HIM speaks worried and angry.")
    game.elohim(elohim_messages[58])

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)
    
    game.elohim(elohim_messages[59])

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)
    
    game.elohim(elohim_messages[60])

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)
    
    game.elohim(elohim_messages[61])

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)
    
    game.elohim(elohim_messages[62])

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)
    
    game.add_prompt("Exiting from the fog caused by the clouds at the end of the long staircase, you see a long set of puzzles that block your way. They separate you from the truth, if you want to uncover it you'll have to solve them all.")
    game.elohim(elohim_messages[63])

    chosen_option = game.choose_option(["Exit the tower and go to heaven.", "Proceed your path in the tower."])
    if chosen_option == "Exit the tower and go to heaven.":
        H(game, terminal)

    game.T5_ = True


def H1(game, terminal):

    game.H1_ = True

    QR = QR_H1
    foundtexts = foundtexts_H1
    time_capsule = time_capsule_H1

    game.add_prompt("You find yourself in a beatiful open garden, with the sun shining high in the sky, with some waterfalls and a crystal clear water pond. To progress you'll need to cross the garden trought the 3 sectors C,A,B in which it is divided. But you'll not need to solve any more puzzles since you were judged worthy.")

    game.elohim(elohim_messages[43])

    terminal.start(game, foundtexts)

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    chosen_option = game.choose_option(["Proceed on your way to heaven.", "Go back and enter the tower."])
    if chosen_option == "Go back and enter the tower.":
        T(game, terminal)



def H2(game, terminal):
    QR = QR_H2
    foundtexts = foundtexts_H2
    time_capsule = time_capsule_H2

    game.H2_ = True

    terminal.start(game, foundtexts)

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    chosen_option = game.choose_option(["Proceed on your way to heaven.", "Go back and enter the tower."])
    if chosen_option == "Go back and enter the tower.":
        T(game, terminal)




def H3(game, terminal):
    QR = QR_H3
    foundtexts = foundtexts_H3
    time_capsule = time_capsule_H3

    game.H3_ = True

    terminal.start(game, foundtexts)

    if time_capsule:
        game.listen_timecapsule(time_capsule)

    game.display_messages(QR)

    chosen_option = game.choose_option(["Proceed on your way to heaven.", "Go back and enter the tower."])
    if chosen_option == "Go back and enter the tower.":
        T(game, terminal)

    

