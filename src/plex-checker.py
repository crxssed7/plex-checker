from xml.etree.ElementTree import Element
from plexapi.myplex import MyPlexAccount

if __name__ == '__main__':
    plexUsername = input('What is your Plex username: ')
    plexPassword = input('What is yout Plex password: ')
    plexServer = input('What is the name of your server that you want to connect to: ')

    try:
        # Connect to Plex
        account = MyPlexAccount(plexUsername, plexPassword)
        plex = account.resource(plexServer).connect()

        # Print welcome message
        print()
        print('Welcome to Plex Checker by crxssed!')
        print('Plex user: ' + account.username)
        print()

        # Bool to determine whether to break the search loop
        loop = True

        # Predermined list for shows 
        shows = None

        while loop:
            tv_show = input('What TV show are you looking for today? ')
            print('These are the results for your query:')
            shows = [x for x in plex.search(tv_show) if x.type == 'show']
            for show in range(len(shows)):
                print(str(show) + ". " + shows[show].title)
            if not shows:
                choice = input('No shows found, do you want to search again? Y/N: ')
                if choice == 'N' or choice == 'n':
                    loop = False
                    exit()
            else:
                loop = False

        choice_for_show = int(input('Choose the number corresponding to the show you want: '))
        chosen_show = shows[choice_for_show]

        

    except Exception as e:
        print('error: ' + str(e))