import os

class View(object):

    def __init__(self):
        self.prompt = '$=> '
        self.title = '''
$$$$$$$\  $$\   $$\           $$$$$$$$\ $$\           $$\        $$\\
$$  __$$\ \__|  $$ |          $$  _____|\__|          $$ |       $$ |
$$ |  $$ |$$\ $$$$$$\         $$ |      $$\  $$$$$$\  $$$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\\
$$$$$$$  |$$ |\_$$  _|        $$$$$\    $$ |$$  __$$\ $$  __$$\\\\_$$  _|  $$  __$$\ $$  __$$\\
$$  ____/ $$ |  $$ |          $$  __|   $$ |$$ /  $$ |$$ |  $$ | $$ |    $$$$$$$$ |$$ |  \__|
$$ |      $$ |  $$ |$$\       $$ |      $$ |$$ |  $$ |$$ |  $$ | $$ |$$\ $$   ____|$$ |
$$ |      $$ |  \$$$$  |      $$ |      $$ |\$$$$$$$ |$$ |  $$ | \$$$$  |\$$$$$$$\ $$ |
\__|      \__|   \____/       \__|      \__| \____$$ |\__|  \__|  \____/  \_______|\__|
                                            $$\   $$ |
                                            \$$$$$$  |
                                             \______/
'''
        self.context = '''
You are a pit fighter, this is a fight to the death, good luck
'''
        self.chunks = [self.title, self.context]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        #print self.title
        self.print_state(self.chunks)


    def get_prompt(self):
        return self.prompt

    def print_state(self, chunks):
        for x in self.chunks:
            print x

    def print_box_array(self, array, width=30):
        print "+------------------------------+"
        for item in array:
            print "|  " + item.get_name()
        print "+------------------------------+"