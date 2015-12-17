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

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print self.title
        print self.print_state()

    def get_prompt(self):
        return self.prompt

    def print_state(self):
        print '''
You are a pit fighter. Fight your way out of the pit, earn new items with each victory.

This is a fight to the death, good luck.
        '''
