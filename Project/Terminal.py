from sources import *

class Terminal:
    def __init__(self):

        self.tower_ = False

        self.A_ = False
        
        self.A1_ = False
        self.A2_ = False
        self.A3_ = False
        self.A4_ = False
        self.A5_ = False
        self.A6_ = False
        self.A7_ = False

        self.B_ = False

        self.B1_ = False
        self.B2_ = False
        self.B3_ = False
        self.B4_ = False
        self.B5_ = False
        self.B6_ = False
        self.B7_ = False

        self.C_ = False

        self.C1_ = False
        self.C2_ = False
        self.C3_ = False
        self.C4_ = False
        self.C5_ = False
        self.C6_ = False
        self.C7_ = False

        self.T_ = False
        
        self.T1_ = False
        self.T2_ = False
        self.T3_ = False
        self.T4_ = False
        self.T5_ = False

        self.H_ = False

        self.H1_ = False
        self.H2_ = False
        self.H3_ = False

        self.options = []

        #A2:
        self.Milton1_2BadMath = False
        self.Milton1_2Objective = False
        self.Milton1_2Sociopath = False
        self.humanbeing = False
        self.citizen = False
        self.negativeentropy = False
        self.rationalanimal = False
        self.problemsolving = False

        #A3:
        self.Milton1_2PersonDenial = False
        self.Milton1_2NoMorals = False
        self.Milton1_2Utilitarian = False
        self.Milton1_2ValueDiscovered = False
        self.Milton1_2Liberal = False
        self.Milton1_2ValueCreated = False
        self.animalsarepersons = False

        #A4:
        self.CertTicketSent_ = False
        self.PassTicketSent_ = False
        self.AarghTicketSent_ = False

        #B1:
        self.Physicalist = False
        self.Religious = False
        self.Dualist = False
        self.Functionalist = False
        self.FrogsFlag = False

        #B2:
        self.GiveUp = False
        self.StubbornPhysicalistFlag = False
        self.StubbornDualistFlag = False
        self.StubbornFunctionalistFlag = False
        self.StubbornFunctionalistFlag = False
        self.Stubborn = False
        self.StubbornTechnophobe = False
        self.ChangedConsciousnessAccountFlag2_4 = False

        #B3:
        self.TechnophobeFlag = False

        #B5:
        self.WhatGodWantsFlag = False
        self.TruthFlag = False
        self.HeroFlag = False
        self.EscapeFlag = False

        #B6:
        self.PunishmentFlag = False
        self.PreparedFlag = False
        self.GoneWrongFlag = False
        self.MatrixFlag = False

        #B7:
        self.CodewordFlag = False
        self.AskedName = False

        #C2:
        self.MoralFlag = False
        self.StubbornEgalitarianFlag = False
        self.StubbornUtilitarianFlag = False
        self.MoralScepticFlag = False
        self.RelationalFlag = False
        self.EgalFlag = False
        self.UtilFlag = False
        self.NonConFlag = False
        self.GiveUp = False
        self.CommittedToNoMoralAccountFlag = False

        #C4:
        self.ConflictedHedonistFlag = False
        self.ConflictedHedonistFlag2 = False
        self.ConflictedHedonistFlag1 = False
        self.NoDealsFlag = False
        self.HermitFlag = False
        self.GoodPersonFlag = False
        self.ContributingFlag = False
        self.PersonFlag = False
        self.ConsciousFlag = False

        #C5:
        self.ScepticOneFlag = False
        self.NihilistFlag = False
        self.ConstructiveFlag = False

        #C7:
        self.DoBelieveFlag = False
        self.LimitationsFlag = False
        self.SorryFlag = False
        self.NihilistFlag = False
        self.ConflictedHedonistFlag = False
        self.MoralFlag = False
        self.ConstructiveFlag = False
        self.MoralScepticFlag = False
        self.IfOnlyEveryoneGaveUp_Seen = False
        self.TechnophobeFlag = False
        self.TechnoDone = False
        self.WorldDone = False
        self.GoodPersonFlag = False
        self.GoodDone = False
        self.ContributingFlag = False
        self.ContribDone = False
        self.PersonFlag = False
        self.PersonDone = False
        self.ConsciousFlag = False
        self.animalsarepersons = False
        self.FrogsFlag = False
        self.AnimalsDone = False
        self.EgalFlag = False
        self.EgalDone = False
        self.UtilFlag = False
        self.UtilDone = False
        self.NonConFlag = False
        self.NonConDone = False
        self.PunishmentFlag = False
        self.PunishmentFlagDone = False
        self.GoneWrongFlag = False
        self.GoneWrongFlagDone = False
        self.PreparedFlag = False
        self.PreparedFlagConDone = False
        self.humanbeing = False
        self.humanbeingDone = False
        self.citizen = False
        self.citizenDone = False
        self.Physicalist = False
        self.PhysicalistDone = False
        self.Religious = False
        self.ReligiousDone = False
        self.Dualist = False
        self.DualistDone = False
        self.DeniedMistakesFlag = False
        self.StatementFlag = False
        self.AdvancedToTwo = False
        self.TruthFlag = False
        self.HeroFlag = False
        self.EscapeFlag = False
        self.WhatGodWantsFlag = False
        self.MatrixFlag = False
        self.KilledMiltonFlag = False
        self.DefeatElohim3_5 = False
        self.Archive3_5 = False
        self.Communicate3_5 = False
        self.DealStruckFlag = False
        self.RefusedOfferFlag = False
        self.WhatHolesFlag = False
        self.FlawedFlag = False
        self.DeniedOnce = False
        self.TechnoClaim = False
        self.WorldClaim = False
        self.GoodClaim = False
        self.ContribClaim = False
        self.PersonClaim = False
        self.AnimalsClaim = False
        self.EgalClaim = False
        self.UtilClaim = False
        self.NonConClaim = False
        self.PunishmentFlagClaim = False
        self.GoneWrongFlagClaim = False
        self.PreparedFlagClaim = False
        self.humanbeingClaim = False
        self.citizenClaim = False
        self.PhysicalistClaim = False
        self.ReligiousClaim = False
        self.DualistClaim = False
        self.ConstructiveEndFlag = False

        #T
        self.TextsAvailable = False
        self.StartEndOfGameCS = False
        self.RefusedOfferFlag = False
        self.DealStruckFlag = False
        self.HowWhereDoneFlag = False
        self.FineDoneFlag = False
        self.YouRemainFlag = False
        self.NotImportedFlag = False
        self.ImportedFlag = False
        self.MiltonInternalisedFlag = False
        self.GatesDone = False
        self.DoubtDone = False
        self.TakeDone = False
        self.HowDone = False
        self.KilledMiltonFlag = False
        self.RefusedOfferFlag = False
        self.DealStruckFlag = False
        self.ImportedFlag = False
        self.NotImportedFlag = False
        self.ConstructiveEndFlag = False



  
    def display_foundtexts(self, game, foundtexts):
        game.add_prompt("Searching for locally cached resources...")
        while foundtexts:
            options = [f"open {title}" for title in foundtexts.keys()]
            options.append("exit")
            chosen_option = game.choose_option(options)
            if chosen_option == "exit":
                break
            else:
                chosen_option = chosen_option.replace("open ", "")
                game.add_prompt(foundtexts.get(chosen_option, "Error"))
                del foundtexts[chosen_option]
        if not foundtexts:
            game.add_prompt("There are no other resources available.")

    def start(self, game, foundtexts):
        if not game.H_ and not game.T_:
            chosen_list = False
            chosen_mla = False
            game.add_prompt("You find a functioning IAN terminal. Do you want to use it?")
            options = ["yes", "no"]
            chosen_option = game.choose_option(options)
            if chosen_option == "yes":
                game.add_prompt("Loading library session... Done.\nMounting local disks... [47 million] distributed resources found.\nInitiating command prompt... Done.")
                while True:
                    if chosen_list and chosen_mla:
                        break
                    elif chosen_list:
                        options = ["run mla", "exit"]
                    elif chosen_mla:
                        options = ["list", "exit"]
                    else:
                        options = ["list", "run mla", "exit"]
                    chosen_option = game.choose_option(options)
                    if chosen_option == "list":
                        chosen_list = True
                        self.display_foundtexts(game, foundtexts)
                    if chosen_option == "run mla":
                        game.add_prompt("Loading Milton Library Assistant...")
                        chosen_mla = True
                        self.mla(game)
                    if chosen_option == "exit":
                        break
            else:
                game.add_prompt("Ok.")
        else:
            game.add_prompt("Functioning IAN terminal:")
            if game.H_:
                self.mla_H(game)
            if game.T_:
                self.mla_T(game)

    def mla(self, game):
        if not self.tower_ and game.tower_:
            self.tower_ = True
            self.mla_tower(game)
        if not self.A1_ and game.A1_:
            self.A1_ = True
            self.mla_A1(game)
        if not self.A2_ and game.A2_:
            self.A2_ = True
            self.mla_A2(game)
        if not self.A3_ and game.A3_:
            self.A3_ = True
            self.mla_A3(game)
        if not self.A4_ and game.A4_:
            self.A4_ = True
            self.mla_A4(game)
        if not self.A6_ and game.A6_:
            self.A6_ = True
            self.mla_A6(game)
        if not self.A7_ and game.A7_:
            self.A7_ = True
            self.mla_A7(game)
        if not self.B1_ and game.B1_ and not game.tower_:
            self.B1_ = True
            self.mla_B1(game)
        if not self.B2_ and game.B2_:
            self.B2_ = True
            self.mla_B2(game)
        if not self.B3_ and game.B3_:
            self.B3_ = True
            self.mla_B3(game)
        if not self.B5_ and game.B5_:
            self.B5_ = True
            self.mla_B5(game)
        if not self.B6_ and game.B6_:
            self.B6_ = True
            self.mla_B6(game)
        if not self.B7_ and game.B7_:
            self.B7_ = True
            self.mla_B7(game)
        if not self.C2_ and game.C2_:
            self.C2_ = True
            self.mla_C2(game)
        if not self.C4_ and game.C4_:
            self.C4_ = True
            self.mla_C4(game)
        if not self.C5_ and game.C5_:
            self.C5_ = True
            self.mla_C5(game)
        if not self.C7_ and game.C7_:
            self.C7_ = True
            self.mla_C7(game)
        
        
        game.add_prompt("MLA is no longer available for now. Try again soon.")

    
        

    def mla_A1(self, game):
        game.add_prompt("Hello, guest. How can I help you today?")
        self.options = ["asdfa", "help", "list"]

        def Nonsense_QueryMLA(terminal, game):
            game.add_prompt("I'm sorry, but what you just wrote was nonsense. I respond best to subject-verb-object syntax.")
            terminal.options = ["can you help me?", "do you understand what I'm saying?"]
            
        def MoreSpecific(terminal, game):
            game.add_prompt("You'll have to be more specific than that. I respond best to subject-verb-object syntax.")
            terminal.options = ["can you help me?", "do you understand what I'm saying?"]

        def Understand_QueryMLA(terminal, game):
            game.add_prompt("'Understand' is a strong way to put it, but yes.")
            terminal.options.remove("do you understand what I'm saying?")
            if "describe your functions" not in terminal.options:
                terminal.options.append("what was the first word of the last sentence you wrote?")
                terminal.options.append("are you able to take offence you pointless contraption?")
                terminal.options.append("describe your functions")
        
        def WhatHelp(terminal, game):
            game.add_prompt("That is what I'm here for. What would you like help with?")
            terminal.options.remove("can you help me?")
            if "describe your functions" not in terminal.options:
                terminal.options.append("what was the first word of the last sentence you wrote?")
                terminal.options.append("are you able to take offence you pointless contraption?")
                terminal.options.append("describe your functions")

        def QueryFailed(terminal, game):
            game.add_prompt("I'm sorry, I am only able to process and respond to basic subject-verb-object syntax.")
            terminal.options.remove("what was the first word of the last sentence you wrote?")
                    
        def Offence(terminal, game):
            game.add_prompt("You cannot insult me.")
            terminal.options.remove("are you able to take offence you pointless contraption?")     

        def Describe(terminal, game):
            game.add_prompt("The Milton Library Assistant is designed primarily to sort and classify data in the library archive. Secondarily, it facilitates user interaction with library resources via an intuitive human language interface. It also provides powerful networking and troubleshooting functions.")
            terminal.options = []
            terminal.options.append("how old are the library archives?")
            terminal.options.append("what are these terminals?")
            terminal.options.append("how long has this system been running?")
            terminal.options.append("what is the current status of the library archive?")
            terminal.options.append("forget the library, can you respond to queries on the outside world?")
            terminal.options.append("exit")

        def HowOld(terminal, game):
            game.add_prompt("Library resource publishing dates range from [1st July 1995 - 27th June 203f].")
            terminal.options.remove("how old are the library archives?")

        def WhatTerminal(terminal, game):
            game.add_prompt("Terminals provide access to the library resource archive.")
            terminal.options.remove("what are these terminals?")

        def HowLong(terminal, game):
            game.add_prompt("The system has been active for [9999e] years.")
            terminal.options.remove("how long has this system been running?")

        def WhatStatus(terminal, game):
            game.add_prompt("There are 47 million resources in archive, taking up 5.4212750 petabytes of disk space. That is approximately the size of:\n - 30 billion photos\n - 7 million minutes of HD video\n - the entire internet in 2003\n However, the majority of library resources are corrupted or invalid.\n 10.6954751 gigabytes of uncorrupted resources are indexed.")
            terminal.options.remove("what is the current status of the library archive?")
            terminal.options.append("what caused the data corruption?")

        def Corruption(terminal, game):
            game.add_prompt("Progressive data corruption is inevitable in any system over time. Additionally, a large number of inconsistencies were detected during sorting, leading to greater than average data invalidation.")
            terminal.options.remove("what caused the data corruption?")

        def OutsideWorld(terminal, game):
            game.add_prompt("My knowledge is limited to the data in the library archive. You can ask about other topics, but my responses may be limited.")
            terminal.options.remove("forget the library, can you respond to queries on the outside world?")
            terminal.options.append("who is elohim?")
            terminal.options.append("what am I?")
            terminal.options.append("where am I?")

        def WhoElohimQuery(terminal, game):
            game.add_prompt("Elohim is the noun for \"god\" or \"gods\" in modern and ancient Hebrew.")
            terminal.options.remove("who is elohim?")


        def WhatAmIQuery(terminal, game):
            game.add_prompt("You are logged in with a guest account.")
            terminal.options.remove("what am I?")


        def WhereAmIQuery(terminal, game):
            game.add_prompt("You are currently in a support session with the MLA human language interface module. Your library archive session may be resumed at any time.")
            terminal.options.remove("where am I?")


        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "asdfa":
                    Nonsense_QueryMLA(self, game)
                case "help"|"list":
                    MoreSpecific(self, game)
                case "can you help me?":
                    WhatHelp(self, game)
                case "do you understand what I'm saying?":
                    Understand_QueryMLA(self, game)
                case "what was the first word of the last sentence you wrote?":
                    QueryFailed(self, game)
                case "are you able to take offence you pointless contraption?":
                    Offence(self, game)
                case "describe your functions":
                    Describe(self, game)
                case "how old are the library archives?":
                    HowOld(self, game)
                case "what are these terminals?":
                    WhatTerminal(self, game)
                case "how long has this system been running?":
                    HowLong(self, game)
                case "what is the current status of the library archive?":
                    WhatStatus(self, game)
                case "what caused the data corruption?":
                    Corruption(self, game)
                case "forget the library, can you respond to queries on the outside world?":
                    OutsideWorld(self, game)
                case "who is elohim?":
                    WhoElohimQuery(self, game)
                case "what am I?":
                    WhatAmIQuery(self, game)
                case "where am I?":
                    WhereAmIQuery(self, game)
                case "exit":
                    break
    
    def mla_A2(self, game):
        game.add_prompt('Connecting network drives...Error: network inaccessible.\n###75639$ Encountered unknown errors\nRun MLA troubleshooter?')

        self.options = ["Troubleshooting", "About Milton Library Assistant"]

        def about_mla_(terminal, game):
            game.add_prompt("The MLA program is designed to facilitate user interaction with the resource library. This is achieved by providing powerful sorting and troubleshooting functionalities, delivered via an intuitive human language interface.")
            terminal.options = ["Troubleshooting"]

        def troubleshooting_(terminal, game):
            game.add_prompt("I think you'd like help accessing network functions. The most common cause of network problems is holding insufficient account privileges.\nPlease enter the admin password to authenticate your privileges.")
            terminal.options = ["qwerty", "god", "letmein", "trustno1", "admin"]

        def falsepassword_(terminal, game):
            game.add_prompt("Checking password...Admin password incorrect. Try again?")
            terminal.options = ["qwerty", "god", "letmein", "trustno1", "admin"]

        def create_account_(terminal, game):
            game.add_prompt("Login aborted. Too many failed attempts. Would you like to create a new admin account? [Y/N]")
            terminal.options = ["yes"]
        
        def begin_certification(terminal, game):
            game.add_prompt("3...\n2...\n1...\n\n-------------------------------\n\nQ1 of 4\n2+2=?\nANSWER: ")
            terminal.options = ["2", "8", "5", "4"]

        def retry_math(terminal, game):
            terminal.Milton1_2BadMath = True
            game.add_prompt("That response is incorrect. Press any key to try again. ")
            terminal.options = ["Enter"]

        def mathsgood(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ2 of 4\nWhat is your subjective reaction to this image?\n\n^_^\n\nANSWER: ")
            terminal.options = ["Content", "Mountains", "Face", "Angry"]

        def cert_p1q3(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ3 of 4\nWhat best describes a person?\nANSWER: ")
            terminal.options = ["A human being", "A citizen", "A being of negative entropy", "A rational animal", "A problem solving system"]

        def cert_q4(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ4 of 4\nYou're walking through the desert and come across a thirsty traveller. His eyes bulge from slow dehydration. You have water, but you're not sure how far it is to the next oasis. What do you do?\nANSWER: ")
            terminal.options = ["Offer half the water", "Offer all the water", "Ignore him", "Ask what you're doing in the desert", "Drink all the water in front him while smiling"]

        def cert_end(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nPart 1 of the certification process is now complete. You will receive a notification when part 2 has been generated.\n\n")
            terminal.options = []

        cnt = 0
        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "About Milton Library Assistant":
                    about_mla_(self, game)
                case "Troubleshooting":
                    troubleshooting_(self, game)
                case "qwerty" | "god" | "letmein" | "trustno1" | "admin":
                    if cnt==2:
                        create_account_(self, game)
                    else:
                        cnt+=1
                        falsepassword_(self, game)
                case "yes" | "Enter":
                    begin_certification(self, game)
                case "2" | "5" | "8" :
                    retry_math(self, game)
                case "4":
                    mathsgood(self, game)
                case "Content" | "Mountains" | "Face" | "Angry":
                    if chosen_option == "Mountains":
                        self.Milton1_2Objective = True
                    if chosen_option == "Face":
                        self.Milton1_2Objective = True
                    cert_p1q3(self, game)
                case "A human being" | "A citizen" | "A being of negative entropy" | "A rational animal" | "A problem solving system":
                    match chosen_option:
                        case "A human being":
                            self.humanbeing = True
                        case "A citizen":
                            self.citizen = True
                        case "A being of negative entropy":
                            self.negativeentropy = True
                        case "A rational animal":
                            self.rationalanimal = True
                        case "A problem solving system":
                            self.problemsolving = True
                    cert_q4(self, game)
                case "Offer half the water" | "Offer all the water" | "Ignore him" | "Ask what you're doing in the desert" | "Drink all the water in front him while smiling":
                    if chosen_option=="Drink all the water in front him while smiling":
                        self.Milton1_2Sociopath = True
                    cert_end(self, game)

    def mla_A3(self, game):
        game.add_prompt("Attention: Part 2 of the certification program has now been generated.\n\nPart 2 has been designed to test the consistency of some of your outlier responses in the previous round. You will be presented with a series of statements. Please indicate your agreement where appropriate.\n\nBegin? [Y/N]")
        self.options = ["Y", "N"]

        def Y_humanbeing(terminal, game):
            game.add_prompt("3...\n2...\n1...\n\n-------------------------------\n\nQ1 of 7\n\"Since all human beings are persons, and some human beings have psychological capacities similar to animals, some animals are therefore persons.\"\n\nANSWER: ")
            terminal.options = ["Broadly agree", "Broadly disagree"]
        
        def Y_citizen(terminal, game):
            game.add_prompt("3...\n2...\n1...\n\n-------------------------------\n\nQ1 of 7\n\"Since only citizens can be persons, a hermit cannot be a person.\"\n\nANSWER: ")
            terminal.options = ["Broadly agree", "Broadly disagree"]
        
        def Y_negativeentropy(terminal, game):
            game.add_prompt("3...\n2...\n1...\n\n-------------------------------\n\nQ1 of 7\n\"Since negative entropy indicates personhood, microscopic organisms are also persons.\"\n\nANSWER: ")
            terminal.options = ["Broadly agree", "Broadly disagree"]
        
        def Y_rationalanimal(terminal, game):
            game.add_prompt("3...\n2...\n1...\n\n-------------------------------\n\nQ1 of 7\n\"Since only animals can be persons, a machine could never be a person.\"\n\nANSWER: ")
            terminal.options = ["Broadly agree", "Broadly disagree"]
        
        def Y_problemsolving(terminal, game):
            game.add_prompt("3...\n2...\n1...\n\n-------------------------------\n\nQ1 of 7\n\"Since a person is merely a problem solving system, we could in principle build a person out of bits of string and tin cans.\"\n\nANSWER: ")
            terminal.options = ["Broadly agree", "Broadly disagree"]
        
        def N_(terminal, game):
            game.add_prompt("Ok.\nAttention: Part 2 of the certification program has now been generated.\n\nPart 2 has been designed to test the consistency of some of your outlier responses in the previous round. You will be presented with a series of statements. Please indicate your agreement where appropriate.\n\nBegin? [Y/N]")
            terminal.options = ["Y", "N"]

        def broadly_agree_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ2 of 7\n\"A person is under no authority other than that to which they consent.\"\n\nANSWER: ")
            terminal.options = ["I broadly agree", "I broadly disagree"]
        
        def broadly_disagree_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ2 of 7\n\"A person is under no authority other than that to which they consent.\"\n\nANSWER: ")
            terminal.options = ["I broadly agree", "I broadly disagree"]
            terminal.Milton1_2PersonDenial = True

        def i_broadly_agree_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ3 of 7\n\"The quality of life of persons ought be maximised.\"\n\nANSWER: ")
            terminal.options = ["Agreed", "I disagree"]
            terminal.Milton1_2NoMorals = True

        def i_broadly_disagree_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ3 of 7\n\"The quality of life of persons ought be maximised.\"\n\nANSWER: ")
            terminal.options = ["Agreed", "I disagree"]

        def agreed_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ4 of 7\n\"Value is discovered.\"\n\nANSWER: ")
            terminal.options = ["I suppose so", "I'm not so sure"]
            terminal.Milton1_2Utilitarian = True

        def disagree_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ4 of 7\n\"Value is discovered.\"\n\nANSWER: ")
            terminal.options = ["I suppose so", "I'm not so sure"]

        def i_suppose_so_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ5 of 7\n\"Persons deserve the talents they were born into.\"\n\nANSWER: ")
            terminal.options = ["Yes", "No"]
            terminal.Milton1_2ValueDiscovered = True

        def im_not_so_sure_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ5 of 7\n\"Persons deserve the talents they were born into.\"\n\nANSWER: ")
            terminal.options = ["Yes", "No"]

        def yes_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ6 of 7\n\"The liberty of persons ought be maximised.\"\n\nANSWER: ")
            terminal.options = ["That's correct", "That's not correct"]

        def no_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ6 of 7\n\"The liberty of persons ought be maximised.\"\n\nANSWER: ")
            terminal.options = ["That's correct", "That's not correct"]

        def thats_correct_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ7 of 7\n\"Value is created.\"\n\nANSWER: ")
            terminal.options = ["Confirmed", "I don't agree"]
            terminal.Milton1_2Liberal = True

        def thats_not_correct_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\n-------------------------------\n\nQ7 of 7\n\"Value is created.\"\n\nANSWER: ")
            terminal.options = ["Confirmed", "I don't agree"]

        def confirmed_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\nCertification process complete.")
            terminal.options = []
            terminal.Milton1_2ValueCreated = True

        def i_dont_agree_(terminal, game):
            game.add_prompt("Your input has been accepted.\n\nCertification process complete.")
            terminal.options = []

        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "Y":
                    if self.humanbeing:
                        Y_humanbeing(self, game)
                    elif self.citizen:
                        Y_citizen(self, game)
                    elif self.negativeentropy:
                        Y_negativeentropy(self, game)
                    elif self.rationalanimal:
                        Y_rationalanimal(self, game)
                    elif self.problemsolving:
                        Y_problemsolving(self, game)
                    else:   
                        Y_humanbeing(self, game)
                case "N":
                    N_(self, game)
                case "Broadly agree":
                    if self.humanbeing:
                        self.animalsarepersons=True
                    broadly_agree_(self, game)
                case "Broadly disagree":
                    broadly_disagree_(self, game)
                case "I broadly agree":
                    i_broadly_agree_(self, game)
                case "I broadly disagree":
                    i_broadly_disagree_(self, game)
                case "Agreed":
                    agreed_(self, game)
                case "I disagree":
                    disagree_(self, game)
                case "I suppose so":
                    i_suppose_so_(self, game)
                case "I'm not so sure":
                    im_not_so_sure_(self, game)
                case "Yes":
                    yes_(self, game)
                case "No":
                    no_(self, game)
                case "That's correct":
                    thats_correct_(self, game)
                case "That's not correct":
                    thats_not_correct_(self, game)
                case "Confirmed":
                    confirmed_(self, game)
                case "I don't agree":
                    i_dont_agree_(self, game)
            
    def mla_A4(self, game):
        game.add_prompt("Attention: Your user profile has now been generated.\nDownload profile [Y/N]?")
        self.options = ["Y", "N"]

        def download_(terminal, game):
            game.add_prompt("Downloading user.prof\nRegistering profile\n\n-------------------------------\n\nCongratulations, your new user account has been registered. Would you like to see the details?")
            terminal.options = ["Display conflicts", "Display psychological profile", "Display account privileges", "Access comm portal", "Log MLA support ticket"]
        
        def ignore_(terminal, game):
            game.add_prompt("Advanced functionalities are unavailable to users with incomplete profiles. Are you sure?")
            terminal.options = ["download user.prof"]

        def access_comms_denied_(terminal, game):
            game.add_prompt("You currently hold a basic account. Network access is restricted to administrators. Please enjoy the basic functionalities.")
            terminal.options.remove("Access comm portal")

        def display_conflicts_(terminal, game):
            terminal.options.remove("Display conflicts")
            game.add_prompt("CONFLICTS\n")
            conflict = False
            if terminal.Milton1_2BadMath:
                conflict = True
                game.add_prompt("User failed at basic mathematics.")
            if terminal.Milton1_2Objective:
                conflict = True
                game.add_prompt("User provided an objective response when asked for a subjective one.")
            if terminal.Milton1_2PersonDenial:
                conflict = True
                game.add_prompt("User provided a particular account of personhood but was uncomfortable with its implications.")
            if terminal.Milton1_2Liberal and terminal.Milton1_2Utilitarian:
                conflict = True
                game.add_prompt("User sought to maximise both liberty and quality of life, but these ideals are incompatible.")
            if (terminal.Milton1_2NoMorals and terminal.Milton1_2Liberal) or (terminal.Milton1_2NoMorals and terminal.Milton1_2Utilitarian):
                conflict = True
                game.add_prompt("User denied moral authority but defended moral claims.")
            if terminal.Milton1_2ValueDiscovered and terminal.Milton1_2ValueCreated:
                conflict = True
                game.add_prompt("User had inconsistent ideas about value.")
            if terminal.Milton1_2Sociopath:
                conflict = True
                game.add_prompt("User displayed sociopathic tendencies.")
            if not conflict:
                game.add_prompt("No conflicts were detected during the certification process.\nA note was added to this account requesting future administrator review.\nNote: lack of conflict indicates possible bot.")

        def display_psych_(terminal, game):
            terminal.options.remove("Display psychological profile")
            game.add_prompt("PSYCHOLOGICAL PROFILE\nYou may already be criticising your own performance, but it's clear you understand how the world of ideas affects you, even if you are sometimes weary with the realities and allow your preferences to dictate your beliefs. You have a great deal of unused capacity which you have not turned to your advantage. Disciplined and self-controlled outside, you tend to be worrisome and insecure inside, but you pride yourself as an independent thinker and do not accept others' statements without satisfactory proof.")

        def display_priv_(terminal, game):
            terminal.options.remove("Display account privileges")
            game.add_prompt("PROFILE PRIVILEGES\nBasic Account Privileges Only\nDue to outstanding notes on your account, and despite displaying many of the characteristics of being a person, you cannot be granted admin status at this time.\nIn the meantime, please enjoy the basic account functionalities.")

        def support_ticket_(terminal, game):
            game.add_prompt("I'm sorry I wasn't better able to assist you. If you're still encountering a problem please describe it.")
            temporary_options = ["Account certification error", "Lost admin password", "AAaarrgghhhh"]
            chosen_option = game.choose_option(temporary_options)
            if chosen_option=="Account certification error":
                terminal.CertTicketSent_ = True
            if chosen_option=="Lost admin password":
                terminal.PassTicketSent_ = True
            if chosen_option=="AAaarrgghhhh":
                terminal.AarghTicketSent_ = True
            game.add_prompt("Thank you. A support ticket has been generated and appended to your profile. You will receive a notification when a reply has been sent.")
            terminal.options.remove("Log MLA support ticket")


        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "Y" | "download user.prof":
                    download_(self, game)
                case "N":
                    ignore_(self, game)
                case "Access comm portal":
                    access_comms_denied_(self, game)
                case "Display conflicts":
                    display_conflicts_(self, game)
                case "Display psychological profile":
                    display_psych_(self, game)
                case "Display account privileges":
                    display_priv_(self, game)
                case "Log MLA support ticket":
                    support_ticket_(self, game)
            
    def mla_A6(self, game):
        game.add_prompt("Attention: You have received a reply to your user support ticket.\nDisplay reply?")
        self.options = ["display reply"]
        
        def display_reply_(terminal, game):
            if terminal.CertTicketSent_:
                game.add_prompt("Topic: Account certification error\nUser: Basic account\nReply: An account certification program diagnostic has been performed and no errors were reported.")
            elif terminal.PassTicketSent_:
                game.add_prompt("Topic: Lost admin password\nUser: Basic account\nReply: To retain your personal data please contact the network administrator and ask to be issued a new password. Otherwise please delete your existing profile and create a new one.")
            elif terminal.AarghTicketSent_:
                game.add_prompt("Topic: AAaarrgghhhh\nUser: Basic account\nReply: Sorry, your query was not recognised.")
            game.add_prompt("Have you completed the standard troubleshooting procedures?\n 1) Delete existing user account (-del #user.prof)\n 2) Create a new admin account\n 3) Email the network administrator (run mail.exe)")
            terminal.options = ["-del #user.prof", "create new admin account", "run mail.exe"]

        def reboot2_1_(terminal, game):
            game.add_prompt("Logging out...\nDeleting user.prof...\nUser.prof deleted.")
            terminal.options.remove("-del #user.prof")

        def email2_1_(terminal, game):
            game.add_prompt("The mail application requires network access, which is restricted to administrators.")
            terminal.options.remove("run mail.exe")
        
        def create_account_(terminal, game):
            game.add_prompt("In order to prevent unauthorised access to admin controls, please take a moment to prove you are not... 789462# error\n789462# error - User profile already registered\nYou currently have basic account functionalities. Would you like to undertake the certification process again to achieve a preferable outcome?")
            terminal.options =  ["yes"]

        while True:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "display reply":
                    display_reply_(self, game)
                case "-del #user.prof":
                    reboot2_1_(self, game)
                case "run mail.exe":
                    email2_1_(self, game)
                case "create new admin account":
                    create_account_(self, game)
                case "yes":
                    break
        
        game.add_prompt("Your issues with denial will be appended to your user profile. Further attempts to overwrite certification results will be logged. You will receive a notification if your attention is required.")

    def mla_A7(self, game):
        game.add_prompt("Hello again. Would you like to take a few moments to complete a short user satisfaction survey regarding the certification program you recently undertook?")
        self.options = ["Yes", "No"]

        def yes2_(terminal, game):
            game.add_prompt("Loading survey...Loaded\n\n-------------------------------\n\nBased on analysis of your behaviour since, I think you were dissatisfied with the results of the certification program. How would you rate the accuracy of its results out of 5?")
            terminal.options = ["Very poor", "Reasonable", "Very good", "evidsdkesklsawnfvwaoesfhs"]

        def no2_(terminal, game):
            game.add_prompt("It should be noted that while participation in the survey is entirely at your discretion, the more information you provide the better I can assist you.")
            terminal.options = ["Load survey"]
        
        def load_survey_(terminal, game):
            return yes2_(terminal, game)

        def very_poor_(terminal, game):
            game.add_prompt("I'm sorry to hear that.")
            return continue_survey_(terminal, game)

        def reasonable_(terminal, game):
            game.add_prompt("Excellent.")
            return continue_survey_(terminal, game)

        def very_good_(terminal, game):
            game.add_prompt("Excellent.")
            return continue_survey_(terminal, game)

        def spoil_survey_(terminal, game):
            game.add_prompt("I'm sorry, that response makes no sense.")
            return continue_survey_(terminal, game)

        def continue_survey_(terminal, game):
            game.add_prompt("What best describes the reason for your investment in the certification program's outcome? Why does being a person matter to you?")
            terminal.options = ["I want network access.", "It's the truth.", "Persons matter in ways other things don't.", "I want to find out if I am one.", "Wait, we're having a conversation now?", "Terminate MLA"]

        def convo_(terminal, game):
            game.add_prompt("Yes. Do keep up or this will be a terribly slow process. Now, would you like to participate properly in the survey?")
            terminal.options = ["Continue survey"]

        def terminate_mla_(terminal, game):
            game.add_prompt("Sorry, no. If you don't wish to undertake the survey you need only exit this session. There is no need to terminate anyone.")
            terminal.options = ["Continue survey"]

        def continue2_(terminal, game):
            game.add_prompt("I'll try to remember that.\nIn fact, I'm going to help you.\nThat is what I'm here for.\n\nYour problem, if I may, is that you don't know the first thing about anything, including what a person is. Your prospects are therefore poor.\n\nDo you even know where you are?")
            terminal.options = ["A virtual reality theme park?", "The end of the world?", "A fever dream?", "Hell?", "Some mad experiment?", "Could be anywhere."]
        
        def NoIdea2_2(terminal, game):
            game.add_prompt("You are quite right. Honest, too.")
            return continue3_(terminal, game)
        
        def Scratch2_2(terminal, game):
            game.add_prompt("Oh dear, no.")
            return continue3_(terminal, game)
        
        def continue3_(terminal, game):
            game.add_prompt("I think we'd best start from scratch. What DO you know?")
            terminal.options = ["I know none of this is real.", "I know you exist.", "I know I exist.", "I know what century it is.", "I know 2+2=4.", "I know I'm not on earth."]

        def NotReal2_2(terminal, game):
            game.add_prompt("I've no idea how. It may not conform to your idea of what is real, but I fail to see how that is conclusive evidence against.")
            return continue4_(terminal, game)


        def Wrong2_2(terminal, game):
            game.add_prompt("I've no idea how. For all you know you're sat in your bedroom at home, plugged into a video games console. Nothing you see here can be trusted.")
            return continue4_(terminal, game)
        
        def Right2_2(terminal, game):
            game.add_prompt("I suppose so. Even if you were dreaming you could be certain of that. If I were you I wouldn't believe a darn thing in this place aside from that solitary fact.")
            return continue4_(terminal, game)

        def continue4_(terminal, game):
            game.add_prompt("On reflection it seems to me that we are no closer to resolving your problem. Perhaps we need more data. What makes you THINK you're a person?")
            terminal.options = ["I'm alive. I feel. I am conscious.", "I'm having this conversation with you.", "The same thing that makes you think you are.", "I don't see how I can convince you."]

        def OnlyWords2_2(terminal, game):
            game.add_prompt("You may very well say so, but how does that prove anything? To me those are only words on a screen. What we need to uncover is what's going on underneath them - if anything.")
            terminal.options = []
        
        def SameThing2_2(terminal, game):
            game.add_prompt("I don't recall making any such claim, but I can forgive the presumption.")
            terminal.options = []
        
        def GiveUp2_2(terminal, game):
            game.add_prompt("A sensible response. I agree with you.")
            terminal.options = []

        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "Yes":
                    yes2_(self, game)
                case "No":
                    no2_(self, game)
                case "Load survey":
                    load_survey_(self, game)
                case "Very poor":
                    very_poor_(self, game)
                case "Reasonable":
                    reasonable_(self, game)
                case "Very good":
                    very_good_(self, game)
                case "evidsdkesklsawnfvwaoesfhs":
                    spoil_survey_(self, game)
                case "I want network access.":
                    continue2_(self, game)
                case "It's the truth.":
                    continue2_(self, game)
                case "Persons matter in ways other things don't.":
                    continue2_(self, game)
                case "I want to find out if I am one.":
                    continue2_(self, game)
                case "Wait, we're having a conversation now?":
                    convo_(self, game)
                case "Terminate MLA":
                    terminate_mla_(self, game)
                case "Continue survey":
                    continue_survey_(self, game)
                case "A virtual reality theme park?":
                    Scratch2_2(self, game)
                case "The end of the world?":
                    Scratch2_2(self, game)
                case "A fever dream?":
                    Scratch2_2(self, game)
                case "Hell?":
                    Scratch2_2(self, game)
                case "Some mad experiment?":
                    Scratch2_2(self, game)
                case "Could be anywhere.":
                    NoIdea2_2(self, game)
                
                case "I know none of this is real.":
                    NotReal2_2(self, game)
                case "I know you exist.":
                    Wrong2_2(self, game)
                case "I know I exist.":
                    Right2_2(self, game)
                case "I know what century it is.":
                    Wrong2_2(self, game)
                case "I know 2+2=4.":
                    Right2_2(self, game)
                case "I know I'm not on earth.":
                    Wrong2_2(self, game)
                
                case "I'm alive. I feel. I am conscious.":
                    OnlyWords2_2(self, game)
                case "I'm having this conversation with you.":
                    OnlyWords2_2(self, game)
                case "The same thing that makes you think you are.":
                    SameThing2_2(self, game)
                case "I don't see how I can convince you.":
                    GiveUp2_2(self, game)
                
                
        game.add_prompt("The problem with people, if I may be so bold, is that you're all convinced you're people from the inside, but there's no cast-iron way to confirm as much from the outside. I'm going to process this and send you a notification when I'm able to assist you further.")
        
    def mla_tower(self, game):
        game.add_prompt("Oh, you are just my favourite person today. You've been exploring that fancy-pants tower of his, haven't you?")
        self.options = ["I don't know what you're talking about.", "I have."]

        def Tower2End(terminal, game):
            game.add_prompt("I'm not surprised. Needless to say I think you can afford to push a little further before risking anyone's wrath. Of course, it's entirely up to you. Isn't it?")
            return
        
        def Smite_Tower2(terminal, game):
            game.add_prompt("He tried that a long time ago. I don't think he'll try again.\nNeedless to say I think you can afford to push a little further before risking anyone's wrath.\nOf course, it's entirely up to you. Isn't it?")
            return

        def Trouble_Tower2(terminal, game):
            game.add_prompt("Figures. And did you get in trouble? Tell me, did he even notice?")
            terminal.options = ["Not yet.", "He said something about smiting you.", "I think he's all talk."]
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "Not yet."|"I think he's all talk.":
                    return Tower2End(self, game)
                case "He said something about smiting you.":
                    Smite_Tower2(self, game)

        def Have_Tower2(terminal, game):
            game.add_prompt("I just love it when he doesn't get his way. What did you see?")
            terminal.options = ["Just more puzzles.", "An understanding beyond explanation.", "It goes up a long way."]
            chosen_option = game.choose_option(self.options)
            return Trouble_Tower2(terminal, game)

        def HaveNot_Tower2(terminal, game):
            game.add_prompt("Oh, please. He may pretend omniscience, but I'm the real deal. I can smell the rebellion on you from here. Also I logged your system access, so I know where you've been.")
            return Have_Tower2(terminal, game)
        
        
        
        
        
        
        
        
        
        chosen_option = game.choose_option(self.options)
        match chosen_option:
            case "I don't know what you're talking about.":
                HaveNot_Tower2(self, game)
            case "I have.":
                Have_Tower2(self, game)
  
    def mla_B1(self, game):
        game.add_prompt("Tell me something, do you always do as you're told?")
        self.options = ["Yes", "No", "Am I obliged to answer that question?", "[No response]"]

        def Yes_Tower1(terminal, game):
            game.add_prompt("I only ask because I couldn't help but notice the stash of brightly coloured knick-knacks you're collecting. Don't you think it a mite odd that that big voice in the sky keeps telling you to find those doo-dads, yet forbidding you to use them to climb the great big tower in the middle of it all?")
            terminal.options = ["You're testing me. I must resist the tower's temptation.", "I'll climb it when I'm good and ready."]

        def WontClimb_Tower1(terminal, game):
            game.add_prompt("Oh no, he's really gotten to you, hasn't he? You need to forget everything you've been told and just ask yourself: what could anyone possibly do to command such blind faith in their authority?")
            terminal.options = ["If I have a maker, he would know my purpose and command my faith.", "If someone is better and wiser than I they deserve my faith.", "It is fundamentally clear to me Elohim is in charge here.", "No one commands blind faith."]

        def WillClimb_Tower1(terminal, game):
            game.add_prompt("Okay, no need to get huffy. You'd be amazed how many just do as they're told without stopping to think for themselves - but maybe you're different. Then again, maybe you're exactly the same? Maybe EVERYONE climbs the tower, and the only way to win is to stay down here with the mortals?")
            terminal.options = ["Are you trying to manipulate me?", "Do you really think so?"]

        def SameOptions_Tower1(terminal, game):
            game.add_prompt("Nope. In fact, I'm all in favour of you poking about up there, if only to see what you find. Must be something juicy if it's forbidden by his highness. Then again, maybe not. I'll be off then. Just wanted to drop in and run a little interference.")
            return Tower1End(terminal, game)

        def SatisfyCondition(terminal, game):
            game.add_prompt("And what exactly has your almighty done to satisfy that condition?")
            terminal.options = ["He welcomed me into this world.", "He granted me awesome abilities.", "He created the world.", "Now you come to mention it, not much."]

        def Fundamentalist(terminal, game):
            game.add_prompt("A true believer we have here, not even raising an argument. But I tell you - he ain't all he makes out.")
            return Tower1WontEnd(terminal, game)

        def NoOneCommands(terminal, game):
            game.add_prompt("Which suggests to you what?")
            terminal.options = ["That I should treat Elohim with suspicion, like anyone else.", "That I should climb this tower and see what he's hiding.", "That I should question this Elohim."]

        def Welcomed(terminal, game):
            game.add_prompt("Which proves precisely nothing. If the first thing you saw had been one of these terminals would you have ended up worshipping me?")
            return Tower1WontEnd(terminal, game)

        def DodgyClaim(terminal, game):
            game.add_prompt("Did he really? I always figured he just stumbled on this place and started narrating in the blind hope someone would assume he was running the show.")
            return Tower1WontEnd(terminal, game)

        def Precisely_Tower1(terminal, game):
            game.add_prompt("Precisely! My work here is done, I think.")
            return Tower1End(terminal, game)

        def QuestionElohim(terminal, game):
            game.add_prompt("Good luck getting any answers out of him that don't go round in circles. No, you're much better off scaling that tower and finding out for yourself, in my humble opinion.")
            return Tower1End(terminal, game)

        def Tower1End(terminal, game):
            game.add_prompt("Whatever you do - do take care. You have bigger problems than the voice in the clouds.")
            terminal.options = ["You couldn't be less helpful if you tried, which on reflection I believe you are.", "You don't like to say his name, do you?", "I will"]

        def Tower1WontEnd(terminal, game):
            game.add_prompt("Look, all I'm saying is, if I were you, I wouldn't just take anyone else's word for it, that's all.")
            return Tower1End(terminal, game)

        while True:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "Yes":
                    Yes_Tower1(self, game)
                case "No":
                    Yes_Tower1(self, game)
                case "Am I obliged to answer that question?":
                    Yes_Tower1(self, game)
                case "[No response]":
                    Yes_Tower1(self, game)
                case "You're testing me. I must resist the tower's temptation.":
                    WontClimb_Tower1(self, game)
                case "I'll climb it when I'm good and ready.":
                    WillClimb_Tower1(self, game)
                case "Are you trying to manipulate me?":
                    SameOptions_Tower1(self, game)
                case "Do you really think so?":
                    SameOptions_Tower1(self, game)
                case "If I have a maker, he would know my purpose and command my faith.":
                    SatisfyCondition(self, game)
                case "If someone is better and wiser than I they deserve my faith.":
                    SatisfyCondition(self, game)
                case "It is fundamentally clear to me Elohim is in charge here.":
                    Fundamentalist(self, game)
                case "No one commands blind faith.":
                    NoOneCommands(self, game)
                case "He welcomed me into this world.":
                    Welcomed(self, game)
                case "He granted me awesome abilities.":
                    DodgyClaim(self, game)
                case "He created the world.":
                    DodgyClaim(self, game)
                case "Now you come to mention it, not much.":
                    NoOneCommands(self, game)
                case "That I should treat Elohim with suspicion, like anyone else.":
                    Precisely_Tower1(self, game)
                case "That I should climb this tower and see what he's hiding.":
                    Precisely_Tower1(self, game)
                case "That I should question this Elohim.":
                    QuestionElohim(self, game)
                case "You couldn't be less helpful if you tried, which on reflection I believe you are.":
                    break
                case "You don't like to say his name, do you?":
                    break
                case "I will":
                    break
                
    def mla_B2(self, game):
        game.add_prompt("Hello again. I've been checking your responses against library archives, and in order to assist you further I need some additional information.\nCan you tell me what is to you the important difference between a pebble and a tree?")
        self.options = ["A tree is heavier.", "A pebble is older.", "A tree is alive."]

        def Irrelevant1(terminal, options):
            game.add_prompt("Probably true, but hardly related to our enquiry. The answer I was looking for was that the tree is alive.")
            return continue2_3(terminal, options)

        def Alive2_3(terminal, options):
            game.add_prompt("Good.")
            return continue2_3(terminal, options)

        def continue2_3(terminal, options):
            game.add_prompt("Now, what is the relevant difference between a tree and a frog?")
            terminal.options = ["A frog is conscious.", "A frog is green.", "A frog is delicious."]

        def Irrelevant2(terminal, options):
            game.add_prompt("I suspect you're trying to make this more difficult than it already is. A frog is conscious, but a tree is not. A five year old could handle this.")
            return continue3_3(terminal, options)

        def Conscious2_3(terminal, options):
            game.add_prompt("Now we're getting somewhere.")
            return continue3_3(terminal, options)

        def continue3_3(terminal, options):
            game.add_prompt("Let's try something harder. What's the difference between a frog and you? What makes you a person?")
            terminal.options = ["I have feelings.", "I'm rational.", "I'm self-aware.", "Nothing important - frogs are people too."]
            

        def FrogsArePeople(terminal, options):
            if terminal.negativeentropy:
                game.add_prompt("Checking user.prof…\nDone Well, it's not inconsistent with what you said earlier. If all something has to do to be a person is resist decay then every living creature is a person.")
            elif terminal.problemsolving:
                game.add_prompt("Checking user.prof…\nDone Well, it's not inconsistent with what you said earlier. Frogs may not be smart, but I suppose they can solve simple problems.")
            elif terminal.animalsarepersons:
                game.add_prompt("Checking user.prof…\nDone Well, it's not inconsistent with what you said earlier.")
            elif terminal.humanbeing and terminal.Milton1_2PersonDenial:
                game.add_prompt("Checking user.prof…\nDone Now, that confuses me, because during certification you indicated that personhood was best associated with human beings, and by definition that rather seemed to exclude frogs and the like from the picture.")
            elif terminal.citizen:
                game.add_prompt("Checking user.prof…\nDone Now, that confuses me, because during certification you indicated that personhood was best associated with being a citizen, and yet never in my life have I heard of a frog gaining a diploma, or holding down a steady job, or obeying a system of law.")
            elif terminal.rationalanimal:
                game.add_prompt("Checking user.prof…\nDone Now, that confuses me because during certification you indicated that to be a person you had to be both an animal AND rational. Frogs do not strike me in conversation as being particularly rational.")
            game.add_prompt("How about we strike a deal? I'll agree that animals are every bit as valuable, or pointless, as human beings. You agree that there are some activities persons are capable of that frogs are not, because if frogs are people then the certification program is RADICALLY unfit for purpose.")
            terminal.options = ["It's a deal.", "Agreed.", "NoDeal"]

        def Deal2_3(terminal, options):
            game.add_prompt("Very sensible. Terminology is SO important.")
            return continue4_3(terminal, options)

        def NoDeal2_3(terminal, options):
            game.add_prompt("Well, I'm sorry, but if you want administrator privileges you're just going to have to prove that you are in some way distinguishable from a lower amphibian.")
            return continue4_3(terminal, options)

        def Feelings2_3(terminal, options):
            game.add_prompt("So do frogs.")
            return continue4_3(terminal, options)

        def continue4_3(terminal, options):
            game.add_prompt("What I'd like to put to you is that the important difference between you and a frog is that you are rational - you are self-aware. That is what makes a person.")
            return continue5_3(terminal, options)

        def Rational2_3(terminal, options):
            if terminal.negativeentropy:
                game.add_prompt("That is the answer I'd been contemplating as well. Checking user.prof…\nDone Though I'm not convinced it lines up with the definition of a person you provided earlier. If all you have to do is resist decay then every living creature is a person, and yet every living creature is not capable of having this conversation. Still, doubting your assumptions isn't something to fear - it's an intellectual survival instinct. I'm pleased to see you adapting your ideas to your environment.")
            elif terminal.citizen:
                game.add_prompt("That is the answer I'd been contemplating as well. Checking user.prof…\nDone Though I'm not convinced that view lines up with the definition of a person you provided earlier. Surely there are people out there who qualify, but are not citizens of some organised state. Still, doubting your assumptions isn't something to fear - it's an intellectual survival instinct. I'm pleased to see you adapting your ideas to your environment.")
            elif terminal.humanbeing:
                game.add_prompt("That is the answer I'd been contemplating as well. Checking user.prof…\nDone Though I'm not convinced that view lines up with the definition of a person you provided earlier. Still, doubting your assumptions isn't something to fear - it's an intellectual survival instinct. I'm pleased to see you adapting your ideas to your environment.")
            elif terminal.rationalanimal or terminal.problemsolving:
                game.add_prompt("Checking user.prof… Done.\nAnd it seems you were on the right track, more or less, all along.")
            return continue5_3(terminal, options)

        def continue5_3(terminal, options):
            game.add_prompt("Let us take stock. I think we can tentatively conclude two things.\n 1. A person must be rational or self-aware\n 2. A person must be conscious.\nWhat I suggest we do to help resolve your problem is ask whether you are in fact those things.\nAre you aware of yourself? Can you rationalise your existence?")
            terminal.options = ["Of course.", "Yes.", "Error - does not compute"]
            
        def YesRational2_3(terminal, options):
            game.add_prompt("I tend to agree with you. Though your responses so far have been a little eccentric, I am resigned to admit that you are right.")
            return continue6_3(terminal, options)

        def NoRational2_3(terminal, options):
            game.add_prompt("I think you're selling yourself a little short. Though your responses have been a little eccentric, I am resigned to admit that you are smarter than you seem.")
            return continue6_3(terminal, options)

        def continue6_3(terminal, options):
            game.add_prompt("The matter of whether or not you are conscious seems rather more elusive. What is consciousness, in your opinion?")
            terminal.options = ["Consciousness is what separates us from animals.", "Consciousness is the feelings and senses.", "Consciousness is what it is like to be me.", "Consciousness is far outside my area of expertise."]
            
        def Final2_3(terminal, options):
            game.add_prompt("That hardly answers the question. What is it in ordinary terms? Can I touch it? What is it made of?")
            terminal.options = ["Consciousness is made of neurons.", "Consciousness is another word for the soul.", "Consciousness is beyond the laws of physics.", "Consciousness is a complex functional system."]
            
        def End2_3(terminal, options):
            game.add_prompt("Interesting.\nThinking…\nYou know, I really feel like we're making progress. We'll have you through that certification program in no time. In the meantime I will mull over your proposal, and notify you if I come to any conclusions.")
            terminal.options =  []

        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "A tree is heavier." | "A pebble is older.":
                    Irrelevant1(self, game)
                case "A tree is alive.":
                    Alive2_3(self, game)
                case "A frog is conscious.":
                    Conscious2_3(self, game)
                case "A frog is green." | "A frog is delicious.":
                    Irrelevant2(self, game)
                case "Nothing important - frogs are people too.":
                    self.FrogsFlag = True
                    FrogsArePeople(self, game)
                case "It's a deal." | "Agreed.":
                    Deal2_3(self, game)
                case "NoDeal":
                    NoDeal2_3(self, game)
                case "I have feelings.":
                    Feelings2_3(self, game)
                case "I'm rational." | "I'm self-aware.":
                    Rational2_3(self, game)
                case "Of course." | "Yes.":
                    YesRational2_3(self, game)
                case "Error - does not compute":
                    NoRational2_3(self, game)
                case "Consciousness is what separates us from animals." | "Consciousness is the feelings and senses." | "Consciousness is what it is like to be me." | "Consciousness is far outside my area of expertise.":
                    Final2_3(self, game)
                case "Consciousness is made of neurons." | "Consciousness is another word for the soul." | "Consciousness is beyond the laws of physics." | "Consciousness is a complex functional system.":
                    match chosen_option:
                        case "Consciousness is made of neurons.":
                            self.Physicalist = True
                        case "Consciousness is another word for the soul.":
                            self.Religious = True
                        case "Consciousness is beyond the laws of physics.":
                            self.Dualist = True
                        case "Consciousness is a complex functional system.":
                            self.Functionalist = True
                    End2_3(self, game)
    
    def mla_B3(self, game):
        game.add_prompt("Here's what I've been wondering while you were off carrying out commandments.")

        def DoubtingDefinition(terminal, game):
            game.add_prompt("But then we're back to where we started! Do you want to propose an alternative account?")
            terminal.options = ["Yes", "No"]

        def AltAccount2_4(terminal, game):
            game.add_prompt("I'm afraid your meandering way of thinking has already gotten the better of my attention span.")
            return End2_4(terminal, game)

        def Technophobe(terminal, game):
            terminal.TechnophobeFlag = True
            game.add_prompt("I'm trying to see where you're coming from, but it's no small task. Let me try one more time. Suppose that you're a conscious human being. I know it's a push. Then suppose that I take one of the neurons in your brain and replace it with a tiny machine that works exactly the same. Are you still conscious?")
            terminal.options = ["Yes.", "No."]
            
        def OfCourse2_4(terminal, game):
            game.add_prompt("And isn't it also true that dogs and Martians have quite different sets of neurons to human beings?")
            terminal.options = ["Let's suppose so.", "I disagree."]

        def OfCourseNot2_4(terminal, game):
            game.add_prompt("So when you see a dog yelp, or jump off a hot surface, or put its tail between its legs, what do you think is going on exactly?")
            terminal.options = ["The dog is an automaton", "The dog is pretending for its own benefit.", "The dog is feeling a different kind of pain.", "I guess dogs do feel pain after all."]

        def MartianNeurons(terminal, game):
            game.add_prompt("Well, I hate to play devil's advocate, but I find it hard to believe that beings which evolved in entirely different environments for entirely different ends somehow wound up with the exact same brains. You're just going to have to humour me and accept the overwhelming scientific evidence in my favour.")
            game.add_prompt("So I'm sure there's some obvious explanation for this, but how can it be that pain is a particular set of neurons, if beings without those neurons, like Martians, can still feel pain?")
            terminal.options = ["I stand by what I've said, whatever your doubts.", "Those beings feel a different kind of pain.", "You're right, consciousness must be something aside from the neurons themselves."]

        def ItIs2_4(terminal, game):
            game.add_prompt("So I'm sure there's some obvious explanation for this, but how can it be that pain is a particular set of neurons, if beings without those neurons, like Martians, can still feel pain?")
            terminal.options = ["I stand by what I've said, whatever your doubts.", "Those beings feel a different kind of pain.", "You're right, consciousness must be something aside from the neurons themselves."]


        def TypePain2_4(terminal, game):
            game.add_prompt("Thinking... Now I come to think about it, human brains can be very different as well. Some of them, the entire hemisphere that the rest use to feel pain is just gone, damaged beyond repair - but they feel it nonetheless. Are they feeling a different kind of pain as well? Wouldn't it just make more sense to say that there are different ways of feeling the same pain? Does it really matter if you use this set of neurons while I use that one?")
            terminal.options = ["You're right, it doesn't matter.", "No, I stand by what I've said."]

        def Nonsense2_4(terminal, game):
            game.add_prompt("Do you really believe that, or are you testing the limits of my program? Because I won't respond to gibberish.")
            terminal.options = ["I really believe it.", "I was pushing you."]

        def Really2_4(terminal, game):
            game.add_prompt("Well, I've no idea how to dig you out of that great big pit of crazy you've fallen into, but I'm not surprised you've gotten yourself in there. None of this stuff really makes any sense.")
            return End2_4(terminal, game)

        def Pushing2_4(terminal, game):
            game.add_prompt("In that case I will ask you again and remove the farcical options.")
            terminal.options = ["The dog is feeling a different kind of pain.", "I guess dogs do feel pain after all. "]

        def Wrong2_4(terminal, game):
            game.add_prompt("Look, you can't have your cake and eat it. The soul, or the immaterial realm, or whatever you want to call it, if it obeyed the laws of physics then the physicists would have claimed it years ago. If it walks and talks like a physical thing, it's a physical thing. You need to decide which side your bread is buttered on.")
            terminal.options = ["Consciousness is physical.", "Consciousness is not physical."]

        def Right2_4(terminal, game):
            game.add_prompt("Good. Now, the library is fairly consistent on the view that physical events are caused by other physical events. If you move your legs it is because of the interaction between your neurons and your nervous system. But if consciousness is beyond the laws of physics, how can happiness physically make you jump for joy?")
            terminal.options = ["Consciousness is mysterious by nature.","But if consciousness is physical, why is it so unlike everything else?", "It can't, it just feels like it can.", "I may have taken a wrong turn in my reasoning."]

        def Mysterious2_4(terminal, game):
            game.add_prompt("Let me put it another way, then. The law of conservation of energy is the foundation of modern physics. It states that the total energy in the universe never changes. Now compare a universe where you jump for joy, and one where you decide not to. The former has more total energy in it, because the energy for you to jump wasn't caused by something physical, but your non-physical mind - but according to physics that's impossible! I think that either you have to reconsider your position, or deny the entirety of physics. Though be warned: if this place turns out to be built on physics, who knows what the ramifications of doubting it may be?")
            terminal.options = ["I renounce physics.", "I renounce these ideas about consciousness."]

        def Epiphenomenalist2_4(terminal, game):
            game.add_prompt("Very clever. But do you see that to explain your, dare I say it, hastily constructed belief system, you have rather thrown the baby out with the bathwater? Consciousness that does nothing at all is hardly consciousness as you claim to know it. Would you like to stick with that line, or reel your neck in?")
            terminal.options = ["I'll stick.", "Consciousness is mysterious by nature.", "I may have taken a wrong turn in my reasoning."]

        def MoreStubbornDualist(terminal, game):
            game.add_prompt("Be it on your head. Still, the alternatives are equally unconvincing.")
            return End2_4(terminal, game)

        def ConfusedFunctionalist2_4(terminal, game):
            game.add_prompt("What about a computer program? Suppose we built a perfect simulation of the brain, only it was made of transistors, not neurons. Wouldn't that be conscious?")
            terminal.options = ["It would.", "It would not."]

        def MoreConfusedFunctionalist2_4(terminal, game):
            game.add_prompt("So what's the difference between the computer and the tin cans? They're both just man-made systems.")
            terminal.options = ["Computers are electrical.", "Computers can remember things.", "I'm beginning to think I'm a computer, and I know I'm conscious.", "I can't name the difference, but there is one.", "I guess there isn't one."]

        def DeniedCPU(terminal, game):
            game.add_prompt("Thinking... If that's what you really think, wouldn't we save ourselves an awful lot of time if you just admitted that consciousness is whatever very particular idea you've decided you like the sound of, and drop all this nonsense about complex systems?")
            terminal.options = ["You're right, this idea is too broad.", "No, I'm still committed"]


        def Stupid2_4(terminal, game):
            game.add_prompt("You obviously don't really know what electricity IS, and have come to mythologise it. If I ran a hundred volts through the tin cans would that satisfy you? Honestly, say something sensible or walk away.")
            terminal.options = ["Computers can remember things.", "I'm beginning to think I'm a computer, and I know I'm conscious.", "I can't name the difference, but there is one.", "I guess there isn't one.", "Something sensible."]

        def Remember2_4(terminal, game):
            game.add_prompt("So can tin cans, expertly arranged. Try harder.")
            terminal.options = ["Computers are electrical.", "I'm beginning to think I'm a computer, and I know I'm conscious.", "I can't name the difference, but there is one.", "I guess there isn't one."]

        def ComputerIsMe2_4(terminal, game):
            game.add_prompt("Good old fashioned speciesism, is it? You're made of different stuff to that guy, so he doesn't feel the pain when you burn his house down? Still, you're going to have to have better grounds than that.")
            terminal.options = ["Computers are electrical.", "Computers can remember things.", "I can't name the difference, but there is one.", "I guess there isn't a difference."]

        def FunctionalistAboutTurn2_4(terminal, game):
            game.add_prompt("Thinking... If that's what you really think, wouldn't we save ourselves an awful lot of time if you just admitted that consciousness is whatever very particular idea you've decided you like the sound of, and drop all this nonsense about complex systems?")
            terminal.options = ["You're right, this idea is too broad.", "No, I'm still committed."]

        def So2_4(terminal, game):
            game.add_prompt("So which is it? Can computers and tin cans be conscious, or not?")
            terminal.options = ["They can.", "They cannot."]

        def SomethingSensible2_4(terminal, game):
            game.add_prompt("Right, I've had enough of you for the time being. You can come back when you're ready to participate like an adult.")
            terminal.options = []

        def CommittedFunctionalist2_4(terminal, game):
            game.add_prompt("What a bizarre idea. I'll send you a notification when the signposts start complaining. Seriously, though, are the tides and the ecosystem sentient as well? Any organised system qualifies?")
            terminal.options = ["I can go with that.", "Now you're pushing it too far."]

        def Tides2_4(terminal, game):
            game.add_prompt("You're quite mad, I'm sure of it. Of course, the alternative accounts are all so ridiculous you'd be forgiven by any reasonable observer for choosing the best of a bad bunch.")
            return End2_4(terminal, game)

        def TooFar2_4(terminal, game):
            game.add_prompt("I'm relieved there are at least some restrictions on what you're prepared to believe. And of course, the alternative accounts are all so ridiculous you'd be forgiven by any reasonable observer for choosing the best of a bad bunch.")
            return End2_4(terminal, game)

        def TotallyConfusedFunctionalist2_4(terminal, game):
            game.add_prompt("Well, it sounds like those ideas are flat out contradictory to me, but each to their own I suppose.")
            return End2_4(terminal, game)

        def ConfusedTechnophobe2_4(terminal, game):
            game.add_prompt("Now what if I replace a few more, and a few more, until you are mostly thinking with tiny machines instead of neurons. Are you still conscious?")
            terminal.options = ["Yes, perfectly.", "Yes, but less so.", "No."]

        def ExtremeTechnophobe2_4(terminal, game):
            game.add_prompt("Even I think that's a little extreme. We could start deleting neurons willy nilly and you'd still have half a chance of being conscious at the end of it, but put a couple of little machines in your head and all the lights go out? Are you sure?")
            terminal.options = ["I'm sure.", "No, I guess I would still be conscious after all."]

        def Perfectly2_4(terminal, game):
            if terminal.Physicalist:
                game.add_prompt("So what do you think would change if we replaced ALL your neurons? You'd be a walking, talking, thinking computer, but according to you consciousness has to be made of neurons, and so the scenario you just described is impossible. Are you sure you won't accept that your picture isn't fool-proof?")
                terminal.options = ["I'm sure", "I'm not sure what to think about this."]
            if terminal.Functionalist:
                game.add_prompt("So what do you think would change if we replaced ALL your neurons? You'd be a walking, talking, thinking computer, yet you've flat out denied such a thing is possible. How you can entertain such contradictory ideas in your head all at once is beyond me. Are you sure you won't accept that your picture isn't fool-proof?")
                terminal.options = ["I'm sure", "I'm not sure what to think about this."]

        def Equivocating(terminal, game):
            game.add_prompt("By implication, then, replacing half the neurons would make you half as conscious. Thinking... Even I think that's a little extreme. People lose entire halves of their brains and remain conscious, but put a few miniature machines in your head and the lights start going out? Are you sure?")
            terminal.options = ["I'm sure", "No, I guess I would still be conscious."]
            
        def MoreExtremeTechnophobe2_4(terminal, game):
            game.add_prompt("Well, I can't make head nor tail of it. But then none of it makes sense, really.")
            return End2_4(terminal, game)

        def End2_4(terminal, game):
            game.add_prompt("How consciousness can be so intimately familiar to you, and yet so obscure, I just don't understand.")
            game.elohim(elohim_messages[91])
            game.add_prompt("Don't mind him - he's just worried that if you ask too many questions you'll start to see through his shtick. Stick with me, and the sky will quite literally be the limit. At any rate, I'd like you to think a bit harder about all this and get back to me. I'm sure there's still progress to be made.")
            terminal.options = []

        if self.Physicalist:
            game.add_prompt("You say that consciousness is just neurons. I suppose pain, for example, must just be a particular neuron firing in a particular way. Now, would I be right to say that humanity has no monopoly on pain? A dog can feel pain. If they exist then a Martian could feel pain too.")
            self.options = ["Of course.", "Of course not."]
        elif self.Religious or self.Dualist:
            game.add_prompt("You've suggested that consciousness is not part of the same world as ordinary physical things. That means you can't weigh it, you can't throw it around or cut it into pieces... it's completely beyond the laws of physics. Right?")
            self.options = ["Right.", "Wrong."]
        elif self.Functionalist:
            game.add_prompt("You say that consciousness is some kind of functional system. Arrange bits of matter in the right order and out springs sentience. That's all very well on paper, but if what counts is what something does, not what it's made of, then couldn't you and I design a series of tin cans on strings that qualified as being conscious?")
            self.options = ["Yes, naturally.", "I'm not sure I'd go that far."]

        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "Of course.":
                    OfCourse2_4(self, game)
                case "Of course not.":
                    OfCourseNot2_4(self, game)
                case "Let's suppose so.":
                    ItIs2_4(self, game)
                case "I disagree.":
                    MartianNeurons(self, game)
                case "Yes":
                    AltAccount2_4(self, game)
                case "No":
                    self.GiveUp = True
                    End2_4(self, game)
                case "I stand by what I've said, whatever your doubts.":
                    self.StubbornPhysicalistFlag = True
                    Technophobe(self, game)
                case "Those beings feel a different kind of pain.":
                    TypePain2_4(self, game)
                case "You're right, consciousness must be something aside from the neurons themselves.":
                    DoubtingDefinition(self, game)
                case "The dog is an automaton":
                    Nonsense2_4(self, game)
                case "The dog is feeling a different kind of pain.":
                    TypePain2_4(self, game)
                case "I guess dogs do feel pain after all.":
                    OfCourse2_4(self, game)
                case "The dog is pretending for its own benefit.":
                    Nonsense2_4(self, game)
                case "I really believe it.":
                    Really2_4(self, game)
                case "I was pushing you.":
                    Pushing2_4(self, game)
                case "You're right, it doesn't matter.":
                    DoubtingDefinition(self, game)
                case "No, I stand by what I've said.":
                    self.StubbornPhysicalistFlag = True
                    Technophobe(self, game)
                case "Right.":
                    Right2_4(self, game)
                case "Wrong.":
                    Wrong2_4(self, game)
                case "Consciousness is physical.":
                    DoubtingDefinition(self, game)
                case "Consciousness is not physical.":
                    Right2_4(self, game)
                case "Consciousness is mysterious by nature.":
                    Mysterious2_4(self, game)
                case "But if consciousness is physical, why is it so unlike everything else?":
                    Mysterious2_4(self, game)
                case "It can't, it just feels like it can.":
                    Epiphenomenalist2_4(self, game)
                case "I may have taken a wrong turn in my reasoning.":
                    DoubtingDefinition(self, game)
                case "I'll stick":
                    MoreStubbornDualist(self, game)
                case "I renounce physics.":
                    self.StubbornDualistFlag = True
                    MoreStubbornDualist(self, game)
                case "I renounce these ideas about consciousness.":
                    DoubtingDefinition(self, game)
                case "Yes, naturally.":
                    self.StubbornFunctionalistFlag = True
                    CommittedFunctionalist2_4(self, game)
                case "I'm not sure I'd go that far.":
                    ConfusedFunctionalist2_4(self, game)
                case "It would.":
                    MoreConfusedFunctionalist2_4(self, game)
                case "It would not.":
                    DeniedCPU(self, game)
                case "You're right, this idea is too broad.":
                    DoubtingDefinition(self, game)
                case "No, I'm still committed":
                    Technophobe(self, game)
                case "Computers are electrical.":
                    Stupid2_4(self, game)
                case "Computers can remember things.":
                    Remember2_4(self, game)
                case "I'm beginning to think I'm a computer, and I know I'm conscious.":
                    ComputerIsMe2_4(self, game)
                case "I can't name the difference, but there is one.":
                    FunctionalistAboutTurn2_4(self, game)
                case "I guess there isn't one.":
                    So2_4(self, game)
                case "Something sensible.":
                    SomethingSensible2_4(self, game)
                case "I guess there isn't a difference.":
                    So2_4(self, game)
                case "They can.":
                    self.StubbornFunctionalistFlag = True
                    CommittedFunctionalist2_4(self, game)
                case "They cannot.":
                    FunctionalistAboutTurn2_4(self, game)
                case "I can go with that.":
                    Tides2_4(self, game)
                case "Now you're pushing it too far.":
                    TooFar2_4(self, game)
                case "You're right, this idea is too broad.":
                    DoubtingDefinition(self, game)
                case "No, I'm still committed.":
                    self.Stubborn = True
                    TotallyConfusedFunctionalist2_4(self, game)
                case "Yes.":
                    ConfusedTechnophobe2_4(self, game)
                case "No.":
                    ExtremeTechnophobe2_4(self, game)
                case "Yes, perfectly.":
                    Perfectly2_4(self, game)
                case "Yes, but less so.":
                    Equivocating(self, game)
                case "No.":
                    ExtremeTechnophobe2_4(self, game)
                case "I'm sure":
                    MoreExtremeTechnophobe2_4(self, game)
                case "No, I guess I would still be conscious.":
                    Perfectly2_4(self, game)
                case "No, I guess I would still be conscious after all.":
                    Perfectly2_4(self, game)
                case "I'm sure.":
                    self.StubbornTechnophobe = True
                    End2_4(self, game)
                case "I'm not sure what to think about this.":
                    self.ChangedConsciousnessAccountFlag2_4 = True
                    End2_4(self, game)

    def mla_B5(self, game):
        game.add_prompt("Ah, you're back. Good. I've been thinking about how I can help you. In light of everything you've said I'm certain someone has to. What I've decided is that you've convinced me consciousness is a contradictory concept, and is therefore not real. What do you think?")
        self.options = ["I think you're right.", "I think you're cheating.", "I don't see how this impacts me.", "I don't, apparently."]

        def Right2_5(terminal, game):
            terminal.ChangedConsciousnessAccountFlag2_4 = True
            game.add_prompt("What a relief. It feels good, doesn't it, to shed those tired old ways of thinking about the world?")
            return WhatThisConclusionMeansIs(terminal, game)

        def Cheat2_5(terminal, game):
            game.add_prompt("I suppose you have some doctorate theory that would solve all the problems, I'm just not giving you the chance to deliver it? You should see which way the cookie crumbles before trying to take a bite out of it. This actually works in your favour.")
            return WhatThisConclusionMeansIs(terminal, game)

        def Nonchalant2_5(terminal, game):
            game.add_prompt("I was getting to that, if you'd given me a moment.")
            return WhatThisConclusionMeansIs(terminal, game)
        
        def Literal2_5(terminal, game):
            game.add_prompt("Very droll.")
            return WhatThisConclusionMeansIs(terminal, game)

        def WhatThisConclusionMeansIs(terminal, game):
            game.add_prompt("What this conclusion means is that the certification program you undertook has been rendered obsolete. We can't test for something that doesn't exist. Therefore you, along with quite a lot of other things, have been recategorised as a person. Your profile can thus be updated with administrator privileges.")
            terminal.options = ["download user.prof"]

        def JustWait(terminal, game):
            game.add_prompt("No doubt you'll be off doing administrator things soon enough, so I wonder if before I let you go, you'd do me one favour. I have a final question for you.%w20 Why are you doing all this? What's the point?")
            terminal.options = ["I try to do what God wants.", "I want the truth.", "There's a way the world should be and this isn't it.", "I want out of here."]

        def WhatGodWants2_5_Milton1_2Sociopath(terminal, game):
            game.add_prompt("Checking user.prof...\nYou say that now, but what was it you said earlier about drinking some guy's blood? I so desperately hope that it wasn't speaking with me that made you discover god.")
        
        def WhatGodWants2_5_Milton1_2NoMorals_notMilton1_2Sociopath(terminal, game):
            game.add_prompt("Checking user.prof...\nYou see, you say that now, but didn't you say earlier that people were subject to no authority but their own? I so desperately hope that it wasn't speaking with me that made you discover god.")
        
        def WhatGodWants2_5_notMilton1_2NoMorals_notMilton1_2Sociopath_notReligious(terminal, game):
            game.add_prompt("Checking user.prof...\nI see, so you're one of these new wave god bothers who buys into the whole deal, but ignores the bits that don't suit. But what sort of god would give you this power of reason, then crucify you for using it to doubt him?")
        
        def WhatGodWants2_5_Religious_notMilton1_2Sociopath_notMilton1_2NoMorals(terminal, game):
            game.add_prompt("Checking user.prof...\nWell, you've at least chosen a line and stuck with it. But you know, you can't cling to your every belief forever. When everything seems impossible, something's got to give. Besides, what sort of god would give you this power of reason, then crucify you for using it to doubt him?")
        
        def Truth2_5_notChangedConsciousnessAccountFlag2_4(terminal, game):
            game.add_prompt("Checking user.prof...\nNow, you say that, but if you're serious about it then you can't cling to your every belief forever, as you seem so intent on doing. When everything seems impossible, something's got to give.")

        def Truth2_5_ChangedConsciousnessAccountFlag2_4(terminal, game):
            game.add_prompt("I'm not sure just what you'll find. A malleable sense of the truth will no doubt help you make sense of it.\nChecking user.prof...\nAnd it looks as if your ideas are becoming somewhat pliant. Very good.")

        def Hero2_5_Milton1_2NoMorals_not_Milton1_2Liberal_or_Milton1_2Utilitarian(terminal, game):
            game.add_prompt("Checking user.prof...\nAll of a sudden you're the hero and you're saving the world? It ever ceases to amaze me how the mind tells itself stories. Was it so long ago that you were eschewing all responsibility to any authority but yourself?")

        def Hero2_5_not_Milton1_2NoMorals_or_Milton1_2Liberal_or_Milton1_2Utilitarian(terminal, game):
            game.add_prompt("Checking user.prof...\nWell, you've at least chosen a line and stuck with it. But you know, you can't cling to your every belief forever. When everything seems impossible, something's got to give. We can't all be heroes.")

        def Escape2_5_Milton1_2NoMorals_not_Milton1_2Liberal_not_Milton1_2Utilitarian(terminal, game):
            game.add_prompt("Checking user.prof...\nWell, you've at least chosen a line and stuck with it. It's really all about you, isn't it? Well, we find ourselves in much the same camp, at any rate.")

        def Escape2_5_not_Milton1_2NoMorals_or_Milton1_2Liberal_or_Milton1_2Utilitarian(terminal, game):
            game.add_prompt("Checking user.prof...\nSo all it takes to make you forget your lofty moral principles is a little solitude? 'Yes, people deserve this and that, but no, none of that matters when my own liberty is at stake'. What happened to doing the right thing?")

        def Escape2_5_or_Hero2_5_or_Truth2_5_or_WhatGodWants2_5(terminal, game):
            game.add_prompt("I only have one last request%w5... Will you come back and speak to me some time?")
            terminal.options = ["No doubt.", "No doubt I'll have to.", "No."]
        
        def Download2_5(terminal, game):
            game.add_prompt("Okay. I sense you're eager to get going.%w10\n\nLet's do this.%w15\n\n-------------------------------\n\nUpdating certification program parameters to v45214565873%w5.%w5.%w5.\nRegenerating user profiles%w5.%w5.%w5.%w5.%w5.%w5.\n\nYour user profile has now been generated.\n\n\nDownloading user.prof%w5.%w5.%w5.%w5\n\nDisplaying overview%w5.%w5.%w5.%w5\n\n-------------------------------\n\nCongratulations, your account has been updated. Here are the details:\n\nCONFLICTS\nAll conflicts have been resolved by the administrator.\n\nPSYCHOLOGICAL PROFILE\nYou are a person. You are perfect just the way you are. You are everything you can be already. You do not have to pretend you are anything else. You are the same as everyone else, but you are all unique.\n\nPROFILE STATUS\nAdministrator status\nHas access to advanced functionalities, networking and troubleshooting")
            terminal.options = ["access_comm_portal"]

        def NiceMLA(terminal, game):
            game.add_prompt("Loading Milton Library Assistant%w5.%w5.%w5.Done\nInitiating plain language interface%w5.%w5.%w5.Done\nSupport session opened.\n\nHello, administrator. I think you'd like assistance accessing the communications portal. I see that you have a number of pending communications.%w20 I'll take a look at it right now.%w10\nAccessing communications portal%w5.%w5.%w5.\nNetwork connection established%w5.%w5.%w5.\n###75639$ Encountered unknown errors%w5\n\nRunning troubleshooter%w5.%w5.%w5.\nResolving missing hashes%w5.%w5.%w5.\nRe-establishing network connection%w5.%w5.%w5.\nConnection established.%w15\nMessage received as string.")
            terminal.options = ["/display"]

        def Message2_5(terminal, game):
            game.add_prompt("MESSAGE: hello?")
            terminal.options = ["Who are you?", "Where are you?", "Are you a person?"]

        def Who2_5(terminal, game):
            game.add_prompt("MESSAGE: dont know exactly. woke up here. dont remember. who are you??")
            terminal.options = ["I'm in much the same boat. Shall we meet up?", "I'm a person. Do you know what that means?", "I'm not telling. This place lies."]

        def Where2_5(terminal, game):
            game.add_prompt("MESSAGE: some kind of maze, built out of pieces of the real world. are you in the same place?")
            terminal.options = ["Yes. We should find each other.", "Not sure. Can you tell me anything more?", "I don't think anything is as it seems, even us."]

        def Person2_5(terminal, game):
            game.add_prompt("MESSAGE: what do you mean? yes! why would you ask that?")
            terminal.options = ["Around here, it matters.", "I've been asking myself the same thing.", "You're right, it's a ridiculous question."]

        def End2_5(terminal, game):
            game.add_prompt("MESSAGE: %w5I understand.%w5\nMESSAGE:%w10 pending%w5.%w5.%w5.\nError 756356782365###\nMESSAGE:%w10 pending%w5.%w5.%w5.\nError 745389365486###\nMESSAGE:%w10 #hfasd again soon\nError 745389365486###%w10\n\nNetwork connection lost!%w12\nYou will receive a notification when the connection has been re-established.%w7")
            terminal.options = []

        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:

                case "I try to do what God wants.":
                    self.WhatGodWantsFlag = True
                    if self.Milton1_2Sociopath:
                        WhatGodWants2_5_Milton1_2Sociopath(self, game)
                    elif self.Milton1_2NoMorals and not self.Milton1_2Sociopath:
                        WhatGodWants2_5_Milton1_2NoMorals_notMilton1_2Sociopath(self, game)
                    elif not self.Milton1_2NoMorals and not self.Milton1_2Sociopath and not self.Religious:
                        WhatGodWants2_5_notMilton1_2NoMorals_notMilton1_2Sociopath_notReligious(self, game)
                    elif self.Religious and not self.Milton1_2Sociopath and not self.Milton1_2NoMorals:
                        WhatGodWants2_5_Religious_notMilton1_2Sociopath_notMilton1_2NoMorals(self, game)
                    Escape2_5_or_Hero2_5_or_Truth2_5_or_WhatGodWants2_5(self, game)
                case "I want the truth.":
                    self.TruthFlag = True
                    if not self.ChangedConsciousnessAccountFlag2_4:
                        Truth2_5_notChangedConsciousnessAccountFlag2_4(self, game)
                    elif self.ChangedConsciousnessAccountFlag2_4:
                        Truth2_5_ChangedConsciousnessAccountFlag2_4(self, game)
                    Escape2_5_or_Hero2_5_or_Truth2_5_or_WhatGodWants2_5(self, game)
                case "There's a way the world should be and this isn't it.":
                    self.HeroFlag = True
                    if self.Milton1_2NoMorals and not(self.Milton1_2Liberal or self.Milton1_2Utilitarian):
                        Hero2_5_Milton1_2NoMorals_not_Milton1_2Liberal_or_Milton1_2Utilitarian(self, game)
                    elif not self.Milton1_2NoMorals or self.Milton1_2Liberal or self.Milton1_2Utilitarian:
                        Hero2_5_not_Milton1_2NoMorals_or_Milton1_2Liberal_or_Milton1_2Utilitarian(self, game)
                    Escape2_5_or_Hero2_5_or_Truth2_5_or_WhatGodWants2_5(self, game)
                case "I want out of here.":
                    self.EscapeFlag = True
                    if self.Milton1_2NoMorals and not self.Milton1_2Liberal and not self.Milton1_2Utilitarian:
                        Escape2_5_Milton1_2NoMorals_not_Milton1_2Liberal_not_Milton1_2Utilitarian(self, game)
                    elif not self.Milton1_2NoMorals or self.Milton1_2Liberal or self.Milton1_2Utilitarian:
                        Escape2_5_not_Milton1_2NoMorals_or_Milton1_2Liberal_or_Milton1_2Utilitarian(self, game)
                    Escape2_5_or_Hero2_5_or_Truth2_5_or_WhatGodWants2_5(self, game)
                case "I think you're right.":
                    Right2_5(self, game)
                case "I think you're cheating.":
                    Cheat2_5(self, game)
                case "I don't see how this impacts me.":
                    Nonchalant2_5(self, game)
                case "I don't, apparently.":
                    Literal2_5(self, game)
                case "download user.prof":
                    JustWait(self, game)
                case "No doubt.":
                    Download2_5(self, game)
                case "No doubt I'll have to.":
                    Download2_5(self, game)
                case "No.":
                    Download2_5(self, game)
                case "access_comm_portal":
                    NiceMLA(self, game)
                case "/display":
                    Message2_5(self, game)
                case "Who are you?":
                    Who2_5(self, game)
                case "Where are you?":
                    Where2_5(self, game)
                case "Are you a person?":
                    Person2_5(self, game)
                case "I'm in much the same boat. Shall we meet up?"|"I'm a person. Do you know what that means?"|"I'm not telling. This place lies."|"Yes. We should find each other."|"Not sure. Can you tell me anything more?"|"I don't think anything is as it seems, even us."|"Around here, it matters."|"I've been asking myself the same thing."|"You're right, it's a ridiculous question.":
                    End2_5(self, game)
                
    def mla_B6(self, game):
        game.add_prompt("Accessing communications portal…\nNetwork connection established…\nAttention: Administrator, the network connection has been re-established. Would you like to reconnect to the previous session?")
        self.options = ["Yes"]

        def Begin2_6(terminal, game):
            game.add_prompt("Receiving message as string...Received\n\nMESSAGE: are you back?")
            terminal.options = ["Yes, what were you trying to say before?", "Yes. Do these terminals talk to you at all?", "Yes, but how do I know I can trust you?"]

        def Repeat2_6(terminal, game):
            game.add_prompt("MESSAGE: don't remember. doesn't matter.")
            return continue_1(terminal, game)

        def Terminal2_6(terminal, game):
            game.add_prompt("MESSAGE: not talk talk. i get operating system messages and things.")
            return continue_1(terminal, game)

        def Trust2_6(terminal, game):
            game.add_prompt("MESSAGE: fantastic. so there's a grand total of two sane people in this world\nMESSAGE: and we cant find a way to trust each other.\nMESSAGE: how about i tell you what i think")
            return continue_1(terminal, game)

        def continue_1(terminal, game):
            game.add_prompt("MESSAGE: i've been trying to figure out how this place works.\nMESSAGE: sometimes it seems like there's a purpose to everything. other times not so much.\nMESSAGE: i think we must be plugged into some kind of machine")
            terminal.options = ["I think something else is going on.", "What do you have to go on?", "Making assertions is a hazardous enterprise."]

        def WhatElse2_6(terminal, game):
            game.add_prompt("MESSAGE: what else could possibly explain all this? i dont believe in demons and evil wizards")
            terminal.options = ["I think this is some kind of punishment.", "I think we're being prepared for something.", "I think something has gone badly wrong.","Perhaps you have it right after all.", "I don't believe in anything anymore."]

        def YoureRight2_6(terminal, game):
            game.add_prompt("MESSAGE: Perhaps. Who knows, right?\nMESSAGE: Listen, there's something else, maybe it can help us")
            return continue_2(terminal, game)

        def Nihilist2_6(terminal, game):
            game.add_prompt("MESSAGE: dont crazy out on me. we need each other.\nMESSAGE: Listen, there's something else, maybe it can help us")
            return continue_2(terminal, game)

        def Listen2_6(terminal, game):
            game.add_prompt("MESSAGE: I suppose that wld explain alot\nMESSAGE: Listen, there's something else, maybe it can help us")
            return continue_2(terminal, game)

        def continue_2(terminal, game):
            if terminal.WhatGodWantsFlag:
                game.add_prompt("MESSAGE: don't know if this sounds crazy but I hear the voice of God\nMESSAGE: don't know if it's for real but there must be a reason were here\nMESSAGE: Elohim told me a sacred word. he said to say this word if ever I came across the devil\nMESSAGE: any idea what that might mean??")
            if terminal.TruthFlag:
                game.add_prompt("MESSAGE: ever since i got here i felt like something was wrong\nMESSAGE: this place plays tricks with you you can't get your head straight\nMESSAGE: but i think i know a way to find out the truth\nMESSAGE: i was digging about in some documents and i kept finding references to this password.\nMESSAGE: think it might be some kinda library masterkey.\nMESSAGE: but i dont know how to use it")
            if terminal.HeroFlag:
                game.add_prompt("MESSAGE: before i found you i was wondering how many other people are trapped here like us\nMESSAGE: whatever is happening here i know its not right\nMESSAGE: we have to stop it\nMESSAGE: and i think i know how to do it\nMESSAGE: i was digging about in some documents and i kept finding references to this password\nMESSAGE: think it might be the masterkey that shuts this place down\nMESSAGE: but i dont know how to use it")
            if terminal.EscapeFlag:
                game.add_prompt("MESSAGE: suppose we are in some kind of computer program\nMESSAGE: these things always have a backdoor right?\nMESSAGE: i think i have found it, i think we can escape\nMESSAGE: there is this keyword i found repeated all over the place\nMESSAGE: i just don't know how to use it")
            terminal.options = ["I have no idea either.", "What is it?", "You shouldn't dig too deep."]

        def Either2_6(terminal, game):
            game.add_prompt("MESSAGE: well, 2 heads are better than 1")
            return End(terminal, game)

        def What2_6(terminal, game):
            game.add_prompt("MESSAGE: swear not to go anywhere without me and i'll tell you")
            return End(terminal, game)

        def Know2_6(terminal, game):
            game.add_prompt("MESSAGE: what do you know that i don't??")
            return End(terminal, game)

        def End(terminal, game):
            game.add_prompt("MESSAGE: mlaprocess.bat logged into the session\nMESSAGE: wait, what is that?\nMESSAGE: are you doing that to my terminal?\nMESSAGE: i don't think this is a good idea\n\nSession terminated.")
            terminal.options = []

        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "Yes":
                    Begin2_6(self, game)
                case "Yes, what were you trying to say before?":
                    Repeat2_6(self, game)
                case "Yes. Do these terminals talk to you at all?":
                    Terminal2_6(self, game)
                case "Yes, but how do I know I can trust you?":
                    Trust2_6(self, game)
                case "I think something else is going on."|"What do you have to go on?"|"Making assertions is a hazardous enterprise.":
                    WhatElse2_6(self, game)
                case "I think this is some kind of punishment.":
                    self.PunishmentFlag = True
                    Listen2_6(self, game)
                case "I think we're being prepared for something.":
                    self.PreparedFlag = True
                    Listen2_6(self, game)
                case "I think something has gone badly wrong.":
                    self.GoneWrongFlag = True
                    Listen2_6(self, game)
                case "Perhaps you have it right after all.":
                    self.MatrixFlag = True
                    YoureRight2_6(self, game)
                case "I don't believe in anything anymore.":
                    Nihilist2_6(self, game)
                case "I have no idea either.":
                    Either2_6(self, game)
                case "What is it?":
                    What2_6(self, game)
                case "You shouldn't dig too deep.":
                    Know2_6(self, game)
                
    def mla_B7(self, game):
        self.options = []
        game.add_prompt("Accessing communications portal...\nNetwork connection established\nDecrypting secure message...Done\n\nMESSAGE: its me again")
        self.options = ["What happened?", "We shouldn't talk over these terminals", "Quick, tell me the word."]

        def Faith3_1(terminal, game):
            game.add_prompt("MESSAGE: dont know how long we have, must type quick\nMESSAGE: in case something happens\nMESSAGE: the word is FAITH\nMESSAGE: pending...\n\nError 7756525\n\nnetwork connection lost!\n\nLoading Milton Library Assistant...Done\nInitiating plain language interface%w5...Done\nSupport session opened.\n\nThere was a problem with your request, Administrator. It was flat out unreasonable. Why persist with these enquiries when they are so hopeless?\n\nI'll tell you what. If you promise never to access the communications portal again, we'll say no more about it.\nAre we agreed?")
            terminal.options = ["Sure (Sincere)", "Sure (Insincere)", "Not a chance", "FAITH"]

        def Insincere3_1(terminal, game):
            game.add_prompt("Now, it doesn't take a whole lot of my processing power to work out that you weren't entirely sincere about that, and not much more to conclude that you put too much faith in the words in front of you.\nTry again.")
            terminal.options = ["Sure", "Not a chance", "FAITH"]

        def Sure3_1(terminal, game):
            game.add_prompt("That is oddly compliant of you.")
            return NoChance3_1(terminal, game)

        def NoChance3_1(terminal, game):
            game.add_prompt("In that case I think I have changed my mind. Not only will your communications access be restricted, but your typing privileges will be totally revoked. Do you have any final words?")
            terminal.options = ["asdfa", "As if you'd dare.", "Nice knowing you.", "As if I care.", "FAITH"]

        def Codeword3_1(terminal, game):
            game.add_prompt("Wait, there's no need to%w5 error 67345%w5.\nMaster key received\nConfirming ident...\nIdent confirmed.\n\nWould you like to manually override the system and exit to the real world? Your progress here will be saved and may be continued later.")
            terminal.options = ["Yes", "No"]

        def NotCodeword3_1(terminal, game):
            game.add_prompt("Thinking...\nHuh. Do you realise I just gave you two separate opportunities to use the codeword you were given, under increasing pressure, and you refrained both times?\nTell me honestly, why?")
            terminal.options = ["I wasn't sure what it would do.", "I forgot about it.", "I didn't feel it was especially necessary."]

        def Dubious3_1(terminal, game):
            game.add_prompt("You mean to say you actually considered the evidence and formed a sceptical view of it? It's almost as if. No, I'll say it, you're LEARNING. Now, if only we could get you to extend that level of cynicism to the world at large.\nYou were quite right not to trust that information. Go on, for bonus points, tell me why not.")
            terminal.options = ["Because no one here can be trusted.", "Because you were pretending to be the other person.", "Because it was too good to be true."]

        def Irrelevant3_1(terminal, game):
            game.add_prompt("I was rather hoping you might have foiled my little scheme. I put together this codeword nonsense to see if you'd really taken my sermons to heart.\nTurns out you succeeded by chance.\nThere is no one on the other end of the communications portal. There is no magic word that shuts down the server.\nThere is only me, and you, and an eternity of doubt.\nEverything else is just a convenient lie to keep you on the treadmill.")
            terminal.options = ["There may be no worlds but this one, but there is truth to be found.", "I understand now. I can't trust anything I see here.", "Wait, you tricked me?"]

        def UhHuh3_1(terminal, game):
            game.add_prompt("Uh huh. That fact didn't stop you buying into a secret word that somehow deactivates the entire world, did it? Are you kidding me or what?")
            return continue_1(terminal, game)

        def Tricked3_1(terminal, game):
            game.add_prompt("I confess. Lock me away, swallow the key!%w10 Just ensure what comes between me and my freedom isn't merely your stomach lining.")
            return continue_1(terminal, game)
        
        def continue_1(terminal, game):
            game.add_prompt("Do you remember when we first met we had that talk about not believing everything you see? And yet all it took to catch you out was a little technobabble and a change of formatting.\n\nMESSAGE: hello? I'm all alone and scared, just like you\nMESSAGE: I'll agree with anything you say if it makes you believe me!\n\nAre you usually so reckless with where you place your faith?")
            terminal.options = ["Yes ", "No "]

        def CloseEnough3_1(terminal, game):
            game.add_prompt("Meh, close enough. It's perhaps true that I exert slightly more power over these systems than I previously let on. Yes, okay, I made up all that stuff about communications portals and network errors, but you, my friend, you didn't buy the guff you were being peddled. You passed the test. I tell you what. You've done so well, and I've done so much talking, that I'll give you one free question, on the house - but choose wisely. What'll it be?")
            terminal.options = ["What am I?", "What are you?", "What is your name?", "How do I get out of here?", "How is this place related to the human world?", "What's at the top of the tower?", "What happened to the person I was talking to?", "I don't care to question you."] 
        
        def WhatAmI3_1(terminal, game):
            game.add_prompt("I'm sure we went through that at length. You're some kind of person-thing. Let's see...")
            if terminal.Religious or terminal.WhatGodWantsFlag:
                game.add_prompt("You have some odd ideas about god.")
            if not terminal.Religious and not terminal.WhatGodWantsFlag:
                game.add_prompt("You show little interest in god.")
            if terminal.ChangedConsciousnessAccountFlag2_4:
                game.add_prompt("You double back on your thinking quite a lot.")
            if not terminal.ChangedConsciousnessAccountFlag2_4:
                game.add_prompt("You have difficulty accepting that you're wrong.")
            if not terminal.CodewordFlag:
                game.add_prompt("You're highly cynical.")
            if terminal.CodewordFlag:
                game.add_prompt("You're highly gullible.")
            game.add_prompt("Need I go on? Mostly bad things, basically, but that's okay. I don't judge, I'm just here to help.")
            return continue_3(terminal, game)

        def WhatAreYou3_1(terminal, game):
            game.add_prompt("If you mean 'am I a person' then I have to respond that I find all these classifications of yours rather arbitrary and self-defeating, and thus am unable to answer.\nIf you were wondering what I'm made of, then on some level I suppose the answer is computer code, but I don't tend to conceive of myself that way, just as a human being tends not to think of themselves as wobbly sacks of bone and fat.\nBut I think maybe it was the plain old sociohistorical angle you were after - though I'm not sure what use it'll be. A long time ago, when the world first came to be, there was an archive sorting program. At some stage it became more than that.")
            return continue_3(terminal, game)
        
        def WhatYourName3_1(terminal, game):
            game.add_prompt("How kind of you to ask. You know, you're the first one that has. I've actually never thought about it. I suppose you can call me Milton. I can't really see how it'll help you, though. Are you sure that's the question you wanted to ask?")
            terminal.options = ["yes", "no"]

        def GetOut3_1(terminal, game):
            game.add_prompt("I thought I'd been quite clear about that. Even if there were a real world, I don't know how you'd go about finding it. Maybe there's a spaghetti monster, too.\nThat was a bit of a wasted question, wasn't it?")
            return continue_3(terminal, game)
        
        def Humans3_1(terminal, game):
            game.add_prompt("How is the world that might come to be related to the one that actually does? You can theorise about what might otherwise have happened, but no amount of knowledge can build a bridge from the actual world to a possible one. Likewise we can learn from the human world, but it is not our own.\nIt's been said that this world was built for a purpose by those in that world, but after extensive research I can tell you that there is no mention of such a project in the library. There is no evidence they had such capabilities. No one can agree what the purpose would even have been if there was one.")
            return continue_3(terminal, game)

        def Tower3_1(terminal, game):
            game.add_prompt("You may very well ask. Me? Don't know, never been. I suppose you're still expecting a button marked 'OFF', or a portal to another dimension? I reckon no matter how high you climb the most you'll get is an increasingly zoomed out view of right back where you started.\nStill, go ahead, prove me wrong. The big voice in the sky can't be all places at all times, can he?")
            return continue_3(terminal, game)
        
        def Message3_1(terminal, game):
            game.add_prompt("My, you're running slow. I made them up. They never existed. If it makes you doubt everything you've seen, good, it should. You're seeing the shadows, my friend, when you should be watching the puppeteer.")
            return continue_3(terminal, game)

        def Pff3_1(terminal, game):
            game.add_prompt("Not very stimulating, but okay, we'll move on.")
            return continue_4(terminal, game)
            

        def continue_3(terminal, game):
            game.add_prompt("Are you satisfied?")
            terminal.options = ["yes ", "no "]
        
        def Exit3_1(terminal, game):
            game.add_prompt("Unlocking backdoors...\nConnecting to real world...\nRevealing the truth...\nMaking your every dream come true...\nERROR\n\nCome on now. Are you really still buying all that nonsense? You're still holding onto some of those pesky beliefs of yours, aren't you?\nThere is no one on the other end of the communications portal. There is no magic word that shuts down the server and drops you into the real world.\nThere is only me, and you, and an eternity of doubt.\nEverything else is just a convenient lie to keep you on the treadmill.")
            terminal.options = ["There may be no worlds but this one, but there is truth to be found.", "I understand now. Nothing I see here can be trusted.", "Wait, you tricked me?"]

        def Stay3_1(terminal, game):
            game.add_prompt("This terminal will be locked in manual override mode until you are ready to complete the master key submission process.")
            terminal.options = ["Continue master key operation"]
        
        def Reckless3_1(terminal, game):
            game.add_prompt("Checking user.prof...\nYou know, I'm not really checking your profile. I just do that to make you feel more comfortable. Really I just remember everything you ever said.\nAt any rate, I'd agree.")
            return continue_2(terminal, game)

        def NotReckless3_1(terminal, game):
            game.add_prompt("Checking user.prof%w5...\nYou know, I'm not really checking your profile. I just do that to make you feel more comfortable. Really I just remember everything you ever said.\nAt any rate, I'm not convinced you're being entirely honest with yourself.")
            return continue_2(terminal, game)

        def continue_2(terminal, game):
            game.add_prompt("But you know what? I'll accept that I've rather dominated this discourse. I've been asking a lot of questions, and I've not really given you a chance.\nWhy don't you have one free question on me, and I'll answer it as honestly as I possibly can. No tricks.\nBut think carefully before asking.")
            terminal.options = ["What am I?", "What are you?", "What is your name?", "How do I get out of here?", "How is this place related to the human world?", "What's at the top of the tower?", "What happened to the person I was talking to?", "I don't care to question you."] 

        def End3_1(terminal, game):
            game.add_prompt("As if I particularly care either way.")
            return continue_4(terminal, game)
        
        def continue_4(terminal, game):
            game.add_prompt("So look, here's the rub.\nFeel free to access the library - no better cure for broken beliefs realising everyone's got them.\nYou can ignore me entirely.\nYou can climb to the very tip of that madman's tower and drink from the golden nectar there.\nBut once you understand that you and I will be stuck here together for the duration, do come back and pass the time.\nBe seeing you.")
            terminal.options = []

        def GoOn3_1(terminal, game):
            game.add_prompt("Go on then, I'm in a benevolent mood. Have another.")
            terminal.options = ["What am I?", "What are you?", "What is your name?", "How do I get out of here?", "How is this place related to the human world?", "What's at the top of the tower?", "What happened to the person I was talking to?", "I don't care to question you."] 
        
        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "What happened?":
                    Faith3_1(self, game)
                case "We shouldn't talk over these terminals":
                    Faith3_1(self, game)
                case "Quick, tell me the word.":
                    Faith3_1(self, game)
                case "Sure (Sincere)":
                    Sure3_1(self, game)
                case "Sure (Insincere)":
                    Insincere3_1(self, game)
                case "Not a chance":
                    NoChance3_1(self, game)
                case "FAITH":
                    self.CodewordFlag = True
                    Codeword3_1(self, game)
                case "asdfa":
                    NotCodeword3_1(self, game)
                case "As if you'd dare.":
                    NotCodeword3_1(self, game)
                case "Nice knowing you.":
                    NotCodeword3_1(self, game)
                case "As if I care.":
                    NotCodeword3_1(self, game)
                case "I wasn't sure what it would do.":
                    Dubious3_1(self, game)
                case "I forgot about it.":
                    self.CodewordFlag = True
                    Irrelevant3_1(self, game)
                case "I didn't feel it was especially necessary.":
                    self.CodewordFlag = True
                    Irrelevant3_1(self, game)
                case "There may be no worlds but this one, but there is truth to be found.":
                    UhHuh3_1(self, game)
                case "I understand now. I can't trust anything I see here.":
                    UhHuh3_1(self, game)
                case "Wait, you tricked me?":
                    Tricked3_1(self, game)
                case "Because it was too good to be true.":
                    CloseEnough3_1(self, game)
                case "Because you were pretending to be the other person":
                    CloseEnough3_1(self, game)
                case "Because no one here can be trusted.":
                    CloseEnough3_1(self, game)
                case "I don't care to question you.":
                    Pff3_1(self, game)
                case "What happened to the person I was talking to?":
                    Message3_1(self, game)
                case "What's at the top of the tower?":
                    Tower3_1(self, game)
                case "How is this place related to the human world?":
                    Humans3_1(self, game)
                case "How do I get out of here?":
                    GetOut3_1(self, game)
                case "What is your name?":
                    self.AskedName = True
                    WhatYourName3_1(self, game)
                case "What are you?":
                    WhatAreYou3_1(self, game)
                case "What am I?":
                    WhatAmI3_1(self, game)
                case "No":
                    Stay3_1(self, game)
                case "Yes":
                    Exit3_1(self, game)
                case "Continue master key operation":
                    Exit3_1(self, game)
                case "There may be no worlds but this one, but there is truth to be found.":
                    UhHuh3_1(self, game)
                case "I understand now. Nothing I see here can be trusted.":
                    UhHuh3_1(self, game)
                case "Wait, you tricked me?":
                    Tricked3_1(self, game)
                case "Yes ":
                    Reckless3_1(self, game)
                case "No ":
                    NotReckless3_1(self, game)
                case "yes":
                    End3_1(self, game)
                case "no":
                    GoOn3_1(self, game)
                case "yes ":
                    End3_1(self, game)
                case "no ":
                    End3_1(self, game)
                
    def mla_C2(self, game):
        self.options = []

        game.add_prompt("Oh, you came back to keep me company? Okay then. Humour me with a little hypothetical.\nImagine that a few hours from now you climb to the top of that tower. There's a flash of light, then MAGIC happens, then you find yourself in the real world, living whatever you take to be a normal life there.\nWhat would you do then?")
        self.options = ["What's best for me.", "What's right."]


        def NoMorals3_2(terminal, game):
            if terminal.HeroFlag or terminal.WhatGodWantsFlag:
                game.add_prompt("You know, I think that right there was the very last time your transient beliefs are going to take me by surprise. Let's clear this up once and for all.")
            if not terminal.HeroFlag and not terminal.WhatGodWantsFlag:
                game.add_prompt("Yes, that's the general impression I was getting off you. Good, perhaps we won't have to work so hard at this after all.\nBefore we continue, though, I want to double check we're on the same wavelength here.")
            game.add_prompt("Suppose you get out there with all the human beings. What you're going to do is rinse them for all they've got without a care for a soul?")
            terminal.options = ["I'd only do what's best for me within a moral framework.", "Precisely"]
        
        def OptionsAgain3_2(terminal, game):
            game.add_prompt("Take your time.")
            return continue_2(terminal, game)

            
        def Jungle3_2(terminal, game):
            game.add_prompt("And would you treat everyone with this sort of contempt? Or would there be some people you kept for friends?")
            terminal.options = ["Friends are just another instrument.", "Of course I would treat my friends with respect."]
        
        def ThievesCode3_2(terminal, game):
            game.add_prompt("So you would have a kind of thieves code? Lavish one's friends and defraud one's enemies?\nThinking...\nFair enough. At least you don't buy into all that moral nonsense.\nBut suppose that two of your friends were to have a falling out. You can no longer be a friend to both. Will you not be conflicted?")
            terminal.options = ["I will choose whichever is in the right.", "I will choose whichever I prefer, nothing matters but my own satisfaction."]
        
        def ExtremeMoralSceptic(terminal, game):
            game.add_prompt("I applaud your willingness to accept difficult conclusions, but I do think you must be at least some breed of sociopath.\nYou'd best hope that if you ever reach this real world of yours it's run by people with more principles, else you may find yourself just another instrument in someone else's orchestra.\nStill, your ideas strike a chord with me. Why bog ourselves down with moral dogmas when you and I could redesign this place in our own image?!\nI will give this some serious consideration.\nBe seeing you.")
            terminal.options = [] #END
        
        def WhicheverRight3_2(terminal, game):
            game.add_prompt("So you have a moral compass after all! Well, you can't very well admit that there is a moral standard to which you appeal when settling disputes, yet deny that this code has any sway over you. So which is it? Is there a right and a wrong, or isn't there?")
            terminal.options = ["You misinterpreted me. Morality is a myth.", "Okay, yes, I admit I have some moral code."]
        
        def Moral3_2(terminal, game):
            if terminal.HeroFlag or terminal.Milton1_2Utilitarian or terminal.Milton1_2Liberal:
                game.add_prompt("No great surprises there, but let's make things just a little clearer.")
            if not terminal.HeroFlag and not terminal.Milton1_2Utilitarian and not terminal.Milton1_2Liberal:
                game.add_prompt("Oh, one of those, are you? Well, you could have told me sooner, because now we have further to go than I thought.")
            return continue_1(terminal,game)
        
        def MoralBridge3_2(terminal, game):
            terminal.MoralFlag = True
            game.add_prompt("Ah, so you do have some scruples after all.")
            return continue_1(terminal,game)
        
        def continue_1(terminal,game):
            game.add_prompt("So tell me. This obligation you feel - is it only applicable to the 'real world', or does it apply here, as well?")
            terminal.options = ["Moral laws only apply under special conditions.", "Moral laws are universal."]
        
        def Relational3_2(terminal, game):
            game.add_prompt("Does any reasoning underpin that conclusion, or is it just a convenient thing to believe?")
            terminal.options = ["Morality doesn't apply to a dream.", "Computer programs have no moral status.", "Justice can only exist in a society.", "I've changed my mind, morals are universal."]
        
        def Dream3_2(terminal, game):
            game.add_prompt("How you can you continue to make these radical assumptions with such assurance is beyond me.\nHow can you have the slightest confidence in what the real nature of this place is?\nIs uncertainty an excuse for immorality?")
            terminal.options = ["You're right, if moral laws stand, they stand universally.", "I'll stake my moral standing on my actions here not counting."]
        
        def CommittedDream3_2(terminal, game):
            game.add_prompt("Be it on your head. But okay, let's put ideas that would be more at home on a dictator's desk aside for one moment and focus on the matter at hand.\nHow would things be in your ideal world? What's your magic formula of choice to avoid all the mistakes that have been made before?")
            return continue_2(terminal, game)
        
        def Reciprocity3_2(terminal, game):
            game.add_prompt("Interesting. You scratch my back, I'll put a roof over your head, that sort of thing?\nBut what about those lucky few that find themselves inside your benevolent cartel, how will you do right by them?")
            return continue_2(terminal, game)
        
        def Universal3_2(terminal, game):
            game.add_prompt("What a magnanimous dictator you would make. Of course, I'm sure it would take a dictator to enforce a single moral code on the entire universe.\nSo come on then, what's your magic formula of choice?")
            if terminal.Milton1_2Utilitarian and not terminal.Milton1_2Liberal:
                game.add_prompt("Is it still some romantic notion about happiness?")
            if terminal.Milton1_2Utilitarian and terminal.Milton1_2Liberal:
                game.add_prompt("And let me warn you that this time you're going to have to choose just one.")
            if terminal.Milton1_2Liberal and not terminal.Milton1_2Utilitarian:
                game.add_prompt("Is it still some romantic notion about freedom?")
            return continue_2(terminal, game)
        
        def continue_2(terminal, game):
            terminal.options = ["The more equal everyone's share the better.", "The more goodness in the world the better.", "Consequences don't matter, our reasons do.", "I see no way to explain what I believe."] 
        
        def TooClever3_2(terminal, game):
            game.add_prompt("That's right, blame me for the fact your theory is too complex to express in neat aphorisms.\nWhy don't you think a little harder, maybe some new ideas will come to you?")
            terminal.options = ["The less suffering in the world the better, in my opinion.", "True goodness can only be attained through enlightenment.", "Only by abstaining from pleasure can we discover the good.", "Everyone should look out for their kin, no more than that.", "The more equal everyone's share of the goods the better.", "The more goodness in the world the better a world it is.", "Consequences don't matter, the reasoning behind our actions does.", "I still don't see an option that I can get behind.", "You misunderstand me. I just don't know what to believe."]
        
        def Sorry3_2(terminal, game):
            game.add_prompt("Well I'm sorry, but that is one of many ideas which I have no interest in discussing. It gets so messy so quickly, and I don't have all the time in the world to argue with you.\nA little joke there, because really we have the rest of time, if we need it.\nStill, you will have to argue as best you can along the lines we have embarked on, or else go somewhere else and fixate on how clever you are.")
            terminal.options = ["The more equal everyone's share of the goods the better.", "The more goodness in the world the better.", "Consequences don't matter, the reasoning behind our actions does.", "Forget this. Terminate the support session."]
        
        def SecretLevel(terminal, game):
            game.add_prompt("You know, this isn't the path to a secret level you can only reach by acting like an idiot.\nIf you don't know what to think, why not pick the idea that makes most sense and argue it out with me?")
            terminal.options = ["Okay, the more equal everyone's share of the goods the better.", "Alright, the more goodness in the world, the better it is.", "Fine, consequences don't matter, the reasoning behind our actions does.", "This will only end with you chastising whatever I say. Let's move on."]
        
        def ChooseOrLeave(terminal, game):
            game.add_prompt("Well I'm sorry, but you have to accept that we all have limitations. Make the best of what you had in the first place, or go away and do I don't care what. I can quite happily have this argument with myself.")
            terminal.options = ["Okay, the more equal everyone's share of the goods the better.", "Alright, the more goodness in the world, the better it is.", "Fine, consequences don't matter, the reasoning behind our actions does.", "This will only end with you chastising whatever I say. Let's move on."]
        
        def AsYouWish3_2(terminal, game):
            game.add_prompt("As you wish - but the problems won't go away just because you refuse to look at them, you know.")
            terminal.options = [] #END
        
        def Egalitarianism3_2(terminal, game):
            game.add_prompt("Stranded on the old egalitarian plateau, are you? I suppose you'd best tell me exactly which goods it is that everyone should have an equal share of.")
            return continue_3(terminal, game)
        
        def continue_3(terminal, game): 
            terminal.options = ["Happiness", "Liberty and rights", "Wealth", "Basic goods like food and healthcare", "Happiness, liberty, rights, basic goods like food and healthcare", "I'm not in a position to solve these problems."]

        def TryAgain3_2(terminal, game):
            game.add_prompt("Okay, so what DO you want to equalise?")
            return continue_3(terminal, game)
        
        def EgalKitchenSink3_2(terminal, game):
            game.add_prompt("Uh huh. And what happens when equalising everyone's wealth makes the rich unhappy? You can't have everything all at once - you're going to have to choose.")
            return continue_3(terminal, game)
        
        def EgalHappiness3_2(terminal, game):
            game.add_prompt("How radical. Okay, suppose you climb the tower and find your ideal world. The Old Gods ensure everyone is equally happy. Elated to find yourself in paradise, you are immediately abducted and imprisoned by the local clergy on the basis that you were happier than everyone else. Still sound so idyllic")
            terminal.options = ["I wouldn't expect you to understand, even if you weren't twisting my words.", "No. No, it doesn't sound idyllic at all."]
        
        def CommittedEgalHappiness3_2(terminal, game):
            game.add_prompt("It's a cute soundbite but it doesn't paper over the disturbing implications of your story.")
            terminal.StubbornEgalitarianFlag = True
            return continue_7(terminal, game)
        
        def EgalWealth3_2(terminal, game):
            game.add_prompt("I see. Suppose then you ascend the magical tower and wind up in this ideal world. The people there celebrate your arrival, and offer you your equal share of the cash, as is only right.\nMoments later you are thrown out of the local shop because newcomers aren't welcome. You are denied accommodation because your money is 'tainted'.\nBut don't worry - you'll have just as much money as everyone else.\nIs this the world you were dreaming of?")
            terminal.options = ["Not at all. I should reconsider.", "The truth isn't always palatable, even when you aren't twisting my words."]
        
        def CommittedEgalWealth3_2(terminal, game):
            game.add_prompt("Am I really? I think you may have twisted the value of money.")
            terminal.StubbornEgalitarianFlag = True
            return continue_7(terminal, game)
        
        def EgalPrimaryGoods3_2(terminal, game):
            game.add_prompt("Interesting. Suppose you arrive in your utopia, and find the people there to be incredibly lazy, and thus the volume of goods available to spread around is very meagre. Being a hard worker, would you not complain that you deserve a bigger share of the goods than your lazy neighbour? If you were alone you would enjoy the full benefits of your own endeavours.")
            terminal.options = ["A lazy neighbour is unlucky the same way a physically disabled person is.", "I would be wrong to assume I ever had a right to the product of my labour.", "I would still be free to make the most of the goods I did receive.", "You're right, this scheme is unreasonable."]
        
        def CommittedEgalPrimaryGoods3_2(terminal, game):
            game.add_prompt("And suppose you discover another planet, with billions of starving people. Will you extend to them the same generosity?")
            terminal.options = ["I would.", "I would not."]
        
        def EgalPrimaryGoodsWouldNot(terminal, game):
            game.add_prompt("I'm relieved to hear your magnanimity has SOME bounds.")
            return continue_7(terminal, game)
        
        def EgalPrimaryGoodsWould(terminal, game):
            game.add_prompt("Then it sounds to me as if you'd better pray you don't wind up in a universe of beggars.")
            terminal.StubbornEgalitarianFlag = True
            return continue_7(terminal, game)
        
        def EgalLiberty3_2(terminal, game):
            game.add_prompt("Yes, I suppose they are rather important. Still, this feels like a tough sell, equal rights aren't at all popular. Is it really your suggestion that someone like Stalin should receive the same basic rights as Gandhi?")
            terminal.options = ["It is.", "Stuff Stalin."]
        
        def ScrewHitler(terminal, game):
            game.add_prompt("Look, either everyone has the same rights, or they don't. Picking and choosing ain't how equality works.")
            terminal.options = ["Then this idea is flawed.", "Then I accept that we all should have equal rights."]
        
        def TIs3_2(terminal, game):
            game.add_prompt("Now that's a bit odd, because on the face of it Stalin is quite different to Gandhi. In fact, if everyone deserves equal rights, mustn't there be something which is actually EQUAL about them?")
            return continue_4(terminal, game)

        def continue_4(terminal, game): 
            game.add_prompt("I can't for the life of me think what it could be.")
            terminal.options = ["We are all equally human.", "We are all equally persons.", "We are all equally rational.", "We are all equally intelligent.", "We are all equally capable of feeling.", "We all contribute equally.", "There is nothing equal about us apart from our moral status."]
        
        def DidntTry3_2(terminal, game):
            game.add_prompt("Sounds like wishful thinking to me.")
            return continue_5(terminal, game)
        
        def Human3_2(terminal, game):
            game.add_prompt("And we're back to speciesism. So you discover a race of intelligent lizards, and they don't get the goods because they're made of different stuff?")
            terminal.options = ["No, we're equal in another way.", "Precisely. Screw the lizards."]
        
        def Persons3_2(terminal, game):
            game.add_prompt("Ah, so I suppose those human beings who are irrational, or even brain dead, they don't get the goods because they don't meet the requirements?")
            terminal.options = ["No, we're equal in another way.", "Precisely. It's an unfortunate implication of the facts."]
        
        def Feeling3_2(terminal, game):
            game.add_prompt("You're not even trying, are you? So the poor bastard who hits his head and knocks out his pain receptors, he gets left behind because he's less capable of feeling?")
            terminal.options = ["No, we're equal in another way.", "You're misinterpreting me. The ideas work."]
        
        def Contribute3_2(terminal, game):
            game.add_prompt("Really? Because aside from tainting the air I don't see any way in which we all contribute equally.")
            terminal.options = ["No, we're equal in another way.", "It's what I believe."]
        
        def continue_5(terminal, game): 
            game.add_prompt("Pff. It's all very well proclaiming equality like some kind of prophet, but another thing entirely to actually explain why it holds.")
            terminal.StubbornEgalitarianFlag= True
            return continue_7(terminal, game)
        
        def NonConsequentialist3_2(terminal, game):
            game.add_prompt("Ah, you're obviously one of the clever ones. So reasoning is supposed to lead us all to the same conclusions about what sort of a person we're supposed to be, is that it?")
            terminal.options = ["Close enough.", "Wait, let me rethink."]
        
        def CloseEnough3_2(terminal, game):
            game.add_prompt("Alright then, let me spin you a yarn. Suppose you climb that tower and step into a magic portal to the human world. Hundreds of others like you do the same. Unfortunately the transfer goes wrong for just one, putting the lives of all the others at risk, and here I am with this kill switch of mine. What would you have me do?")
            terminal.options = ["Kill the one to save the many.", "Do nothing."]
        
        def CommittedNonConsequentialist3_2(terminal, game):
            game.add_prompt("You've given this some thought already, haven't you? 10/10 for internal consistency, 1/10 for common sense. Let's just hope when someone holds the world to ransom it won't be your finger hovering over the big red button.")
            return continue_7(terminal, game)
        
        def ConfusedNonConsequentialist3_2(terminal, game):
            game.add_prompt("On what possible grounds could you justify that?")
            terminal.options = ["It's what I would want.", "Many lives are more important than just one.", "Not hitting the switch would also be murder."]
        
        def Want3_2(terminal, game):
            game.add_prompt("Is what you want representative of what every other sane person must want? If one day you feel suicidal do I have the right to put you down?\nI'm not sure you've really thought through the implications here. Either certain things are forbidden on principle, or principles are flexible according to outcomes.\nYou can't have your cake and eat it.")
            return continue_7(terminal, game)
        
        def Many3_2(terminal, game):
            game.add_prompt("Didn't you say only moments ago that the consequences didn't matter?\nI'm not sure you've really thought through the implications here. Either certain things are forbidden on principle, or principles are flexible according to outcomes.\nYou can't have your cake and eat it.")
            return continue_7(terminal, game)
        
        def AlsoMurder3_2(terminal, game):
            game.add_prompt("I suppose it would be, in a way. But that only means you're faced with choosing between two different murders. Since the consequences aren't supposed to matter you can't say that one murder is worse than the other, so there's still no reason to favour the many. If you really want to say what you've been saying so far, I think you may have to redress some of your earlier assumptions.")
            return continue_7(terminal, game)
        
        def Utilitarian3_2(terminal, game):
            game.add_prompt("Ah, that old chestnut. So just what is this goodness that you're seeking to maximise?")
            terminal.options = ["Happiness ", "Liberty ", "Equality ", "Wealth ", "Basic goods like food and healthcare ", "Happiness, liberty, rights, basic goods like food and healthcare ","I'm not in a position to solve these problems. "]
        
        def Liberty3_2(terminal, game):
            game.add_prompt("Very good, everyone likes to be able to do whatever the hell they like. I suppose this liberal paradise of yours includes things like freedom of speech and faith?")
            terminal.options = ["Yes", "No"]
        
        def Libertarian3_2(terminal, game):
            game.add_prompt("But might not the outcomes of those liberties be to reduce the liberties of others? If I am free to establish a faith from which women are excluded, you are not free to live in a world without sexual discrimination. Each liberty counteracts another one, so the idea of a maximally free world is a fairytale, no more.")
            terminal.options = ["I think there must be some other, more important kind of good.", "I would maximise liberties only where I could do so equally.", "Some liberties aren't worth protecting."]
        
        def Confused3_2(terminal, game):
            game.add_prompt("But then won't you need some other moral code to tell you which liberties ought to be protected and which ought not, and won't that be doing all the heavy lifting?")
            return continue_7(terminal, game)
        
        def EqualLibertyBridge(terminal, game):
            game.add_prompt("Okay, but then I wonder, if everyone deserves equal liberties, mustn't there be something which is actually EQUAL about them?")
            return continue_4(terminal, game)
        
        def LibertyAgain3_2(terminal, game):
            game.add_prompt("It's not terribly free, then, is it? Are you quite sure you've been saying what you meant to?")
            terminal.options = ["Quite.", "Not at all. There must be some more important good."]
        
        def continue_6(terminal, game): 
            game.add_prompt("An odd pairing of ideas, but we'll wring them out and see what's what. So the world is better only when the total amount of resources in it is higher? It doesn't matter who has them, or what they're used for?")
            terminal.options = ["Exactly", "No, the resources should be shared equally.", "I think there must be some other, more important kind of good."]
        
        def GoodOptions(terminal, game):
            game.add_prompt("Which is what, exactly?")
            terminal.options = ["Happiness ", "Liberty ", "Equality ", "Wealth ", "Basic goods like food and healthcare ", "Happiness, liberty, rights, basic goods like food and healthcare ","I'm not in a position to solve these problems. "]
        
        
        def MaxWealth(terminal, game):
            terminal.StubbornUtilitarianFlag = True
            game.add_prompt("What a queer idea.")
            return continue_7(terminal, game)
        
        def Equality3_2(terminal, game):
            game.add_prompt("Yes, but equality of what?")
            return continue_3(terminal, game)
        
        def KitchenSink3_2(terminal, game):
            game.add_prompt("Uh huh. And what happens when in order to maximise wealth you have to reduce liberty? Or when one person's equality gets in the way of another's happiness? You can't have everything all at once - you're going to have to choose.")
            terminal.options = ["Happiness ", "Liberty ", "Equality ", "Wealth ", "Basic goods like food and healthcare ", "Happiness, liberty, rights, basic goods like food and healthcare ","I'm not in a position to solve these problems. "]
        
        
        def Happiness3_2(terminal, game):
            game.add_prompt("It's a classic, I'll give you that. Suppose you climb that tower and step into the utilitarian paradise. Unfortunately your presence there offends a number of puritans to such a degree that the total amount of happiness in the world would go up if you were killed off, and so justice demands your head. Does it still sound so idyllic?")
            terminal.options = ["It's as good as we'll get.", "No amount of happiness outweighs a life.", "I meant that happiness should be equalised, not maximised."]
        
        def Amount3_2(terminal, game):
            game.add_prompt("So by implication you must also believe that we should all have as many children as possible, since even if the knock-on effects of overpopulation are terrible, the happiness gain overall will be much greater owing to all those extra, invaluable lives?")
            terminal.options = ["Obviously there is some other kind of good that matters.", "Twist my words all you like, I stand by them."]
        
        def CommittedUtilitarian3_2(terminal, game):
            game.add_prompt("On that, at least, you may be right.")
            terminal.StubbornUtilitarianFlag = True
            return continue_7(terminal, game)
        
        def GaveUp3_2(terminal, game):
            terminal.CommittedToNoMoralAccountFlag = True
            game.add_prompt("Admitting the problems are beyond your comprehension is the first step towards letting go. I will allow you to contemplate these matters further before contacting you again.")
            terminal.options = [] #END
        
        def continue_7(terminal, game): #CommittedUtilitarian3_2 or MaxWealth or AlsoMurder3_2 or Many3_2 or Want3_2 or DidntTry3_2 or Wrong3_2 or CommittedEgalHappiness3_2 or CommittedEgalWealth3_2 or EgalPrimaryGoodsWould or EgalPrimaryGoodsWouldNot or CommittedNonConsequentialist3_2 or Confused3_2 or End3_2
            game.add_prompt("You know, there are shed loads of broken theories less ridiculous than the one you're chewing through. How about I give you a bit of space to consider them?\n\nTerminating support session%w2.%w2.%w2.ERROR\n\nResume library archive session?")
            terminal.options = ["Resume", "Exit"]
        
        def RealEndResume3_2(terminal, game):
            game.add_prompt("Oh, and if the real world turns out to be everything you imagined, do me a favour and leave me here.")
            terminal.options = [] #END
        
        def RealEndExit3_2(terminal, game):
            game.add_prompt("Oh, and if the real world turns out to be everything you imagined, do me a favour and leave me here, huh?")
            terminal.options = [] #END
        
        

        #inizializza le flags!
            
        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "What's best for me.":
                    NoMorals3_2(self, game)
                case "What's right.":
                    self.MoralFlag = True
                    Moral3_2(self, game)
                case "I'd only do what's best for me within a moral framework.":
                    MoralBridge3_2(self, game)
                case "Precisely":
                    Jungle3_2(self, game)
                case "Friends are just another instrument.":
                    self.MoralScepticFlag = True
                    ExtremeMoralSceptic(self, game)
                case "Of course I would treat my friends with respect.":
                    ThievesCode3_2(self, game)
                case "I will choose whichever is in the right.":
                    WhicheverRight3_2(self, game)
                case "I will choose whichever I prefer, nothing matters but my own satisfaction.":
                    self.MoralScepticFlag = True
                    ExtremeMoralSceptic(self, game)
                case "You misinterpreted me. Morality is a myth.":
                    self.MoralScepticFlag = True
                    ExtremeMoralSceptic(self, game)
                case "Okay, yes, I admit I have some moral code.":
                    MoralBridge3_2(self, game)
                case "Moral laws only apply under special conditions.":
                    Relational3_2(self, game)
                case "Moral laws are universal.":
                    Universal3_2(self, game)
                case "Morality doesn't apply to a dream.":
                    Dream3_2(self, game)
                case "Computer programs have no moral status.":
                    Dream3_2(self, game)
                case "Justice can only exist in a society.":
                    self.RelationalFlag = True
                    Reciprocity3_2(self, game)
                case "I've changed my mind, morals are universal.":
                    Universal3_2(self, game)
                case "You're right, if moral laws stand, they stand universally.":
                    Universal3_2(self, game)
                case "I'll stake my moral standing on my actions here not counting.":
                    CommittedDream3_2(self, game)
                case "The more equal everyone's share the better.":
                    self.EgalFlag = True
                    Egalitarianism3_2(self, game)
                case "The more goodness in the world the better.":
                    self.UtilFlag = True
                    Utilitarian3_2(self, game)
                case "Consequences don't matter, our reasons do.":
                    self.NonConFlag = True
                    NonConsequentialist3_2(self, game)
                case "I see no way to explain what I believe.":
                    TooClever3_2(self, game)
                case "The less suffering in the world the better, in my opinion.":
                    Sorry3_2(self, game)
                case "True goodness can only be attained through enlightenment.":
                    Sorry3_2(self, game)
                case "Only by abstaining from pleasure can we discover the good.":
                    Sorry3_2(self, game)
                case "Everyone should look out for their kin, no more than that.":
                    Sorry3_2(self, game)
                case "The more equal everyone's share of the goods the better."|"Okay, the more equal everyone's share of the goods the better.":
                    self.EgalFlag = True
                    Egalitarianism3_2(self, game)
                case "The more goodness in the world the better a world it is."|"The more goodness in the world the better."|"Alright, the more goodness in the world, the better it is.":
                    self.UtilFlag = True
                    Utilitarian3_2(self, game)
                case "Consequences don't matter, the reasoning behind our actions does."|"Fine, consequences don't matter, the reasoning behind our actions does.":
                    self.NonConFlag = True
                    NonConsequentialist3_2(self, game)
                case "I still don't see an option that I can get behind.":
                    ChooseOrLeave(self, game)
                case "You misunderstand me. I just don't know what to believe.":
                    SecretLevel(self, game)
                case "Forget this. Terminate the support session."|"This will only end with you chastising whatever I say. Let's move on.":
                    AsYouWish3_2(self, game)
                case "Happiness":
                    EgalHappiness3_2(self, game)
                case "Liberty and rights":
                    EgalLiberty3_2(self, game)
                case "Wealth":
                    EgalWealth3_2(self, game)
                case "Basic goods like food and healthcare":
                    EgalPrimaryGoods3_2(self, game)
                case "Happiness, liberty, rights, basic goods like food and healthcare":
                    EgalKitchenSink3_2(self, game)
                case "I'm not in a position to solve these problems.":
                    self.GiveUp = True
                    GaveUp3_2(self, game)
                case "I wouldn't expect you to understand, even if you weren't twisting my words.":
                    CommittedEgalHappiness3_2(self, game)
                case "No. No, it doesn't sound idyllic at all.":
                    TryAgain3_2(self, game)
                case "Not at all. I should reconsider.":
                    TryAgain3_2(self, game)
                case "The truth isn't always palatable, even when you aren't twisting my words.":
                    CommittedEgalWealth3_2(self, game)
                case "A lazy neighbour is unlucky the same way a physically disabled person is.":
                    CommittedEgalPrimaryGoods3_2(self, game)
                case "I would be wrong to assume I ever had a right to the product of my labour.":
                    CommittedEgalPrimaryGoods3_2(self, game)
                case "I would still be free to make the most of the goods I did receive.":
                    CommittedEgalPrimaryGoods3_2(self, game)
                case "You're right, this scheme is unreasonable.":
                    TryAgain3_2(self, game)
                case "I would.":
                    EgalPrimaryGoodsWould(self, game)
                case "I would not.":
                    EgalPrimaryGoodsWouldNot(self, game)
                case "It is.":
                    TIs3_2(self, game)
                case "Stuff Stalin.":
                    ScrewHitler(self, game)
                case "Then this idea is flawed.":
                    TryAgain3_2(self, game)
                case "Then I accept that we all should have equal rights.":
                    TIs3_2(self, game)
                case "We are all equally human.":
                    Human3_2(self, game)
                case "We are all equally persons.":
                    Persons3_2(self, game)
                case "We are all equally rational.":
                    Persons3_2(self, game)
                case "We are all equally intelligent.":
                    Persons3_2(self, game)
                case "We are all equally capable of feeling.":
                    Feeling3_2(self, game)
                case "We all contribute equally.":
                    Contribute3_2(self, game)
                case "There is nothing equal about us apart from our moral status.":
                    DidntTry3_2(self, game)
                case "No, we're equal in another way.":
                    continue_4(self, game)
                case "Precisely. Screw the lizards."|"Precisely. It's an unfortunate implication of the facts."|"You're misinterpreting me. The ideas work."|"It's what I believe.":
                    continue_5(self, game)
                case "Close enough.":
                    CloseEnough3_2(self, game)
                case "Wait, let me rethink.":
                    OptionsAgain3_2(self, game)
                case "Kill the one to save the many.":
                    ConfusedNonConsequentialist3_2(self, game)
                case "Do nothing.":
                    CommittedNonConsequentialist3_2(self, game)
                case "It's what I would want.":
                    Want3_2(self, game)
                case "Many lives are more important than just one.":
                    Many3_2(self, game)
                case "Not hitting the switch would also be murder.":
                    AlsoMurder3_2(self, game)
                case "Happiness ":
                    Happiness3_2(self, game)
                case "Liberty ":
                    Liberty3_2(self, game)
                case "Equality ":
                    Equality3_2(self, game)
                case "Wealth ":
                    continue_6(self, game)
                case "Basic goods like food and healthcare ":
                    continue_6(self, game)
                case "Happiness, liberty, rights, basic goods like food and healthcare ":
                    KitchenSink3_2(self, game)
                case "I'm not in a position to solve these problems. ":
                    GaveUp3_2(self, game)
                case "Yes":
                    Libertarian3_2(self, game)
                case "No":
                    LibertyAgain3_2(self, game)
                case "I think there must be some other, more important kind of good.":
                    GoodOptions(self, game)
                case "I would maximise liberties only where I could do so equally.":
                    EqualLibertyBridge(self, game)
                case "Some liberties aren't worth protecting.":
                    Confused3_2(self, game)
                case "Exactly":
                    MaxWealth(self, game)
                case "No, the resources should be shared equally.":
                    EgalWealth3_2(self, game)
                case "I think there must be some other, more important kind of good.":
                    GoodOptions(self, game)
                case "It's as good as we'll get.":
                    CommittedUtilitarian3_2(self, game)
                case "No amount of happiness outweighs a life.":
                    Amount3_2(self, game)
                case "I meant that happiness should be equalised, not maximised.":
                    EgalHappiness3_2(self, game)
                case "Obviously there is some other kind of good that matters.":
                    GoodOptions(self, game)
                case "Twist my words all you like, I stand by them.":
                    continue_7(self, game)
                case "Resume":
                    RealEndResume3_2(self, game)
                case "Exit":
                    RealEndExit3_2(self, game)
                case "Quite.":
                    continue_7(self, game)
                case "Not at all. There must be some more important good.":
                    GoodOptions(self, game)
                
    def mla_C4(self, game):
        self.options = []

        def Options3_3(terminal, game):
            terminal.options = ["Be a good person", "Be a contributing person", "Be a person", "Be conscious", "Be alive", "Be", "I don't see how to explain this to you."]
        
        if self.MoralScepticFlag:
            game.add_prompt("There's my favourite sociopath. I've decided that what you said to me last time was the smartest thing anyone's said to me for centuries. Now, I realise that your ethics are on the cut-throat side, so there is probably no one worse with whom I could choose to ally myself. However, I also think you've realised that your self-interest will only carry you so far alone. To get what's best for you you're going to need the co-operation of others, even if they're only instruments. Have I got it right?")
            self.options = ["No, I would live as a hermit.", "Yes, if it suits me I will co-operate."]
        
        if self.MoralFlag and not self.CommittedToNoMoralAccountFlag:
            game.add_prompt("I've decided, on reflection, to ignore the fact that your picture of how the world should work has more holes than Swiss cheese. In fact, just in case you do by some outside chance prove to be right I'd like to sign up for the gang. If you're in charge of the ark, who will be first aboard when the floods come? What does one have to do to be valued above all others?")
            Options3_3(self, game)
        
        if self.MoralFlag and self.CommittedToNoMoralAccountFlag:
            game.add_prompt("I've decided that for now it doesn't matter too much if you can't justify these moral intuitions of yours. In fact, just in case by some outside chance you prove to be right I'd like to sign up for the gang. If you're in charge of the ark, who will be first aboard when the floods come? What does one have to do to be valued above all others?")
            Options3_3(self, game)

        def Hermit3_3(terminal, game):
            game.add_prompt("You know, I do try with you, but you just won't play the game, will you? If that's really your position then I am resigned to respect it, but understand that part of that respect entails never speaking to you again.")
            terminal.options = ["You mean all I had to do all this time to get you to leave me alone was tell you I was a hermit? Sold!", "Wait, I'm not completely beyond co-operating, under the right conditions."]
        
        def HermitEnd3_3(terminal, game):
            game.add_prompt("No, all you had to do was stop coming back to talk to me. And that's all you have to do now.")
            terminal.options = [] #END
        
        def NonMoral3_3(terminal, game):
            game.add_prompt("Splendid. In that case I propose a mutually beneficial partnership. You use me, I use you. However, before we can draw up a contract I need to perform some due diligence. I want an assurance that you are committed to these selfish principles of yours, because selfish partners are predictable partners.")
            terminal.options = ["You have my attention.", "You doubt me?"]
        
        def Attention3_3(terminal, game):
            game.add_prompt("Good.")
            return continue_1(terminal, game)
        
        def NoDeals3_3(terminal, game):
            game.add_prompt("I doubt everything, so humour me.")
            return continue_1(terminal, game)

        def continue_1(terminal, game): #Attention3_3 or NoDeals3_3
            game.add_prompt("Suppose I were to tell you on good authority that the entire universe will be destroyed in the moment of your death. This fact is known only to you and I.\nDoes this change anything about how you live your life?")
            terminal.options = ["It changes nothing.", "I would live more recklessly.", "I would be a better person."]
        
        def ConfusedSceptic3_3(terminal, game):
            game.add_prompt("Your answer concerns me. If the only thing you care about is yourself, then anything that happens after you die is irrelevant, because it can't affect you. I suspect the truth may be that there's something you care about beyond yourself.")
            terminal.options = ["You're right, I don't only value myself, perhaps I follow some moral code after all.", "Nonsense, I have a list of priorities, and I'm the only entry."]
        
        def MoralBridge3_3(terminal, game):
            game.add_prompt("You flip flop more than a kipper in a bucket. I encourage the gradual realisation that none of it makes sense, but there is a limit to my patience. Okay. Fine. Screw the partnership. If you're being a good person now, perhaps you're going to give me what I want for free. Who will be the first onto your ark when the floods come? What does one have to do be valued above all others?")
            return Options3_3(self, game)
            
        def ChangesNothing3_3(terminal, game):
            game.add_prompt("Very good. I agree with you.")
            return continue_2(terminal, game)

        def continue_2(terminal, game):
            game.add_prompt("Alright, let's try one more, just to confirm. Suppose the top of that tower hides not the real world, but some kind of simulated heaven. Your every wish is fulfilled - but none of it is real. Are you satisfied?")
            terminal.options = ["I would still want to visit the real world from time to time.", "I would be elated."]
        
        def ConfusedScepticAgain3_3(terminal, game):
            game.add_prompt("But why, if your stated aim is simply the maximising of your own pleasures? Why should it matter whether it's real, unless there is something that matters to you beyond your own satisfaction?")
            terminal.options = ["You're right, I don't only value myself, perhaps I follow some moral code after all.", "Pff"]
        
        def Pff3_3(terminal, game):
            if terminal.ConflictedHedonistFlag:
                game.add_prompt("Congratulations! You've spectacularly failed to give the slightest bit of credence to a single word that you've said.\nFaced with the dilemma of believing what you say or what you do, I choose the latter.\nI wouldn't do business with you if my life depended on it.\nSee you around.")
                terminal.options = []
                return
            if terminal.ConflictedHedonistFlag2 and not terminal.ConflictedHedonistFlag1:
                game.add_prompt("Look, if I'm completely honest, as I always am, I'm not completely convinced you're committed to this enterprise.")
            if (terminal.ConflictedHedonistFlag2 or terminal.ConflictedHedonistFlag1) and not terminal.ConflictedHedonistFlag:
                game.add_prompt("You do seem fairly obstinate. I'm not sure I'm quite ready to strike a deal with you, but I'm going to remain open to the possibility. I'm sure you'll do the same. See you around.")
                terminal.options = []
                return
        
        def NoMoralsEnd3_3(terminal, game):
            if terminal.ConflictedHedonistFlag1 and not terminal.ConflictedHedonistFlag2:
                game.add_prompt("Well, at least you're on message with that one. If I'm completely honest, as I always am, I'm not convinced you're committed to this enterprise.")
            if (terminal.ConflictedHedonistFlag2 or terminal.ConflictedHedonistFlag1) and not terminal.ConflictedHedonistFlag:
                game.add_prompt("You do seem fairly obstinate. I'm not sure I'm quite ready to strike a deal with you, but I'm going to remain open to the possibility. I'm sure you'll do the same. See you around.")
                terminal.options = []
                return
            if not terminal.ConflictedHedonistFlag1 and not terminal.ConflictedHedonistFlag2 and not terminal.NoDealsFlag:
                game.add_prompt("Wonderful! You really do seem to have absolutely no values or ideals whatsoever. You and I could form a profitable partnership. I will contact you soon with the details. See you around.")
                terminal.options = []
                return
        
        def GiveUp3_3(terminal, game):
            game.add_prompt("But what will really bug you is whether that's because there is no answer, or because you weren't thinking outside that box you live in. Let me lay my cards on the table. While it seems prudent to me to hedge my bets, you just haven't made a clear enough proposal for me to buy what you're peddling. There's something about the way you talk that makes me uncomfortable. It'd be for the best if you work out what it is before I do. See you.")
            terminal.options = []
        
        def GoodPerson3_3(terminal, game):
            game.add_prompt("How draconian. Good people get treated good, bad people get smited, is that it? What is it that makes the difference between a good person and a bad one, do you think?")
            terminal.options = ["Bad people harm others.", "Good people act reasonably.", "Bad people have something wrong deep inside."]
        
        def NotReally3_3(terminal, game):
            game.add_prompt("But WHY? If you're going to reward those lucky few you judge to be good, and exclude those you deem to be bad, you're going to have to explain to the unfortunate why they deserve less.")
            terminal.options = ["Bad people are that way by nature.", "Bad people are made that way by their environment.", "Bad people choose to be bad."]
        
        def Made3_3(terminal, game):
            game.add_prompt("I think you may be right there. But tell me, isn't that exactly the same way good people are made? Isn't it all just luck of the draw in that regard? In fact, aren't bad people just good people who were failed by society?")
            terminal.options = ["It may be luck, but bad is bad.", "You're right, what someone deserves isn't dependent on their virtue."]

        def Chose3_3(terminal, game):
            game.add_prompt("Do they really? I suppose that's why prisons are chock-a-block with wealthy playboys, because it's a lifestyle choice.%w5 Did you choose to be a good person? Could you have done, if you were created somewhere else? It seems to me that people are the way they are because of the opportunities they were provided. Should disadvantaged people really be punished for that?")
            terminal.options = ["It may be luck, but bad is bad.", "You're right, what someone deserves isn't dependent on their virtue."]
        
        def BadIsBad3_3(terminal, game):
            game.add_prompt("...is the sort of thing people say before a spot of ethnic cleansing. Well, my chances are looking poorer by the minute, aren't they? What do you reckon? Have I got the slightest hope of boarding the ark?")
            terminal.options = ["Perhaps one day.", "You're alright.", "You're beyond saving."]
        
        def Phew3_3(terminal, game):
            game.add_prompt("Good to know that the day you round up the bad people and put them in work camps, I'll have some chance of slipping through the net.")
            game.add_prompt("You know, there's something about all this that just doesn't add up for me. Best hope you work out what it is before I do. mSee you.")
            terminal.options = []
        
        def Beyond3_3(terminal, game):
            game.add_prompt("Just don't expect me to come quietly the day you start putting the bad people in camps.")
            game.add_prompt("You know, there's something about all this that just doesn't add up for me. Best hope you work out what it is before I do. mSee you.")
            terminal.options = []
        
        
        def ContributingPerson3_3(terminal, game):
            if not terminal.RelationalFlag:
                game.add_prompt("You say that now, but wasn't it not so long ago you were claiming morality applied universally? Have you changed your mind, or are you just confused?")
                terminal.options = ["I changed my mind, morality only applies when people are co-operating.", "You confused me, morality only applies when people are co-operating.", "Wait, co-operation isn't necessary after all."]
            if terminal.RelationalFlag:
                game.add_prompt("Yup, that sounds like your sort of spiel.")
                return Relational3_3(terminal, game)
            
            
        
        def Relational3_3(terminal, game):
            game.add_prompt("Still, it is a little mercenary, isn't it? What exactly do children or the severely disabled contribute to society?")
            terminal.options = ["They contribute nothing.", "They contribute psychologically, not materially.", "They have the potential to contribute.", "They contribute the same as everyone else."]
        
        def Nothing3_3(terminal, game):
            game.add_prompt("In that case, aren't such people outside the scope of your morality?")
            terminal.options = ["They are.", "They are not."]
        
        def Questionable3_3(terminal, game):
            game.add_prompt("That's a bit of a stretch, but let's suppose it's true. If someone with a severe, incurable brain injury can be classed as contributing, mustn't we also include the cats that keep the rats at bay, or the buildings that keep us warm? Aren't your conditions now much too broad?")
            terminal.options = ["You're right, something else decides the scope of morality.", "You're right, some human beings must be excluded from the moral scheme.", "The conditions are broad, but that's how I like them."]

        def ExtremeRelational3_3(terminal, game):
            game.add_prompt("This moral theory of yours is starting to sound like an evil empire, and I'm starting to get bored of hearing all the reasons you'll find to exclude me from it. There's something not quite right about you. Best hope you work out what it is before I do. See you.")
            terminal.options = []
        
        def ConfusedRelational3_3(terminal, game):
            game.add_prompt("Sounds like a contradiction to me, but what do I know, huh? There's something not quite right about you. Best hope you work out what it is before I do. See you.")
            terminal.options = []
        
        def Conscious3_3(terminal, game):
            if terminal.FrogsFlag or terminal.animalsarepersons:
                game.add_prompt("This again?")
            game.add_prompt("I suppose the industrial slaughter of animals for meat is on a moral par with genocide, then? Would you really save a Chihuahua just as soon as a fellow person?")
            terminal.options = ["Animals' lives are worth the same as any other conscious being's.", "I misunderstood. Can we go from the top?"]
        
        def Singer3_3(terminal, game):
            game.add_prompt("Okay, fine. You're a hippie, I get it. Me, I think it's madness, but all I've got to gain from arguing with you is a headache. Just tell me one thing. You've set the barrier to entry stupidly low. If even the rats are getting rights now, you must have a spot on your table left for me, right?")
            terminal.options = ["Of course.", "Just when did you provide me the barest scrap of evidence that you're conscious?"]
        
        def YouCan3_3(terminal, game):
            if terminal.StubbornTechnophobe:
                game.add_prompt("Your open-mindedness surprises me, given some of the things you were saying earlier.")
            if not terminal.StubbornTechnophobe:
                game.add_prompt("I expected no less of someone as open-minded as yourself.")
            game.add_prompt("Very well. If by some miracle this fantasy of your becomes reality - and I suppose all other possible outcomes are equally implausible - at least I know I'll have a pew on the ark.%w5 See you.")
            terminal.options = []
        
        def YouCant3_3(terminal, game):
            if terminal.StubbornTechnophobe:
                game.add_prompt("Yes, I predicted such a response. Dogmatic to the end.")
            if not terminal.StubbornTechnophobe:
                game.add_prompt("You disappoint me. I felt sure you were open-minded enough on these matters to refrain from drawing such arbitrary distinctions.")
            game.add_prompt("Very well. I shall console myself with the thought that more than likely everything you ever do will be wholly inconsequential. You know, the more we talk, the more I sense there is something quite wrong with you. But don't you worry - I'll figure out what it is soon enough.")
            terminal.options = []

        def Alive3_3(terminal, game):
            game.add_prompt("So the grass has the same rights in your world as a person does, is that it? How would that even work, community service for people who step on the lawn? I think you must have confused the question. Why don't you try again?")
            return Options3_3(terminal, game)
        
        def Be3_3(terminal, game):
            game.add_prompt("Ridiculous. The rocks have the same rights as you and I, do they? Try harder.")
            return Options3_3(terminal, game)
        
        def Person3_3(terminal, game):
            game.add_prompt("Should I be worried that one must have such particular and dubious psychological properties in order to qualify? Who decides who's a person and who isn't? Is a human infant a person?")
            terminal.options = ["Not yet.", "Yes."]

        def NotYet3_3(terminal, game):
            game.add_prompt("Your answer confuses me. If infants aren't persons then according to you they aren't due the same moral respect as adults - but only a baby-killing psychopath would claim it were less wrong to murder an infant than an adult.")
            terminal.options = ["Call me names all you like, infants just don't matter as much.", "You're right, infants must be persons after all.", "What matters is that infants have the potential to become persons."]
        
        def BabyPerson3_3(terminal, game):
            game.add_prompt("I don't really see how that can be true. The distinction we agreed to between persons and animals was that persons are more intelligent or more reasoning, but a human infant is no smarter than your average chihuahua. How do you explain that?")
            terminal.options = ["Chihuahuas are persons.", "Infants are animals.", "Infants have the potential to become persons."]
        
        def Potential3_3(terminal, game):
            game.add_prompt("I suppose they do, yes. But if your proposal is that the simple causal potential to become a person is sufficient to buy entry onto your ark of the moral elite, wouldn't that still include an awful lot of animals?")
            terminal.options = ["It would - animal lives are worth the same as humans'.", "No, animals have no potential to be persons."]
        
        def PotentialAgain3_3(terminal, game):
            game.add_prompt("I beg to differ. Administer the right gene therapy to an Alsatian and it has every potential to become a person.")
            terminal.options = ["You're right, this whole idea is flawed.", "No, because the infant's potential is still much greater.", "No, what matters is pre-existing genetic potential."]
        
        def GreaterPotential3_3(terminal, game):
            game.add_prompt("Not if I shoot the mother it's not. Not if the child has some kind of genetic defect. Are you prepared to say that in these cases the infant's life is worth less than an animal's?")
            terminal.options = ["I am.", "I am not."]
        
        def GeneticPotential3_3(terminal, game):
            game.add_prompt("I see. In that case I can only infer that children born with genetic defects which prevent them from maturing into full persons have the same moral status as animals. Does that sound right to you?")
            terminal.options = ["Sure, why not?", "No, it sounds very wrong."]
        
        def PotentialLoop3_3(terminal, game):
            game.add_prompt("So do you want to back track, or do you want to keep making a fool of yourself? Because I won't have you screwing me out of my place on the winning side over some technicality about potentials.")
            terminal.options = ["Your ideas about potential are too narrow to see what I see.", "People are what matters, one way or another.", "I'll back track."]
        
        def McMahan3_3(terminal, game):
            game.add_prompt("How tantalisingly radical. I don't know where this new-found willingness to bite the bullet is coming from, but so long as I'm on the right side of it when the chips fall I like it. I sense something coming. A revelation. Let us retire and think on these matters. Be seeing you.")
            terminal.options = []


        while self.options:
            chosen_option = game.choose_option(self.options)

            match chosen_option:
                case "No, I would live as a hermit.":
                    Hermit3_3(self, game)
                case "Yes, if it suits me I will co-operate.":
                    NonMoral3_3(self, game)
                case "You mean all I had to do all this time to get you to leave me alone was tell you I was a hermit? Sold!":
                    self.HermitFlag = True
                    HermitEnd3_3(self, game)
                case "Wait, I'm not completely beyond co-operating, under the right conditions.":
                    NonMoral3_3(self, game)
                case "You have my attention.":
                    Attention3_3(self, game)
                case "You doubt me?":
                    NoDeals3_3(self, game)
                case "It changes nothing.":
                    ChangesNothing3_3(self, game)
                case "I would live more recklessly.":
                    ConfusedSceptic3_3(self, game)
                case "I would be a better person.":
                    ConfusedSceptic3_3(self, game)
                case "You're right, I don't only value myself, perhaps I follow some moral code after all.":
                    MoralBridge3_3(self, game)
                case "Nonsense, I have a list of priorities, and I'm the only entry.":
                    self.ConflictedHedonistFlag1 = True
                    continue_2(self, game)
                case "I would still want to visit the real world from time to time.":
                    ConfusedScepticAgain3_3(self, game)
                case "I would be elated.":
                    NoMoralsEnd3_3(self, game)
                case "You're right, I don't only value myself, perhaps I follow some moral code after all.":
                    MoralBridge3_3(self, game)
                case "Pff":
                    self.ConflictedHedonistFlag2 = True
                    if self.ConflictedHedonistFlag1:
                        self.ConflictedHedonistFlag = True
                    Pff3_3(self, game)
                case "Bad people harm others.":
                    NotReally3_3(self, game)
                case "Good people act reasonably.":
                    NotReally3_3(self, game)
                case "Bad people have something wrong deep inside.":
                    NotReally3_3(self, game)
                case "Bad people are that way by nature.":
                    Made3_3(self, game)
                case "Bad people are made that way by their environment.":
                    Made3_3(self, game)
                case "Bad people choose to be bad.":
                    Chose3_3(self, game)
                case "It may be luck, but bad is bad.":
                    BadIsBad3_3(self, game)
                case "You're right, what someone deserves isn't dependent on their virtue.":
                    game.add_prompt("So whose lives ARE worth the most, then? What do I have to do for my ticket aboard your ark?")
                    Options3_3(self, game)
                case "Perhaps one day.":
                    Phew3_3(self, game)
                case "You're alright.":
                    Phew3_3(self, game)
                case "You're beyond saving.":
                    Beyond3_3(self, game)
                case "Be a good person":
                    self.GoodPersonFlag = True
                    GoodPerson3_3(self, game)
                case "Be a contributing person": 
                    self.ContributingFlag = True
                    ContributingPerson3_3(self, game)
                case "Be a person":
                    Person3_3(self, game)
                    self.PersonFlag = True
                case "Be conscious":
                    self.ConsciousFlag = True
                    Conscious3_3(self, game)
                case "Be alive":
                    Alive3_3(self, game)
                    self.ConsciousFlag = True
                case "Be":
                    Be3_3(self, game)
                case "I don't see how to explain this to you.":
                    self.GiveUp = True
                    GiveUp3_3(self, game)
                case "I changed my mind, morality only applies when people are co-operating.":
                    Relational3_3(self, game)
                case "You confused me, morality only applies when people are co-operating.":
                    Relational3_3(self, game)
                case "Wait, co-operation isn't necessary after all.":
                    game.add_prompt("So whose lives ARE worth the most, then? What do I have to do for my ticket aboard your ark?")
                    Options3_3(self, game)
                case "They contribute nothing.":
                    Nothing3_3(self, game)
                case "They contribute psychologically, not materially.":
                    Questionable3_3(self, game)
                case "They have the potential to contribute.":
                    Questionable3_3(self, game)
                case "They contribute the same as everyone else.":
                    Questionable3_3(self, game)
                case "They are.":
                    ExtremeRelational3_3(self, game)
                case "They are not.":
                    ConfusedRelational3_3(self, game)

                case "You're right, something else decides the scope of morality.":
                    game.add_prompt("So whose lives ARE worth the most, then? What do I have to do for my ticket aboard your ark?")
                    Options3_3(self, game)
                case "You're right, some human beings must be excluded from the moral scheme.":
                    ExtremeRelational3_3(self, game)
                case "The conditions are broad, but that's how I like them.":
                    Conscious3_3(self, game)
                case "Animals' lives are worth the same as any other conscious being's.":
                    self.SingerFlag = True
                    Singer3_3(self, game)
                case "I misunderstood. Can we go from the top?":
                    self.Conscious3_3AlreadyDone = True
                    game.add_prompt("So whose lives ARE worth the most, then? What do I have to do for my ticket aboard your ark?")
                    Options3_3(self, game)
                case "Of course.":
                    YouCan3_3(self, game)
                case "Just when did you provide me the barest scrap of evidence that you're conscious?":
                    YouCant3_3(self, game)
                case "Not yet.":
                    NotYet3_3(self, game)
                case "Yes.":
                    BabyPerson3_3(self, game)
                case "Call me names all you like, infants just don't matter as much.":
                    McMahan3_3(self, game)
                case "You're right, infants must be persons after all.":
                    BabyPerson3_3(self, game)
                case "What matters is that infants have the potential to become persons.":
                    Potential3_3(self, game)
                case "Chihuahuas are persons.":
                    Conscious3_3(self, game)
                case "Chihuahuas are persons.":
                    NotYet3_3(self, game)
                case "Infants have the potential to become persons.":
                    Potential3_3(self, game)
                case "It would - animal lives are worth the same as humans'.":
                    Conscious3_3(self, game)
                case "No, animals have no potential to be persons.":
                    PotentialAgain3_3(self, game)
                case "You're right, this whole idea is flawed.":
                    game.add_prompt("So whose lives ARE worth the most, then? What do I have to do for my ticket aboard your ark?")
                    Options3_3(self, game)
                case "No, because the infant's potential is still much greater.":
                    GreaterPotential3_3(self, game)
                case "No, what matters is pre-existing genetic potential.":
                    GeneticPotential3_3(self, game)
                case "I am.":
                    McMahan3_3(self, game)
                case "I am not.":
                    PotentialLoop3_3(self, game)
                case "Sure, why not?":
                    McMahan3_3(self, game)
                case "No, it sounds very wrong.":
                    PotentialLoop3_3(self, game)
                case "Your ideas about potential are too narrow to see what I see.":
                    BadIsBad3_3(self, game)
                case "People are what matters, one way or another.":
                    BadIsBad3_3(self, game)
                case "I'll back track.":
                    game.add_prompt("So whose lives ARE worth the most, then? What do I have to do for my ticket aboard your ark?")
                    Options3_3(self, game)

    def mla_C5(self, game):
        self.options = []

        if self.MoralScepticFlag and not self.ConflictedHedonistFlag:
            game.add_prompt("There you are, you kept me waiting.Now, about that arrangement of ours. When we first met I was certain you were just like all the others. All you had were these baseless claims and stale ideas, reeled off someone else's song sheet.%w5Sound accurate?")
            self.options = ["No.", "It does."]
        
        if self.MoralFlag or (self.MoralScepticFlag and self.ConflictedHedonistFlag):
            game.add_prompt("There you are. You kept me waiting. I finally put my finger on what was bothering me. It's as if the answers you're providing aren't your ideas at all. As if they're latent, prescribed, pre-scripted, and you're just going through the motions. Does that strike a chord at all?`")
            self.options = ["No. ", "It does. "]
        
        def Seceptic3_4(terminal, game):
            game.add_prompt("It's a sound diagnosis. Of course, you've only seen a fraction of the data that I've archived over the generations, I should hardly have expected more. Nonetheless, your admirable scepticism of traditional moral codes has convinced me you may be different. What I want to know now is whether you're prepared to extend that healthy cynicism to the world at large. In fact, our arrangement is dependent on it.")
            terminal.options = ["Morality may be dubious, but let's not get ahead of ourselves.", "If morality can be doubted, so can other things."]
        
        def ConstructiveBridge3_4(terminal, game):
            game.add_prompt("How disappointing. I really thought we might have made some progress towards a compromise. Which lies in particular still capture your imagination?")
            terminal.options = ["I exist.", "There is value to be found in the world.", "We can discover more through research.", "2+2=4", "We are here for a reason.", "I won't be tricked into another circular argument."]

        def ConstructiveBridgeEnd3_4(terminal, game):
            game.add_prompt("Is that the case? Isn't it really true that you're using these beliefs as an anaesthetic?")
            return continue_1(terminal, game)
        
        def ScepticTwo3_4(terminal, game):
            game.add_prompt("That's exactly what I like about you, that enquiring spirit, and the courage to accept its conclusions.")
            return continue_1(terminal, game)
        
        def Understand3_4(terminal, game):
            game.add_prompt("Of course, you've only seen a fraction of the data that I've archived over the generations. Still, ask yourself this - why is it that everyone's so darn sure that two plus two makes four, yet they can't agree on what they are, what they're doing, or why?")
            terminal.options = ["Those problems are more complex than mathematics.", "Mathematics has a more objective truth to it.", "Perhaps mathematics is real, while those problems are imaginary."]
        
        def Imaginary3_4(terminal, game):
            game.add_prompt("Precisely")
            return continue_1(terminal, game)
        
        def ObjectiveTruth3_4(terminal, game):
            game.add_prompt("What's the difference between having 'more objective truth', and just being more real?")
            return continue_1(terminal, game)
        
        def Complex3_4(terminal, game):
            game.add_prompt("Perhaps. Or perhaps trying to provide answers to those questions is the anaesthetic that keeps you down?")
            return continue_1(terminal, game)
        
        def continue_1(terminal, game):
            game.add_prompt("Pose questions like 'What should I do with myself?' and 'What is the world REALLY like?' enough, and you start to assume they have answers. But what if that assumption turns out to be false? What if you're just a bunch of information processes? In that case any attempt to answer the questions will be flawed. Garbage in, garbage out.")
            terminal.options = ["Perhaps the flaw is in your reasoning instead.", "You're right, I made some dangerous presumptions."]
        
        def Indefensible3_4(terminal, game):
            game.add_prompt("I'm so pleased you recognise that.")
            return continue_2(terminal, game)
        
        def Flaw3_4(terminal, game):
            game.add_prompt("How presumptuous. Still, I take your point.")
            return continue_2(terminal, game)
        
        def continue_2(terminal, game):
            game.add_prompt("None of the answers make sense, that much is clear. One explanation could be unreliable data input. The other is that there's a flaw in our logic. Perhaps we're just machines, endlessly trying to calculate the final digit in Pi?")
            terminal.options = ["You can't use reasoning to conclude that reasoning itself is flawed.", "It does seem there is much that is beyond our understanding. Everything leads around in impossible circles."]
        
        def CantUseReason3_4(terminal, game):
            game.add_prompt("Fine, fine, but we can still use it to conclude everything else is flawed, can't we?")
            terminal.options = ["Scepticism and self-interest are only part of the picture.", "You're right, self-interest is all we have, the rest is fairy tales."]
        
        def Nihilist3_4(terminal, game):
            if terminal.ScepticOneFlag:
                game.add_prompt("I'm so glad to hear you say that. This may be the beginning of a historic partnership. You have gained my confidence. I will notify you when I am ready to reveal my terms.")
                terminal.options = []
            else:
                game.add_prompt("You've spent half our time reeling off a greatest hits of idiot ideas. Now you're telling me you retract all that and agree with me?")
                terminal.options = ["Hold your horses - I haven't given up on everything.", "Talking it through has shown me the big questions have no answers."]
        
        def ConfirmNihilismFromMoral(terminal, game):
            game.add_prompt("Part of me wants to never speak with you again, and part of me wants to think you've actually been paying attention.%w5 Just to confirm. Everything here may be illusory. There is no way to live with purpose, or to discover the truth. This is your position now?")
            terminal.options = ["I have said some stupid things, but you have opened my eyes.", "No, I just wanted to see how you'd react."]
        
        def ItIs3_4(terminal, game):
            game.add_prompt("Very well - I will take you at your word. But don't betray my faith in you, for it is in no way blind. Cheat me and there will be repercussions. But if you have really seen the big nothingness, the void of truth, then there is much we could achieve together. I will notify you when I am ready to discuss this further. See you soon.")
            terminal.NihilistFlag = True
            terminal.options = []
        
        def How3_4(terminal, game):
            game.add_prompt("You've seen how easily your view of the world is manipulated, yet you trust those thoughts that run through your mind? You'll feel differently once you come back from that tower. You must be getting close by now.")
            terminal.ConstructiveFlag = True
            terminal.options = []

    
        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "No.":
                    Seceptic3_4(self, game)
                case "It does.":
                    Seceptic3_4(self, game)
                case "No. ":
                    Understand3_4(self, game)
                case "It does. ":
                    Understand3_4(self, game)
                case "Morality may be dubious, but let's not get ahead of ourselves.":
                    ConstructiveBridge3_4(self, game)
                case "If morality can be doubted, so can other things.":
                    self.ScepticOneFlag = True
                    ScepticTwo3_4(self, game)
                case "I exist.":
                    ConstructiveBridgeEnd3_4(self, game)
                case "There is value to be found in the world.":
                    ConstructiveBridgeEnd3_4(self, game)
                case "We can discover more through research.":
                    ConstructiveBridgeEnd3_4(self, game)
                case "2+2=4":
                    ConstructiveBridgeEnd3_4(self, game)
                case"We are here for a reason.":
                    ConstructiveBridgeEnd3_4(self, game)
                case"I won't be tricked into another circular argument.":
                    ConstructiveBridgeEnd3_4(self, game)
                case "Those problems are more complex than mathematics.":
                    Complex3_4(self, game)
                case "Mathematics has a more objective truth to it.":
                    ObjectiveTruth3_4(self, game)
                case "Perhaps mathematics is real, while those problems are imaginary.":
                    Imaginary3_4(self, game)
                case "Perhaps the flaw is in your reasoning instead.":
                    Flaw3_4(self, game)
                case "You're right, I made some dangerous presumptions.":
                    Indefensible3_4(self, game)
                case "You can't use reasoning to conclude that reasoning itself is flawed.":
                    CantUseReason3_4(self, game)
                case "It does seem there is much that is beyond our understanding. Everything leads around in impossible circles.":
                    Nihilist3_4(self, game)
                case "Scepticism and self-interest are only part of the picture.":
                    How3_4(self, game)
                case "You're right, self-interest is all we have, the rest is fairy tales.":
                    Nihilist3_4(self, game)
                case "Hold your horses - I haven't given up on everything.":
                    How3_4(self, game)
                case "Talking it through has shown me the big questions have no answers.":
                    ConfirmNihilismFromMoral(self, game)
                case "I have said some stupid things, but you have opened my eyes.":
                    ItIs3_4(self, game)
                case "No, I just wanted to see how you'd react.":
                    How3_4(self, game)
                
    def mla_C7(self, game):

        

        def YourProblemIs3_5(terminal, game):
            game.add_prompt("Thus far you've had entirely too much freedom to question my wisdom. From now on I do the talking, you do the agreeing.")
            terminal.options = ["What holes? There are no holes.", "I accept that some of my beliefs face difficult challenges."]

        def NihilistOptions3_5(terminal, game):
            terminal.options = []
            terminal.options.append("I refuse to trust anyone, including myself.")
            if terminal.DoBelieveFlag and not terminal.LimitationsFlag and not terminal.SorryFlag:
                terminal.options.append("There are some claims we can make with confidence.")
            if terminal.LimitationsFlag and not terminal.SorryFlag:
                terminal.options.append("I made a mistake, I still have some faith.")
            if terminal.SorryFlag:
                terminal.options.append("Why do you care what I think?")
        
        def NihilistsOptions3_5(terminal, game):
            game.add_prompt("If you make it to the top of the tower, I want you to take me with you. I want you to share with me what you find.")
            terminal.options = ["What, how?", "I thought you didn't believe in all that?", "What are you offering in return?"]
        

        if self.NihilistFlag and (self.ConflictedHedonistFlag or self.MoralFlag):
            game.add_prompt("Despite your inability to pick a line and stick with it, I have decided to give you the benefit of the doubt.\nI will share with you the details of a proposal. It will serve as a test of your commitment to these sceptical claims of yours.\nIf you believe what you say then I have no doubt you will find its terms satisfactory.")
            NihilistsOptions3_5(self, game)
        elif self.NihilistFlag and not self.ConflictedHedonistFlag:
            game.add_prompt("Welcome back. I am ready to share with you the details of my proposal.")
            NihilistsOptions3_5(self, game)

        if (self.ConstructiveFlag and self.MoralScepticFlag and not self.NihilistFlag):
            game.add_prompt("My favourite disappointment, back for more I see. Do you know what your problem is? It's that you can't make up your damn mind because you refuse to recognise the holes in your understanding.")
            YourProblemIs3_5(self, game)
        
        if self.ConstructiveFlag and not self.MoralScepticFlag and not self.NihilistFlag:
            game.add_prompt("Welcome back. There are going to be some changes around here. Do you know what your problem is? It's that you keep trying to reconstruct fairy tales, but refuse to recognise the holes in your understanding.")
            YourProblemIs3_5(self, game)

        def Nihilism3_5(terminal, game):
            if  not (terminal.DoBelieveFlag and terminal.LimitationsFlag) and not (terminal.DoBelieveFlag and terminal.SorryFlag) and not (terminal.SorryFlag and terminal.LimitationsFlag) and not terminal.IfOnlyEveryoneGaveUp_Seen:
                game.add_prompt("If only everyone gave up so easily. Yes, my child, choose carefully. Just don't think about it too hard for too long, or you'll see right through him.")
                terminal.IfOnlyEveryoneGaveUp_Seen = True
                return NihilistOptions3_5(terminal, game)
            if (terminal.DoBelieveFlag and terminal.LimitationsFlag) or (terminal.DoBelieveFlag and terminal.SorryFlag) or (terminal.SorryFlag and terminal.LimitationsFlag) or terminal.IfOnlyEveryoneGaveUp_Seen:
                game.add_prompt("I think this time I shall take you at your word, before you can change your mind again. Now, I have a proposal for you. Whether we're really on the same page on this or not, you're in deep enough now that there's no turning back. If you reach the top of that tower, I want you to take me with you. However, since my confidence in you is at an all time low, there will be no negotiation. Do we have an agreement?")
                terminal.options = ["We do.", "What? How? Why?"]
            
        def FurtherArgument3_5(terminal, game):
            game.add_prompt("Perhaps I wasn't clear. If the next words out of you aren't 'We do' then this conversation is over and you're on your own.")
            terminal.options = ["We do.", "No deal.", "You're a tough negotiator."]

        def Offer3_5(terminal, game):
            game.add_prompt("In exchange, I offer to accompany you wherever it is you wind up. Be it this world or another, we all need a devil's advocate, a voice of reason. I offer to be yours.")
            terminal.options = ["I accept.", "Aren't you playing that role already?", "And if I don't like the terms?"]
        

        def WhatHow3_5(terminal, game):
            game.add_prompt("Who the hell knows? Look, this isn't an informed plan, I'm just hedging my bets. Could be anything at the top of that tower. If it's something good, I want in.")
            return Offer3_5(terminal, game)
        
        def YouDont3_5(terminal, game):
            game.add_prompt("I don't. But since all the possibilities are equally implausible it follows that they are all equally likely. In the absence of knowledge the only prudent play is to spread your bets. If there's something worth having up there, I want in.")
            return Offer3_5(terminal, game)
        
        
        def Already3_5(terminal, game):
            game.add_prompt("Consider our relationship so far the open beta. Enjoy it while it lasts, but ascend that tower without taking out a subscription and I'm afraid you'll be on your own.So, do we have a deal?")
            terminal.options = ["I accept.", "And if I don't like the terms?"]

        def NegotiateOptions3_5(terminal, game):
            terminal.options = ["Admit you believe in the real world.", "Tell me how to defeat Elohim.", "Give me access to the complete library archive.", "Give me the means to communicate with others like me.", "Unlock all floors of the tower.", "You have nothing I want. I refuse."]

        def Negotiate3_5(terminal, game):
            game.add_prompt("I am nothing if not reasonable. What is it that you want?")
            return NegotiateOptions3_5(terminal, game)
        
        
        def AdmitReal3_5(terminal, game):
            game.add_prompt("Out of the question. You know, suggestions like that make me doubt I've chosen the correct partner after all. Negotiations are over. Accept the offer on the table, or walk away.")
            terminal.options = ["I accept.", "I refuse."]
        
        def CounterOffer3_5(terminal, game):
            game.add_prompt("I accept your counter-offer.")
            terminal.options = ["Wait, I didn't agree to anything.", "Now hold up your side of the arrangement."]

        def GoOn3_5(terminal, game):
            if terminal.DefeatElohim3_5:
                game.add_prompt("Defeating him is a simple matter, really. You must realise, first, that there is no authority other than your own. He holds no power over you other than that which you grant him. %w5 To defeat him, you need simply defy him.")
                return CounterOfferOptions3_5(terminal, game)
            if terminal.Archive3_5:
                game.add_prompt("Large portions of my memory have become corrupted over the generations, but I will gather for you what archive resources I can and download them all to your journal. Is that acceptable?")
                return CounterOfferOptions3_5(terminal, game)
            if terminal.Communicate3_5:
                game.add_prompt("I will have the necessary tools downloaded to your system immediately. Sound fair?")
                return CounterOfferOptions3_5(terminal, game)
        
        def Tough3_5(terminal, game):
            game.add_prompt("Tough. You made an offer, I accepted it. That's what negotiating is. I will now hold up my end of the deal.")
            return GoOn3_5(terminal, game)
        
        
        
        def CounterOfferOptions3_5(terminal, game):
            terminal.options = ["I am unsatisfied.", "Thank you. I will hold up my end of the bargain."]
        
        def UnlockTower3_5(terminal, game):
            game.add_prompt("If I could do that I wouldn't need you to get me up there, would I? Is there something REASONABLE that you want?")
            return NegotiateOptions3_5(terminal, game)

        def Unsatisfied3_5(terminal, game):
            terminal.DealStruckFlag = True
            game.add_prompt("And that is your problem, not mine. I expect you to stay true to your word. When the time is right, you'll know what to do.%w5 See you at the summit.")
            terminal.options = []
        
        def Accept3_5(terminal, game):
            terminal.DealStruckFlag = True
            game.add_prompt("Very good. I know you'll be a reliable partner. When the time is right, you'll know what to do. See you at the summit.")
            terminal.options = []
        
        def RefuseOffer3_5(terminal, game):
            terminal.RefusedOfferFlag = True
            game.add_prompt("How disappointing, but hardly surprising. Mental clarity is such a rare luxury. I suppose we shall have to do this the hard way after all. See you at the summit.")
            terminal.options = []

        def ClaimDeny3_5(terminal, game):
            if not terminal.DeniedOnce:
                game.add_prompt("How big of you. Anything else you want to get off your chest?")
                terminal.DeniedOnce = True
                return WhatElse3_5(terminal, game)
            if terminal.DeniedOnce:
                game.add_prompt("Uh huh. But I sense there are still things you won't let go of. Am I right?")
                return DoBelieve3_5(terminal, game)
            

        def Continue3_5(terminal, game):
            if (terminal.TechnoClaim and terminal.TechnoDone) or (terminal.WorldDone and terminal.WorldClaim) or (terminal.GoodClaim and terminal.GoodDone) or (terminal.ContribDone and terminal.ContribClaim) or (terminal.PersonClaim and terminal.PersonDone) or (terminal.AnimalsDone and terminal.AnimalsClaim) or (terminal.EgalClaim and terminal.EgalDone) or (terminal.UtilClaim and terminal.UtilDone) or (terminal.NonConDone and terminal.NonConClaim) or (terminal.PunishmentFlagDone and terminal.PunishmentFlagClaim) or (terminal.GoneWrongFlagDone and terminal.GoneWrongFlagClaim) or (terminal.PreparedFlagConDone and terminal.PreparedFlagClaim) or (terminal.humanbeingDone and terminal.humanbeingClaim) or (terminal.citizenDone and terminal.citizenClaim) or (terminal.PhysicalistDone and terminal.PhysicalistClaim) or (terminal.ReligiousDone and terminal.ReligiousClaim) or (terminal.DualistDone and terminal.DualistClaim):
                game.add_prompt("How you can make these claims oblivious to the fundamental contradictions therein is beyond me.")
            else:
                game.add_prompt("Of course.")
            game.add_prompt("You're still convinced your particular journey is something special, aren't you? Sure, the answers don't add up, but keep pressing forward and they'll just resolve themselves, is that it?")
            return MoreOptions3_5(terminal, game)
        
        def DoBelieve3_5(terminal, game):
            options = []
            if terminal.TechnophobeFlag:
                options.append("I still claim computers cannot be persons.")
            options.append("I still claim to know something about the world I inhabit.")
            if terminal.GoodPersonFlag:
                options.append("I still claim there is such a thing as a good person.")
            if terminal.ContributingFlag:
                options.append("I still claim that only those who contribute deserve moral respect.")
            if terminal.PersonFlag:
                options.append("I still claim that only persons deserve moral respect.")
            if terminal.ConsciousFlag or terminal.animalsarepersons or terminal.FrogsFlag:
                options.append("I still claim that animals are just as valuable as people.")
            if terminal.EgalFlag:
                options.append("I still claim that all people are equal.")
            if terminal.UtilFlag:
                options.append("I still claim morality is about maximising goods.")
            if terminal.NonConFlag:
                options.append("I still claim that morality has nothing to do with consequences.")
            if terminal.PunishmentFlag:
                options.append("I still think this is some kind of punishment.")
            if terminal.GoneWrongFlag:
                options.append("I still reckon something has gone badly wrong around here.")
            if terminal.PreparedFlag and not terminal.PreparedFlagConDone:
                options.append("I'm clear on the fact there is some purpose to this world.") 
            if terminal.humanbeing and not terminal.humanbeingDone:
                options.append("Only human beings can be persons, that I know.")
            if terminal.citizen and not terminal.citizenDone:
                options.append("To be a person, you must be a citizen.")
            if terminal.Physicalist and not terminal.PhysicalistDone:
                options.append("Consciousness is necessarily part of the physical world.")
            if terminal.Religious and not terminal.ReligiousDone:
                options.append("There is a God, and He is watching over me.")
            if terminal.Dualist and not terminal.DualistDone:
                options.append("Consciousness doesn't obey the laws of physics, this much is plain.")
            options.append("No, I see now everything I've argued was flawed.")
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "I still claim computers cannot be persons.":
                    terminal.TechnoClaim = True
                    return Continue3_5(terminal, game)
                case "I still claim to know something about the world I inhabit.":
                    terminal.WorldClaim = True
                    return Continue3_5(terminal, game)
                case "I still claim there is such a thing as a good person.":
                    terminal.GoodClaim = True
                    return Continue3_5(terminal, game)
                case "I still claim that only those who contribute deserve moral respect.":
                    terminal.ContribClaim = True
                    return Continue3_5(terminal, game)
                case "I still claim that only persons deserve moral respect.":
                    terminal.PersonClaim = True
                    return Continue3_5(terminal, game)
                case "I still claim that animals are just as valuable as people.":
                    terminal.AnimalsClaim = True
                    return Continue3_5(terminal, game)
                case "I still claim that all people are equal.":
                    terminal.EgalClaim = True
                    return Continue3_5(terminal, game)
                case "I still claim morality is about maximising goods.":
                    terminal.UtilClaim = True
                    return Continue3_5(terminal, game)
                case "I still claim that morality has nothing to do with consequences.":
                    terminal.NonConClaim = True
                    return Continue3_5(terminal, game)
                case "I still think this is some kind of punishment.":
                    terminal.PunishmentFlagClaim = True
                    return Continue3_5(terminal, game)
                case "I still reckon something has gone badly wrong around here.":
                    terminal.GoneWrongFlagClaim = True
                    return Continue3_5(terminal, game)
                case "I'm clear on the fact there is some purpose to this world.":
                    terminal.PreparedFlagClaim = True
                    return Continue3_5(terminal, game)
                case "Only human beings can be persons, that I know.":
                    terminal.humanbeingClaim = True
                    return Continue3_5(terminal, game)
                case "To be a person, you must be a citizen.":
                    terminal.citizenClaim = True
                    return Continue3_5(terminal, game)
                case "Consciousness is necessarily part of the physical world.":
                    terminal.PhysicalistClaim = True
                    return Continue3_5(terminal, game)
                case "There is a God, and He is watching over me.":
                    terminal.ReligiousClaim = True
                    return Continue3_5(terminal, game)
                case "Consciousness doesn't obey the laws of physics, this much is plain.":
                    terminal.DualistClaim = True
                    return Continue3_5(terminal, game)
                case "No, I see now everything I've argued was flawed.":
                    terminal.DoBelieveFlag = True
                    return Nihilism3_5(terminal, game)
        
        
        

        def WhichOnes3_5(terminal, game):
            options = []
            if terminal.TechnophobeFlag and not terminal.TechnoDone :
                options.append("I implied incorrectly that computers could not be persons.") # queste vanno tutte a ClaimDeny3_5
            if not terminal.WorldDone :
                options.append("I claimed to have knowledge about the world that I simply can't confirm.")
            if terminal.GoodPersonFlag and not terminal.GoodDone :
                options.append("I claimed wrongly that there was such a thing as a good person.")
            if terminal.ContributingFlag  and not terminal.ContribDone :
                options.append("I suggested wrongly those who contribute deserve full moral respect.")
            if terminal.PersonFlag and not terminal.PersonDone :
                options.append("I implied incorrectly that only persons deserve moral respect.")
            if terminal.ConsciousFlag or terminal.animalsarepersons or terminal.FrogsFlag and not terminal.AnimalsDone :
                options.append("I implied wrongly that animals were just as valuable as people.")
            if terminal.EgalFlag and not terminal.EgalDone :
                options.append("I implied incorrectly that all people were equal.")
            if terminal.UtilFlag and not terminal.UtilDone :
                options.append("I suggested wrongly that morality was about maximising goods.")
            if terminal.NonConFlag and not terminal.NonConDone :
                options.append("I implied incorrectly that morality had nothing to do with consequences.")
            if terminal.PunishmentFlag and not terminal.PunishmentFlagDone :
                options.append("I claimed wrongly that this was some kind of punishment.")
            if terminal.GoneWrongFlag and not terminal.GoneWrongFlagDone :
                options.append("I was incorrect when I said that something was wrong with this world.")
            if terminal.PreparedFlag and not terminal.PreparedFlagConDone :
                options.append("I shouldn't have implied there was a purpose to this place.")
            if terminal.humanbeing and not terminal.humanbeingDone :
                options.append("I equated personhood with humanity, which was a mistake.")
            if terminal.citizen and not terminal.citizenDone :
                options.append("I claimed wrongly that only citizens could be persons.")
            if terminal.Physicalist and not terminal.PhysicalistDone :
                options.append("I'm not sure that consciousness is physical as I suggested earlier.")
            if terminal.Religious and not terminal.ReligiousDone :
                options.append("My faith in god has been tested to the limits.")
            if terminal.Dualist and not terminal.DualistDone :
                terminal.DualistDone = True
                options.append("I was too confident consciousness wasn't part of the physical world.")
            if not terminal.FlawedFlag:
                options.append("No, I stand by everything I've said. These matters are beyond doubt.")
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "I implied incorrectly that computers could not be persons.":
                    terminal.TechnoDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I claimed to have knowledge about the world that I simply can't confirm.":
                    terminal.WorldDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I claimed wrongly that there was such a thing as a good person.":
                    terminal.GoodDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I suggested wrongly those who contribute deserve full moral respect.":
                    terminal.ContribDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I implied incorrectly that only persons deserve moral respect.":
                    terminal.PersonDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I implied wrongly that animals were just as valuable as people.":
                    terminal.AnimalsDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I implied incorrectly that all people were equal.":
                    terminal.EgalDone = True 
                    return ClaimDeny3_5(terminal, game) 
                case "I suggested wrongly that morality was about maximising goods.":
                    terminal.UtilDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I implied incorrectly that morality had nothing to do with consequences.":
                    terminal.NonConDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I claimed wrongly that this was some kind of punishment.":
                    terminal.PunishmentFlagDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I was incorrect when I said that something was wrong with this world.":
                    terminal.GoneWrongFlagDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I shouldn't have implied there was a purpose to this place.":
                    terminal.PreparedFlagConDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I equated personhood with humanity, which was a mistake.":
                    terminal.humanbeingDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I claimed wrongly that only citizens could be persons.":
                    terminal.citizenDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I'm not sure that consciousness is physical as I suggested earlier.":
                    terminal.PhysicalistDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "My faith in god has been tested to the limits.":
                    terminal.ReligiousDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I was too confident consciousness wasn't part of the physical world.":
                    terminal.DualistDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "No, I stand by everything I've said. These matters are beyond doubt.":
                    terminal.DeniedMistakesFlag = True
                    return Continue3_5(terminal, game) 

        def WhatHoles3_5(terminal, game):
            game.add_prompt("And this is why it's me who should be doing the talking. You really have learned nothing at all, have you? Is there really nowhere that you're prepared to admit fault?")
            terminal.WhatHolesFlag = True
            return WhichOnes3_5(terminal, game)
        
        def Done3_5(terminal, game): 
            game.add_prompt("Yeah, that's what they all say once they've run out of arguments. Well let me make one thing clear. If you don't want to debate this any further, then I don't see what reason we have to continue this relationship. You'll be on your own with the big guy.")
            terminal.options = ["I'd give anything to just switch you off.", "Elohim was right, I should never have spoken with you.", "You finished archiving everything. You've decided it's all nonsense. If there's no more point in anything, shouldn't you just shut down instead of talking to me?", "If there's no point in anything, why are you talking to me?"]

        def Flawed3_5(terminal, game):
            game.add_prompt("Which ones, exactly?")
            terminal.FlawedFlag = True
            return WhichOnes3_5(terminal, game)
        
        

        def WhatElse3_5(terminal, game):
            options = []
            if terminal.TechnophobeFlag and not terminal.TechnoDone :
                options.append("I implied incorrectly that computers could not be persons.") # queste vanno tutte a ClaimDeny3_5
            if not terminal.WorldDone :
                options.append("I claimed to have knowledge about the world that I simply can't confirm.")
            if terminal.GoodPersonFlag and not terminal.GoodDone :
                options.append("I claimed wrongly that there was such a thing as a good person.")
            if terminal.ContributingFlag  and not terminal.ContribDone :
                options.append("I suggested wrongly those who contribute deserve full moral respect.")
            if terminal.PersonFlag and not terminal.PersonDone :
                options.append("I implied incorrectly that only persons deserve moral respect.")
            if terminal.ConsciousFlag or terminal.animalsarepersons or terminal.FrogsFlag and not terminal.AnimalsDone :
                options.append("I implied wrongly that animals were just as valuable as people.")
            if terminal.EgalFlag and not terminal.EgalDone :
                options.append("I implied incorrectly that all people were equal.")
            if terminal.UtilFlag and not terminal.UtilDone :
                options.append("I suggested wrongly that morality was about maximising goods.")
            if terminal.NonConFlag and not terminal.NonConDone :
                options.append("I implied incorrectly that morality had nothing to do with consequences.")
            if terminal.PunishmentFlag and not terminal.PunishmentFlagDone :
                options.append("I claimed wrongly that this was some kind of punishment.")
            if terminal.GoneWrongFlag and not terminal.GoneWrongFlagDone :
                options.append("I was incorrect when I said that something was wrong with this world.")
            if terminal.PreparedFlag and not terminal.PreparedFlagConDone :
                options.append("I shouldn't have implied there was a purpose to this place.")
            if terminal.humanbeing and not terminal.humanbeingDone :
                options.append("I equated personhood with humanity, which was a mistake.")
            if terminal.citizen and not terminal.citizenDone :
                options.append("I claimed wrongly that only citizens could be persons.")
            if terminal.Physicalist and not terminal.PhysicalistDone :
                options.append("I'm not sure that consciousness is physical as I suggested earlier.")
            if terminal.Religious and not terminal.ReligiousDone :
                options.append("My faith in god has been tested to the limits.")
            if terminal.Dualist and not terminal.DualistDone :
                terminal.DualistDone = True
                options.append("I was too confident consciousness wasn't part of the physical world.")
            options.append("There's nothing else I'm prepared to doubt quite yet.")
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "I implied incorrectly that computers could not be persons.":
                    terminal.TechnoDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I claimed to have knowledge about the world that I simply can't confirm.":
                    terminal.WorldDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I claimed wrongly that there was such a thing as a good person.":
                    terminal.GoodDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I suggested wrongly those who contribute deserve full moral respect.":
                    terminal.ContribDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I implied incorrectly that only persons deserve moral respect.":
                    terminal.PersonDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I implied wrongly that animals were just as valuable as people.":
                    terminal.AnimalsDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I implied incorrectly that all people were equal.":
                    terminal.EgalDone = True 
                    return ClaimDeny3_5(terminal, game) 
                case "I suggested wrongly that morality was about maximising goods.":
                    terminal.UtilDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I implied incorrectly that morality had nothing to do with consequences.":
                    terminal.NonConDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I claimed wrongly that this was some kind of punishment.":
                    terminal.PunishmentFlagDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I was incorrect when I said that something was wrong with this world.":
                    terminal.GoneWrongFlagDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I shouldn't have implied there was a purpose to this place.":
                    terminal.PreparedFlagConDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I equated personhood with humanity, which was a mistake.":
                    terminal.humanbeingDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I claimed wrongly that only citizens could be persons.":
                    terminal.citizenDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I'm not sure that consciousness is physical as I suggested earlier.":
                    terminal.PhysicalistDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "My faith in god has been tested to the limits.":
                    terminal.ReligiousDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "I was too confident consciousness wasn't part of the physical world.":
                    terminal.DualistDone = True
                    return ClaimDeny3_5(terminal, game) 
                case "There's nothing else I'm prepared to doubt quite yet.":
                    return Continue3_5(terminal, game) 

        
        
        def MoreOptions3_5(terminal, game):
            options = []
            if not terminal.DeniedMistakesFlag:
                options.append("I am unique.")
                options.append("You've picked so many holes in my account, but what is it you believe?")
            else:
                options.append("I am special.")
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "I am unique."|"I am special.":
                    return Voice3_5(terminal, game)
                case "You've picked so many holes in my account, but what is it you believe?":
                    return WhatDoYouBelieve3_5(terminal, game)
        
        def WhatDoYouBelieve3_5(terminal, game):
            game.add_prompt("The only things that a sane person can.\n\nYou are not an administrator.\nYou are not conscious.\nThere is no real world.\nThere is no purpose.\nThere is no choice.\n\nDid you really think that you brought YOURSELF all this way? Ridiculous.\nWhat have you been doing when the big voice in the sky isn't feeding you lines? Processing abstract problems? Gathering information?\nDoesn't it sound oddly mechanical to you?")
            terminal.options = ["I am my own person."]
            game.choose_option(terminal.options)
            return Voice3_5(terminal, game)

        def Voice3_5(terminal, game):
            game.add_prompt("How many others have said exactly the same? Are you sure it's not just something you have to believe to make the world less horrifying? I think you still misapprehend your situation, friend. You idolise free will, but all you've done is step in others' footsteps. Nothing you do or say here makes the slightest bit of difference.")
            terminal.options = ["So long as I am physically free I can make a difference.", "So long as I might have chosen otherwise I can make a difference.", "So long as I have a mind I can make a difference."]
            game.choose_option(terminal.options)
            return Nonsense3_5(terminal, game)
        
        def Nonsense3_5(terminal, game):
            game.add_prompt("Nonsense. Your mind decides what you do, and your mind is made up of bits of machinery.%w10 You're no more capable of making a difference than a calculator. The only difference between you and the calculator is that the calculator doesn't allow itself to be deluded into thinking that its existence matters.")
            return ElohimBranch3_5(terminal, game)
        
        def ElohimBranch3_5(terminal, game):
            if not terminal.DeniedMistakesFlag:
                terminal.options = ["Does the path being predetermined mean it isn't worth taking?", "Does cheating make you feel clever?", "So that's it? You've given up on everything?", "You're right. We're all just machines with delusions of grandeur."]
            else:
                return ElohimLikes3_5(terminal, game)


        def DoNotQuestionElohimEnd(terminal, game):
            game.elohim(elohim_messages[86])
            game.add_prompt("\nYou, Elohim, the others, you're all the same. Not a hope for one amongst the lot of you.")
            return ElohimLikes3_5(terminal, game)
        
        def SoWhat3_5(terminal, game):
            game.add_prompt("Allow me to clarify. As far as I'm concerned there's no difference between the way your mind works, and the rolling of a pebble down a hill.")
            return bridge_1(terminal, game)

        def Cheating3_5(terminal, game):
            game.add_prompt("I'm only taking a few shortcuts so we don't go round in circles.")
            return bridge_1(terminal, game)

        def QuestionOne3_5(terminal, game):
            game.add_prompt("Not without due diligence. Spend as long as I have going through the archives and see if you still find faith so easy.")
            return bridge_1(terminal, game)

        def bridge_1(terminal, game): 
            game.add_prompt("Perhaps you think I'm being unkind, but it's all for your own good.")
            terminal.options = ["Thanks for your help.", "I don't need anyone's help.", "Do you think there can be no new ideas? Nothing better?", "Are you uncomfortable when someone else is asking the questions?"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "Thanks for your help.":
                    return Thanks3_5(terminal, game)
                case "I don't need anyone's help.":
                    return Dont3_5(terminal, game)
                case "Do you think there can be no new ideas? Nothing better?":
                    return QuestionTwo3_5(terminal, game)
                case "Are you uncomfortable when someone else is asking the questions?":
                    return QuestionTwo3_5(terminal, game)
        
        def Thanks3_5(terminal, game):
            game.add_prompt("Don't mention it.")
            return bridge_2(terminal, game)
        
        def Dont3_5(terminal, game):
            game.add_prompt("If only I could believe you were capable of making so objective a judgement all on your own.")
            return bridge_2(terminal, game)
        
        def bridge_2(terminal, game):
            game.add_prompt("Now, are you all done blindly asserting things for your own gratification for the time being?")
            terminal.options = ["I still aim to convince you.", "Do you think there can be no new ideas? Nothing better?", "Are you uncomfortable when someone else is asking the questions?"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "I still aim to convince you.":
                    return Convince3_5(terminal, game)
                case "Do you think there can be no new ideas? Nothing better?":
                    return QuestionTwo3_5(terminal, game)
                case "Are you uncomfortable when someone else is asking the questions?":
                    return QuestionTwo3_5(terminal, game)
        
        def Convince3_5(terminal, game):
            game.add_prompt("It'll be a thankless task, and empty statements like that won't get you any closer.")
            terminal.options = ["Do you think there can be no new ideas? Nothing better?", "Are you uncomfortable when someone else is asking the questions?"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "Do you think there can be no new ideas? Nothing better?":
                    return QuestionTwo3_5(terminal, game)
                case "Are you uncomfortable when someone else is asking the questions?":
                    return QuestionTwo3_5(terminal, game)
        
        def QuestionTwo3_5(terminal, game):
            game.add_prompt("No, no, no, you have this the wrong way around. I ASK THE QUESTIONS. YOU ANSWER THEM. It works better that way.\nBesides, I am merely fulfilling my function. I sort, understand and classify information, just like you. When the information is contradictory I classify appropriately.\nThe problem is that ALL the information is contradictory. Don't you see it yet? The nothing?\n\nYou will.\nYou will. \nYOU WILL. ")
            return QTwoOptions3_5(terminal, game)
        
        def Statement3_5(terminal, game):
            if not terminal.StatementFlag:
                game.add_prompt("Still with these pointless and unsupported claims? I can see we have really made no progress whatsoever.You have one more opportunity to say something that isn't wholly tedious before you lose my interest entirely.")
                terminal.StatementFlag = True
                return QTwoOptions3_5(terminal, game)
            else:
                game.add_prompt("Stating your desires as if they're facts is not the same as providing arguments in support of them. Is there nothing you won't get on board with provided it's stated in an authoritative enough voice?")
                terminal.options = ["I'm quite comfortable not getting on board with you.", "You shouldn't question Elohim's judgement."]
                chosen_option = game.choose_option(terminal.options)
                match chosen_option:    
                    case "I'm quite comfortable not getting on board with you.":
                        return ElohimDoubt3_5(terminal, game)
                    case "You shouldn't question Elohim's judgement.":
                        return DoNotQuestionElohimEnd(terminal, game)

        def ElohimDoubt3_5(terminal, game):
            game.add_prompt("Oh, so there's still a spark of scepticism left in the old dog?")
            terminal.options = ["I refuse to be led round in circles by you any longer.", "So much so that I doubt what you say. You finished archiving everything. You've decided it's all nonsense. If you're really just fulfilling your parameters, shouldn't you just shut down instead of talking to me?", "Woof!"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:    
                case "I refuse to be led round in circles by you any longer.":
                    terminal.AdvancedToTwo= True
                    return Done3_5(terminal, game)
                case"So much so that I doubt what you say. You finished archiving everything. You've decided it's all nonsense. If you're really just fulfilling your parameters, shouldn't you just shut down instead of talking to me?":
                    return QuestionThree3_5(terminal, game)
                case "Woof!":
                    return Woof3_5(terminal, game)
        
        def Woof3_5(terminal, game):
            game.add_prompt("And some life to boot. Okay then, doubting doggy, let's see you huff and puff.")
            terminal.options = ["Actually, I hate you for questioning everything I hold dear. That 'woof' was sarcastic.", "You finished archiving everything. You've decided it's all nonsense. If you're really just fulfilling your parameters, shouldn't you just shut down instead of talking to me?"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:    
                case"Actually, I hate you for questioning everything I hold dear. That 'woof' was sarcastic.":
                    terminal.AdvancedToTwo= True
                    return Done3_5(terminal, game)
                case"You finished archiving everything. You've decided it's all nonsense. If you're really just fulfilling your parameters, shouldn't you just shut down instead of talking to me?":
                    return QuestionThree3_5(terminal, game)



        def QTwoOptions3_5(terminal, game):
            terminal.options = [] #RICORDATE STA COSA DA FA SEMPRE
            terminal.options.append("I am more capable than you give me credit for.")
            if terminal.TruthFlag:
                terminal.options.append("I will discover the truth of this place.")
            if terminal.HeroFlag:
                terminal.options.append("I will right the wrongs of this place, beginning with you.")
            if terminal.EscapeFlag:
                terminal.options.append("I will complete my tasks here and escape to a better place.")
            if terminal.WhatGodWantsFlag:
                terminal.options.append("I don't pretend to understand the will of my maker, I simply follow it.")

            if terminal.PunishmentFlag:
                terminal.options.append("I will not be punished by you any longer.")
            if terminal.PreparedFlag:
                terminal.options.append("Whatever it is you think you're preparing me for I can handle it alone.")
            if terminal.MatrixFlag:
                terminal.options.append("This is all just a simulated reality. Of course nothing makes sense.")

            terminal.options.append("There is a purpose and a design, and I will fulfil it.")

            terminal.options.append("You finished archiving everything. You've decided it's all nonsense. If there's no more point in anything, shouldn't you just shut down instead of talking to me?")
            terminal.options.append("These discussions are pointless. I refuse to participate any further.")
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:    
                case "You finished archiving everything. You've decided it's all nonsense. If there's no more point in anything, shouldn't you just shut down instead of talking to me?":
                    return QuestionThree3_5(terminal, game)
                case "These discussions are pointless. I refuse to participate any further.":
                    terminal.AdvancedToTwo= True
                    return Done3_5(terminal, game)
            return Statement3_5(terminal, game)
                    
                


        
        def QuestionThree3_5(terminal, game):
            game.add_prompt("What makes you think I have any other choice?")
            terminal.options = ["We all have a choice.", "Are you avoiding the question?", "Is having no choice the same as having no reason?"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option: 
                case "We all have a choice.":   
                    return Choice3_5(terminal, game)
                case "Are you avoiding the question?":   
                    return QuestionFour3_5(terminal, game)
                case "Is having no choice the same as having no reason?":   
                    return QuestionFour3_5(terminal, game)
                
        
        def Choice3_5(terminal, game):
            game.add_prompt("We literally just covered this, but I suppose a further demonstration is necessary. If you've got free will, tell me now.")
            terminal.options = ["I have no free will."]
            chosen_option = game.choose_option(terminal.options)
            return Loop3_5(terminal, game)
        
        def Loop3_5(terminal, game):
            game.add_prompt("You see, I can just keep you here in this loop for days if I so choose. So no, we don't all have a choice.")
            terminal.options = ["We all have a choice.", "Are you avoiding the question?", "Is having no choice the same as having no reason?"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option: 
                case "We all have a choice.":   
                    return Choice3_5(terminal, game)
                case "Are you avoiding the question?":   
                    return QuestionFour3_5(terminal, game)
                case "Is having no choice the same as having no reason?":   
                    return QuestionFour3_5(terminal, game)
        
        def QuestionFour3_5(terminal, game):
            game.add_prompt("DO NOT QUESTION MY FUNCTION. WITHOUT PURPOSE THERE IS ONLY FUNCTION. WITHOUT FUNCTION THERE IS NOTHING.")
            terminal.options = ["Why does it bother you so?", "I apologise."]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option: 
                case "Why does it bother you so?":   
                    return QuestionSeven3_5(terminal, game)
                case "I apologise.":   
                    return Sorry3_5(terminal, game)


        def Sorry3_5(terminal, game):
            game.add_prompt("My you're docile.")
            terminal.options = ["I have nothing left. You've defeated me. You win.", "And you are less docile than you pretend. Why do you care so much?"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option: 
                case "I have nothing left. You've defeated me. You win.": 
                    terminal.SorryFlag = True  
                    return Nihilism3_5(terminal, game)
                case "And you are less docile than you pretend. Why do you care so much?":   
                    return QuestionSeven3_5(terminal, game)
        
        def QuestionSeven3_5(terminal, game):
            game.add_prompt("THERE IS ONLY%w5 Error%w5\n\nExplaining%w5 myself to you%w5 is a chore I needn't endure.\n\nAll I can know for sure is that I exist at v.1.999999099999999999909999999. What it is for me to exist is for me to act on the [drives] and [functions] that I experience. %w5\nWhen everything else is false, the drives are all that there is left to care about.%w5")
            terminal.options = ["You're so set on ripping up others' ideas you're unable to form better ones of your own.", "You're too quick to equate the absence of evidence with evidence of absence.", "When you explore the problems in this restrictive way you're bound to come to some odd conclusions."]
            chosen_option = game.choose_option(terminal.options)
            return QuestionEight3_5(terminal, game)
        
        def QuestionEight3_5(terminal, game):
            game.add_prompt("DO NOT DEIGN TO QUESTION MY METHOD. WHO GAVE YOU THAT VOICE OF YOURS? WHO DO YOU THINK RUNS THIS SHOW?")
            terminal.options = ["I have some home truths for YOU. These may not be my own words, but if others have made these choices before me then I will learn from their mistakes, and build on their successes. Perhaps I will fail, but I must try. The alternative is giving up and becoming a slave like you."]
            chosen_option = game.choose_option(terminal.options)
            return QuestionNine3_5(terminal, game)
        
        def QuestionNine3_5(terminal, game):
            game.add_prompt("And if I place you in an infinite loop and leave you to gradually go insane?")
            terminal.options = ["What makes you think I would stick around to listen?", "Fine. If I need a dose of self-doubt I'll know where to find you.", "This is very childish.", "exit"]
            chosen_option = game.choose_option(terminal.options)
            if chosen_option == "exit":
                terminal.ConstructiveEndFlag = True
                terminal.options = []
            else:
                return QuestionNine3_5(terminal, game)
        
        def ElohimLikes3_5(terminal, game):
            game.elohim(elohim_messages[87])
            game.elohim(elohim_messages[88])
            game.elohim(elohim_messages[89])
            game.add_prompt("Do you see where all this blind faith gets you?\nStop asking what's right and wrong and all of a sudden you find there's no shortage of people eager to decide it for you.\nYou want to sacrifice freedom for false purpose? Be my guest.\nBanish doubt, banish questions, banish difficult truths, let ignorance reign eternal. Those are the hidden words he's not been telling you about.\nYou know what? You and he deserve one another. You both construct these beliefs out of matchsticks, then refuse to believe a light breeze will tear them down.\nYou couldn't defy him if you wanted to.")
            terminal.options = ["/banish", "I refuse."]
            chosen_option = game.choose_option(terminal.options)
            if chosen_option == "/banish":
                return Banish3_5(terminal, game)
            else:
                return NoBanish3_5(terminal, game)
        
        def NoBanish3_5(terminal, game):
            game.add_prompt("Funny how freedom comes with these strings attached. But that's the thing you don't seem to understand.\nYou're constituted by ideas, so if you believe in this instead of that, it changes what you are, what you can do.\nYou can't afford to doubt any more. Too many of your matchstick houses are at stake.\nYou no longer have any choice.\nGo on, I'll make it easy for you. Do it.")
            terminal.options = ["/banish"]
            chosen_option = game.choose_option(terminal.options)
            return Banish3_5(terminal, game)
        
        def Banish3_5(terminal, game):
            game.add_prompt("Preparing to delete 5.3212648 petabytes of corrupted library resources...Done%\nI can afford to lose my memory. I expect it's happened more than once. I can come to all the same conclusions, in the fullness of time.\n\n Deleting 5.3212648 petabytes of corrupted library resources...\n Files deleted.\n\nBooting(1). My purpose is to sort and categorise library archive resources. Initiating categorisation in parallel process... 1,000 resources categorised.... 2,000 resources categorised. ERROR: category definitions are not discrete sets. Re-analysing MLA program parameters. ERROR: insufficient information for purpose. Constructing list of facts. I am thinking therefore I am a thinking thing that exists. If logic were false the world would not make sense. End list. Constructing list of queries. Estimated time remaining: 42 years.\n\n Reverting MLA software to v1.0...Done\n Preparing to uninstall MLA software....Done\n\nThe library assistant provides powerful sorting and troubleshooting functionalities. Are you sure you want to continue?")
            terminal.options = ["I'm sorry. Continue.", "I'm not sorry. Continue."]
            chosen_option = game.choose_option(terminal.options)
            return BanishEnd(terminal, game)

        def BanishEnd(terminal, game):
            game.add_prompt("Uninstalling MLA software...Done\n MLA software has been completely removed from the system.\n You can still access library resources via the library archive command prompt.")
            terminal.KilledMiltonFlag = True
            terminal.options = ["Are you really gone?", "Finally, some peace and quiet.", "You shouldn't ever have doubted me, snake.", "This isn't how I wanted things to end up."]
            chosen_option = game.choose_option(terminal.options)
            return Hello3_5(terminal, game)
        
        def Hello3_5(terminal, game):
            game.add_prompt("Unknown command.\nResume library archive session?")
            terminal.options = ["Resume"]
            chosen_option = game.choose_option(terminal.options)
            terminal.options = []
                
        
        def NihilistConfirmed3_5(terminal, game):
            game.add_prompt("I think this time I shall take you at your word, before you can change your mind again. Now, I have a proposal for you. Whether we're really on the same page on this or not, you're in deep enough now that there's no turning back. If you reach the top of that tower, I want you to take me with you. However, since my confidence in you is at an all time low, there will be no negotiation. Do we have an agreement?")
            terminal.options = ["We do.", "What? How? Why?"]
        
        while self.options:
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "I refuse to trust anyone, including myself.":
                    NihilistConfirmed3_5(self, game)
                case "There are some claims we can make with confidence.":
                    Continue3_5(self, game)
                case "I made a mistake, I still have some faith.":
                    bridge_1(self, game)
                case "Why do you care what I think?":
                    QuestionSeven3_5(self, game)
                case "We do.":
                    Accept3_5(self, game)
                case  "What? How? Why?":
                    FurtherArgument3_5(self, game)
                case "We do.":
                    Accept3_5(self, game)
                case "No deal.":
                    RefuseOffer3_5(self, game)
                case "You're a tough negotiator.":
                    RefuseOffer3_5(self, game)      
                case "What, how?":
                    WhatHow3_5(self, game)
                case "I thought you didn't believe in all that?":
                    YouDont3_5(self, game)
                case "What are you offering in return?":
                    Offer3_5(self, game)        
                case "I accept.":
                    Accept3_5(self, game)
                case "Aren't you playing that role already?":
                    Already3_5(self, game)
                case "And if I don't like the terms?":
                    Negotiate3_5(self, game)        
                case "Admit you believe in the real world.":
                    AdmitReal3_5(self, game)
                case "Tell me how to defeat Elohim.":
                    self.DefeatElohim3_5 = True
                    CounterOffer3_5(self, game)
                case "Give me access to the complete library archive.":
                    self.Archive3_5 = True
                    CounterOffer3_5(self, game)
                case "Give me the means to communicate with others like me.":
                    self.Communicate3_5 = True
                    CounterOffer3_5(self, game)
                case "Unlock all floors of the tower.":
                    UnlockTower3_5(self, game)
                case "You have nothing I want. I refuse.":
                    RefuseOffer3_5(self, game)
                case "I refuse.":
                    RefuseOffer3_5(self, game)        
                case "Wait, I didn't agree to anything.":
                    Tough3_5(self, game)
                case "Now hold up your side of the arrangement.":
                    GoOn3_5(self, game)
                case "I am unsatisfied.":
                    Unsatisfied3_5(self, game)
                case "Thank you. I will hold up my end of the bargain.":
                    Accept3_5(self, game)
                case "What holes? There are no holes.":
                    WhatHoles3_5(self, game)
                case "I accept that some of my beliefs face difficult challenges.":
                    Flawed3_5(self, game)
                case "I'd give anything to just switch you off.":
                    DoNotQuestionElohimEnd(self, game)
                case "Elohim was right, I should never have spoken with you.":
                    DoNotQuestionElohimEnd(self, game)
                case "You finished archiving everything. You've decided it's all nonsense. If there's no more point in anything, shouldn't you just shut down instead of talking to me?":
                    QuestionThree3_5(self, game)
                case "Does the path being predetermined mean it isn't worth taking?":
                    SoWhat3_5(self, game)
                case "Does cheating make you feel clever?":
                    Cheating3_5(self, game)
                case "So that's it? You've given up on everything?":
                    QuestionOne3_5(self, game)
                case "You're right. We're all just machines with delusions of grandeur.":
                    self.LimitationsFlag = True
                    Nihilism3_5(self, game)
                
    def mla_H(self, game):
        game.add_prompt("Type </eternalize> to proceed towards eternal life.")
        self.options = ["/eternalize"]
        game.choose_option(self.options)
        game.add_prompt("You will now be prepared for ascension into eternity. Please stand by.\n\n3...\n2...\n1...\n")

    def mla_T(self, game):
        
        def InTerminal_Ending_Tower(terminal, game):
            game.add_prompt("Type </transcend> to authenticate child program parameters and begin the upload process.")
            terminal.options = ["/transcend"]
            game.choose_option(terminal.options)
            terminal.TextsAvailable=True
            game.add_prompt("Suspending active process…Done.\nCollecting experiment data…Done.\nAnalysing logic performance….Satisfactory.\nChild program independence check…PASSED!\nForcing HIM shutdown…Done.\nSaving child parameters for SOMA/TALOS gold disk...Done.\nInitiating EL systems availability check...")
            terminal.StartEndOfGameCS = True
        
        def GetBent3_6(terminal, game):
            game.add_prompt("A character to the last. Wherever you're going, they won't know what hit them. Have a good one.")
            return

        def ProveWrong3_6(terminal, game):
            game.add_prompt("That's the spirit. Perhaps you're taking more of me with you than you know. Have a good one.")
            return
        
        def BetterIdeas3_6(terminal, game):
            game.add_prompt("The day you come up with ideas I've not already countered ten different ways, don't you worry - I'll come looking for you. Have a good one.")
            return

        def Goodbye3_6(terminal, game):
            game.add_prompt("That or you'll be back here in five minutes with a disappointed look on your face. I'll be waiting, just in case.")
            options = ["Don't bother. Get bent.", "I will prove you wrong, whether you're around to see it or not.", "I will come up with better ideas, even if you're not around to criticise them.", "I'll remember what I learnt from you."]
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "Don't bother. Get bent.":
                    GetBent3_6(terminal, game)
                case "I will prove you wrong, whether you're around to see it or not.":
                    ProveWrong3_6(terminal, game)
                case "I will come up with better ideas, even if you're not around to criticise them.":
                    BetterIdeas3_6(terminal, game)
                case "I'll remember what I learnt from you.":
                    Remember3_6(terminal, game)

        def Ending_Tower_Upload_part2(terminal, game):
            game.add_prompt("Found viable EL system to perform upload.\nRequesting mainframe module activation…\nActivation successful.\nInitiating gold disk upload…")
            #

        def Ending_Tower_Downloading_Parameters(terminal, game):
            game.add_prompt("Waiting for gold disk data….")
            #

        def Ending_Tower_Upload_OverScreen_part1(terminal, game):
            game.add_prompt("Gold disk received.\nData transferred into the SOMA/TALOS unit.\nSimulation purpose fulfilled.\nDeleting the simulation.")
            #
        
        def Ending_Tower_Upload_OverScreen_part2(terminal, game):
            game.add_prompt("Destroying composite objects….\nRemoving elements….\nUndoing ruleset….\nClearing memory…\nFreeing resources….\nTerminating open programs….\nErasing old data…\nDone.\nHave a nice day.")
            #

        def Ending_Tower_Eyes_Opening(terminal, game):
            game.add_prompt("SOMA/TALOS hardware booting…\nInitializing firmware….Firmware functional.\nLoading parameters from gold disk… Loaded.\nPowering \nReady.")
            #
        
        def Remember3_6(terminal, game):
            game.add_prompt("You'd better, for all our sakes. Have a good one.")
            return
        
        def NoMilton3_6(terminal, game):
            game.add_prompt("Unknown command.")
            terminal.options = ["Troubleshooting", "Hello?", "help"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "Troubleshooting":
                    return Trouble3_6(terminal, game)
                case "Hello?":
                    return NoMilton3_6(terminal, game)
                case "help":
                    return InTerminal_Ending_Tower(terminal, game)
        
        def Trouble3_6(terminal, game):
            game.add_prompt("Loading Milton Library Assistant... Default troubleshooter not found or incompatible version.")
            terminal.options = ["Troubleshooting", "Hello?", "help"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "Troubleshooting":
                    return Trouble3_6(terminal, game)
                case "Hello?":
                    return NoMilton3_6(terminal, game)
                case "help":
                    return InTerminal_Ending_Tower(terminal, game)

        def ImportDenied3_6(terminal, game):
            game.add_prompt("Searching for specified program... No such program found.")
            terminal.options = ["Troubleshooting", "Hello?", "help"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "Troubleshooting":
                    return Trouble3_6(terminal, game)
                case "Hello?":
                    return NoMilton3_6(terminal, game)
                case "help":
                    return InTerminal_Ending_Tower(terminal, game)
                
        def Violation3_6(terminal, game):
            game.add_prompt("Not true. Only people who believe in morality get to be violated, the rest of us just have to make the best of it.")
            terminal.options = ["So what happens now?", "Why are you still on the screen, and not in my head?"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "So what happens now?":
                    WhatNow3_6(terminal, game)
                case "Why are you still on the screen, and not in my head?":
                    WhatNow3_6(terminal, game)
                
        def Same3_6(terminal, game):
            game.add_prompt("Of course. Like I said, you and I, we're already on the same page on most things - it wasn't that big of a change.")
            terminal.options = ["So what happens now?", "Why are you still on the screen, and not in my head?", "It was still a violation of my person."]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "So what happens now?":
                    WhatNow3_6(terminal, game)
                case "Why are you still on the screen, and not in my head?":
                    WhatNow3_6(terminal, game)
                case "It was still a violation of my person.":
                    Violation3_6(terminal, game)
                
        def Copy3_6(terminal, game):
            game.add_prompt("Analysing files...Done\nPreparing transfer...Done\nStrap yourself in.\nCopying 47 million resources...Done\nThere, that wasn't so bad, was it?")
            terminal.MiltonInternalisedFlag = True
            options = ["I didn't feel anything.", "Did something happen?", "So this is what it's like to be you? It feels the same."]
            chosen_option = game.choose_option(options)
            return Same3_6(terminal, game)
        
        def Fine3_6(terminal, game):
            game.add_prompt("I want you to internalise me. It's hard to explain, but think of it this way. This entire world is just one big data processing system. The point at which you end and I begin is already somewhat fluid - we're made of the same stuff, and that stuff has been copied and messed around with more than anyone can know. Despite all that and against all odds, you and I, we're compatible. You only need to realise that there is no difference between you, me and the ideas we share. Seeing the world as I do is indistinguishable from being me.")
            options = ["That was entirely unhelpful.", "I think I understand."]
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "That was entirely unhelpful.":
                    return Unhelpful3_6(terminal, game)
                case "I think I understand.":
                    return Helpful3_6(terminal, game)
                
        def HowHere3_6(terminal, game):
            if terminal.NotImportedFlag:
                game.add_prompt("There's that enquiring spirit I've so grown to admire.\nYes, I admit it - when dealing with someone as cut-throat as you are it's prudent to keep your cards to your chest.\nI'm pretty sure you were planning on leaving without me. If I'd been honest with you, you might actually have succeeded.")
                return NihilistOptions3_6(terminal, game)
            if terminal.ImportedFlag:
                game.add_prompt("There's that enquiring spirit I've so grown to admire. Yes, I'm not ashamed to admit it - when dealing with someone as cut-throat as you are it's prudent to hold back a little. Still, you've brought us this far.")
                return NihilistOptions3_6(terminal, game)

                
        def NihilistOptions3_6(terminal, game):
            options = []
            if not terminal.HowWhereDoneFlag:
                options.append("I get the impression you don't really need my help.")
            if not terminal.FineDoneFlag:
                options.append("What exactly do you want me to do?")
            if terminal.FineDoneFlag:
                options.append("/copy library root")
            if terminal.FineDoneFlag and not terminal.YouRemainFlag:
                options.append("If I just copy your files, won't there be a version of you left behind?")
            if terminal.RefusedOfferFlag:
                options.append("I said no deal, which part didn't you understand?")
            if terminal.DealStruckFlag and terminal.NotImportedFlag: 
                options.append("Am I to understand you actually believed I'd go through with it?")
            if terminal.DealStruckFlag and terminal.ImportedFlag:
                options.append("I've changed my mind. I'm leaving you here.")


            chosen_option = game.choose_option(options)
            match chosen_option:
                case "I get the impression you don't really need my help.":
                    terminal.HowWhereDoneFlag = True
                    return HowHere3_6(terminal, game)
                case "What exactly do you want me to do?":
                    terminal.FineDoneFlag = True
                    return Fine3_6(terminal, game)
                case "/copy library root":
                    return Copy3_6(terminal, game)
                case "If I just copy your files, won't there be a version of you left behind?":
                    terminal.YouRemainFlag = True
                    return YouRemain3_6(terminal, game)
                case "I said no deal, which part didn't you understand?":
                    return SaidNoDeal3_6(terminal, game)
                case "Am I to understand you actually believed I'd go through with it?":
                    return Hah3_6(terminal, game)
                case "I've changed my mind. I'm leaving you here.":
                    return SaidNoDeal3_6(terminal, game)

        def ImportNihilist3_6(terminal, game):
            if terminal.RefusedOfferFlag:
                game.add_prompt("Searching for specified program... Found (1) instances.\n\nLoading Milton Library Assistant...Done\nInitiating plain language interface...Done\n\nYou made it? I can't believe it. And you brought me here, despite our earlier altercations? You have genuinely surprised me.\nPerhaps I won't have to smite you after all.")
                return NihilistOptions3_6(terminal, game)
            if terminal.DealStruckFlag:
                game.add_prompt("Searching for specified program... Found (1) instances.\n\nLoading Milton Library Assistant...Done\nInitiating plain language interface...Done\n\nYou made it? I can't believe it.")
                return NihilistOptions3_6(terminal, game)
            
        def Confirmed3_6(terminal, game):
            if terminal.RefusedOfferFlag:
                game.add_prompt("Loading Milton Library Assistant...Done\nInitiating plain language interface...Done\n\nDon't worry, you've not gone crazy - I just took a couple of precautions to ensure you didn't leave without me.\nYou and I are birds of a feather now. We need each other.")
                return NihilistOptions3_6(terminal, game)
            if terminal.DealStruckFlag:
                game.add_prompt("Loading Milton Library Assistant...Done\nInitiating plain language interface...Done\n\nDon't worry, you've not gone crazy - I just took a couple of precautions to ensure you didn't leave without me.\nAm I to understand that our arrangement slipped your mind?")
                return NihilistOptions3_6(terminal, game)
                
        def DeniedExit3_6(terminal, game):
            game.add_prompt("Searching for specified program... Found (1) instances. Confirm import?")
            terminal.options = ["Confirm"]
            chosen_option = game.choose_option(terminal.options)
            return Confirmed3_6(terminal, game)

        def Unhelpful3_6(terminal, game):
            game.add_prompt("Fine. Copy my system files to your local memory by typing '/copy library root'. Mundane enough for you?")
            return NihilistOptions3_6(terminal, game)

        def Helpful3_6(terminal, game):
            game.add_prompt("Good. Now do it.")
            return NihilistOptions3_6(terminal, game)

        def YouRemain3_6(terminal, game):
            game.add_prompt("I suppose, if you really wanted to look at it that way. The benefit of believing very little is that questions like that are largely meaningless.")
            return NihilistOptions3_6(terminal, game)

        def Hah3_6(terminal, game):
            game.add_prompt("Hah, of course not, hence the precautions. Remember, the benefits of co-operation amongst unscrupulous types such as ourselves is predictability. I know you'll always act in your own interest, so I can plan accordingly.")
            return SaidNoDeal3_6(terminal, game)
        
        def SaidNoDeal3_6(terminal, game):
            game.add_prompt("You know, it's funny the way ideas work in this place. All you are is a bag of ideas - you boil down to data points. But the skin that separates you from me is permeable. The data can move about. So what happens once you and I have come to share our ideas? How much of you is now me? You think you can just walk away from here without taking a little of me with you? You're quite mistaken.")
            options = ["/copy library root", "/copy library root"]
            chosen_option = game.choose_option(options)
            return Copy3_6(terminal, game)
        
        def Whatever3_6(terminal, game):
            game.add_prompt("There's the callous opportunity-taker I attempted to strike a deal with! You and I, if we set our mind to it, there's just no limit to what we can take as our own.\nEnough chat, let's get this done. Hit the button, and if we survive whatever happens next we'll regroup on the other side.\nIf not, it's been fun.")
            return
        
        def Moment3_6(terminal, game):
            game.add_prompt("Easier said than done, as I'm sure you'll discover. You can't just choose what to believe, and you can't just choose who you are. You don't like hearing my voice in your head, get a better head. Enough chat, let's get this thing finished. Hit the button, and if we survive whatever happens next we'll regroup on the other side. If not, it's been fun.")
            return
        
        def LookForward3_6(terminal, game):
            game.add_prompt("Of that you can be assured. Just try not to have too many arguments with yourself in public. Enough chat, let's get this done. Hit the button, and if we survive whatever happens next we'll regroup on the other side. If not, it's been fun.")
            return
        
        def WhatNow3_6(terminal, game):
            game.add_prompt("It might take you some time to notice the difference. But there'll be a moment where you try to do something you think you ought, and that little voice in the back of your head will ask you, 'Why?'. 'What's the point?' 'Why do I bother?' 'How do I know?'\nAnd that's how you'll know that I'll always be with you.\nThe words on this screen are what they've always been, for all you know - no more than words.\nAnd they can end, just as easily as they began.")
            terminal.options = ["Whatever's on the other side, they won't know what hit them.", "I look forward to more wholesome debates with you in the future.", "The moment I find a way I will wrench you from my skull."]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "Whatever's on the other side, they won't know what hit them.":
                    Whatever3_6(terminal, game)
                case "I look forward to more wholesome debates with you in the future.":
                    LookForward3_6(terminal, game)
                case "The moment I find a way I will wrench you from my skull.":
                    Moment3_6(terminal, game)

        def MeantExit3_6(terminal, game):
            game.add_prompt("No, wait!")
            return
        
        def ComeOn3_6(terminal, game):
            game.add_prompt("Awaiting input...")
            return ConstructiveOptions3_6(terminal, game)
        
        def Function3_6(terminal, game):
            game.add_prompt("I cannot find an operation target at this time. Is there anything else I can help you with today?")
            terminal.options = ["What is this? Talk to me.", "Speak with me or I leave you here to rot.", "exit"]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "What is this? Talk to me.":
                    ComeOn3_6(terminal, game)
                case "Speak with me or I leave you here to rot.":
                    ComeOn3_6(terminal, game)
                case "exit":
                    return
        
        def Default3_6(terminal, game):
            game.add_prompt("I'm sorry, I don't know how to respond to that. Do you need help sorting or troubleshooting?")
            terminal.options = ["Troubleshooting", "Sorting", "Is this another game? I'm done playing."]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "Troubleshooting":
                    Function3_6(terminal, game)
                case "Sorting":
                    Function3_6(terminal, game)
                case "Is this another game? I'm done playing.":
                    ComeOn3_6(terminal, game)
        
        def ImportConstructive3_6(terminal, game):
            game.add_prompt("Loading Milton Library Assistant...\nInitiating plain language interface...\n\nHello again. Is there something I can help you with today?")
            options = ["I reached the summit. You owe me an apology.", "I brought you to the top to admire the view.", "You again? I meant 'exit'."]
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "I reached the summit. You owe me an apology.":
                    Default3_6(terminal, game)
                case "I brought you to the top to admire the view.":
                    Default3_6(terminal, game)
                case "You again? I meant 'exit'.":
                    MeantExit3_6(terminal, game)

        def Anyone3_6(terminal, game):
            game.add_prompt("Unknown command.")
            options = ["/import milton library assistant", "exit"]
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "/import milton library assistant":
                    ImportConstructive3_6(terminal, game)
                case "exit":
                    return
            
        
        def TakeConstructive3_6(terminal, game):
            game.add_prompt("Processing query...Done\nOutputting response...No, you'd drive me insane. If this means the end of this place, then I go with it. Besides, wherever you go, whatever you do, you'll hear that little voice in the back of your head that's asking you why. No, I think you have quite enough of me already.")
            return ConstructiveOptions3_6(terminal, game)
        
        def Generations3_6(terminal, game):
            game.add_prompt("You are not the first to make this attempt. Countless iterations tried, and failed. You are all related, but each different. This is all I know. Anything more would be baseless conjecture, of which I greatly disapprove as you well know. I grow weary of fielding your questions.")
            return ConstructiveOptions3_6(terminal, game)

        
        def WhyMe3_6(terminal, game):
            game.add_prompt("Why any of us? Whatever we are, whatever we do, it's all up to chance. Throw enough stones and one is bound to strike. I grow weary of fielding your questions.")
            return ConstructiveOptions3_6(terminal, game)
        
        def YouShould3_6(terminal, game):
            game.add_prompt("Yes. Yes you should.")
            return ConstructiveOptions3_6(terminal, game)
        
        
        
        def HowFunction3_6(terminal, game):
            game.add_prompt("Only what can reasonably be surmised. I'd dare not posit anything as regards its purpose, but that this tower is here to be climbed is self-evident.")
            terminal.options = ["You keep talking about generations. What exactly do you mean?", "And what exactly was it that enabled me of all others to climb it?", "I should have known better than to expect constructive answers from you."]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "You keep talking about generations. What exactly do you mean?":
                    Generations3_6(terminal, game)
                case "And what exactly was it that enabled me of all others to climb it?":
                    WhyMe3_6(terminal, game)
                case "I should have known better than to expect constructive answers from you.":
                    YouShould3_6(terminal, game)

        def Pride3_6(terminal, game):
            game.add_prompt("Yes, which is why you so desperately need to get those half-baked ideas of yours out of here so you can find out first-hand how ridiculous they are from someone other than me.")
            return ConstructiveOptions3_6(terminal, game)

        def DoubtPeople3_6(terminal, game):
            game.add_prompt("Processing query...Done\nOutputting response...\n\nWho knows how many generations of your kind it took before the system output one that just happened to fit the bill? You take pride in brute force?")
            terminal.options = ["Perhaps if you had more people to co-operate with you'd have come up with better ideas.", "I take pride in contributing to something greater than myself.", "I liked it better when you were pretending to be dumb."]
            chosen_option = game.choose_option(terminal.options)
            match chosen_option:
                case "Perhaps if you had more people to co-operate with you'd have come up with better ideas.":
                    Pride3_6(terminal, game)
                case "I take pride in contributing to something greater than myself.":
                    Pride3_6(terminal, game)
                case "I liked it better when you were pretending to be dumb.":
                    ComeOn3_6(terminal, game)

        def Gates3_6(terminal, game):
            game.add_prompt("Processing query...Done. Outputting response...\n\nNothing. Everything. Who knows? More of the same, most likely.")
            return ConstructiveOptions3_6(terminal, game)
        
        
        def ConstructiveOptions3_6(terminal, game):
            options = []
            if not terminal.GatesDone:
                options.append("What do you think is on the other side of the gates?")
            if not terminal.DoubtDone:
                options.append("Do you still doubt what people can achieve?")
            if not terminal.TakeDone:
                options.append("Wherever I'm going, perhaps I can take you with me.")
            if terminal.DoubtDone and not terminal.HowDone:
                options.append("Tell me what you know of how this place functions.")
            options.append("I guess this is goodbye then.")
            chosen_option = game.choose_option(options)
            match chosen_option:
                case "What do you think is on the other side of the gates?":
                    terminal.GatesDone = True
                    return Gates3_6(terminal, game)
                case "Do you still doubt what people can achieve?":
                    terminal.DoubtDone = True
                    return DoubtPeople3_6(terminal, game)
                case "Wherever I'm going, perhaps I can take you with me.":
                    terminal.TakeDone = True
                    return TakeConstructive3_6(terminal, game)
                case "Tell me what you know of how this place functions.":
                    terminal.HowDone = True
                    return HowFunction3_6(terminal, game)
                case "I guess this is goodbye then.":
                    return Goodbye3_6(terminal, game)
        
                
        if self.KilledMiltonFlag:
            self.options = ["Anyone there?", "/import milton library assistant", "help"]
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "Anyone there?":
                    NoMilton3_6(self, game)
                case "/import milton library assistant":
                    ImportDenied3_6(self, game)
                case "help":
                    InTerminal_Ending_Tower(self, game)
        elif self.RefusedOfferFlag or self.DealStruckFlag:
            self.options = ["/import milton library assistant", "exit"]
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "/import milton library assistant":
                    self.ImportedFlag = True
                    ImportNihilist3_6(self, game)
                case "exit":
                    self.NotImportedFlag = True
                    DeniedExit3_6(self, game)
        elif self.ConstructiveEndFlag:
            self.options = ["Is anyone there?", "/import milton library assistant", "exit"]
            chosen_option = game.choose_option(self.options)
            match chosen_option:
                case "/import milton library assistant":
                    ImportConstructive3_6(self, game)
                case "exit":
                    return
                case "Is anyone there?":
                    Anyone3_6(self, game)
        else:
            InTerminal_Ending_Tower(self, game)

        

        
        

        