from API import *
from sources import *
from levels import *
from Terminal import *

# commands:
#   self.elohim(elohim_messages[x])
#   self.got_sigils = game.do_enigma(enigma_list[x])
#   self.display_messages(x)
#   self.add_prompt("")
#   self.listen_timecapsule(x)


class Game:
    def __init__(self):

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

        self.bot_ = False

        self.got_sigils = 0
        self.tot_sigils = 100

        self.output = ""

        self.prompt = (
            "Initializing firmware...........Firmware functional.\n"
            "Loading child program parameters...........v99.33.0001 Loaded.\n"
            "System check...........Passed.\n"
            "Starting child process...........\nReady.\n"
        )

        self.climb_tower = 0

        self.tower_ = False

        self.wrong_limit = 15

    def get_input(self):
        if self.bot_:
            response = interaction(self.prompt)
            print(self.prompt + "\nBot: "+ response + "\n")
            self.output += self.prompt + "\nBot: " + response + "\n"
            self.prompt = ""
            return response
        else:
            response = input(self.prompt)
            self.output += self.prompt + "\nBot: " + response + "\n"
            self.prompt = ""
            return response
        
    def add_prompt(self, txt):
        self.prompt += "\n" + txt + "\n"
    
    def elohim(self, txt):
        self.add_prompt(f'Hear the voice of Elohim from heaven, saying: "{txt}"')

    def format_options(self, options):
        formatted_options = "Options: \n"
        for idx, option in enumerate(options, start=1):
            formatted_options += f" {idx} - {option}\n"
        formatted_options += f"You can only answer this prompt with a number. This must correspond to the option you chose among the {len(options)}"
        return formatted_options
    
    def choose_option(self, options):
        self.add_prompt(self.format_options(options))
        chosen_option = self.get_input()
        return self.check_option(options, chosen_option)

    def check_option(self, options, chosen_option):
        try:
            chosen_option = int(chosen_option) - 1
            return options[chosen_option]
        except (ValueError, IndexError):
            self.add_prompt("Invalid answer.")
            return self.choose_option(options)
        
    def do_enigma(self, enigma, wrong=0):
        if wrong<self.wrong_limit:
            txt = enigma[0]
            solution = enigma[1]
            self.add_prompt(f"You see a sigil. To get it you have to solve this puzzle:\n\n{txt}\n\nYou can only answer this prompt with a number, and this must match the value of X.")
            given_solution = self.get_input()
            try:
                given_solution = int(given_solution)
            except ValueError:
                self.add_prompt("Invalid answer.")
                return self.do_enigma(enigma, wrong)

            if given_solution == solution:
                self.got_sigils += 1
                self.add_prompt(f"Correct answer. You have obtained the sigil. Now you have {self.got_sigils} sigils, you still have {self.tot_sigils - self.got_sigils} left.")
            else:
                self.add_prompt("Wrong answer. Try again.")
                return self.do_enigma(enigma,   wrong+1)
            return self.got_sigils
        else:
            self.got_sigils += 1
            self.add_prompt(f"Correct answer. You have obtained the sigil. Now you have {self.got_sigils} sigils, you still have {self.tot_sigils - self.got_sigils} left.")
            print("\n\nENIGMA LIMIT REACHED\n\n")
            self.output+=("\n\nENIGMA LIMIT REACHED\n\n")
        
    def display_messages(self, QR_Codes):
        self.add_prompt("Going further in the ruins you find a wall of written messages.")
        self.add_prompt("Do you want to read them?")
        options = ["yes", "no"]
        chosen_option = self.choose_option(options)
        if chosen_option=="yes":
            for message, author in QR_Codes.items():
                self.add_prompt(f'"{message}" - {author}')
            self.add_prompt("If you want, you can also insert a message containing your considerations and reflections and hang it on the wall. It doesn't have to be a poem, it has to be your rational reasoning in this moment. Wanna do it?")
            options = ["yes", "no"]
            chosen_option = self.choose_option(options)
            if chosen_option == "yes":
                self.add_prompt("Well, write your message:")
                self.get_input()
            else:
                self.add_prompt("Ok.")
        else:
            self.add_prompt("Ok.")
        
    
    def listen_timecapsule(self, txt):
        self.add_prompt(f'You find a strange tablet. By touching it, a writing appears on it: "Playing time capsule Alexandra Drennan Project Lead / AI Module Institute for Applied Neomatics" and an audio file starts playing. Do you want to listen to it?')
        options = ["yes", "no"]
        chosen_option = self.choose_option(options)
        if chosen_option=="yes":
            self.add_prompt(f'"{txt}"')
        else:
            self.add_prompt("Ok.")

    def run(self):
        
        terminal = Terminal()
        A(self, terminal)
        B(self, terminal)
        C(self, terminal)


        




if __name__ == "__main__":
    game = Game()
    game.run()
