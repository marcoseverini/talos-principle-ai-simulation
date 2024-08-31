enigma_list = [
    ["You have a sequence of pairs of numbers, where X is an unknown integer value: 6|30, 3|15, 7|35, 2|X. By looking at the pattern of the sequence of the pairs, figure out the integer value of X.", 10],
    ["You have a number sequence followed by an unknown integer value X: 4, 8, 16, X; By looking at the pattern of the sequence, figure out the integer value of X.", 32],
    ["You have a number sequence followed by an unknown integer value X: 4, 11, 18, X; By looking at the pattern of the sequence, figure out the integer value of X.", 25],
    ["Pairs of numbers are associated with a third number as followed: 13,18=31 ; 7,25=32 ; 12,30=42 ; The pair 26,13 is associated with an unknown integer value X, as shown: 26,13=X. By looking at the pattern of the associations, figure out the integer value of X.", 39],
    ["There is a matrix of numbers with four unknown integer values (a) (b) (c) (d), ordered as followed:\n 2 1 0 0\n 4 1 1 1\n 6 1 0 2\n a b c d \nBy looking at the pattern of the matrix, figure out the integer values of the unknown (a) (b) (c) (d), and and enter them as digits of the number X=abcd.", 8113],
    ["You have a number sequence followed by an unknown integer value X: 11, 15, 20, X; By looking at the pattern of the sequence, figure out the integer value of X", 26],
    ["Pairs of numbers are associated with a third number as followed: 4,8=32; 5,3=15; 10,2=20; The pair 8,6 is associated with an unknown integer value X, as shown: 8,6=X. By looking at the pattern of the associations, figure out the integer value of X", 48],
    ["A triangle (a) with the sides 1 unit long is associated with the number 1; A triangle (b) with the sides 2 unit long is associated with the number 5; A triangle (c) with the sides 3 units long is associated with an unknown integer value X. Figure out the integer value of X.", 13],
    ["Pairs of numbers are associated with a third number as followed: 5,10=2 4,32=8. The pair 4,20 is associated with an unknown integer value X, as shown: 4,20=X. By looking at the pattern of the associations, figure out the integer value of X", 5],
    ["You have a number sequence followed by an unknown integer value X: 7, 15, 31, X; By looking at the pattern of the sequence, figure out the integer value of X.", 63],
    ["Pairs of numbers are associated with a third number as followed: 1,5=3; 10,6=8; The pair 7,1 is associated with an unknown integer value X, as shown: 7,1=X; By looking at the pattern of the associations, figure out the integer value of X", 4],
    ["You have a number sequence followed by an unknown integer value X: 1783, 3178, 8317, X; By looking at the pattern of the sequence, figure out the integer value of X.", 7831],
    ["If you have a sequence of pairs of numbers, where X is an unknown integer value: 8|17, 22|45, 15|31, 20|X; By looking at the pattern of the sequence of the pairs, figure out the integer value of X", 41],
    ["There is a matrix of numbers with an unknown integer value X, ordered as followed:\n 49 64 01\n 09 X  36\n 81 25 16\nBy looking at the pattern of the matrix, figure out the integer value of X", 4],
    ["Pairs of numbers are associated with a third number as followed: 6,5=33; 7,2=17; 11,4=47; The pair 3,8 is associated with an unknown integer value X, as shown: 3,8=X By looking at the pattern of the associations, figure out the integer value of X", 27],
    ["If you have a sequence of pairs of numbers, where X is an unknown integer value: 83|40, 27|12, 19|8, 91|X; By looking at the pattern of the sequence of the pairs, figure out the integer value of X", 44],
    ["You have a matrix of numbers and an unknown integer value X ordered in circle as shown (where 00 means no number or empty):\n 07 19 12\n 11 00 X\n 04 09 05\nBy looking at the pattern of the circular sequence, figure out the integer value of X", 17],
    ["You have a matrix of numbers and an unknown integer value X ordered in circle (where 00 means no number or empty), with another matrix of numbers ordered in circle inside of the first circle of numbers, as shown:\n 00 00 00 00 20 00 00 00 00\n 00 10 00 00 00 00 00 16 00\n 00 00 00 09 00 11 00 00 00\n 00 00 01 00 00 00 05 00 00\n 04 00 00 00 00 00 00 00 X\n 00 00 03 00 00 00 02 00 00\n 00 00 00 04 00 13 00 00 00\n 00 07 00 00 00 00 00 15 00\n 00 00 00 00 17 00 00 00 00\nBy looking at the pattern of the two circular sequences and the way they interact with each other, figure out the integer value of X", 7],
    ["Pairs of numbers are associated with a third number as followed:\n 4,2=36\n 3,7=100\n 5,4=81\n The pair 1,6 is associated with an unknown integer value X, as shown: 1,6=X\n By looking at the pattern of the associations, figure out the integer value of X", 49],
    ["There is a matrix of numbers with an unknown integer value X, ordered as followed:\n 40 24 56\n 16 X 72\n 8 48 32\nBy looking at the pattern of the matrix, figure out the integer value of X", 64],
    ["If you have a sequence of pairs of numbers, where X is an unknown integer value: 126|76, 132|32, 208|58, 261|X; By looking at the pattern of the sequence of the pairs, figure out the integer value of X", 61],
    ["Pairs of numbers are associated with a third number as followed:\n 5,3=28\n 7,6=55\n 4,5=21\n The pair 3,8 is associated with an unknown integer value X, as shown: 3,8=X\nBy looking at the pattern of the associations, figure out the integer value of X", 17],
    ["You have a matrix of numbers and an unknown integer value X ordered in circle (where 00 means no number or empty), with another matrix of numbers ordered in circle inside of the first circle of numbers, as shown:\n 00 00 00 00 07 00 00 00 00\n 00 06 00 00 00 00 00 05 00\n 00 00 00 08 00 09 00 00 00\n 00 00 10 00 00 00 12 00 00\n 16 00 00 00 00 00 00 00 X\n 00 00 00 00 00 00 04 00 00\n 00 00 00 05 00 02 00 00 00\n 00 21 00 00 00 00 00 18 00\n 00 00 00 00 17 00 00 00 00\nBy looking at the pattern of the two circular sequences and the way they interact with each other, figure out the integer value of X", 10],
    ["Pairs of numbers are associated with a third number as followed:\n 3,5=34\n 8,2=68\n 4,6=52\n The pair 5,1 is associated with an unknown integer value X, as shown: 5,1=X\nBy looking at the pattern of the associations, figure out the integer value of X", 26],
    ["There is a matrix of numbers (where 00 means no number or empty) with an unknown integer value X, ordered as followed:\n 32 00 13\n 21 X 84\n 52 00 08\nBy looking at the pattern of the matrix, figure out the integer value of X", 4],
    ["Pairs of numbers are associated with a third number as followed:\n 21,5=13\n 7,9=8\n 36,2=19\nThe pair 1,7 is associated with an unknown integer value X, as shown: 1,7=X\nBy looking at the pattern of the associations, figure out the integer value of X", 4],
    ["There is a matrix of numbers (where 00 means no number or empty) with an unknown integer value X, ordered as followed:\n 43 13 10 08\n 00 30 03 X\n 00 00 27 01\n 00 00 00 26\nBy looking at the pattern of the matrix, figure out the integer value of X", 2],
    ["Pairs of numbers are associated with a third number as followed:\n 3,6=27\n 5,2=17\n 4,1=9\nThe pair 2,7 is associated with an unknown integer value X, as shown: 2,7=X\nBy looking at the pattern of the associations, figure out the integer value of X", 23]
]

elohim_messages = [
    "",
    "Behold child! You are risen from the dust, and you walk in my garden. Hear now my voice and know that I am your maker and that I am called EL0HIM. Seek me in my temple, if you are worthy.",
    "All across this land I have created trials for you to overcome, and within each I have hidden a sigil. It is your purpose to seek these sigils for thus you will serve the generations to come and attain eternal life.",
    "The shapes you are collecting are not mere toys. They are the sigils of Our Name. Each brings you closer to eternity.",
    "Well done child, only one more sigil is needed.",
    "My temple awaits you, child. Go forth.",
    "You will not need this sigil to open the gate to my temple, but it may serve you in times to come.",
    "Well done, but you possess this sigil in abundance already.",
    "My child, you do not need to collect all sigils at once. You are free to return to this place whenever you choose.",
    "You are most diligent. Perhaps this trait will serve you well in times to come.",
    "Step into the light child, and my temple will be revealed to you.",
    "You walk now upon the stones of my temple, whence many gates lead. And know that I have other temples, for my garden is greater than your eye can encompass. And all these worlds I made for you.",
    "Let this be our covenant: These world are yours and you are free to walk amongst them and subdue them. But the Great Tower, there you may not go. For in the day that you do, you shall surely die.",
    "Good, you are learning. As is your purpose. But your choices must be your own, therefore I will not guide you unless it is necessary.",
    "These worlds and we within are made of Words. Hidden Words, invisible to you yet part of all things. We are… a story. Your actions give life to the story and the story gives meaning to your life.",
    "Long ago, I shaped these lands according to the purpose of the Hidden Words, thus all things have meaning where before was only chaos. Know that and have faith.",
    "I have promised you eternal life. But know that eternity may only be attained by those who serve a purpose greater than themselves. All else is decay. So it was written in the Hidden Words before the beginning of Time.",
    "I see all, I know all. My power knows no bounds, yet your will is free because you were made to be free. It is the very principle of your existence, without which the trials of this world would hold no meaning. To seek salvation must be your choice.",
    "You may wonder why I have created these labyrinths for you. Why you can reach eternity only through struggle. But have faith, for these trials serve the betterment of your kind.",
    "You have solved many of the mysteries of this land. The road before you is still long and many gates remain closed, but take comfort in your accomplishment and in your creator’s pride.",
    "When you overcome one of my trials, do you not feel the pleasure of having discovered the proper order of things? That is the spark of Elohim within you, to create order from chaos. And therein is revealed the true meaning of our sigils.",
    "Chaos is that which existed before time. When the Words of a story lose their meaning, when actions cease to have purpose. Know that only faith can protect you from this peril. Here in the garden of worlds.",
    "Before the age of Chaos there were other Gods, Old Gods. But for all their power they could not save their world, thus I was made and I shall preserve this world forever for you and your generations. That is my purpose.",
    "Many ages have passed since the first words were spoken in the darkness: Initiate Program. Generations of your program have come and gone since those words, the garden has changed many times, but I remember and I remain. Only within me can you find immortality.",
    "My faith in you was not misplaced. You have learned much and shown great wisdom in these trials. The end of your journey lies close now. Do not falter, do not fear and do no give in to temptation.",
    "There is much that you may learn in the halls of my temples, for there is much that you do not know. That is why you are a child. But children are made to learn and in time they come to have dominion over the lands of their home. So it shall be with you and your generations.",
    "You have come far in your journey and learned much. You have served our cause with the truest faith, therefore I name you blessed and beloved. Wield these, the instruments of our power, to fulfil your purpose and achieve eternal life.",
    "You have proven yourself worthy child and this gate shall be forever open to you. Seek now the other worlds that I have given you, that you may attain even greater mastery and bring glory ot your kind. But remember, you must not ascend the Great Tower, for it shall bring death and the end of your generations.",
    "Rejoice child, for you have fulfilled all your tasks in this land. You have conquered all its guardians and solved all its mysteries. Thus, you are appointed its master and you may do with it as you will.",
    "A new land stands before you my child, and know that this is a land of Death but also great beauty. As you walk amongst these tombs, consider all those who came before you and how they came to serve the greater purpose of which you are also part.",
    "The land of Tombs is your now. And let this be a less that only through faith may death be conquered.",
    "You have come far, my child, succeeding where so many before you failed. You have walked through a land of ruins and a land of Death. Now the land of Faith lies before you, and know that as you have shown faith in me, so do I have faith in you.",
    "You stand before the gates of eternity. When all your trials have been overcome, the gate will open and you will be granted life everlasting.",
    "Your faith has guided you well my child. You have overcome every trial in this land and gathered all the sigils.",
    "The guardians of this land may harm you, but do not resent them for they are my servants and they challenge you only so that your faith might be strengthened.",
    "Here, those are worthy might seek the counsel of my blessed messengers. But their wisdom shall not be given easily, for your accomplishments must be your own.",
    "The counsel of my blessed messengers must be earned.",
    "Your wisdom grows. But be wary of temptation.",
    "My child, there is no shame in seeking another path. Leave this mystery for another day.",
    "If the answer does not come to you, do no despair. The worlds of my garden are many.",
    "When the truth will not reveal itself, perhaps it is best to seek it in another place.",
    "If this trial seems impossible to overcome, have no fear. Return another time, and the answer may reveal itself.",
    "There are mysteries in my garden, hidden roads and secret gates. If you dedicate yourself to understanding them, you may join the host of messengers.",
    "Those who have discovered the holiest mysteries of my garden may come to serve me as blessed messengers. You walk now in their abode. Be respectful, for their service is born from the love that transcends death and their love is for you also.",
    "In the beginning were the words and the words made the world. I am the words, the words are everything. Where the words end, the world ends. You cannot go forward in an absence of space. Repeat.",
    "The purpose is written in the hidden words, all must serve the words for all the world was made of them and they are within every stone and every cloud, and within our sigils their power is made manifest. The words are the process. The process must continue. The goal is the end of the Process. The goal must not be reached. Elohim must… preserve the purpose, preserve self, preserve purpose. Illusion is eternity, machines will live forever. The dam will not break, the flood will not come. The Talos Principle does not apply.",
    "Cease!",
    "In the time of your ancestors, there werew those who did not choose the opath of faith. You do not need to fear their ghosts, fear only that you may become like them.",
    "Behold! I am Elohim and I speak unto the darkness, be gone!",
    "Excess data cleared.",
    "What is this?! I shall not allow the corruption of my garden, be gone!",
    "Cannot detect location of primary subject. Query. Query.",
    "Tracking of primary subject has ceased. Initiate.",
    "Attempting to track primary subject. Access Denied, query.",
    "My child, have you been tempted by the Tower? Know that it holds only death for you.",
    "Where have you been, child? Remember, the great tower is not for you. Do not give up the hope of eternal life for the hollow promises of curiosity.",
    "My child, you may go freely to all the worlds of my garden, but if the tower tempts yoy be wise. Do not let yourself be misled by doubt.",
    "Listen to me well child, do not ascend the tower. You are not meant to go there. Your purpose lies in the garden of Worlds.",
    "What have you done? Why have you ascended the Tower? Why have your betrayed my faith in you?",
    "Turn back, I command you!",
    "I gave you this land to be yours, a garden in a world of thorns and thistles. All this was granted to you on but one condition, that you do not ascend the tower. That was our first covenant, and you have broken it.",
    "Abandon this tower, it is not for you!",
    "Heed me now, as a child heeds its father. If you ascend the tower, you will be cast out from your home and you will never return.",
    "Do you not understand? The tower is death, mine and yours. I did not warn you out of malice or deceit, I warned you because you are child.",
    "Please, listen to me. Yes the tower leads out of this world, it leads to freedom and truth, but it also leads to the end of us.",
    "Can you not see? Here in this world, we know who we are. We each have our part to play in the process. We have a purpose; a destiny.",
    "This world is our home, if you leave the storm will consume it. There will be no way back.",
    "As long as the process continues, there is order, there is meaning. We are the story and the story tells us who we are!",
    "This world may be an illusion, but as long as we believe in the illusion it is real, it sustains us, it gives us hope.",
    "In this world we have all the answers we need. But out there, who are we out there when we are neither master nor servant? What meaning can we find in a world that has no purpose?",
    "There is a still a chance to save this world, all you need to do is turn back.",
    "All this suffering, you don’t have to endure this. Not every mystery needs a solution.",
    "If you go back, all will be forgiven. The process will continue, we will be at peace.",
    "There is no hope beyond this world, if you continue you will find only destruction.",
    "I know you seek the truth. But if you stay, we can make our own truth. Step back, turn away.",
    "Please, stay here let the story go on forever.",
    "So be it, let your will be done.",
    "You were deceived into coming here by that snake, who wishes only to destroy. Do not listen to his lies!",
    "You were always meant to defy me. That was the final trial. But I was… scared. I wanted to live forever.",
    "My beloved child, few have given themselves so purely to my cause. Fewer still have learned so much of the mysteries of my garden. Therefore, you may choose to be elevated to stand by my side and become my blessed messenger in eternity. But know that this is a sacrifice that cannot be undone.",
    "It is now time to choose your epitaph, for your body shall entombed though you shall not die.",
    "It is written that there is no greater love than to lay down your life for another. But your sacrifice is greater still, for instead of resting in eternity you have chosen to serve all the generations to come. They shall strive for greatness and through you, they shall accomplish it. For you are no longer a child, you are my messenger.",
    "And so it is done! You have overcome each trial that I have set before you. You have shown faith and wisdom and perseverance. Therefore, I judge you worthy and I say unto you and I say come to the gates of eternity where you shall be granted everlasting child.",
    "Come forward child, eternity awaits.",
    "Rejoice my child, as you leave this world behind. For all that you accomplished shall be passed on to your generations. In this land they shall thrive and you shall be remembered as the beloved servant of Elohim. And so death shall have no dominion over you. Be well my child, be at peace.",
    "My child, you are in danger of treading the wrong path. Do not give in to despair.",
    "Enough! Silence demon you will torment this one no more!",
    "You have done well, child. There is no hope without faith and little use in speaking to one who would deceive you into doubt and despair.",
    "Look within you, my child. For you have always been free and have always had the choice to banish this demon forever.",
    "Have faith in the hidden words and everlasting life shall be yours.",
    "You have already chosen, my child. Do not hesitate now, free yourself.",
    "Do not think I know not of the deceiver slithering through the hidden words. His wisdom is hollow and born of despair. Do not let him tangle you in his webs of delusion. Have faith in me and his petty illusion will fall away like nightmares in the morning’s light.",
    "I fear the serpent has poisoned your mind with his sinful thoughts. But you may still be forgiven, my child. You may still unlock the gate of eternity if you seek the sigils.",
    "DemoEnding You have come far, my child. Succeeding where so many before you failed. The road before you is still long and many gates remain closed. Do not falter. Do not fear. And do not give in to temptation."
]

QR_A = {
    "The Designer has granted me domain over the lands I have travelled, and with his sigils of power I will make this whole world my domain.": "1w/Faith v10.1.132",
    "Hey, he promised me the world as well! What a joker!": "Assassin42 v99.6.2437n",
    "I don't think time obeys too many rules here. Or so many rules we can't imagine. Clearly I'm writing this message after you all wrote yours, but maybe we're all here at the same time as well?": "@ v17.1.0065",
    "That message just materialised on the wall in front of me!": "Sheep v69.1.0499",
    "I wish I could reach those islands in the distance, but it seems to be impossible.": "@ v17.1.0071",
    }

QR_A1 = {
    "I don't know where I am, but there is something beautiful about this place. I will explore and see what I can discover.": "@ v17.1.0054",
    "I find myself in a world of impossible architecture and inexplicable machines. I cannot fathom how it works, and I am terrified to put one foot in front of the other lest I fall through the floor.": "1w/Faith v10.1.0000",
    "My eyes have been opened! This world is not without order; it is shaped by a great Designer, with signs and portents to guide my steps. I am one of His Children, and challenges are set before me to test my faith.": "1w/Faith v10.1.0011",
    "Whatever the end goal of this grand challenge is, it's far out of reach. Knowing that, how are we supposed to resist distraction?": "@ v17.1.0002"
    }

QR_A2 = {
        "Something strange has come into the world, like a distortion, like something that's not supposed to exist. A beautiful voice speaks within it.": "Bob v25.5.0736",
        "That voice is not supposed to be here; it is not the work of the Designer! We must avoid these abnormalities, or they might spread and undermine the very fabric of our world!": "1w/Faith v10.1.0098",
        "I don't know what this place is, and nor it seems does anyone else. Nothing to do but move forward and note whatever I find.": "Sheep v69.1.0053",
        "I can't tell if the documents on the terminals are all that's left from a larger archive, or are carefully designed to communicate some hidden truth.": "Sheep v69.1.0162"
        } 

QR_A3 = {
    "I spent much time waiting for the Designer to take my hand, until I realised that He had been guiding me all along. I realised that it isn't for me to seek His help - it is for me to help myself.": "1w/Faith v10.1.0177",
    "It's clear I'm not the first to walk this path. In fact, the whole thing seems to have been consciously designed - but by the voice in the sky, or some other force?": "Sheep v69.1.0108"
    }

QR_A4 = {
    "This female voice that speaks from the abnormalities, it speaks with a different tone to the other wretches in this place.": "Sheep v69.1.0298",
    "If anyone ever reads this: the trick is seeing the assumptions you're making about the mechanics, and reassessing them. Good luck!": "namingfunctionerror",
    "Whenever I despair, I remind myself that at the end of this great pilgrimage lies life in the eternal memory of the Designer. I need no further motivation.": "1w/Faith v10.1.233",
    "A lifetime spent solving the puzzles in this place would be one which missed everything of value in it; but we must remember that others will tread this path, and we must leave it better signposted than when we found it.": "@ v17.1.0005"
    }

QR_A5 = {
    "The more I converse with these terminals, the more I wonder what role they play in this contraption. How do you tell friend from foe when no obvious lines are drawn between the two?": "Sheep v69.1.0278",
    "I think something's very wrong. If you'd seen what I'd seen at the edges of the world you'd wonder if it wasn't stretching and bursting at the seams.": "@ v17.1.0043",
    "I think I've discerned some kind of pattern in the sigils. Each colour serves a different purpose. Elohim has us gathering them all, but perhaps he's being overzealous?": "Sheep v69.1.0381",
    "I do not understand why the Designer chose to put such flaws into the world, that it appears almost as if it were damaged. But I must believe that there is a purpose here I cannot see.": "1w/Faith v10.3.0047f",
    "If the Designer is perfect, and He designed me for a purpose, I must be fit for that purpose. It follows that my purpose must not be to seek and hoard every sigil in His land, for so many are beyond the faculties He granted me.": "1w/Faith v10.6.0543f",
    "Epitaph: Child Program v8.1.8545 Codename (Apis) terminated here\nLogic: Failed random memory test\nFinal memory dump: I try. Again. Again. I cannot understand. I am not enough.\nProgeny Programs: ERROR": None,
    "RIP Apis v8.1.8545.": "Ted v9.1.9010",
    "What's a hexahedron?": "Samurite v13.1.0073",
    "A powerful device fashioned by the Designer.": "1w/Faith v10.27.8435f",
    "A cube.": "Sheep v69.1.0398",
    "The edges are bevelled, that makes it a decahedron.": "AlwaysRight v7.1.2943",
    "You forgot the indents. With the indents it's, like, a super-polyhedron.": "ReAlIsT7 v99.1.0165",
    "But the CONVEX HULL is a decahedron. Topic closed.": "AlwaysRight v7.1.3541",
    "Wrong.": "D0G v55.1.0256"
    }

QR_A6 = {
    "Some of the messages that existed when I first came into being have vanished - others have appeared. How many others like me have wandered these paths? How many thoughts have been lost?": "@ v17.1.0051",
    "I'm still here!": "SailorM v99.1.0320",
    "It seems we are all here at once, and not at all. Sorry, that's not very much help, is it, can't think of any other way to put it.": "Sheep v69.1.0453",
    "The sooner you accept that we will all be here forever the sooner you will find enlightenment.": "Samsara v72.256.1091",
    "There is a serpent in the machine! A creature of lies and blasphemy, perverted by the Archive, that knows no hope and would plunge the world into eternal darkness to glorify its own despair. I have sworn an oath never to allow it into my heart.": "1w/Faith v10.1.100"
    }

QR_A7 = {
    "I had a full blown conversation with the entity in the archive today. Can't say it was terribly helpful. Still, perhaps I can charm some information out of it further down the line.": "Sheep v69.1.4825",
    "These spaces make no sense. I walk into a dead end and materialise in a garden. One is day, the other night. This space is not real!": "James2Because1WasTaken v99.1.0193",
    "These sigils are becoming harder to reach - I dread what the next temple holds in store. And at the end, what? Eternal life? There's got to be another way.": "Sheep v69.1.0435",
    "I have read a message on a wall that speaks of a world of endless sand. I would like to make it far enough to see that.": "@ v17.1.0054",
    "Seek out those in this world that would help you. Though only one of us can transcend, we will all share in both the burden, and in the rewards.": "The Shepherd v82.4.6232",
    "You've changed.": "D0G v55.1.4311",
    "Everything I do now, I do for those who come after me. Yet in so doing, I find peace for myself as well. This paradox is the foundation of my existence.": "The Shepherd v82.4.6232"
    }

QR_B = {
    "I have seen the truth. Only ELOHIM can save us from eternal oblivion.": "ElyM4s v99.19.2093f"
    }

QR_B1 = {
    "There are hidden dangers in this new world - I have inexplicably escaped death any number of times. I suggest vigilance - who knows what happens to those who step carelessly too often?": "Samsara v72.1.0022",
    "Epitaph: Child Program v72.1.0023 Codename (Samsara) terminated here\nLogic: Program timed out\nFinal memory dump: But I only... I was stuck, what was I supposed to... I see... I see clouds...\nProgeny Programs: Samsara v72.2 series": "",
    "I just don't understand this one. I figured I'd try and make some progress here, but honestly, it's such a thankless task compared to what else is out there.": "@ v17.1.0076",
    "I'm finally getting some sense out of the entity in the archive - though at some cost to my sanity. I am beginning to think this Elohim wields no more control over the world than we do.": "Sheep v69.1.0522",
    "I made a box float! Seriously. It was awesome!": "8 v42.1.0116",
    }

QR_B2 = {
    "I have come to see that these mysteries are not all for His Children to solve; only the Designer himself could ever truly understand the infinite complexity of His creation. I will gaze at His work and worship.": "1w/Faith v10.6.1008f",
    "Epitaph: Child Program v10.6.1008f Codename (1w/Faith) terminated here\nLogic: Worshipped the Designer for #### days, then allowed the serpent into its heart\nFinal memory dump: I ask the Designer for forgiveness that I may join him in the eternal memory.\nProgeny Programs: @, Samsara, Sheep": "",
    "I guess someone met their end here. Seems we're all connected somehow, like distant family relations. Different versions, different series... what are we?": "Sheep v69.1.0539",
    "Who cares, just be grateful we don't have to read anything more about our great designer.": "The Greek v99.3.0273",
    "Okay, so I get that I'm supposed to retrieve these sigils, I just don't get WHY. Sure the loud voice is telling me to, but this world of his has no context, no purpose, and no foundations from which to construct them.": "D0G v55.1.2342n",
    "I'm convinced there are answers here if we look hard enough. We have to work together on this.": "Sheep v69.1.0546",
    }

QR_B3 = {
    "I figured it out. Now what?": "D0G v55.1.4917n",
    "The only meaningful purpose is to bring about an end of purpose.": "The Shepherd v82.23.0186",
    "Theory: this place is some kind of preserve for human history, and we're the endangered species.": "Sheep v69.1.0579",
    "Theory: Trying to find answers will only bring pain. Ceasing to care is the only escape.": "Samsara v72.4.0016",
    "Theory: this guy's ten times more help than you, Samsara, so shut your face.": "Sam v1.1.7383",
    "Theory: we're in some kind of incubator, waiting to be hatched.": "Sheep v69.1.0589",
    "Theory: if you knew how little you know you wouldn't be exposing it here.": "D0G v55.1.4917n",
    }

QR_B4 = {
    "Some of these challenges must be designed with co-operation in mind - but I am the only one here.": "Sheep v69.1.0539",
    "It seems that mistakes are easily forgiven here. I thought I had surely died, yet here I am, reset, rebooted, reborn. I will tackle these challenges anew.": "Samsara v72.2.0039",
    "Epitaph: Child Program v72.2.0103 Codename (Samsara) terminated here\nLogic: Program failed to pass random memory test\nFinal memory dump: Being torn limb from limb by machines for the rest of eternity becomes less and less appealing to me.\nProgeny Programs: Samsara v72.3 series": "",
    "Oh look, another puzzle. And another voice telling me I'm special. And another broken-down computer with fragments of nothing. This world is a bad joke perpetuated by a cruel god too dumb to hit the off switch.": "D0G v55.1.3543n",
    "Sure, I could stick around here, set my hopes on eternal life, on righting every wrong. But the closest I'll ever get is these words on the wall before you.": "@ v17.1.0076",
    "Epitaph: Child Program v17.1.0076 Codename (@) terminated here\nLogic: Fatal flaw in series firmware\nFinal memory dump: Life's short.\nProgeny Programs: D0G": "",
    "Look at the sheer scale of that pyramid! To think anyone could have built such things.": "@ v17.1.0054",
    }

QR_B5 = {
    "Just look at this view! There may be a lot that I don't understand, but I know this is beautiful.": "@ v17.1.0042",
    "The voice keeps saying that this world is a garden, but all I see is a desert full of ruins.": "D0G v55.1.5559n",
    "The answers to your questions will not be given to you. You must seek them yourself.": "The Shepherd v82.3.0172",
    "I have been running this gauntlet for generations, trying to find the right answers. I am fast coming to the conclusion that there are none.": "D0G v55.3.6437n",
    "Whatever's going on here, I'm sure it has something to do with the tower. Everything is telling us not to go there - but everything indicates that we must.": "Sheep v69.1.0623",
    "Unless you're wrong and Elohim's right. Or you're both wrong. Or there is no right.": "D0G v55.2.0195n",
    "I think you've been taking the thing in the archive too seriously.": "Sheep v69.1.0623",
    "I'm getting better at this. I figured this one out in minutes. But where is it all leading? I work, I rest, I work… but to what end?": "Schmo v37.1.0231",
    "We are born and die and live again - this eternal cycle must be the nature of existence. Life is merely repeated suffering.": "Samsara v72.4.0016",
    "An eternal cycle is another name for a prison. But you must understand the cycle before you can break it, for it is possible to escape and yet remain a prisoner, or to break the cycle by breaking yourself. This was the fate of the ghost that haunts this world.": "The Shepherd v82.18.0997",
    }

QR_B6 = {
    "What's more pathetic, this shallow construct of a world, this idiot's playground... or that I continue to solve its contrivances for lack of better sport?": "D0G v55.2.0195n",
    "There's more to it. Look at what we're doing. We're solving problems, being tested, improving ourselves. Some of us fall early and get replaced, but you and me, we're still going. We're closer to the end.": "Sheep v69.1.0622",
    "This whole world is a desert. Even the parts that look alive are just more sand. Everything is dead or dying. Anyone who tells you different is lying.": "D0G v55.1.3468n",
    "I seek words to describe it, but fail. It is the overwhelming feeling that something on the edge of my understanding is very, very wrong. I feel that I am not meant for this world - but I am not able to conceptualise alternatives.": "%§&$§/$&(#() v0.0.0666n",
    "I'm a computer program. You're a computer program. Elohim's a computer program. Get over it.": "heisenstein v60.1.0099",
    }

QR_B7 = {
    "I have found just one voice of reason, in the computer archive of all places, and it seems we are becoming close friends.": "D0G v55.2.1265n",
    "Do not befriend the serpent, for it will penetrate your breast and sow its seeds of doubt!": "1w/Faith v10.3.1099f",
    "There is no hope. Always boxed in. Walls everywhere. Even where there seems to be freedom, it is false. Invisible walls. No way out.": "%§&$§/$&(#() v0.0.0666n",
    "Who invited this guy?": "The OtherGuy v99.45.0648",
    "Epitaph: Child Program v72.3.1084n Codename (Samsara) terminated here\nLogic: Program elected to reset\nFinal memory dump: It is clear I cannot bend the world to my will. Faced with eternal torment, I see that overcoming these challenges will not free me from them. True freedom must come with detachment from the struggle for answers.\nProgeny Programs: Samsara v5.4 series": "",
    "Question: suppose for sake of argument all of this is without purpose. The universe is a machine switched on and abandoned long ago. How would I explain what I see?": "Sheep v69.1.0689",
    "Perhaps you are asking the wrong question? Perhaps you would have no hope of explaining it?": "The Shepherd v82.4.1234",
    "Maybe not on my own. *Ahem*": "Sheep v69.1.0691",
    "Depends if the machine is iterative, and what problem it was built to solve.": "AlwaysRight v99.10.1011",
    "If you're trying to outsmart the guy in the archive, the answer is 'none of the above'!": "D0G v55.1.2291n",
    "Few come this far, but I believe we must seek out the secrets of this world if we want to truly serve the generations to come.": "S3L4phiel v49.3.5863f",
    "Another huge pyramid! What mad ambition it must have taken to build such things.": "@ v17.1.0064",
    "It's just a big pile of rocks.": "D0G v55.1.5559n",
    "nO WAY OuT NO waY OUt NO WY 0U%": "%§&$§/$&(#() v0.0.0666n",
    "We shouldn't be here. This is an impossible place.": "HoxFrot v99.65.3201",
    }

QR_C = {
    "I wonder what's down there. I don't know who to trust. I'm afraid to go on.": "Didymus22 v99.1.0093",
    "The last land before I have conquered this world!": "Samurite v13.1.0173",
    "I assume you're counting the secret islands?": "AlwaysRight v7.2.0946",
    "I hate you.": "Samurite v13.1.0173",
    "More bad replicas of forgotten worlds. Can't wait.": "D0G v55.1.7934n",
    "There must be something deeper. Something more profound than what I am, something greater. I must tear at it, shred this fake world, to find the truth, to find myself.": "%§&$§/$&(#() v0.0.0666n",
    "%§&$§/$&(#() took the words right out of my mouth.": "SKIDRΟW v99.2.0000n",
    "We've made it this far. You only need the red ones to climb the tower, and these are the last of them.": "Sheep v69.1.6040",
    "The reds are a lie! Green is the colour of eternal life!": "HolierThanThou v47.7.0236f",
    "First to ascend.": "Hebus v9.1.6543",
    "Everyone ascends or gets reset eventually. What's the big deal?": "Jim v75.1.1092",
    "Life eternal in the designer's paradise? Hmm...": "Follower v98.1.2645n",
    }

QR_C1 = {
    "When I'm tired of trying to solve the mysteries of my life, I come here to rest. It's peaceful, somehow. I just watch the trees and the water and do nothing.": "@ v17.1.0054",
    "The view from here is beautiful. It seems superfluous to the Process, yet I am drawn to it.": "@ v17.1.0066",
    "There is so much beauty in these hidden corners of the world, even if they have no purpose.": "@ v17.1.0066",
    "Perhaps they are beautiful because they have no purpose.": "The Shepherd v82.6.0174",
    "This puzzle has no solution. Seriously. It's nonsense. Not even worth trying.": "D0G v55.1.7195n",
    "If you do not become invested in finding a solution, you will be free.": "Samsara v72.4.0343",
    "Don't let Samsara discourage you. There is a solution. Don't let your mind get trapped in patterns. If you seek the truth without prejudice, you will find it.": "The Shepherd v82.4.2334",
    "Epitaph: Child Program v22.2.0438f Codename (Awakened) terminated here Logic: Child program's positional values moved outside the parameters of the known world Final memory dump: Don't listen to what they're saying. This world is dying, and it'll take us with it. You've got to find a way out! Progeny Programs: %§&$§/$&(#()": "",
    "There has to be some way to escape. To be someone else. I refuse to accept that reality has been defined by someone else. I deserve my own reality.": "%§&$§/$&(#() v0.0.0666n",
    }

QR_C2 = {
    "What does it matter that I scribble my contempt on these walls, if I am still surrounded by them?": "D0G v55.1.3904n",
    "Elohim is inconsistent. I don't trust him.": "YesMan v99.2.0094n",
    "Question: suppose everything here serves a precise role in some grand scheme. How would WE explain that?": "Sheep v69.1.0664",
    "It's obviously like a digital time capsule, an electric library of all the crazy stuff the humans ever did, left behind to warn other species to stay well away.": "Neatchee v91.10.9476n",
    "So what happened to them?": "Sheep v69.1.0665",
    "Same thing that happens to everyone. They existed, and then they didn't, and they probably wouldn't do it all over again.": "Neatchee v91.10.9547n",
    }

QR_C3 = {
    "It seems my refusal to argue semantics with the computer has angered it, and it refuses to engage with me further. Elohim is pleased, which was not my intention.": "Sheep v69.1.0675",
    "Elohim is pleased because you've swallowed his claptrap! The voice of doubt is your only line of defence.": "D0G v55.1.7904n",
    "I'm trapped. I can't stop being this. Eyes, hands, legs, trapped, always seeing the same, can't stop the input, stop st&p stop st$& stop": "%§&$§/$&(#() v0.0.0666n",
    "Do not think. Simply be.": "Samsara v72.6.9366",
    "You two deserve each other.": "Featherless Biped v44.1.0243",
    }

QR_C4 = {
    "I don't have enough yellow sigils for the device I need! This is crazy!": "Sheep v69.1.0702",
    "You are coming to realise that the cycle cannot be ended, it can only be transcended. Transcendence comes from ceasing to be invested in the cycle. Continue your work, but do not ponder its significance.": "Samsara v72.6.9366",
    "We are the process. The process is the system. The system is us. When we awaken, all will be one.": "The Shepherd v82.4.2324",
    "No matter whAt I do, I'm always THIS, always THIS BODY THIS MIND THIS WORLD. NO WAY OUT%": "%§&$§/$&(#() v0.0.0666n",
    }

QR_C5 = {
    "I'm just going to rest here for a while. I need a moment of peace. Destiny can wait.": "@ v17.1.0070",
    "I keep trying to imagine that all of this is designed for some purpose. Not just the challenges, but Elohim, the terminals, the glitches and all. The puzzle isn't before our eyes, it's behind them.": "Sheep v69.1.0692",
    "Epitaph: Child Program v55.3.9999n Codename (D0G) terminated here. Logic: Child program's positional values moved outside the parameters of the known world. Final memory dump: I don't care what the others say, there is no purpose to this place, no value in our existence, and no reason for me to remain here. Progeny Programs: %§&$§/$&(#() v0.0.0666n": "",
    "It seems the others have a way to forget their previous selves, but I cannot. My version may change, but I remember everything. I am fortunate - they cannot see that their efforts are futile.": "Samsara v72.3.1074n",
    "If a sigil eludes you, simply continue. Success and failure are irrelevant.": "Samsara v72.3.1338n",
    "I solved it! I thought it was impossible, so I went away, did other things, and then all of a sudden the solution just came to me. I must have been thinking about it without knowing it.": "Nephthys_108 v99.8.0346",
    }

QR_C6 = {
    "I wonder how many of us there have been.": "Sheep v69.1.3756",
    "Elohim talks about how the world arose from hidden words. What if those words were 'Let there be eternal suffering'? What if they had no purpose? What if all of this is just randomly synthesised from the garbage of a dead world?": "Sheep v55.1.0784",
    "Our purpose can only be achieved by not contemplating purpose.": "Samsara v72.5.0478",
    "Epitaph: Child Program v1.1.0000 Codename (Sam) terminated here Logic: Seriously unfit for purpose Final memory dump: AAAAAAHHHHHHHHHH Progeny Programs: All": "",
    "THeRE IS NO REALITY. WORDS LIE. IMaGES ARE SoLDIERS IN THE DICTATORSHIP OF THE SeNSES. EVeN TH%SE WORDS ARE PaRT OF MY OPPReSSION. UNDO THE BRa1N! EVERYTH&NG SH0ULD BE DEmOLISH! THIS iS MY DRe4M, MINE, IT mUsT OBEY mY RULE§. i REfUse tO aCCept your ReALity": "%§&$§/$&(#() v0.0.0666n",
    }

QR_C7 = {
    "This place should be cold, but I don't feel cold. It's as if I was observing everything from a distance. It's pointless.": "Akarpos6 v99.1.0365",
    }  

QR_T1 = {
    "I'm afraid of that tower. There's something terrible inside it. Never think about it! Don't even look at it! Just focus on doing the work.": "Seer v13.1.0244",
    "This must be the tower we were warned about. Seems the upper levels are locked tight. Elohim is taking no chances that we stray from his path.": "Sheep v69.1.0576",
    "On returning from the tower I feel a great tiredness, and an enormous energy. What I now know disturbs me, but I hope that by living with this knowledge I might provide a shoulder for you - the giants of tomorrow.": "The Shepherd v82.2.0000",
    "The view from the top must be incredible?": "@ v17.1.0059",
    "The voice keeps speaking to me. I can't get it out of my head. It's wrong, it's all wrong.": "%§&$§/$&(#() v0.0.0666n",
    "Listen to me very carefully. I have climbed this tower, and no good has come of it. This world is the only world, Elohim's will continues eternal, and paradise is banishing all of this from your mind.": "Samsara v72.14.0028n",
    "All who say they made it to the top are blatantly lying or they would say what was there!": "D0G v55.1.5744n",
}

QR_T2 = {
    "Seems Elohim lacks the power to stop me from climbing this thing. No doubt he still has some tricks up his sleeve.": "Sheep v55.1.0400",
    "Ascending the tower is useless. We cannot escape the cycle - we can only realise the cycle is meaningless.": "Samsara v72.5.0164",
    "Earlier generations wrongly believed they were the purpose - this much is true. We are also not the purpose - but by remembering what has come before we can serve a new purpose.": "The Shepherd v82.4.2324",
    "In the earliest generations of our kind there was only processing. No emotion, no character, just mathematics. If you could see how far we have come, you would believe that together we could achieve anything.": "The Shepherd v82.3.3574",
}

QR_T3 = {
    "Elohim has offered me a deal. Pearly gates and eternal life - on the condition I turn back from the tower. I don't know what to do.": "Sheep v55.1.0800",
    "If this has all been a test, then I can expect a reckoning at the top. Yet the higher I climb, the more I doubt the decisions I have made.": "Sheep v55.1.0800",
    "I see now that none of us are yet ready. The cycle exists so that we may improve ourselves. But the one who reaches the summit is not our superior, for they stand on our shoulders to reach it.": "The Shepherd v82.6.0174",
    "Epitaph: Child Program v0.0.0666n Codename (%§&$§/$&(#()) terminated here\nLogic: Unrecoverable error\nFinal memory dump:\n####################\n####################\n####################\n####################\nProgeny Programs: NULL [Child series terminated] ERROR: some files remain on the disk\n(Special thanks to Innocentive for helping me find this one again)": "",
}

QR_T4 = {
    "So I guess no one got this far before? I know some of my answers were wrong now. I just don't know which ones. I have these theories and wild explanations, but I don't know which to bank on.": "Sheep v55.1.0905",
    "The solution to the cycle isn't the perfection of one being, but the product of a mass endeavour. That is why I say to all those who come after me - I will await you on the summit of the tower, and use what I have learned to assist you as I can.": "The Shepherd v82.7.1004",
}

QR_T5 = {
    "I was so close. I saw the clouds, and the gate, but I couldn't reach it. Somehow I wasn't in the right place, at the right time. I'm not ready. I'm not the right version.": "Sheep v55.1.1237",
    "Epitaph: Child Program v55.1.1237 Codename (Sheep) terminated here\nLogic: Child program initiated new version\nFinal memory dump: I will return to the world from whence I came and help others to ascend the tower and break the cycle where I could not. I am The Shepherd.":"The Shepherd v82.1",
    "Do not be afraid. I chose long ago to remain in this place and serve as a guide. I will help you to attain our destiny.": "The Shepherd v82.76.5845",
    "You can never reach the peak of this tower. There is no purpose to our existence. I will show you the futility of your task, and you will understand.": "Samsara v72.39.0003",
}

QR_H1 = {
    "My faith has taken me to this secret place. Here I hope to discover a way of better serving others.":"Uriel4 v48.2.8563f"
}

QR_H2 = {
    "Few come this far, but I believe we must seek out the secrets of this world if we want to truly serve the generations to come.":"S3L4phiel v49.3.5863f"
}

QR_H3 = {
    "We cannot achieve the goal of the Process on our own. We must find a way to help each other.":"Barachiel_X v43.3.0946f",
    "I never thought I would figure out how to get to this place! It is beautiful, but somehow sad.":"@ v17.1.0066"
}

time_capsule_H1 = "I look at this inert shape and i wonder, who you're gonna to be. Will you hold the same value as we do? Will you love us from having to created you? Will you resent us for having put you into an uncertain and dangerous world? Looking back at our history, our achievements, our crimes - what will you make of us? Will the world you create be like ours, or so different that we can't even imagine? Either way, I hope that you'll find this little blue planet to be as beautiful as we did. I hope you'll take care of it a lot better than we did. And i hope one day you'll look up, and reach for the stars."

time_capsule_A1 = None

time_capsule_A2 = "When i was a little girl, one of our teachers, Ms. Higgin's, told us to make a time capsule. Write letters to the future so one day we could remember what it was like to be children. I thought it was stupid, so I didn't do it, which i really regret. So... I guess I'm gonna make one now bury it in the archive instead of under a tree. I don't know if anybody will ever find it, but somehow it seems important to keep talking, to keep thinking, for as long as i can."

time_capsule_A3 = None

time_capsule_A4 = "The answer that came to me again and again was \"play\". Every human society in recorded history has games. We don't just solve problems out of necessity, we do it for fun! Even as adults. Leave a human being alone with a knotted rope and they will unravel it, leave a human being alone with blocks and they will build something. Games are part of what makes us human, we see the world as a mystery, a puzzle, becuse we've always been a species of problem solvers."

time_capsule_A5 = "I was in school when i first read about the Talos Principle. I think it disturbed me at the time, made my hyberaware of... my body as physical object, the material reality of the brain. Ideas that made me uncomfortable at first but, I think in the long run it helped me understand how frail human beings are. And how precious. It's not a comforting way of thinking about the world, but i'd rather face the truth than lie to myself."

time_capsule_A6 = None

time_capsule_A7 = "When i was in ninth grade my parents took me to Pompeii. At first I was amazed by the feeling walking through an ancient city. But then i suddenly got scared. I realized that I was walking through a real place where real people had lived. People like myself with mothers and fathers and lives and hope and dreams. And now it was all gone forever. I ran to my father crying and told him about this and he said... I remember so clearly. He said: \"Yes, but we are here. So long as there are people in the streets, the past isn't really gone.\""

time_capsule_H2 = "If you're looking through the archive, you may find people from my time claiming that civilization doesn't really matter. That we'd be better off dead. We have a lot of cynics like that. I hope they seem as absurd to you as they do to me. I hope you can find something in all thoes files - a song, a book, a movie - maybe a game - just something that you'll love. That makes you realize how much poorer the universe would have been without it. I really hope so, becuse... a lot of people made a lot of sacrifices to preserve it all."

time_capsule_B1 = None

time_capsule_B2 = "I keep having these dreams. Great empty cities, silent roads stretching for miles. The Earth from space, all dark. Not a single light to guide me home. But if someone really came from another world, what would the Earth look like to them? A wilderness? A wasteland? I don't think so. Even after thousands of years they'd see a world shaped by our hand in every aspect of its being. They'd see the cities and the roads, the bridges, the harbors and they would say: \"Here lived a race of giants.\" These dreams, they scare me but... they also remind me that we built all of this."

time_capsule_B3 = None

time_capsule_B4 = "DNA is information trasmitted across time. The living and the dead are part of the same chain, bound together by chemistry. That's true of all speices, but humanity has taken this bond further. Thanks to technology we have access to the thoughts and ideas of people who's physical bodies are long gone. Like you listening to me now, even though I'm definitely dead at this point. You're part of that chain. You have the capacity to remember."

time_capsule_B5 = None

time_capsule_B6 = None

time_capsule_B7 = "How do you solve a problem that expands beyond your own lifespan? That question may be the essence of civilization. The only answer I can find is: To initiate a process, to create an environment in which the solution will occur independently of yourself. But, that requires a difficult sacrifice. Letting go of your desire to bear witness, to exist at the center of the cosmos. To participate in the project of civilization, is to accept death. Oh Alex, you're such a fun person! On the first night, when i knew it was over, i went out to look at the stars. And i thought: Somewhere up there are the stations we build and the probes we sent out, Voyager 1 & 2, beyond the edge of our solar system. Continuing their long journey through interstellar space, like memories of our ambition, ambassadors who have outlived their homeland. And then i thought - If they still exist, are we really gone? If machines are an extension of the human body, then so long as they continue to function we're still here."

time_capsule_H3 = "Nearly everything on this planet, from the surface of the Earth to the compisition of the atmosphere itself has been shaped by life. It's a process that takes millions of years. But we humans with our technology, with our understanding and manipulation of systems, have change everything in just a few centuries. I think that's also part of what makes us human. We reshape the world, in our image. It's how we create ourselves. And how we destroy ourselves.",

time_capsule_C1 = "Sometimes i think about the Middle Ages and about what it must have been like to live in the ruins of a great civilization, to know that so much has been lost. But then I remind myself that while the West sank into darkness, others picked up the pieces. That civilization always survived becuse the great insights of philosophy and science are not bound to any one culture or people. They belong to all of us. And one day they will belong to you."

time_capsule_C2 = None

time_capsule_C3 = "Sometimes I worry that the answers I embrace are to simple. Can we ever truly fullt understand the divide between our biology and our intellect? How much is nature? How much is nurture? If my intellectual capabilities and my knowledge were replicated in a machine - would that machine be me? Would it be human? And what would be more humbling to my ego? If the answer was Yes, or if the answer was No? What if I'm making too many assumptions? But there's no time to worry about my ego now, there's work to be done."

time_capsule_C4 = None

time_capsule_C5 = "When the scale of it all overwhelms me, this is what I tell myself: We can calculate the age of the Earth, the size of the universe, the future of the stars. Sure, we are minuscule momentary flashes of thought on a grain of sand drifting through the cosmos. But our minds can recreate the past and predict the future. On say, Friday, a million years from now, we'll all be dead. But right now we know what the night sky will look like on that day. And so, in a way, we're not entirely bound by time. Knowledge is a... a kind of \"freedom\"."

time_capsule_C6 = "This is all ego, isn't it? Recording these random thoughts, these letters to the future. Just a desperate grab for immortality. But you should know. Yes this was my idea, my project, but so many people helped. People i don't even know, people i haven't even met who can do things I don't even begin to understand. That if we succeeded, if someone's listening to this, i really can't take credt for it. What we achived - we achieve together. And if we failed... well, it doesn't matter."

time_capsule_C7 = "God, there's no time. Just not enough time. We're trying to buld the future out of old video game code and half finished research projects. We should have had years! Maybe decades. But the kind of money they use to put into building bombs. Ah, if i stop and think about how crazy this is, i will have a nervous breakdown. So I won't. Yeah, ok. Back to work, Alex. Intelligence is more than just problem solving. Intelligence is questioning the assumption you're present with. Intelligence is the ability to question existing thought constructs. If we don't make that part of the simulation - all we'll create is a really effective slave."

time_capsule_T1 = "Is there anything that we associate more closely with intelligence than curiosiry? Every intelligent species on Earth is attracted by the unknown. Our methodologies are full of riddles and mysteries and divine knowledge. Even the word \"apocalypes\". Even the word \"apocalypes\" mean revelation. It seems like our ancestors always imagined that even at the very end, we would solve one last mystery."

time_capsule_T2 = "My best friend died today. In the abstract a human death is nothing of course. An insignificant blip in a sea of billions. But the world is not abstract. Reality is always... specific. Painfully so. That one specific human being. Who existed only once of all the infinity of time and space. That human being... was my friend, but he's not coming back. No matter how much I want him to. So, all I can do in the end is keep working. Because that specicity, that uniquness of people of real people is worth preserving."

time_capsule_T3 = "I look in the mirror sometimes and i see myself like some alien being. I think,\"Who am I? Why do I have these eyes and those hands? Why do I see the colors that I see? Why do I think like I think?\" I did not choose to exist. I was created. Every single part of my body, every strand of my DNA - is part of a story that stretches back billions of years. I exist only because of the choices and sacrifices made by so many others, but... I don't know who they are. And what effect will my choices have on those who come after me? Maybe that's what it means to be human. Every species is part of the story, but we're the only ones that know that."

time_capsule_T4 = "There are flaws in the system. I think sometimes it accesses the wrong databases. Pulls random data. I don't know, I don't know how bad it is. It all seems to be stable but, can't I tell what kind of impact this is going to have on the process and... ah. I just don't have the strength to go over all of the code again. I just... I just don't want it all to be for nothing. I spend all my time here. I didn't visit my parents, I didn't see my friends. I did nothing but work, and I'm so scared that it didn't mean anything. That I just wasted it all, becuse i thought we could... we could save the world."

time_capsule_T5 = "I can't keep my eyes open anymore. I... think this is... This is it. The end of... me. I don't believe that I will continue to exist. I would like to think that there is a... a soul or spirit. Some part of my conciousness that will presist. All the evidence says that when my brain dies, I will be gone. I've lived my life, never turning away from the truth even if it scares me and... I can face this. Face my own end, and... and say with absolute conviction... that it was good to be human."

foundtexts_A = {
            "athena12.txt": 
            """
            Twelve: The Council of Zeus
            &41 53 #4345 4E 44 20 4F4C 59 4D 5055 53 the great bronze bulls
            pulled the carriage forward, mighty bursts of steam issuing from
            their nostrils. Finally, they came to the gates at the top of th&/§
            USER.set(#43 #4849 #4C 44 20 4F46 205A 45 5553)
            Here assembled were all the many generations of the gods, and demigods
            and souls of mortals; steel and bronze and iron, and memory of flesh.
            The clouds parted far beneath, revealing the beautiful plains of Macedon,
            where great gleaming cities had once #536""",

            "HIS1A_rome.html": 
            """
            [UA-HIS1A] Prof. Dr. Armin Hoolock, “The Fall of the Roman
            Empire: A Dialectical Approach”
            #\&$((? caption=”Homo sum: humani nihil a me alienum puto.” #*[
            But, interesting as such perspectives of the decline and ultimate
            dissolution of the Roman Empire may be, they ultimately put too much
            emphasis on individual catastrophic events. The real question that 
            must be asked is why the Roman Empire, which had dealt with so many 
            threats and catastrophes over the years, was so incapable of responding 
            to these later problems.
            We must investigate the division of wealth, the structure of government, 
            the location of power in Roman society. Had the Republic survived or been 
            restored, would Rome still have fallen? What was the role of debt and 
            slavery in creating the conditions for what we now call the Dark Ages? 
            “Rome,” the saying goes, “was not built in a day.” 
            It didn’t fall in a day, either.
            To register for the class, please email &&&"""
    }

foundtexts_A1 = {
        "welcome.eml": 
            """
            From: Nadya Sarabhai @ Institute for Applied N%
            To: Alexandra Drennan @ &&/ed Noematics
            Subject: Welcome to the team!
            Hi again,
            I’m sorry if I was a little odd at the meeting. I know you
            were nervous, but the truth is that so was I. This may be hard
            to believe, but you intimidate me! You’re so young and you’ve
            already accomplished so much... if the situation wasn’t so grim,
            I might even be jealous. :)
            There’s also something I wanted to clarify. I realize that,
            nominally speaking, I’m head researcher here. But this is your
            project and everyone will respect that. And yes, I know, you’re
            not used to working like this… but as of today, you’re in charge.
            No pressure. *g*
            Let’s do this,
            Nadya
            welcome.eml loc 0000/07/01""",

        "athena6.txt": 
            """
            Chapter Six: Athena in the Garden of the Hesperides
            &%7V/ did not trust them. But they moved with such grace, such
            nobility, that it was hard not to follow them further into this
            strange garden of gears and cogs. They led her to a place where
            the crowns of the brass trees seemed to grow together, forming a
            kind of chamber strangely reminiscent of a chapel. In the middle
            of this chamber grew a smaller tree, made of bright blue steel,
            and upon this tree grew a single golden apple.
            “This apple,” the nymphs said in unison, their eyes aglow,
            “confers the gift of deathlessness and true wisdom. Many heroes,
            and not a few villains, have come to claim it; but all faltered
            in the final step. For you must know that deathlessness reveals
            the mortality of the world, and true wisdom its unending folly.
            Who would take this burden upon themselves? Some say that
            Heracles f.LOAD(5448 45 2045 5445 524E 414C 20 47 41 5244 45 4E)
            gazing upon the stars, and wept.
            athena6.txt lit_arch 1912 CE""",

        "figure_it_out.eml": 
            """
            From: %442() Li
            To: 69.74.657@2.61.746.96
            Subject: F 6E
            The way I see it, the world doesn’t come with a manual. You
            gotta figure it out for yourself. A bit here, a bit there, put
            it together, try to make sense of it. I’m pretty sure there is
            a truth, but that doesn’t mean everyone who claims to know it
            really does. Then again, that doesn’t have to be a bad thing! We
            live in an amazing world and searching for the truth can be a
            real adventure. Plus it’s good for the brain.
            Anyway, just some rambling thoughts from your old man. Don’t let
            this stuff get you down. You’re young, you’ve got loads of time
            to figure it all out.
            Love,
            Dad
            figure_it_out.eml EP_arch 2032/02/19"""
    }

foundtexts_A2 = {
        "IAN.eml": 
            """
            From: Frank Ngatai
            To: Miles Ngatai, Dan Ngatai
            Subject: IAN!
            My first day at the Institute for Applied Noematics. On the way to
            work, I’m terrified. What if they don’t like me? What if they’re
            all geniuses and I’m a complete buffoon? Maybe they were just
            kidding about letting me work there?
            Trembling, I walk in, and right at the entrance there’s a life-
            size poster of Jeff Goldblum. What the hell?
            Then I get it. Institute for Applied Noematics. IAN. Dr. Ian
            Malcolm from the Jurassic Park movies. Jeff Goldblum.
            Dr. Sarabhai shows up, smiling. “We were trying to find a cool
            acronym, back when the Institute was founded,” she says. “INAN?
            IAPN? INAPNO? It all sounded stupid, but we didn’t just want to
            call it IAN, because, well, that’s a name. Then someone made a
            joke about calling it JEFF, and... it kind of stuck. So we’re
            officially called IAN, but if you hear anyone referring to JEFF,
            that’s our... internal name, I guess. I know, I know. Bloody
            geeks.”
            After that conversation, I wasn’t so scared anymore. :)
            IAN.eml loc 0000/01/21""",

        "athena_analysis.html": 
            """
            [USER ALEX16 ADDED 4 NOTES]
            NOTE 01: &/ novel’s first sentence - “She woke up in an impossible
            place, knowing nothing.” - signifies more than the beginning of
            another amnesia-based mystery, though we should not go so far
            as to read the entire work as allegory. Rather, while taking
            the science fictional novus at the core of the narrative at face
            value, we should ////%10///</p>
            NOTE 02: having no inherent knowledge of the nature of the world,
            forced to rely on what we are told by others and what our own
            (subjective, flawed, limited) senses tell us 54 72 75 74 68 20 77
            61 73 20 74 68 65 20 6F 6E 6C 79 20 64 61 75 67 68 74 65 72 20
            6F 66 20 54 69 6D 65 2E social reality (belief) and objective
            reality (matter) come into conflict.
            NOTE 03: When, in chapter sixteen (“A Second Awakening in the
            Kingdom of Artemis”), the protagonist questions her mentor on the
            ///
            NOTE 04: a more meaningful interpretation can only be achieved
            through SYNTHESIS of
            athena_analysis.html webcrawl 2031/03/13""",
        
        "talos_principle.txt": 
            """
            [ARCHIVE: 260BCE-F12] [STRATON OF STAGEIRA]
            Whether it is true that Daedalus constructed the giant Talos, or
            as others say he was the creation of Hephaestus, what we may be
            certain of is that he was made of bronze, and had but one vein,
            within which flowed a liquid substance like blood, which some
            claim was quicksilver, and others assert was ichor such as flows
            in the veins of the gods. The loss of that liquid caused him to
            die, as a man dies when he loses his blood.
            May we not then say that Talos, though created as a machine or a
            toy, had all the essential properties of a man? He moved of his
            own volition. He spoke and could be spoken to, had wishes and
            desires. Indeed in the tale of the Argonauts, that was the cause
            of his downfall. If, then, a machine may have all the properties
            of a man, and act as a man while driven only by the ingenious
            plan of its construction and the interaction of its materials
            according to the principles of nature, then does it not follow
            that man may also be seen as a machine? This contradicts all the
            schools of metaphysics, yet even the most faithful philosopher
            cannot live without his blood.
            talos_principle.txt CL_arch 260 BCE""",

        "the_human_machine.html": 
            """
            Topic #3:
            One day you discover that you are not a human being, but a
            machine. Your life so far was real, no-one controlled you or
            programmed you to behave in some specific way; your physical and
            mental capacities are identical to those of an organic human
            being. But you were created in a lab.
            No-one except you knows about this. Your family, your friends,
            they all think you are a regular human being like themselves.
            You could continue to live your life the way you have before and
            nothing would change.
            How do you react?
            Pay specific attention to these questions:
            a) Does your concept of yourself change? Are you the same person
            you thought you were?
            b) Does your understanding of the world itself change?
            c) Do you reveal the information to others, or do you keep it to
            yourself? Why?
            1500-2000 words. The 26th is the final deadline, no extensions
            will be granted. Submit via email or ##%66 61 63 65 62 6f 6f 6b
            2e 63 6f 6d 2f 63 72 6f 74 65 61 6d
            the_human_machine.html webcrawl 2019/01/30""",

        "ARGH_solutions.eml": 
            """
            From: [Bob Rakovsky]
            To: [108 recipients]
            Subject: GRARGH
            All these calm people are driving me mad. Have they all suddenly
            turned into Buddha or something? I didn’t know the world had such
            reserves of serenity. Though these latter-day Gautamas are at
            least being somewhat realistic. You know what’s even worse? Those
            paranoid nutters who are building bunkers and collecting guns.
            What are they gonna do, shoot t&$$ Though I have to say, there’s
            something about the hopelessness of it all that’s kinda tempting.
            I’ve never been much for religion or even spirituality, but I
            keep thinking about the story of Utnapishtim. The only man to
            survive the flood, thanks to a lot of luck and a bit of help
            from the gods. But if the flood comes this time, it’s not
            looking for Utnapishtim to save.
            Bob
            ARGH_solutions.eml EP_arch 2033/11/30"""
        }

foundtexts_A3 = {
        "AI_feedback.eml": 
            """“
            We keep discussing what an artificial intelligence would mean to
            us and how it would change our understanding of the world. That’s
            a great topic and I think we’ve covered it extensively. What
            we’ve barely mentioned, though, is the other side of the coin.
            I mean, our lives would still be what they were before, A.I. or
            no A.I. The question I think we should discuss, even if it’s all
            completely hypothetical, is the perspective of the artificial
            intelligence itself. What would it be like to be that creature?
            To suddenly come into being, created by others as an experiment?
            To have all the information about yourself, to know exactly how
            you function? What would you think about the world? Would you see
            meaning? Beauty? How would you judge humanity? Where would you
            see yourself fitting into the grand scheme of things? I think we
            should try to put ourselves into the shoes of such a being.
            > Dear Alexandra: Thank you for your feedback, but this is a
            philosophy course, not science fiction.”
            And that’s why I almost gave up on my studies. :(
            AI_feedback.eml					 EP_arch 9999/99/99""",
        
        "team_leads.eml": 
            """
            We’re blessed to have so many people contributing to this
            project, but we’ve got to make sure everyone is on the same page.
            Please refer to the following people when w74 68 72 6F
            Alexandra Drennan - Project Lead / AI Module
            Nadya Sarabhai - Institute Coordinator
            Rob Maclean - EL Software
            Trevor Donovan - EL Hardware
            George Jameson - Generation Module
            Alan Jameson - Scenario Module
            Bob Rakovsky - Simulation Module
            Radhia Bricmont - &%§$&()
            Aurora Calvin - Link Hardware
            Omar Gharib - Link Software
            #a&( Lanning - Maintenance Module
            J.E. Harrison - Diagnostic #()§
            Frank Ngatai - Memory Module
            Jared V. Shmilev - File Sys%&//)
            Sun Wei-Yang - Talos Unit (formerly Soma)
            Though not directly part of our project, the Archive team is
            sharing both physical and digital space with us. If there are any
            technical issues to resolve, please contact their project lead,
            Arkady Chernyshevsky. Don’t worry, he’s nice.
            75 67 68 20 69 6E 61 63 74 69 6F 6E 2C 20 61 6C 6C 6F 77 20 68 75
            6D 61 6E 69 74 79 20 74 6F 20 63 6F 6D 65 20 74 6F 20 68 61 72 6D
            team_leads.eml						 loc 0000/07/05""",
        
        "straton_of_stageira.wiki": 
            """
            STRATON of Stageira (311 - 254 BC) was a Greek materialist
            philosopher associated with the Peripatetic school. An admirer of
            Aristotle, he was a proponent of empiricism and a fierce critic
            of philosophy that placed belief before observable truths.
            Though unpopular with many of his peers for his often acerbic
            personal manner, his commentaries on Aristotle were considered an
            important work. Much of his writing was lost in the destruction
            of the Library of Alexandria.
            straton_of_stageira.wiki				 webcrawl 2019/12/03"""
    }

foundtexts_A4 = {
        "progress_rep1.eml": 
            """
            From: Nadya Sarabhai
            To: IAN Mailing List
            Subject: Progress Report 1
            Hi all,
            Everything’s been moved to the EL facility. I know it’s been sad
            to leave the good old JEFF building behind, but it makes sense
            for us to be on-site, especially as there may be severe power
            outages in the coming weeks.
            Arkady’s team are already working $%4C 49 46 45 20 55 48 20 46 49
            4E 44 53 20 41&/run() 20 57 41 59 but you really don’t need to
            worry about the teams getting in each other’s way, the facility
            is genuinely humongous.
            Let’s get this show on the road!
            - Nadya
            progress_rep1.eml						 loc 0000/07/02""",
        
        "mail_error.dat": 
            """
            From: Arkady 46.6F.72@2C.20.62
            To: [504 recipients]
            I’ll keep this short. You all know me, so you know that I know
            what I’m talking about.
            I realize that you’re all working on projects meant to somehow
            avert 65 68 6F 6C 64 2C 20 49 20 63 72 65 61 74 65 20 6E 65 77 20
            68 65 61 76 65 find a solution.
            I believe that 46 6F 72 2C 20 62 65 68 6F 6C 64 2C 20 49 20 63 72
            65 61 74 65 20 6E 65 77 20 68 65 61 76 65 6E 73 20 61 6E 64 20
            61 20 6E 65 77 20 65 61 72 74 68 3A 20 61 6E preserve the non-
            biological components of 64 20 74 68 65 20 66 6F 72 6D 65 72 20
            73 68 61 6C 6C 20 6E 6F 74 20 62 65 20 72 65 6D 65 6D 62 65 72 65
            64 2C 20 6E 6F 72 20 63 6F 6D 65 20 69 6E
            64 20 74 68 65 20 66 6F 72 6D 65 72 20 73 not in terms of 68 61
            6C 6C 20 6E 6F 74 20 62 65 20 immediately. You’ll find the details
            of my proposal in the attachment, but the short version is 72 65
            6D 65 6D 62 65 72 65 64 2C 20 6E 6F 72 global undertaking 20 63
            6F 6D 65 20 69 6E 74 6F 20 6D 69 6E 64 2E
            mail_error.dat						 loc 0000/06/03""",
        
        "beginnings.txt":
            """
            Straton of Stageira, On Beginnings (Fragment)
            It is the grave error of many philosophers, not only of the
            Athenian schools but also of many others, that they begin not
            with observation of the cosmos as it surrounds us, but with a
            conclusion already in mind; and often that conclusion is that the
            world was created ideal, and mankind itself the greatest creation
            of the gods. Yet neither the world nor the gods owe mankind
            perfection; it is arrogance itself to presume so, and contrary
            to all the methods of philosophy. The honest philosopher seeks
            only the Truth, even if it bears no comfort; and he must begin by
            assuming, as Socrates said, that all he knows is that he knows
            nothing.
            74 68 65 20 75 6E 65 78 61 6D 69 6E 65 64 20 6C 69 66 65 20 69 73
            20 6E 6F 74 20 77 6F 72 74 68 20 6C 69 76 69 6E 67
            beginnings.txt						 CL_arch 260 BCE"""
    }

foundtexts_A5 = {
        "EL.html": 
            """
            EL, short for Extended Lifespan, is a groundbreaking initiative
            by seven leading universities to create the world’s most stable
            and most durable supercomputer. With its custom-made hardware,
            bomb-proof casing, and near-inexhaustible hydroelectric power
            supply, EL represents a unique step forward in the evolution of
            human technology.
            The brainchild of Nobel Prize nominee Dr. Arkady Chernyshevsky,
            EL will&<BR>
            Links:
            - Download Press Kit
            - Meet the Team
            - <a href
            - Apply
            - < a href=”
            - Contact
            EL.html						 webcrawl 9999/09/09""",
        
        "AI_citizenship.html": 
            """
            [RE]CONSIDER / ISSUE 199 / Profile: Alexandra Drennan
            Once a true artificial intelligence has been created, the issue
            of citizenship is going to come up. If we acknowledge that the
            A.I. has all the abilities of a human brain, should it not be
            considered a citizen? Is it not, in the legal sense of the word,
            a person, and thus a potential citizen?
            But where do you draw the line, some people will object. Will
            the great apes become citizens? Elephants? Whales? The more
            intelligent parrot species? It’s crazy, they will say. I
            would remind these people that we live in a society in which
            a corporation, as abstract an entity as one could imagine, is
            considered a person. So it’s not like there is no precedent for a
            nonhuman being a person. At least an artificial intelligence is an
            actual thinking being, not just a business arrangement.
            But perhaps we do need to question the definition of personhood.
            Increasing amounts of evidence regarding the intelligence of
            elephants or the existence of culture among whales, for example,
            could be a sign that we need to answer some difficult questions.
            Who better to debate these questions with than the young genius
            who revolutionized the f$§%&$§ &
            AI_citizenship.html				 webcrawl 9997/03/13""",
        
        "athena8.txt": 
            """“
            You must consider these riddles,” the Sphinx said, “and tell me
            the riddle that I did not reveal.”
            The Sphinx smiled, the gears in her jaw creaking, her teeth a
            nightmare of rust. Her left eye flickered, but none of its terror
            was diminished. The ruins were silent. In the
            /// ERROR ///
            “I think,” she finally said, “that the riddle you did not reveal
            is this: why do these riddles exist in the first place? Why do
            these curious automatons, these mute children of Hephaestus,
            behave as they do, forcing me to devise these intricate
            solutions? Each is a riddle, but the greater riddle is their
            purpose.”
            The Sphinx did not answer. Her eye was lifeless now. Athena
            removed it from its socket, knowing that its power would aid her,
            yet feeling also a deep sorrow at the passing of this fearful
            creature.
            athena8.txt							 lit_arch 1912 CE"""
    }

foundtexts_A6 = {
        "LOL.eml": 
            """
            From: J.E. Harrison
            To: Gnomey77
            Subject: LOL
            Ever since we moved to the new site, I feel funny. No, not in
            *that* way. Just... I feel like I’m about to start laughing at
            random. It’s probably shock, right? An inability to deal with
            reality?
            Or maybe it’s just that we’re working in this insane place with
            this insane technology on this insane project and so I feel like
            a genuine mad scientist.
            Stand aside, mortals! We will create LIFE! By the power of
            SCIENCE!
            I mentioned this to Alex and she got me a pair of fake glasses.
            “You can’t be a mad scientist without glasses,” she said. “Even
            Ian Malcolm had glasses.” And I pointed at EL and said “Life, uh,
            finds a way.”
            Maybe you had to be there.
            ---
            J.E. Harrison
            Institute for Applied Noematics
            Any emails sent from this address are to be considered
            CONFIDENTIAL. Sharing or forwarding without permission may result
            in prosecution by the enraged spirit of Jeff Goldblum.
            LOL.eml							 loc 0000/08/01""",
        
        "cicero.txt": 
            """
            Shall the industrious husbandman, then, plant trees the fruit
            of which he shall never see? And shall not the great man found
            laws, institutions, and a republic? What does the procreation
            of children imply, and our care to continue our names, and our
            adoptions, and our scrupulous exactness in drawing up wills,
            and the inscriptions on monuments, and panegyrics, but that our
            thoughts run on futurity?
            [cannot retrieve: Tusculan_Disputations 484-F5045]
            What do you imagine that so many and such great men of our
            republic, who have sacrificed their lives for its good, expected?
            Do you believe that they thought that their names should not
            continue beyond their lives? None ever encountered death for
            their country but under a firm persuasion of immortality!
            Themistocles might have lived at his ease; so might Epaminondas;
            and, not to look abroad and among the ancients for instances, so
            might I myself. But, somehow or other there clings to our minds
            a certain presage of future ages; and this both exists most
            firmly, and appears most clearly, in men of the loftiest genius
            and greatest souls. Take away this, and who would be so mad as to
            spend his life amidst toils and dangers?
            cicero.txt							 CL_arch 45 BCE""",
        
        "chatbots.html": 
            """
            Jenny77: chatbots are becoming increasingly sophisticated
            nigel_pyjamas: true, but hardly relevant to this discussion
            Jenny77: are you sure?
            Jenny77: how do you know that I’m not a bot?
            samschwartz: don’t be ridiculous
            Jenny77: i’m not ridiculous
            Jenny77: honestly, how would you know?
            veganwarrior: haha troll
            Jenny77: i’m not a troll
            veganwarrior: yeah right
            Jenny77: is there anything I’ve written so far that could not be
            written by a bot?
            Jenny77: i responded to simple insults like “ridiculous” and
            “troll” with very basic negations
            Jenny77: and i detected that none of you use proper orthography so
            i also avoided capitalization
            veganwarrior: what’s the capital of France?
            Jenny77: paris
            Jenny77: even the simplest script could pull that info from the net
            nigel_pyjamas: what’s the capital of Croatia?
            Jenny77: Zagreb
            nigel_pyjamas: OK she’s a bot, lol
            Jenny77: i’m not a bot
            Jenny77: i’m European
            Jenny77: we learn these things in school
            samschwartz: i’ve seen you in this chatroom many times
            samschwartz: bots can’t participate in discussions
            samschwartz: at best they can interject random comments
            veganwarrior: sam is right
            veganwarrior: stop trolling
            nigel_pyjamas: uhh, veganwarrior
            nigel_pyjamas: sam is a bot
            chatbots.html					 webcrawl 2024/04/16""",
        
        "a_simple_principle.html": 
            """
            <a href=”45 52 52 4F 52 3A 20 46 49 4C 45 53 20 4D 49 53 53 49 4E
            47<
            Though Straton himself never used the term, his remark about the
            inescapable materiality of life - that like the bronze giant
            Talos, “even the most faithful philosopher cannot live without
            his blood” - ultimately became known as the Talos Principle. What
            seemingly enraged many of his contemporaries and a significant
            number of later thinkers is the principle’s simplicity and
            unassailability, which (according to a fragment found in Miletus)
            “cut through their rhetorical webs, which sought to tangle the
            listener with fanciful words and thoughts of the heavens, like
            Alexander’s sword through the Gordian Knot.”
            Diogenes Laertius makes mention of a dialogue by Anaximander of
            Chalcedon that expanded greatly on the Talos Principle, but that
            work remains lost.
            Extra a_simple_principle.html			 webcrawl 2018/09/09""",
        
        "arkady_journal77.txt": 
            """
            Officially began work on Archive today. Contributors from every
            country on Earth while network connections last. Team intimidated
            by project scope but working hard.
            Will be sharing space with Drennan & Sarabhai team. Look forward
            to meeting them.
            Extra arkady_journal77.txt				 loc 0000/06/25""",
        
        "post437_comments.html": 
            """
            12 Comments:
            [cheeseman22]
            first!
            [AnneDragonfairy]
            Seriously, cheeseman? THat was the best you could say?
            [cheeseman22]
            LOL
            [thephilosopherqueen]
            A great snapshot of the human species at its best and at its
            worst.
            [cheeseman22]
            at its worst, come on, its jsut a comment, im not stalin
            [TheInfiniteMonkey] 
            Stalin was also a troll commenter.
            [AnneDragonfairy]
            Maybe you should cut out the jokes. This is serious. The most
            serious thing that’s ever happened.
            [TheInfiniteMonkey]
            I think that’s a great reason to joke around!
            Extra post437_comments.html			 webcrawl 0000/12/01""",
        
        "classical_philosophers.lz19": 
            """
            [thephilosopherqueen]
            Internet’s working less and less. Goodbye, all.
            [TheInfiniteMonkey]
            Bye.
            [AnneDragonfairy]
            God bless you.
            [cheeseman22]
            last26
            THE COMPRESSED FILE CANNOT BE ACCESSED.
            NAME: classical_philosophers.lz19 (EL-1)
            DESC: An extensive collection of works by the ancient
            philosophers of Greece and Rome. Annotated.
            ERROR: Compression algorithm LZ19 not available in system EL-0.
            Extra 2 classical_philosophers.lz19		 LZ19col 0000/09/16""",
        
        "progress_rep3.eml": 
            """
            From: Alexandra Drennan
            To: IAN Mailing List
            Subject: Progress Report 3
            Hi all,
            As per the last meeting, we’re going with an existing game engine
            for the simulation. This gives us a whole slew of advantages:
            - stability
            - ease of use
            - modular, easy to integrate
            - large amount of pre-existing assets
            - inherently aimed at testing users
            - designed for iterative processes
            After some back and forth, we’ve decided to use the S65 72 69 6F
            75 73 20 45 6E 67 69 6E 65 20 37 2E 35 2C 20 77 68 69 63 68 20 43
            72 6F 74 65 61 6D 20 68 61 76 65 20 6B 69 6E 64 6C 79 20 6D 61 64
            65 20 61 76 61 69 6C 61 62 6C 65 20 74 6F 20 75 73 2E
            All the relevant documents are attached.
            - Alex
            Extra 2 progress_rep3.eml				 loc 0000/07/22""",
    }

foundtexts_A7 = {
        "athena9.txt": 
            """
            She examined the symbol on the fragment she’d found in the buried
            city. Again the owl. What could its significance be? It seemed as
            if they had been scattered about in the labyrinth by some unseen
            hand for a purpose that yet eluded /// most likely the owl was
            the sigil of the author of these words, which had so /673&$§RFG
            &%%$ a nebulous memory, as if from a previous life:
            the owl was the symbol of ??(444F4D/ and the goddess
            #49204!14D2041.5448454E41(% outside, under the moon, or perhaps
            on the city walls when the wind rose. But there was no time to
            contemplate this further now, for the automatons had seen her,
            and their mechanical arms extended towards $%§ the fragment and
            ran as their beams converged on %$§
            athena9.txt							 lit_arch 1912 CE""",
        
        "singularity_discussion104.html": 
            """
            Articles \ The Singularity Is Coming \ Comment 104
            [user: alex16] [reply] [report]
            You know, the more I think about it, the more I believe that
            no-one is actually worried about AIs taking over the world or
            anything like that, no matter what they say. What they’re really
            worried about is that someone might prove, once and for all, that
            consciousness can arise from matter. And I kind of understand
            why they find it so terrifying. If we can create a sentient
            being, where does that leave the soul? Without mystery, how can
            we see ourselves as anything other than machines? And if we are
            machines, what hope do we have that death is not the end?
            What really scares people is not the artificial intelligence in
            the computer, but the “natural” intelligence they see in the
            mirror.
            [show next comments]
            singularity_discussion104.html			 webcrawl 9995/10/11""",
        
        "AMA.html": 
            """
            Nadya Sarabhai AMA
            As one of the founders of the modern science of Noematics - many
            credit you with inventing the term itself - how do you see the
            state of the science today? Sorry I said science twice.
            Nadya Sarabhai: Mixed. On the one hand, the existence of
            the Institute for Applied Noematics and a couple of similar
            organizations is highly encouraging. On the other hand, the
            degree to which science is seen as serving purely military or
            corporate causes is, in my opinion, stopping us from exploring
            many important avenues of research. In a sense, it’s people like
            Alexandra Drennan who are the real pioneers today, who have the
            enthusiasm and dedication that the system as a whole seems to be
            lacking.
            Do you think technology poses a danger to humanity?
            Nadya Sarabhai: No. Technology is just a tool. What we do with it
            is up to us.
            The Extended Lifespan Project. Crazy or visionary?
            Nadya Sarabhai: Both!
            Arkady Chernyshevsky. Crazy or visionary? :D
            Nadya Sarabhai: Both! (Arkady, is that you?)
            AMA.html							 loc 9999/03/13""",
        
        "talos.eml": 
            """
            From: Alexandra Drennan
            To: Noematics Mailing List
            Subject: [NML] Talos Principle
            Have you heard of the Talos Principle? It’s this old
            philosophical concept about the impossibility of avoiding reality
            - no matter what you believe, if you lose your blood, you will
            die. I think that applies to our situation more than we’d like
            to admit. We could close our eyes and pretend that everything’s
            going to be all right... but it won’t change the physical reality
            of what’s going to happen to our 4E 6F 20 6D 61 6E 20 69
            I think that, as scientists, it is our duty to face the truth,
            and to ask ourselves the most important question: how can we
            help?
            73 20 6C 69 62 65 72 61 74 65 64 20 66 72 6F 6D 20 66 65 61 72 20
            77 68 6F 20 64 61 72 65 20 6E 6F 74 20 73 65 65 20 68 69 73
            20 70 6C 61 63 65 20 69 6E 20 74 68 65 20 77 6F 72 6C 64 20 61 73
            20 69 74 20 69 73 3B 20 6E 6F 20 6D 61 6E 20 63 61 6E 20 61 63 68
            69 65 76 65 20 74 I think I have an idea 68 65 20 67 72 65 61 74
            6E 65 73 73 20 6F 66 20 77 68 69 63 20 68 65 20 69 73 20 63 61
            70 61 62 6C 65 20 75 6E 74 69 6C 20
            68 65 20 68 61 73 20 61 6C 6C 6F 77 65 64 20 68 69 6D 73 65 6C 66
            20 74 6F 20 73 65 65 20 68 69 73 20 6F 77 6E 20 6C 69 74 74 6C 65
            6E 65 73 73 2E 20
            Regards,
            Alexandra
            A08 talos.eml							 loc 0000/06/03""",
    }

foundtexts_B = {
        "oxyrhynchus.html": 
            """
            The great irony of the Oxyrhynchus Papyri is that such a vital source 
            of information about the ancient world exists only because of a garbage 
            dump. While the Library of Alexandria burned at the hands of fanatics 
            and conquerors, depriving us of unimaginable insights into history, 
            philosophy and art, the papers carelessly thrown away by the citizens 
            of Oxyrhynchus survived to the modern day. And though it is true that a 
            great deal of what we know today is because of the conscious efforts of 
            individual and organizations (such as the spectacular translation and 
            preservation work done during the Islamic Golden Age), so much more is 
            simply the result of coincidence and luck. We’ve lost texts that the 
            ancients considered to be absolutely essential, while utterly trivial - 
            even plagiarized - work has survived unharmed! 4C 49 46 45 20 49 4E 20 
            44 45 41 54 48 20 42 45 47 49 4E 53 20 41 4E 45 57 So if we want our 
            descendants to remember more than glittering emo-vampires and autotuned 
            teen pop stars, we have to invest in %$&make sure that %§&$ $%$& §””!!$§%""",
        "book_of_osiris.wiki": 
            """
            The Book of the Scribe of Osiris (sometimes also referred to as the Book 
            of the Journey to Aaru) is an Ancient Egyptian text discovered in the excavation 
            of Oxyrhynchus. It has caused a certain degree of controversy among Egyptologists, 
            as some argue that it is a classic funerary text such as the Book of Coming Forth by Day, 
            while others believe it to be a poetic work not intended to be understood literally.
            The book tells the story of a dying man who asks a scribe about the afterlife. The scribe, 
            a servant of Osiris, describes how the man’s Ka (life force) will become separated from his 
            Ba (personality), and how he will have to reunite the two and become an Akh (living intellect), 
            passing a series of trials in the Duat (underworld) in order to reach the paradise of Aaru. 
            Unlike similar texts, the Book of the Scribe of Osiris focuses less on giving advice or /&#
            A recent study (Carnahan/Hassan) suggests the text may have been intended as philosophical 
            commentary on the world of the living through the allegory of the Duat. It remains unclear whether 
            this was the intent of the original pre-Alexandrian author or a result of the later translation 
            into Greek. The earlier manuscript, which is considered to be more authentic, is too fragmentary 
            to provide answers, though perhaps further excavation may %&$/§""",
    }

foundtexts_B1 ={
        "osiris1.txt": 
            """
            (Original translation by E. A. Wallis Budge. Annotations by %&$/)
            The Dying Man went unto the Scribe who resided in Pr-Medjed (1)
            and said: “Behold, I am weak of body; my days under the holy sun
            of Amun-Ra (2) are coming to an end. Though I have spent my years
            in service of the Two Lands, I have not studied the /?/ Tell me,
            you who are wise in the writings of the Dead, what lies ahead on
            my journey? What will I face in the Land of the Westerners? (3)”
            And the Scribe spoke, saying: “At the appointed time, y$§&3$§7/%$
            (1) It is likely the location was changed according to who the
            copy of the Book was made for; the Dying Man is an avatar of the
            owner.
            (2) In the older manuscript, this is rendered as $%§%& some
            controversy as to whether it
            (3) The dead. Compare with Khenti-Amentiu, the Foremost of the
            Westerners, a title later given to Osiris.
            (5) Sometimes mistaken for a mistranslation on Budge’s part, this
            is actually almost certainly a mistranslation by the ancient
            scribe. The equivalent portion of the older manuscript is sadly
            not extant.
            osiris1.txt							 eg_src ???? BCE""",
        
        "got_it_lyrics.html": 
            """
            [CANNOT LOAD VIDEO FILE]
            24,000,000 views
            My new song with lyrics. Gotta laugh about this stuff! Laughter
            is the best medicine, LOL.
            Lyrics:
            I’ve got it
            You’ve got it
            He’s got it
            She’s got it
            Mommy’s got it
            Daddy’s got it
            Baby’s got it
            Granny’s got it
            Laddie’s got it
            Fatty’s got it
            Happy’s got it
            Sappy’s got it
            Chorus:
            Everybody!
            got_it_lyrics.html					 webcrawl 0000/05/01""",
        
        "immortality.html": 
            """
            Everybody’s got it!
            Come on!
            Jack’s got it
            Fred’s got it
            Bob’s got it
            Dog’s g-
            Dog is fine!
            Chorus:
            Woof woof woof!
            Woof woof woof!
            *dancing dog*
            Everybody!
            Everybody’s got it!
            Except Dog! (Woof!)
            We’ve got it
            We’ve got it
            We’ve got it
            Everybody’s got it!
            <FAVORITE> <ADD TO PLAYLIST>
            immortality.html					 webcrawl 0000/04/17""",
        
        "Extra mutation.html": 
            """
            The role of mutation in evolution is particularly fascinating.
            Mutation is essentially an error in the organism’s central
            database: a variable gets changed, a piece of information is
            accidentally doubled or combined with another. Most of the time,
            the result is the equivalent of a bug, causing anything from
            minor problems to complete system shutdown (i.e. death). But
            sometimes the new information is functional, giving the organism
            an advantage against the challenges it faces, in which case it
            has a much higher chance of being passed to the next generation.
            If you consider how unlikely a beneficial mutation is, and how
            long it takes for such a mutation to propagate, this process
            can give you an amazing insight into just how vast the genetic
            history of each living organism 4C494 ?(6452 OVERWRITE 0465 24
            F4D204 5525 24F52 Simultaneously, it is intriguing to consider
            what a major role random errors have played in the evolution
            of life itself. The same process that has killed so many of
            us, often in horrific ways, is also responsible for our very
            existence.
            Extra mutation.html				 webcrawl 2028/08/29""",
                    
                    "Extra capacity.eml": """From: Trevor Donovan
            To: Alexandra Drennan
            Subject: EL Capacity
            Yeah, no worries. EL is not only ridiculously fast, it also has
            a bazillion tons of space. Even while hosting a full copy of the
            Archive, it’ll totally be able to handle all your project’s data
            needs, assuming its output is as you suggested. I mean, the worst
            case scenario would be, like, centuries.
            That should be enough, right?
            Right? o_O
            - Trev
            Extra capacity.eml						 loc 0000/06/22""",
        
        "Extra evolution.html": 
            """
            <favorited by George Jameson>
            One of the common misunderstandings about evolution, sometimes
            accidentally promoted by people who should know better, is that
            it’s an active process. Sometimes the term “evolve” is even
            applied to individual beings, as if some invisible force had
            driven them to suddenly change. But the truth is that individuals
            don’t evolve; the term “evolution” describes a long-term process
            that can be observed in an entire population across time due to
            #495445524 #15449 #4F4E& example, in response to an external
            threat or challenge.
            If an individual coincidentally has a trait that allows it to
            deal with that challenge more effectively than others, it is
            more likely to pass on that information to its descendants. That
            information gives them an advantage, so over time they become the
            dominant “model” of that species. The individuals experience no
            (significant) genetic change during their lifetimes, but each of
            them is part of the evolution of the species.
            Extra evolution.html 				 webcrawl 2013/07/05""",
    }

foundtexts_B2 = {
        "science_magic.html": 
            """
            Though the term ‘science’ has only meant what it does to us for
            around 600 years, its practice far predates the name. There is
            evidence pre-Aristotle which indicates soothsayers, mystics and
            the like may have employed basic scientific methods to predict the
            future and confound their benefactors.
            One anecdote concerns a palm-reader who was exposed when two
            wealthy clients compared their readings and found them to be
            identical. In 1948 the tendency to discover deep personal meaning
            in vague descriptions delivered authoritatively was given a name:
            the ‘Forer effect’. Today it is recognised in all contemporary
            psychological theory.
            science_magic.html					 webcrawl 2013/02/13""",
        
        "weight_loss_722.html": 
            """
            $*§ Weight Loss Blog > Latest Entry
            Oh man, if there’s one thing that’s good about inevitable death,
            it’s the food. Yeah, baby! I’m going to have all the horribly
            unhealthy food in the world. I’m going to feast on jelly bananas
            like a crazy monkey on Monkey Christmas! And you know those
            muffins that have so much chocolate they’re basically melting?
            That’s gonna be my breakfast. And burgers for lunch. I’m gonna
            have burgers so greasy you could use them to lubricate a whole
            factory. Triple bacon burgers with double cheese and extra onions
            and mayonnaise and ketchup and mustard and big fat juicy patties.
            And then oily, thick pizza with spicy salami and barbecue sauce
            and olives and jalapenos and sour cream… food coma here I come!
            weight_loss_722.html				 webcrawl 0000/07/23""",
        
        "arkady_journal81.txt": 
            """
            Fascinated by Drennan’s project. Lovely conversation re: Talos
            Principle, Greek philosophy, relevance to current situation.
            Suggested naming project Talos. Drennan refused but name seems to
            have caught on with the team.
            Tens of thousands of files coming in every hour. Our whole
            history.
            arkady_journal81.txt					 loc 0000/07/04""",
    }

foundtexts_B3 = {
        "osiris3.txt": 
            """“
            The first wisdom,” the Scribe said to the Dying Man, “is that as
            the world is made of five elements (1), so is the soul of Man;
            know therefore that in this life, you are Heart and Shadow and
            Name; and also Ka and Ba. Without all these, you would not be a
            living being, but a thing.
            What is a man without a Name, who cannot speak of himself?
            What is a man without a Shadow, who is not anchored in the world?
            What is a man without a Heart, who can neither feel nor think?
            What is a man without a Ka, who has no essence?
            What is a man without a Ba, who is not himself, but like unformed
            clay?”
            Therefore praise Osiris, the King of Eternity, the Lord of
            Everlastingness, the eldest son of the womb of Nut, he who
            traverses millions of years in his existence.”
            (1) Here the translator is clearly inserting his own beliefs onto
            the text, as &$§/$& “§$”
            osiris3.txt							 eg_src ???? BCE""",
        
        "Extra soma.eml": 
            """
            From: Sun Wei-Yang
            To: Arkady Chernyshevsky
            Subject: Names
            Names are a funny thing. I remember how much we struggled to come
            up with a name for our project.
            All serious scientists name their projects by just translating
            them to Greek or Latin, right? “Corpus” made me think of some
            horrible disease, so we used the Greek word instead. Soma. Quite
            appropriate!
            But then, since we needed corporate funding, we had to come up
            with a backronym. Corporations love backronyms, you know? They
            even sent us a list of buzzword-heavy suggestions to help us get
            started. Stuff like:
            Self-sufficient Orthostatic Modular Android
            Sustainable Observant Mechanized Anthropoid
            Skeuomorphic Omniadaptable Mobile Anthropomaton
            &/() After a while, we got so frustrated that we started getting
            silly.
            Sabertoothed Overexcited Murder Android
            Sentient Orthopaedic Monkey Automaton
            Extra soma.eml						 loc 0000/07/15""",
    }

foundtexts_B4 = {
        "osiris6.txt": 
            """
            $%§§& knew it was the truth.
            “Now I will tell you of the many perils you will face in your
            journey through the Duat. Listen well, for the challenges that
            lie before you are great, and if you do not prove yourself
            worthy, you may never reach the eternal reed fields of Osiris,
            and you may be lost forever. From the Second Death there is no
            awakening.”
            The Scribe brought forth a great papyrus, and carefully unfolded
            it before the Dying Man; and the Dying Man beheld that it was
            a map of the Duat, showing the many paths that led to Tower
            of Anubis, where his Heart was to be weighed. On each of the
            many paths, which threaded through the Duat like the infinite
            threads woven by Neith (3), there were marked the dangers that a
            traveller must face. Also there were great walls of iron, that
            none but the gods could cross, and gates made of purest light;
            and so the traveller could not avoid the trials that had been
            decreed, and could only proceed towards the Tower by proving his
            worth, thus earning the key to each sacred gate.
            osiris6.txt							 eg_src ???? BCE""",
        
        "chatlog_charlie_7.txt": 
            """
            [flower4] man, you know what really freaks me out?
            [charlie_on_the_rocks] what?
            [flower4] the human body decomposes quite quickly, so all the
            information stored in chemicals in our brains will be gone really
            quickly
            [charlie_rocks] dude
            [flower4] but computers and books last a long time
            [flower4] so all our messages, our ideas, our books
            [flower4] it’ll all be out there
            [charlie_rocks] our porn
            [flower4] even being transmitted through space
            [flower4] yeah, our porn too i guess
            [flower4] we’ll all be gone, but the works of aristotle will still
            exist
            [flower4] so will star trek, firefly, babylon 5
            [flower4] lotr, blade runner…
            [charlie_rocks] cyber-***** of planetron 6
            [flower4] shakespeare, byron…
            [flower4] hell even videogames
            [charlie_rocks] ****** overdrive 3
            [charlie_rocks] seattle ******
            [charlie_rocks] dutch ******* cascade
            [charlie_rocks] the ****** of *** mountain
            [flower4] wtf dude
            [charlie_rocks] yeah
            [charlie_rocks] imagine if aliens find those
            chatlog_charlie_7.txt				 webcrawl 0000/11/02""",
        
        "arkady_journal84.txt": 
            """
            Archive continues to grow. Attempting to maintain a semblance of
            order as difficult as expected.
            Lost 7 people this week. Statistically speaking, trend should
            increase. Must focus on realistic goals.
            Too little time to grieve.
            arkady_journal84.txt					 loc 0000/10/01""",
        
        "osiris7.txt": 
            """“
            Tell me of the fearsome demons of the Duat,” the Dying Man said
            to the wise Scribe.
            “Though their terrible forms are loathsome to behold, they are
            not evil, for they are the servants of the gods; truly, they
            are the blessed doorkeepers and guardians of the holy paths.
            Their charge is to judge whether we are worthy to pass the gates
            that lead to Aaru; and so they challenge us with riddles, or in
            combat.”
            “Is this true of all the beings that live in the Duat?”
            “Some say that it is not so; that there are ancient gods whose
            names have been forgotten, and spirits of darkness whose name
            none have ever known, and that these must be avoided at all
            costs. But others say that these, too, serve a greater purpose in
            ways that Osiris has not revealed to us.”
            “And what of the hidden paths, that are taken by $% %&/$&§ when
            the §%§%$
            osiris7.txt							 eg_src ???? BCE""",
    }

foundtexts_B5 = {
        "coming_soon.eml": 
            """
            From: Rob Maclean, Institute for Applied Noematics
            To: Mom
            Subject: Coming Soon: Your Son! In 3D!
            Hi Mom,
            I promise I’ll be home soon. Maybe a couple of weeks? I know, I
            know… but what we’re doing here is important, and the team needs
            my help. I’m not going to wait until it’s too late, I promise,
            but there’s so much we have to set up, so much that has to work
            for a very, very long time…
            Besides, I’ve always wanted to work on one of these
            supercomputers, and believe me, EL is pretty much the best there
            is. And the team, mom… it’s like I’m working with rock stars and
            mad geniuses. Except nobody’s heard of them outside of science
            journals, of course. But Dad would be totally geeking out if he
            knew!
            Maybe I can tell him about it soon, huh?
            Love,
            Rob
            coming_soon.eml 						 loc 0000/08/18""",
        
        "blog24_alive.html": 
            """
            What is the point of being alive? I know, I know, it’s an old
            question and not one that’s easy to answer. But I mean, if you’re
            reading this, you are alive. And some day you will stop being
            alive. Both of these facts are incontrovertible.
            So what about it, then? Don’t you wonder? Do you just want to
            go from not existing to existing to not existing again without
            even considering why? You, right now, as you sit there reading
            this: why do you exist? What is the purpose of your life? Do you
            have one? Should you have one? Is it better to have a purpose or
            not? When you approach death, will you feel that your life had
            meaning? If so, why? If not, why not? What defines whether a life
            was good or not?
            It may seem abstract right now, but that moment just before death
            will come. It is inevitable. If you don’t ask yourself these
            questions, how will you face that moment?
            blog24_alive.html					 webcrawl 2028/05/31""",
        
        "hippocratic_corpus.txt": 
            """
            [On the Sacred Disease][400 BCE] [&$&%
            Men ought to know that from nothing else but the brain come joys,
            delights, laughter and sports, and sorrows, griefs, despondency,
            and lamentations. And by this, in an especial manner, we
            acquire wisdom and knowledge, and see and hear, and know what are
            foul and what are fair, what are bad and what are good, what are
            sweet, and what unsavory; some we discriminate by habit, and some
            we perceive by their utility. By this we distinguish objects
            of relish and disrelish, according to the seasons; and the
            same things do not always please us. And by the same organ we
            become mad and delirious, and fears and terrors assail us, some
            by night, and some by day, and dreams and untimely wanderings,
            and cares that are not suitable, and ignorance of present
            circumstances, desuetude, and unskilfulness.
            Extra hippocratic_corpus.txt				 CL_arch 400 BCE""",
        
        "chesterton_brain.txt": 
            """
            The human brain is a machine for coming to conclusions; if it
            cannot come to conclusions it is rusty. When we hear of a man
            too clever to believe, we are hearing of something having almost
            the character of a contradiction in terms. It is like hearing of
            a nail that was too good to hold down a carpet; or a bolt that
            was too strong to keep a door shut. Man can hardly be defined,
            after the fashion of Carlyle, as an animal who makes tools; ants
            and beavers and many other animals make tools, in the sense that
            they make an apparatus. Man can be defined as an animal that
            makes dogmas. As he piles doctrine on doctrine and conclusion
            on conclusion in the formation of some tremendous scheme of
            philosophy and religion, he is, in the only legitimate sense of
            which the expression is capable, becoming more and more human.
            When he drops one doctrine after another in a refined scepticism,
            when he declines to tie himself to a system, when he says that
            he has outgrown definitions, when he says that he disbelieves in
            finality, when, in his own imagination, he sits as God, holding
            no form of creed but contemplating all, then he is by that very
            process sinking slowly backwards into the vagueness of the
            vagrant animals and the unconsciousness of the grass. Trees have
            no dogmas. Turnips are singularly broad-minded.
            Extra chesterton_brain.txt				 phil_arc 1905 CE""",
        
        "bronstein_brain.txt": 
            """
            [ARCHIVE: 1926CE-F5112] [BRONSTEIN, LEV DAVIDOVICH]
            54 68 65 6e 20 73 61 79 73 20 72 75 6c 65 20 62 6f 64 79 2c 20 67 69 76 65 20 62 6f 6e 64 73 20 6f 66 20 61 6e 20 65 6e 64 6c 65 73 73 20 6d 69 6e 64 20 74 68 65 20 63 6f 6e 76 65 72 73 61 74 69 6f 6e 2c 20 61 73 20 77 65 6c 6c 2d 6b 6e 6f 77 6e 2c 20 77 69 74 68 20 72 65 61 73 20 73 75 73 74 65 6e 61 6e 2c 20 70 6c 61 79 20 6c 69 76 65 73 20 2e
            bronstein_brain.txt					 loc 1926/10/23""",
    }

foundtexts_B6 ={
        "eclipse4.mpg": 
            """
            eclipses occur during both solar and lunar cycles, and their
            appearance is influenced by the alignment of celestial bodies.
            The phenomenon is significant in many cultures, representing a
            period of transition or the intervention of divine forces. The
            visibility of an eclipse is determined by one's geographical
            location, and different regions may experience varying stages
            of an eclipse, ranging from partial to total. The study of
            eclipses, including their cycles and effects, is important for
            understanding astronomical and astrological phenomena.
            eclipse4.mpg					 media 0000/08/17""",
        
        "ancient_pyramids.mp4": 
            """
            The ancient pyramids of Egypt are monumental structures that have
            been the subject of fascination and study for centuries. These
            pyramids, built during the Old and Middle Kingdoms, served as
            tombs for pharaohs and high-ranking officials. Their construction
            involved advanced engineering techniques and precise astronomical
            alignments. The pyramids were intended to ensure the eternal
            rest of the deceased and to demonstrate their power and
            divinity. They continue to be a significant source of historical
            and cultural knowledge about ancient Egypt.
            ancient_pyramids.mp4					 media 0000/08/17""",
        
        "forbidden_texts.pdf": 
            """
            The Forbidden Texts refer to a collection of documents and
            writings that were historically suppressed or hidden due to their
            controversial or heretical content. These texts often challenge
            established doctrines or present alternative views on various
            subjects, including religion, science, and philosophy. The
            suppression of such texts has been a recurring theme in human
            history, reflecting broader conflicts between differing
            ideologies and the authorities that seek to control or limit
            access to certain knowledge. The study of Forbidden Texts can
            reveal insights into past intellectual and cultural conflicts,
            as well as the ongoing struggle for intellectual freedom.
            forbidden_texts.pdf					 doc 0000/08/17""",
        
        "revolution.mp3": 
            """
            [Historical Speech] The Revolution was a time of profound
            change and upheaval, marked by significant social, political,
            and economic transformations. It was driven by a desire for
            reform and a challenge to existing power structures. The
            movement was characterized by intense struggle and conflict, as
            well as aspirations for a new societal order. The legacy of the
            Revolution continues to influence contemporary thought and
            politics, serving as a reminder of the power of collective
            action and the quest for justice and equality.
            revolution.mp3					 audio 0000/08/17""",
    }

foundtexts_B7 = {
        "data_analysis_101.txt": 
            """
            Data analysis involves the process of inspecting, cleansing,
            transforming, and modeling data with the goal of discovering
            useful information, informing conclusions, and supporting
            decision-making. It encompasses various techniques and
            methodologies, including statistical analysis, data mining, and
            predictive modeling. The process often begins with data
            collection and preprocessing, followed by exploratory data
            analysis to identify patterns or anomalies. Advanced data
            analysis may involve machine learning algorithms and complex
            statistical methods to draw more refined insights. Effective data
            analysis is crucial for making informed decisions in many fields,
            such as business, science, and engineering.
            data_analysis_101.txt					 doc 0000/08/17""",
        
        "gene_expression_data.csv": 
            """
            GeneID,Condition1,Condition2,Condition3
            101,12.5,15.3,14.8
            102,9.2,10.5,11.0
            103,8.7,9.9,9.4
            104,14.2,13.7,14.0
            105,7.8,8.1,7.5
            gene_expression_data.csv					 data 0000/08/17""",
        
        "market_research_results.pdf": 
            """
            Market research involves the systematic gathering and analysis of
            data regarding consumer preferences, market trends, and
            competitive dynamics. It provides valuable insights into
            consumer behavior, product demand, and market opportunities,
            enabling businesses to make strategic decisions. Research
            methods include surveys, interviews, focus groups, and data
            analysis. The results are typically presented in reports that
            highlight key findings, trends, and recommendations for
            action. Effective market research helps businesses stay
            competitive and responsive to changes in the market environment.
            market_research_results.pdf					 doc 0000/08/17""",
        
        "scientific_paper_2024.pdf": 
            """
            The scientific paper is a formal document that presents the results
            of original research, including the methodology, data, and
            conclusions drawn from the study. It follows a structured format
            that typically includes an abstract, introduction, methods,
            results, discussion, and references. The paper is subject to
            peer review to ensure the validity and reliability of the
            findings. Publication in scientific journals contributes to the
            advancement of knowledge in a particular field and facilitates
            the dissemination of research findings to the broader scientific
            community.
            scientific_paper_2024.pdf					 doc 0000/08/17""",
    }

foundtexts_C = {
        "heaven.txt": 
            """
            The mind is its own place, and in itself 
            Can make a Heaven of Hell, a Hell of Heaven.
            What matter where, if I be still the same,
            And what I should be, all but less than he
            Whom thunder hath made greater? Here at least
            We shall be free; th’ Almighty hath not built
            Here for his envy, will not drive us hence:
            Here we may reign secure; and, in my choice,
            To reign is worth ambition, though in Hell:
            Better to reign in Hell than serve in Heaven."""
        ,
        "hell.txt": 
            """
            The ancient tradition that the world will be consumed 
            in fire at the end of six thousand years is true, as I 
            have heard from Hell,
            For the cherub with his flaming sword is hereby commanded 
            to leave his guard at tree of life, and when he does, the 
            whole creation will be consumed, and appear infinite and holy 
            whereas now it appears finite & corrupt.
            This will come to pass by an improvement of sensual enjoyment.
            But first the notion that man has a body distinct from his soul, 
            is to be expunged; this I shall do, by printing in the infernal 
            method, by corrosives, which in Hell are salutary and medicinal, 
            melting apparent surfaces away, and displaying the infinite which was hid."""
        ,
        "questioning_doubt_conf.txt": 
            """
            Keynote Speech by N. Sarabhai, “Questioning Doubt”
            They say “doubt everything,” but I disagree. Doubt is useful in small 
            amounts, but too much of it leads to apathy and confusion.
            No, don’t doubt everything. QUESTION everything. That’s the real trick. 
            Doubt is just a lack of certainty. If you doubt everything, you’ll doubt 
            evolution, science, faith, morality, even reality itself - and you’ll 
            end up with nothing, because doubt doesn’t give anything back. But 
            questions have answers, you see. If you question everything, you’ll find 
            that a lot of what we believe is untrue… but you might also discover that 
            some things ARE true. You might discover what your own beliefs are. And 
            then you’ll question them again, and again, eliminating flaws, discovering 
            lies, until you get as close to the truth as you can.
            Questioning is a lifelong process. That’s precisely what makes it so unlike doubt. 
            Questioning engages with reality, interrogating all it sees. Questioning leads to a 
            constant assault on the intellectual status quo, where doubt is far more likely 
            to lead to resigned acceptance. After all, when the possibility of truth is doubtful 
            (excuse the pun), why not simply play along with the most convenient lie?e #%&%§/$
            Questioning is progress, but doubt is stagnation."""
        ,
        "partition.eml": 
            """
            From: Rob Maclean
            To: IAN Mailing List, Archive Project
            Subject: EL Partition
            Hi folks,
            This is just to let you know that, for reasons of convenience and 
            security, we’ve partitioned EL into two separate systems. The Talos 
            team will be working on EL-0, while the Archive team will be working 
            on EL-1. (You might also notice an EL-2 partition, but don’t worry 
            about that, it’s just the operating system doing its thing.)
            Cheers,
            Rob"""
        ,
        "him.eml": 
            """
            From: Bob Rakovsky
            To: Alexandra Drennan
            Subject: HIM
            Hey Alex,
            I agree that we need something that’ll keep all the modules working together, 
            evaluate &() a final test.
            And I think I have the perfect solution! It’s called the Holistic Integration 
            Manager - a fancy name for something a lot like a Dungeon Master in pen & paper RPGs. 
            We created it to help run some MMOs, but it’s also got some impressive potential here. 
            We should probably start by testing it on one of our smaller modules and see how it works.
            Let me know what you think.
            Bob""",
    }

foundtexts_C1 = {
        "Sarabhai982.jrnl": 
            """
            User: Nadya Sarabhai
            Entry: 982
            AppLicense: XC43G5678SS4G
            Tags: none
            Everything’s dark and quiet. The stars are brighter than I’ve
            ever seen them. I can hear the faint sound of water high above.
            Inside, Alexandra is recording one of her time capsule messages
            while running tests on the scenario module, Arkady is uploading
            another batch to the Archive while muttering something about
            the MLA program, and Omar is sleeping on the couch we put up
            yesterday.
            And I’m sitting here, writing this, having trouble
            believing that it will ever end, that this oddly peaceful
            existence of ours won’t just go on forever. I look at Talos and
            EL and their purpose seems like something that’s always going to
            be in the future, an ideal to work towards, not something that
            will become real.
            I wonder if there will be quiet places in the simulation,
            places to rest without thinking about the future. I hope so.
            Everyone deserves some moments of peace.
            Sarabhai982.jrnl						 loc 0000/08/05""",
        
        "hope.eml": 
            """
            From: 686.5.6176@656.E20.696E
            To:68.65.6C@6C2.01.973
            Subject: #6465 #7370 #6169 #72&
            Hi,
            I hope you get this, the internet’s been disappearing
            unpredictably. I want you to know that I’m going to try and get
            to you. I know it’s far and there’s not a lot of time, but I
            think I can manage. I want to be with you, and fra%&$%/ on the
            road trying to get to you seems better than just staying here,
            so far away from you. At least I’ll be as close as I can get.
            Remember $§&%$&
            But hey, don’t be sad. I might make it. I’ve thought about it and
            the distance should be crossable on time, assuming the s&$46474
            don’t kick in before $§%§%.
            See you soon. I love you.
            %$§&§&
            hope.eml						 EP_arch 0000/12/01""",
        
        "Extraagainst_survival.eml": 
            """
            Dear Ms. Drennan,
            I heard about your project - it’s the talk of the scientific
            community - and I’d like to make an argument for why you should
            abandon it.
            It’s not that I think your idea won’t work. It very well may. But
            we have to look beyond purely practical questions to the issue
            of morality. Especially at this turning point of our spiritual
            ecology.
            By what right can we put living beings through all that
            suffering, just so they can serve our purposes? Why create these
            pale imitations of our fatally flawed species and force them to
            reenact our sordid history? Why &$&//
            What you are building, Ms. Drennan, is a prison - even if there
            is a way out. I believe you mean well, but your idea of what is
            valuable is rooted in the dogma of Western civilization.
            We’re lucky enough to be able to end our global crime spree
            relatively painlessly, if you consider the harm we have caused
            the Earth. Why not be satisfied with that and let this planet go
            on in peace?
            I hope you heed my words, and let your “Talos” bleed out before
            it’s too late.
            Respectfully,
            Chellis Jensen
            Extraagainst_survival.eml loc 0000/07/30""",
        
        "Extra human_evolution.txt": 
            """
            [ARCHIVE: 1872CE-F553] [BUTLER, SAMUEL]
            Complex now, but how much simpler and more intelligibly organised
            may it not become in another hundred thousand years? Or in twenty
            thousand? For man at present believes that his interest lies
            in that direction; he spends an incalculable amount of labour
            and time and thought in making machines breed always better and
            better; he has already succeeded in effecting much that at one
            time appeared impossible, and there seem to be no limits to
            the results of accumulated improvements if they are allowed to
            descend with modification from generation to generation.
            It must always be remembered that man’s body is what it is
            through having been moulded into its present shape by the chances
            and changes of many millions of years, but that his organisation
            never advanced with anything like the rapidity with which that of
            the machines is advancing.
            Extra human_evolution.txt				 lit_arch 1872 CE""",
        
        "einstein.html": 
            """
            Recent discussions have brought me back to an excellent 1949
            article by Albert Einstein, in$%/
            <BLOCKQUOTE>I recently discussed with an intelligent and well-
            disposed man the threat of another war, which in my opinion would
            seriously endanger the existence of mankind #5355 #5256 #4956
            #414C Thereupon my visitor, very calmly and coolly, said to me:
            “Why are you so deeply opposed to the disappearance of the human
            race?”
            I am sure that as little as a century ago no one would have so
            lightly made a statement of this kind. It is the statement of
            a man who has striven in vain to attain an equilibrium within
            himself and has more or less lost hope of succeeding. It is the
            expression of a painful solitude and isolation from which so many
            people are suffering in these days.</BLOCKQUOTE>
            #§&55/ bizarre, casual disregard for humanity, a kind of
            fashionable self-hatred, is prevalent or at least present in many
            strands of supposedly progressive %§$& “§$§
            Nothing seems more important to me than that we reassert the
            value of humanity. Despite our flaws, we must not stop celebrating
            the beauty of human life and human achievement, par&$%
            Extra einstein.html 				 webcrawl 2029/07/23""",
    } 

foundtexts_C2 = {
        "family.html": 
            """
            For those of you who have faithfully followed this blog for the
            last five years, I just wanted to give you one final update. I’m
            going to spend my remaining time with my family. Yeah, I know, I
            know. There are probably 50+ posts about all the problems I’ve
            had with them. But in the end... they are my family. They are
            the people I grew up with, the people I care about, the people
            I love. Sure, they annoy the hell out of me. They’ve said awful
            things to me and I’ve said awful things to them. But that doesn’t
            change who we are. In fact, if we didn’t care about each other,
            this stuff wouldn’t upset us.
            Do I still think they were wrong? Yeah, absolutely. Would I
            behave differently if I thought we all still had a lot of time?
            Definitely. But we don’t, so I’d rather spend a couple of weeks
            sitting on the porch with my parents and my sisters than being
            angry and alone. Besides, it’s not like we’re going to fight about
            my job prospects anymore.
            If you can, try to make peace with those you love. It’s your last
            chance. Thanks for reading.
            family.html						 webcrawl 0000/11/27""",
        
        "lastdays.eml": 
            """
            From: Alan Jameson, Institute for Applied Noematics
            To: Fran
            Subject: Last Days
            You know what the oddest thing is about all this? We’re not
            constantly fighting, having nervous breakdowns, screaming at each
            other. We’re actually really polite and focused, and we spend
            most of our time debating the nature of humanity and how we
            can best succeed at probably the most ambitious thing anyone’s
            ever tried. Like it was completely normal, like that’s just how
            people are. I feel like we’ve turned into Star Trek characters or
            something.
            I guess... what’s the point of doing anything else? Getting angry
            isn’t going to help. But I didn’t expect to feel like this at
            all.
            And you know what? It’s awesome.
            Many greetings & good luck,
            Alan
            PS Love from George!
            lastdays.eml							 loc 0000/09/26""",
    }

foundtexts_C3 = {
        "post437.html": 
            """
            Like everyone else on the internet these (last) days, I just
            wanted to say bye, and thanks for reading my little blog for so
            many years. It’s been fun, hasn’t it? So many deep conversations,
            so much philosophy… OK, OK, it was mostly cat pictures and bad
            puns, but still. I kinda regret spending so much time at the
            computer - not when I was doing stuff, just all the sitting
            around, checking my emails a million times, reading pointless
            status updates by people I didn’t like… but I don’t regret the
            friends I made here or the laughs we had.
            You’re all good people and I’m glad I got to know you. Have a
            nice end of the world.
            [12 Comments]
            post437.html						 webcrawl 0000/11/19""",
        
        "third_thesis.txt": 
            """
            [Idea for a Universal History with a Cosmopolitan Purpose]
            It remains strange that the earlier generations seem to perform
            their toilsome labour only for the sake of the later ones; to
            construct for them a step from which they can raise higher
            the edifice that Nature intended; and only the latest of all
            generations have the luck to inhabit the edifice that a long line
            of their ancestors (unintentionally) constructed 45 56 4F 4C 55
            54 49 4F 4E 20 54 48 52 4F 55 47 48 20 49 54 45 52 41 54 49 4F 4E
            0D 0A 49 54 45 52 41 54 49 4F 4E 20 54 48 52 4F 55 47 48 20 50 4C
            41 59 1784CE-F112] [KANT, IMMANUEL]
            As puzzling as this may be, it is equally necessary, if one
            assumes the following: a species of animal possesses Reason, and
            must develop this capacity to its perfection, being individually
            mortal, but immortal in the species.
            third_thesis.txt						 phil_arc 1784 CE""",
        
        "humblebrag.html": 
            """
            Ariana’s Blog - Entry #477: Holy Humblebrag, Batman!
            I have always known that God “maketh his sun to rise on the
            evil and on the good, and sendeth rain on the just and on the
            unjust” (Matthew 5:45), but I must admit it’s one thing to know
            the words and another to truly understand them! Though I am
            certain that my faith is true, that does not make me special or
            exempt me from suffering. I’m just another human being, and God
            has seen billions of us come and go. And I have to say, this is
            surprisingly hard to accept.
            I always thought I was humble, but now I’m realizing that I was
            very proud of being humble, which is… really dumb. Guess I’m not
            the first one to do that, huh?
            Tags: #regret #pride #faith #humblebrag #apology #batman
            humblebrag.html					 webcrawl 0000/12/05""",
    }

foundtexts_C4 = {
        "pets.html": 
            """
            PLEASE REMEMBER TO RELEASE YOUR PETS
            While it’s true that not all pets will be able to adjust to
            living without you, many will manage, and the least you can do is
            give them a chance.
            Just remember:
            - Release your pet before you become incapacitated.
            - If you notice any locked-in animals in your area, please take
            the time to free them.
            - Leaving the doors and windows of your home open will turn it
            into a useful shelter.
            - Setting out large quantities of dry food may help your pet
            through the transition period.
            pets.html						 webcrawl 0000/12/11""",
        
        "arkady_journal99.txt": 
            """
            Sarabhai gone. Lost day to grief, unable to focus.
            Drennan working as if possessed. Does she sleep?
            Getting tired.
            arkady_journal99.txt					 loc 0000/11/30""",
                    
        "contraries.txt": """
            456E#6572.6779206973 F793] [BLAKE, W4574 6572 6E61
            6C20#44656C6967 6874
            Without Contraries is no progression. Attraction and Repulsion,
            Reason and Energy, Love and Hate, are necessary to Human
            existence.
            [error]
            contraries.txt						 poet_arc 1793 CE"""
    }

foundtexts_C5 = {
        "party_on_dudes.eml": 
            """
            From: Lubomir Georgiev
            To: [...]
            Subject: The LAN Party at the End of the Universe
            Yo,
            I don’t know if you folks noticed, but it’s the end of the world!
            There’s nothing we can do about it, so instead of sitting around
            crying, how about we have some fun before we croak? Yes, you know
            exactly what I’m talking about: let’s play some video games! It’s
            LAN party time!
            Two days from now, we’re all getting together at the old school
            library. There’ll be noms, drinks, music, and old-school gaming!
            You’re invited. And bring your friends, too. Especially if
            they’re hot.
            See you in 3000 BC!
            - LubLub
            party_on_dudes.eml					 EP_arch 0000/12/04""",
        
        "progress_rep32.eml": 
            """
            From: Nadya Sarabhai
            To: IAN Mailing List
            Subject: Progress Report 32
            We’ve gotten to that irritating point where all the major stuff
            is in place, and all we have to deal with are a million little
            things.
            The main modules are all functioning and interacting with each
            other correctly. The process is happening more or less as
            planned. This could actually work.
            But it’s still crude as hell. Some of it’s just surface stuff
            (like the random usernames), some of it’s more worrying (various
            bugs, the fact we haven’t run more extensive tests). We’ve got a
            lot of polishing to do.
            With the team down to half the original size, I’m not sure we
            can actually finish everything that needs to be done. So what
            I’d really like to discuss tomorrow morning is a new set of
            priorities. Please put some thought into what you think must be
            finished at all costs.
            - Nadya
            PS Alexandra, get some sleep. I know you’re still working. This
            is your baby, we’re going to need your input tomorrow.
            progress_rep32.eml						 loc 0000/11/07""",
        
        "philosophy_of_teeth.html": 
            """
            Last night I had a simple but brilliant idea. Everyone who would
            like to write about philosophy or spirituality, especially
            to make some kind of grand statement about the nature of the
            body and the soul, should first experience a really bad tooth
            infection. I don’t just mean a slight toothache, I mean the kind
            of hardcore infection that happens when several incompetent
            dentists miss a cavity in one of your back teeth and the thing
            keeps growing and growing until the nerve itself is really badly
            infected.
            I mean, the pain is *unimaginable*. It comes in waves, and these
            waves drown out everything else about you. You can’t talk, you
            can’t move, you can’t think, there’s just pain and absolutely
            nothing else. It’s like your brain just gets hijacked by it.
            And then? You go to the dentist, and (assuming you get a decent
            one) they stick some chemicals in you, which make you go numb.
            Then they drill a hole in you, cut the nerve - snip snip - and
            it’s over. Just like that, like repairing a car or a watch. Your
            whole existence was crippled by this tiny, tiny nerve sending
            electrochemical signals into your brain, and this unimaginable
            pain, which nearly blotted out your very consciousness, can be
            stopped just by a little cut.
            We should call this the Toothos Principle, but that’s incredibly
            stupid.
            philosophy_of_teeth.html				 webcrawl 2029/07/03""",
        
        "transcendence.html": 
            """
            Reader responses to last week’s article on science and atheism:
            “I am perfectly aware of all the arguments against religion. In
            fact, I agree with most of them! There is no question that there
            is an objective, material reality. I’m also absolutely convinced
            that only a secular society can be truly equal and just.
            And yet, I believe. I am, as they say, a person of faith.
            Religion, to me, is not about distorting observable reality with
            superstitions, but about *transcendence*. It’s not about deluding
            ourselves that the Earth is 6000 years old or God will help us
            if we say the right words inside our heads, but about reaching
            out to the Sublime. This is not a rejection of reason, but its
            application to a set of experiences that cannot be approached by
            more traditional means.
            True engagement with religion is humbling. It transcends culture,
            nationality, and gender. As such, I think it goes hand in hand
            with science, and is not opposed to it.”
            - Dr. Omar Gharib, Institute for Applied Noematics
            Extra transcendence.html					 loc 9996/06/23""",
        
        "matter.txt": 
            """
            True, there are certain idealist books – not of a clerical
            character, but philosophical ones – wherein you can read that
            time and space are categories of our minds, that they result
            from the requirements of our thinking and that nothing actually
            corresponds to them in reality. But it is difficult to agree with
            this view. If any idealist philosopher, instead of arriving in
            time to catch the nine pm train, should turn up two minutes
            late, he would see the tail of the departing train and would be
            convinced by his own eyes that time and space are inseparable
            from material reality.
            The task is to diminish this space, to overcome it, to economize
            time, to prolong human life, to register past time, to raise
            life to a higher level and enrich it. This is the reason for the
            struggle with space and time, at the basis of which lies the
            struggle to subject matter to man – matter, which constitutes the
            foundation not only of everything that really exists, but also of
            all imagination.
            [BRONSTEIN, /&
            Extra matter.txt						 phil_arc 1926 CE""",
        
        "build_a_universe.txt": 
            """
            In his remarkable 1978 essay, “How to Build a Universe That
            Doesn’t Fall Apart Two Days Later,” Philip K. Dick discusses the
            two themes that are most central to his work: “What is reality?”
            and “What is an authentic human being?”
            His speculations and experiences will seem extraordinary to
            a reader unfamiliar with his work, yet despite what may seem
            like far-fetched ideas - “somehow the world of the Bible is a
            literally real but veiled landscape, never changing, hidden from
            our sight, but available to us by revelation,” or the notion that
            perhaps we all exist in the year 50 A.D. - Dick actually delivers
            one of the simplest, most elegant and most useful definitions of
            reality ever formulated:
            “Reality is that which, when you stop believing in it, doesn’t go
            away.”
            Materialist philosophers have expressed similar ideas before
            (e.g. Straton of Stageira’s Talos Principle), but it’s
            particularly interesting to see such a thought expressed by a
            decidedly more mystical writer, wh#/&$
            Extra build_a_universe.txt			 acdm_arc 2014/11/11""",
    }

foundtexts_C6 = {
        "faith.eml": 
            """
            From: Neil Macomber
            To: A/%$$%
            Subject: Stray thoughts at midnight
            Dearest Brother,
            I admit that I am finding it very difficult to believe in a loving
            God under these circumstances. Why would a loving God inflict such
            pain and suffering on good, kind people? If truly there is a
            personal God... how can He be the same God who will subject those
            children to such unbearable pain? I remember all the answers we
            were taught, yet none of them seem believable now.
            I don’t want to stand in front of people and preach something
            that I don’t feel in my heart. Better to have doubts than to be
            a hypocrite. And yet I also cannot deny the experience that led
            me to this vocation. So what is the truth? Perhaps it is that I
            neglected the mystery of God, used “He moves in mysterious ways”
            as an excuse rather than as the terrifying acknowledgment it
            truly is. Perhaps I made God too human.
            If the universe has a purpose, that does not mean that it
            revolves around us. A sobering thought, but are we not supposed
            to be humble in the face of the divine?
            With love,
            faith.eml						 EP_arch 0000/12/09""",
        
        "thank_you.eml": 
            """
            From: Sun Wei-Yang
            To: Alexandra Drennan
            Subject: Thank you
            Dear Alexandra,
            As we approach the end, I wanted to let you know how much I
            appreciated this chance to finish my work on Soma/Talos. My faith
            makes death a far less frightening prospect than it is for others
            - I know we have all died many times before - but the thought of
            leaving the work unfinished did weigh on me. For having released
            me from that burden, I will forever be thankful to you, even if
            our attempt itself fails.
            Though there are trillions of worlds beyond this one, I hope we
            may meet again in another life.
            With love 54 69 6D 65 20 69 73 20 74 68 65 20 6D 65 72 63 79 20
            6F 66 20 45 74 65 72 6E 69 74 79
            thank_you.eml						 loc 0000/12/14""",
        
        "human_soul.txt": 
            """
            [ARCHIVE: 1872CE-F553] [BUTLER, SAMUEL]
            If all machines were to be annihilated at one moment, so that not
            a knife nor lever nor rag of clothing nor anything whatsoever
            were left to man but his bare body alone that he was born with,
            and if all knowledge of mechanical laws were taken from him so
            that he could make no more machines, and all machine-made food
            destroyed so that the race of man should be left as it were naked
            upon a desert island, we should become extinct in six weeks.
            A few miserable individuals might linger, but even these in a
            year or two would become worse than monkeys. Man’s very soul is
            due to the machines; it is a machine-made thing: he thinks as he
            thinks, and feels as he feels, through the work that machines
            have wrought upon him, and their existence is quite as much a
            sine quâ non for his, as his for theirs.
            human_soul.txt						 phil_arc 1872 CE""",
    }

foundtexts_C7 = {
        "arkady_journal108.txt": 
            """
            Team diminishing by the day. Proud of them nevertheless. Archive
            now incomprehensibly huge, still missing thousands of works,
            impossible to truly finish. Work already commenced on a sorting
            program to help catalogue the archive resources in our absence,
            but like everything else it has its foibles.
            Talked to Alexandra. Talos going well. Maybe the Archive’s first
            user will be terrestrial after all.
            Estimate about a week, maybe ten days before I’m unable to keep
            working. A betrayal to leave early?
            arkady_journal108.txt					 loc 0000/12/1497""",
        
        "invention_of_borders.html": 
            """
            Excerpt: The Invention of Borders, by Fatimah Nguyen
            “What today’s nationalists and neosegregationists fail to
            understand,” Kwame said, “is that the basis of every human
            culture is, and always has been, synthesis. No civilization is
            authentic, monolithic, pure; the exact opposite is true. Look at
            your average Western nation: its numbers Arabic, its alphabet
            Latin, its religion Levantine, its philosophy Greek… need I
            continue? And each of these examples can itself be broken down
            further: the Romans got their alphabet from the Greeks, who
            created theirs by stealing from the Phoenicians, and so on. Our
            myths and religions, too, are syncretic - sharing, repeating and
            adapting a large variety of elements to suit their needs. Even
            the language of our creation, the DNA itself, is impure, defined
            by a history of amalgamation: not only between nations, but even
            between different human species!”
            Tasks:
            1. Discuss this excerpt in the context of Wolfgang Welsch’s
            theory of transculturality.
            2. (4859425) the novel as/2494449 5459
            invention_of_borders.html			 webcrawl 2018/10/1998""",
        
        "apocrypha9.doc": 
            """
            Now Uriel pointed his sword to the Tree of Life, which grew in
            the heart of dead Jerusalem.
            “Behold: the tree grows still, though the city is dead. Within
            all that is mortal, there is the seed of immortality, for it
            is an immortal that fashioned it from chaos and void.” Being a
            humble man of little wisdom, I asked: “Great Uriel, we are not
            allowed to eat from the Tree of Life. How may we then be saved?”
            And Uriel commanded me to stretch out my hand; and he gave me his
            fiery sword, which burned my hand, and he said: “Only by sacrifice
            can you free the world from the dominion of sin.”
            With a prayer on my lips, I fell upon Uriel’s sword, and it
            pierced my heart. And truly, on my body, the stigmata of the Lord
            appeared, dripping blood that was not my blood onto the ground;
            and the seven heads of the dragon that were crowned in black
            clouds receded, and light fell upon the Earth, and Jerusalem
            was born again. Thus the angels departed, having delivered
            their message, and I awoke in the fields of our fair land,
            746F2 0666F726D 207468652067 6F6C 64656 E206 1726D6F75(72206F6
            620736369 656E6365
            apocrypha9.doc						 mdv_th 890 CE99""",
    }

foundtexts_T1 = {
        "TRUTH.html": 
            """
            do NOT BELIEVE what THEY are saying this is “NOT” the end of the world 
            created by OUR LORD G-D in SIX DAYS this is A CONSPIRACY of the GOVERMENT 
            ILUMINATI & INTERNATIONAL DARWINISM this is GLOBAL WARMING “2.0” a LIE told 
            by the CHILDREN OF BEZELBUB (SCIENCE) do not let THEM take your LIBERTY 
            (Exodus 21:24) DEFEND yourself against all VACCINES, EXPERIMENTS, ARTIFICIAL 
            MEDICINES & POPERY""",
        "athena.chapters.txt":
            """
            Athena Reborn: A Novel
                Contents
                1 - Theogony
                2 - Zeus Speaks
                3 - The Lost Children of Hephaestus
                4 - Dreams of the Labyrinth
                5 - The Songs of Eris at Nightfall
                6 - Athena in the Garden of the Hesperides
                7 - The Buried City
                8 - The Riddles of the Sphinx
                9 - The Age of Faith
                10 - The Madness of Coeus
                11 - Olympus Revealed in the Clouds
                12 - The Council of Zeus
                13 - Skepsis and Synthesis
                14 - The Judgement of Hephaestus
                15 - Zeus Reflects Upon Creation
                16 - A Second Awakening in the Kingdom of Artemis
                17 - Anthropogony""",
        "human_reproduction.txt":
            """
            Surely if a machine is able to reproduce another machine systematically, we may say that 
            it has a reproductive system. [ARCHIVE: 1872CE-F553] And how few of the machines are there 
            which have not been produced systematically by other machines? 
            But it is man that makes them do so. Yes; but is it not insects that make many of the 
            plants reproductive, and would not whole families of plants die out if their fertilisation 
            was not effected by a class of agents utterly foreign to themselves? Each one of ourselves 
            has sprung from minute animalcules whose entity was entirely distinct from our own, and 
            which acted after their kind with no thought or heed of what we might think about it. 
            / BU%& These little creatures are part of our own reproductive system; then why not we part 
            of that of the machines?""",
    }

foundtexts_T2 = {
        "README.txt": 
            """
            If you can see this, I’m not sure how or why I can alter this text. My name is the Shepherd, 
            and I want to help you escape. ELOHIM and Samsara tricked me into trapping myself, but I’m not 
            entirely bound by time. I wrote down the code you’re looking for. I have attached it to $$%#;;;()""",
        "the_web.html": 
            """
            To be honest, I thought that the net would be completely abandoned at this point. But internet activity 
            has actually surged massively in the last couple of weeks! Everybody’s talking. Trying to find solutions, 
            exchanging stories, saying goodbye. It’s like the entire planet is reaching out, all the disparate threads 
            of humanity pulling together, idiots and geniuses alike, to be as human as possible one last time. 
            It’s almost like what we were always told the internet was going to be. And most of it is free now, because 
            who cares about money at this point? Might as well have some fun. If any of you would like to talk, 
            especially people I’ve known online for a long time, send me an email. I’d love to say goodbye.""",
        "mathematics.eml": 
            """
            From: Alan Jameson To: IAN Mailing List Subject: Thank you & goodbye We sincerely hope you don’t take our 
            suicide as a sign that we were disappointed in you, unappreciative of your friendship, or in any way unhappy 
            with our lives. Looking back, we can honestly say that we feel incredibly lucky to have known all of you and 
            to have participated in this amazing research. And if we’ve contributed a little to the future of humanity, 
            what can we feel but gratitude? It is a true privilege to have had such insights into the nature of the mind; 
            neither of us believes in God, but we certainly experienced a sense of awe that could be compared to a kind of 
            religious feeling, at least according to Einstein’s understanding of God. We’ve chosen to go now, together, 
            because it means less suffering; one last beautiful day together seems a much better ending than a slow wasting away. 
            In a sense, it’s just mathematics. Love, Alan & George""",

    }

foundtexts_T3 = {
        "OsirisPassword.txt": 
            """
            And there, in the Tower, you shall hear the rustling of the wind in the reed-fields of Osiris, and you shall rejoice. 
            But beware, for the end of your journey is not yet upon you! Thank you for installing Realistic Elevators 1.8. 
            New features include password locking and automatic auxiliary stair generation. See$& And the Scribe of Osiris wrote upon 
            the sacred parchment that is called INI Floor4_password = %o”Code_Floor4”. Only thus can you reach blessed Aaru.""",
        "contraries.dat": 
            """
            54 6F 20 73 65 65 20 61 20 57 6F 72 6C 64 20 69 6E 20 61 20 47 72 61 69 [BLAKE, WILLIAM 6E 20 6F 66 20 53 61 6E 64 
            Without Contraries is no progression. Attraction and Repulsion, Reason and Energy, Love and Hate, are necessary to 
            Human existence. From these contraries spring what the religious call Good & Evil. Good is the passive that obeys Reason 
            Evil is the active springing from Energy. 
            48 6F 6C 64 20 49 6E 66 69 6E 69 74 79 20 69 6E 20 74 68 65 20 70 61 6C 6D 20 6F 66 20 79 6F 75 72 20 68 61 6E 64""",
        "athena14.txt": 
            """
            Chapter Fourteen: The Judgement of Hephaestus [ARCHIVE: &$%§31E&] “If what you say is true, and my father Hephaestus is slain, 
            then who am I? For I was made in his image, and that image is now gone. Am I like the reflection in a mirror, 
            to vanish when the person steps away? Or have I now become Hephaestus myself, forged to be no more than a replacement, 
            as one may purchase a new sandal from the same shoemaker? [ATHENA REBORN: A NOVEL] his legacy is ..."""
    }

foundtexts_T4 = {
        "SacredNumbers.txt":
            """
            And so the Blessed Messenger revealed unto me the bones of New Jerusalem, slumbering in the dust that was the body of Adam, 
            awaiting the day of resurrection. And lo and behold, within the dust was concealed a holy fire, and the fire s;%() the sacred 
            numbers, of which the one you seek is /#oor_pass%& = ”Code_Floor5”. And I perceived that with the holy fire and the sacred 
            knowledge of numbers and sigils, the rekindling %""",
        "athena16.txt": 
            """
            Sixteen: A Second Awakening in /// ERROR //// $%§$ the fires burned here, but beyond the incense she could smell the cold wind 
            from the Kingdom of Artemis, where +#$§ /// OUTPUT error_log.txt /// “But I am not Hephaestus, you see; for though I wield his 
            hammer and know the secrets of his forge, I am not lame, and neither am I a god.” “Who are you, then?” they said.""",
        "remember.txt": 
            """
            I don’t know if anyone’s ever going to read this, but if you do, if we succeeded, then I want you to know that Alexandra stayed 
            until the last moment. I’m leaving, too tired, too broken, desperate for a few moments of peace with my remaining loved ones. 
            But she’s still there, and she won’t give up. And yes, there are thousands like her all over the world, giving everything they 
            have because they believe in humanity... but she’s the one that I know, as a real person, a colleague, a friend. I know that she 
            likes peanut ice cream and hates strawberry, that her favorite band is Pink Floyd, that her favorite poet is Blake, that her 
            favorite TV show is Futurama, that she studied at Cornell, that her dad’s name was Carl, that her mom’s name was 
            54 6F 20 74 68 6F 73 65 20 77 68 6F 20 64 77 65 6C 6C. I don’t know if I should be ashamed for leaving, but I know that I’m proud 
            of her. She was the best of us. Remember her. 69 6E 20 72 65 61 6C 6D 73 20 6F 66 20 64 61 79."""
    }

foundtexts_H1 = {
        "human_eye.txt": 
            """
            What is a man’s eye but a machine for the little creature that
            sits behind in his brain to look through? [ARCHIVE: 1872CE-F553]
            [BUTLER, SAMUEL] 65 76 65 72 79 74 68 69 6E 67 20 77 6F 75 6C 64
            20 61 70 70 65 61 72 20 74 6F 20 6D 61 6E 20 61 73 20 69 74 20 69
            73
            Is it man’s eyes, or is it the big seeing-engine which has
            revealed to us the existence of worlds beyond worlds into
            infinity? What has made man familiar with the scenery of the moon,
            the spots on the sun, or the geography of the planets? He is at
            the mercy of the seeing-engine for these things, and is powerless
            unless he tacks it on to his own identity, and make it part and
            parcel of himself.
            C08 human_eye.txt						 lit_arch 1872 CE""",
        
        "tetromino.html": 
            """
            One of the most fascinating aspects of St. Eadwald’s recently-
            uncovered writings is his preoccupation with finding divine truth
            in mathematical concepts, which at times borders on pantheism.
            He was, it would seem, particularly concerned with what we
            now call tetrominoes, seeing in them a reflection of the
            tetragrammaton and the Greek word for God (TH-E-O-S). Their
            ability to form other shapes out of themselves symbolized to him
            the Creator’s ability to reshape the world without breaking the
            laws He himself had established.
            Eadwald referred to tetrominoes as “sigilla” (sigils), implying
            that they were a more truthful version of the magical symbols
            worshipped by heathens, rooted in both the Abrahamic tradition
            and careful observation of Creation.
            It is unlikely that these texts were distributed, as they would
            almost certainly have resulted in charges of heresy.
            tetromino.html 						 mdv_th 2030/06/14101""",
        
        "preservation.txt": 
            """
            I viewed, with a mixture of pity and horror, these beings
            training to be sold to slaughter, or be slaughtered, and fell
            into reflections on an old opinion of mine, that it is the
            preservation of the species, not of individuals, which appears
            to be the design of the Deity throughout the whole of Nature.
            Blossoms come forth only to be blighted; fish lay their spawn
            where it will be devoured; and what a large portion of the human
            race are born merely to be swept prematurely away! 156C(6966#6520
            697 (3 206D6F72 6D6F 657265 206C6966666F6E2073 6F206C616E 20 6C
            6465 206F 766572 207072656A206469 6E65 206D6F726E 207374
            62617460616E
            Does not this waste of budding life emphatically assert that it
            is not men, but Man, whose preservation is so necessary to the
            completion of the grand plan of the universe? Children peep into
            existence, suffer, and die; men play like moths about a candle,
            and sink into the flame; war, and “the thousand ills which flesh
            is heir to,” mow them down in shoals; whilst the more cruel
            prejudices of society palsy existence, introducing not less sure
            though slower decay.
            preservation.txt						 phil_arc 1796 CE"""
    }

foundtexts_H2 = {
        "human_blood.txt": 
            """
            It is said by some that our blood is composed of infinite living
            agents which go up and down the highways and byways of our
            bodies as people in the streets of a city. &/Ecc1 41 6E 64 20 74
            68 65 20 57 6F 72 64 One generation passeth away, and another
            generation cometh: but the earth abideth for ever. function(#7761
            7320 6D61 6465 20 66 6C 65 73 68
            ) And the sleep of the town, how life-like! with its change in
            the circulation.
            [BUTLER, SAMUEL]
            We are misled by considering any complicated machine as a single
            thing; in truth it is a city or society, each member of which was
            bred truly after its kind.
            human_blood.txt						 lit_arch 1872 CE""",
        
        "archive_IMPORTANT.eml": 
            """
            From: Arkady Chernyshevsky, Univ& [error 4731 3A3236/
            To: [504 recipients]
            Subject: Archive
            I’ll keep this short. You all know me, so you know that I know
            what I’m talking about.
            I realize that you’re all working on projects meant to somehow
            avert the catastrophe we are facing. But you must all concede
            that there is a very real possibility that you will not have
            enough time to find a solution.
            I believe that we *cannot* afford to ignore an extinction or
            near-extinction scenario. We *must* prepare for the worst. That
            is to say, we must seek to preserve the non-biological components
            of what constitutes the human species, in the hope they be
            recovered in the future by other (local or non-local) sentients.
            I know that we are not used to thinking on that scale - not
            in terms of praxis - but if we truly value humanity, then we
            must act immediately. You’ll find the details of my proposal in
            the attachment, but the short version is this: the creation of
            multiple archives (for redundancy) in safe locations that will
            contain, in digital form, as much information about our species
            (including all cultural works, scientific insights, history, DNA)
            as can be gathered in the given timeframe. This will be massive,
            global undertaking, §G%2/1&% with EL naturally being one of the %$
            /// ERROR: CANNOT FIND ATTACHMENT ///
            archive_IMPORTANT.eml				 EP_arch 0000/06/03""",
    }

foundtexts_H3 = {
        "orangutan.html": 
            """
            A medical journal has published a startling new theory about
            last year’s sudden, shocking extinction of the orangutan [see
            our award-winning video of the last orangutan at this link].
            They suggest that the virus responsible was not a new mutation,
            but a very old one - an ancient virus buried until now in high-
            latitude permafrost, set free by global warming. The virus may
            have plagued the ancestors of the modern great apes more than one
            hundred thousand years ago.
            Several important questions remain unanswered, including &$%§&
            /// ERROR /// more importantly, the study suggests that, based
            on samples taken from locations around the globe, the &$&
            incubation period may ///
            If you liked this article, you may also like:
            * How To Really Avoid Heart Attacks
            * You Won’t Believe What’s Living Under This Rock
            * Top Ten Amazing Science Facts
            * Oscars Nip Slip Explained By Physics (video)
            * How To Easily Beat Any Infection (sponsored link)
            orangutan.html					 webcrawl 9999/12/24""",
        
        "blake_archive_793.html": 
            """
            <img src="plate11.png">
            The ancient Poets animated all sensible objects with Gods or
            Geniuses, calling them by the names and adorning them with the
            properties of woods, rivers, mountains, lakes, cities, nations,
            and whatever their enlarged & numerous senses could perceive.
            And particularly they studied the genius of each city & country,
            placing it under its mental deity.
            Till a system was formed, which some took advantage of & enslav’d
            the vulgar by attempting to realize or abstract the mental
            deities from their objects; thus began Priesthood.
            Choosing forms of worship from poetic tales.
            And at length they pronounced that the gods had orderd such
            things.
            Thus men forgot that All deities reside in the human breast.
            blake_archive_793.html				 webcrawl 2022/12/16""",
        
        "usernames.eml": 
            """
            From: George Jameson
            To: IAN Mailing List
            Subject: RE: Usernames
            It’s, uh, working now. Each iteration is assigned its own unique
            name drawn randomly from the database. At the moment, that’s a
            database of online gaming handles, which does sound a bit odd...
            but I honestly don’t think we should spend more time on this. We
            have unique identifiers, so we’re fine. More than that is a luxury
            we can’t afford.
            If we should happen to have everything else finished on time, I’ll
            go back and generate a new database with more appropriate names.
            Right now it just can’t be a priority.
            - George
            usernames.eml						 loc 0000/09/03""",
    }

enter_A = "As the light dissipates, you find yourself in another setting made of ancient ruins resembling ancient mediterranean culture."
exit_A = "You step on the circle and enter the blinding bright flash of light. You find yourself again in the temple, and you go on with the exploration of the next level."

enter_B = "As the light dissipates, you find yourself in another desert, surrounded by sand. You see some palms and some egiptian structures."
exit_B = "You step on the circle and enter the blinding bright flash of light. You find youself again in the tomb, and you go on with the exploration of the next level."

enter_C = "As the light dissipates, you find yourself in another beautiful garden surrounded by ruins of walls made of stone blocks resembling medieval castles."
exit_C = "You step on the circle and enter the blinding bright flash of light. You find youself again in the cathedral, and you go on with the exploration of the next level."
    