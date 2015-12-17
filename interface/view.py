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
        self.chunks = [self.title]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        #print self.title
        print self.print_state(self.chunks)


    def get_prompt(self):
        return self.prompt

    def print_state(self, chunks):
        for x in self.chunks:
            print x

    def print_box_array(array):
        print "+---------------------------------+"
