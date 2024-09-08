import helper as h, time as t

#  TITLE SCREEN
## ========================================================================
def displayTitleSeries():
    h.clearScreen()
    displayTitleA()
    displayTitleB()
    displayTitleC()

def displayTitleA():
    print('''

            ██████  ██ ███████ ███████  ██████  ██    ██  █████  ██████      ██ ███    ██ ████████ ██████   ██████  ██████  ██    ██  ██████ ████████ ██  ██████  ███    ██    
            ██   ██ ██    ███  ██      ██    ██ ██    ██ ██   ██ ██   ██     ██ ████   ██    ██    ██   ██ ██    ██ ██   ██ ██    ██ ██         ██    ██ ██    ██ ████   ██ ██ 
            ██████  ██   ███   ███████ ██    ██ ██    ██ ███████ ██   ██     ██ ██ ██  ██    ██    ██████  ██    ██ ██   ██ ██    ██ ██         ██    ██ ██    ██ ██ ██  ██    
            ██   ██ ██  ███         ██ ██ ▄▄ ██ ██    ██ ██   ██ ██   ██     ██ ██  ██ ██    ██    ██   ██ ██    ██ ██   ██ ██    ██ ██         ██    ██ ██    ██ ██  ██ ██ ██ 
            ██████  ██ ███████ ███████  ██████   ██████  ██   ██ ██████      ██ ██   ████    ██    ██   ██  ██████  ██████   ██████   ██████    ██    ██  ██████  ██   ████    

''')
    h.pressEnter()

def displayTitleB():
    print('''

                     ,gggggggggggg,                                               ,ggggggggggg,                                                                    
                    dP"""88""""""Y8b,                                        8I  dP"""88""""""Y8, ,dPYb,                                                      I8   
                    Yb,  88       `8b,                                       8I  Yb,  88      `8b IP'`Yb                                                      I8   
                    `"  88        `8b                          gg           8I   `"  88      ,8P I8  8I                                                   88888888
                        88         Y8                          ""           8I       88aaaad8P"  I8  8'                                                      I8   
                        88         d8  ,gggg,gg     ggg    gg  gg     ,gggg,8I       88""""Y8ba  I8 dP   ,ggg,     ,g,       ,g,      ,ggg,    ,ggg,,ggg,    I8   
                        88        ,8P dP"  "Y8I    d8"Yb   88bg88    dP"  "Y8I       88      `8b I8dP   i8" "8i   ,8'8,     ,8'8,    i8" "8i  ,8" "8P" "8,   I8   
                        88       ,8P'i8'    ,8I   dP  I8   8I  88   i8'    ,8I       88      ,8P I8P    I8, ,8I  ,8'  Yb   ,8'  Yb   I8, ,8I  I8   8I   8I  ,I8,  
                        88______,dP',d8,   ,d8b,,dP   I8, ,8I_,88,_,d8,   ,d8b,      88_____,d8',d8b,_  `YbadP' ,8'_   8) ,8'_   8)  `YbadP' ,dP   8I   Yb,,d88b, 
                        888888888P"  P"Y8888P"`Y88"     "Y8P" 8P""Y8P"Y8888P"`Y8     88888888P"  8P'"Y88888P"Y888P' "YY8P8PP' "YY8P8P888P"Y8888P'   8I   `Y88P""Y8 

''')
    h.pressEnter()
    
def displayTitleC():
    print("                                                                                                             David Blessent... That's me!")
    h.pressEnter()


#  PAGE ONE
## ========================================================================
def displayPageOneSeries():
    h.clearScreen()
    displayPageOneA()
    displayPageOneB()
    displayPageOneC()
    displayPageOneD()
    displaySystemCrash()

def displayPageOneA():
    print('''
                +--==============================================--+--==============================================--+--=============================================--+
                |      __        ___  __          ___              |       ___            __   __    ___  ___         |          __   __        __  ___  __             |
                |     /  \ \  / |__  |__) \  / | |__  |  | .       |      |__   /\  \  / /  \ |__) |  |  |__  .       |         |__) /  \  /\  /__`  |  /__` .          |
                |     \__/  \/  |___ |  \  \/  | |___ |/\| .       |      |    /~~\  \/  \__/ |  \ |  |  |___ .       |         |__) \__/ /~~\ .__/  |  .__/ .          |
                |                                                  |                                                  |                                                 |
                |    NAME        :       DAVID RAY BLESSENT        |    FOODS       :       1) BLUEBERRIES            |    5- WON COSTUME CONTEST AS NINJA TURTLE FF    |   
                |    DOB         :       11-27-1989                |                :       2) PEANUT BUTTER          |    7- PURCHASED COPY OF POKEMON BLUE ON DAY 1   |
                |    HOMETOWN    :       TOMAHAWK, WISCONSIN       |                                                  |    9- DEFEATED THE WINDFISH IN LOZ: LA DX       |
                |    RESIDES     :       APPLETON, WISCONSIN       |    BAND        :       STREETLIGHT MANIFESTO     |   11- FINISHED 2ND IN STOCK MARKET (-72%)       |
                |                                                  |    ALBUM       :       P.S. - GRACELAND          |   14- JOB AT SAMMY'S SUBS, RESTAURANT CURSE     |
                |    ALLERGENS   :       ANTI-HISTAMINES           |    DISNEY SONG :       BARE NECESSITIES          |   15- CONVINCED OLD MAN HE HAD A FLAT TIRE      |
                |                                                  |                                                  |   16- PLAYED FIRST SHOW HALLOWEEN DANCE         |
                |    EDUCATION   :       B.A. ANTHRPOLOGY          |    AUTHORS     :       1) ALBERT CAMUS           |   17- LOST INTERNET ACCESS FIGHTING HS          |
                |                :       UNIVERSITY OF MINNESOTA   |                :       2) ALDOUS HUXLEY          |   18- GRADUATED, DESPITE THE GUIDANCE...        |
                |                                                  |                :       3) PHILIP K DICK          |   21- CZECH REPUBLIC ARCHAEOLOGY                |
                |    HOBBIES     :       READING, WRITING          |    BOOK        :       SPEAKER FOR THE DEAD      |   22- 3D MODELING AND FLINT KNAPPING            |                          
                |                :       VIDEO + BOARD GAMES       |    MOVIES      :       THE GREAT RACE (1965)     |  [10YR WINDOW OF RESTAURANTS AND TOURING BANDS] |                           
                |                :       MAKING MUSIC              |    SNES        :       CHRONO TRIGGER            |   32- BACK TO SCHOOL FOR PROGRAMMING            |
                |                                                  |                                                  |   34- ANY% GLITCHLESS POKEMON BLUE 2HR57MIN     |                     
                +--==============================================--+--==============================================--+--=============================================--+''')
    h.pressEnter()

def displayPageOneB():
    print('''
                +--==============================================--+--==============================================--+--=============================================--+
                |   __   __   __   ___  ___  __   __     __        |       ___      ___       __   ___  __            |           __                    __              |
                |  |__) |__) /  \ |__  |__  /__` /__` | /  \ |\ |  |      |__  |  |  |  |  | |__) |__  /__`  .        |          /__` |__/ | |    |    /__` .           |
                |  |    |  \ \__/ |    |___ .__/ .__/ | \__/ | \|  |      |    \__/  |  \__/ |  \ |___ .__/  .        |          .__/ |  \ | |___ |___ .__/ .           |
                |                                                  |                                                  |                                                 |
                |   GARDEN       :      PULLED WEEDS               |   5YR__________                                  |                CUSTOMER SERVICE                 |   
                |   RESTAURANT   :      COOKED, WAITED, BARTENDED  |   IN FIVE YEARS I WILL BE RUNNING MY SOFTWARE    |              INVENTORY MANAGEMENT               |     
                |   GROCERY      :      DELI'D, BREAD BUYER        |   STARTUP, A POS SYSTEM BUILT FOR RESTAURANTS    |            MANHATTANS + LAST WORDS              |   
                |   CALL CENTER  :      PET SUPPLIES               |   AND BARS, WITH FEATURES FOR CLUBS/MEMBERSHIP   |            DOOM 1993 LEVEL DESIGN               |        
                |   SNOW REMOVAL :      SUFFERED                   |                                                  |        NEGOTIATION (HOSTAGE & OTHERWISE)        | 
                |   WAREHOUSE    :      DROPPED A PALLET OF CORONA |   10YR_________                                  |          PURCHASING + VENDOR RELATIONS          |
                |   GOLF COURSE  :      BARTENDED                  |   IN TEN YEARS AHP WILL HAVE GROWN TO ITS FULL   |                 BASS GUITARS                    |
                |                                                  |   POTENTIAL AND I WILL HAVE ASSEMBLED A TEAM OF  |          AUDIO PRODUCTION/ENGINEERING           |
                |   WEB DEV      :      WAGE WAR V PACKAGE DEPENDS |   OF PEOPLE MORE BRILLIANT AND TALENTED THAN I   |         SAMPLERS/SEQUENCERS/SYNTHESIZER         |
                |                :      WEASEL2!                   |   TO INSTANTIATE ALL MY OBJECTS                  |               LARAVEL FRAMEWORK                 |
                |                :      REPORT GENERATOR FOR ERP   |                                                  |                MYSQL WORKBENCH                  |
                |                                                  |   20YR_________                                  |            FIXING MY DAD'S COMPUTER             |
                |   OWNER        :      ALMOND HOUSE PUBLISHING    |   LEADING A VILLAGE OF REBELS IN A DYSTOPIAN     |             MATERIAL CULTURE THEORY             |
                |                                                  |   APOLOCALYTIC NIGHTMARE, WITH MY FRIEND JOHN    |            EXISTENTIALIST LITERATURE            |
                +--==============================================--+--==============================================--+--=============================================--+''')
    h.pressEnter()
    h.clearScreen()

def displayPageOneC():
    print('''
          


                +--==============================================--+--==============================================--+--=============================================--+
                |                                                                                                                                                       |
                |                                                             That's a little bit about me.                                                             |
                |                                                 You can call me David or Dave, it doesn't matter to me.                                               |
                |                                                                                                                                                       |
                |                                                         Historically, I've also repsonded to:                                                         |
                |                                        Davey, Daver, Mr Vid, Divad, Davidivitch, Blessauntwich, Blessent-be-thy-Name,                                 |
                |                                               Doglyfe Dave, Dirtlyfe Dave, Richard's Brother, and Hey You.                                            |
                |                                                                                                                                                       |
                |                          I am excited and honored to be included in this group and to have the opportunity to get to know you all.                    |
                |                              I look forward to collaborating together and hopefully learning a lot more than a thing or two.                          |
                |                                                                                                                                                       |
                +--==============================================--+--==============================================--+--=============================================--+
          


''')
    h.pressEnter()

def displayPageOneD():
    print('''
                                                      ___       __   ___       ___                ___  __             ___       ___  __  
                                                     |__   /\  |__) |__  |  | |__  |    |          |  |__)  /\  \  / |__  |    |__  |__) 
                                                     |    /~~\ |  \ |___ |/\| |___ |___ |___ ,     |  |  \ /~~\  \/  |___ |___ |___ |  \                                                              
''')
    h.pressEnter()
    h.clearScreen()

def displaySystemCrash():
    print('''
    CRITICAL SYSTEM ERROR: FATAL KERNEL PANIC

    SYSTEM FAILURE CODE: 0xDEADDEAD
''')
    t.sleep(1.2)
    print('''
    PROCESSOR FAULT at 0x0000:0xFFFF INTERRUPT FAILURE

    *** KERNEL_MODULE_LOAD_ERROR: COULD NOT INITIALIZE SYSTEM CORE ***

    MEMORY DUMP COMPLETE: 0x0007FFA60000 to 0x0007FFA6FFFF

    ERROR: UNRECOVERABLE BOOT SECTOR CORRUPTION DETECTED
''')
    t.sleep(1.8)
    print('''
    AUTO-TERMINATING SYSTEM!

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
''')
    t.sleep(1)
    h.clearScreen()
    print('''
    AUTO-TERMINATING SYSTEM IN 10...

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
''')
    t.sleep(1)
    h.clearScreen()
    print('''
    AUTO-TERMINATING SYSTEM IN 10...9...

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    WARNING SYSTEM COMPROMISED!
''')
    t.sleep(1)
    h.clearScreen()
    print('''
    AUTO-TERMINATING SYSTEM IN 10...9...8...

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    WARNING SYSTEM COMPROMISED!
''')
    t.sleep(.9)
    h.clearScreen()
    print('''
    AUTO-TERMINATING SYSTEM IN 10...9...8...7...

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    WARNING SYSTEM COMPROMISED!
    WARNING FAILURE IMMINENT!
''')  
    t.sleep(.9)
    h.clearScreen()
    print('''
    AUTO-TERMINATING SYSTEM IN 10...9...8...7...6...

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    WARNING SYSTEM COMPROMISED!
    WARNING FAILURE IMMINENT!
''')  
    t.sleep(.9)
    h.clearScreen()
    print('''
    AUTO-TERMINATING SYSTEM IN 10...9...8...7...6...5...

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    WARNING SYSTEM COMPROMISED!
    WARNING FAILURE IMMINENT!
          
    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
''')  
    t.sleep(.8)
    h.clearScreen()
    print('''
    AUTO-TERMINATING SYSTEM IN 10...9...8...7...6...5...4...

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    WARNING SYSTEM COMPROMISED!
    WARNING FAILURE IMMINENT!
          
    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    
''')
    t.sleep(.8)
    h.clearScreen()
    print('''
    AUTO-TERMINATING SYSTEM IN 10...9...8...7...6...5..4...3...

    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    WARNING SYSTEM COMPROMISED!
    WARNING FAILURE IMMINENT!
          
    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
    PLEASE CONTACT SYSTEM ADMINISTRATOR IMMEDIATELY!
''')  
    print('''

''')


#  BUSY BIZ
## ========================================================================

# cool way to machine-gun method calls a'la Al Swiegert (The Big Book of Small Python Projects)
def displayBusyBiz(duration=0.1, repeat=10):
    ASCII_FRAMES = [asciiNE, asciiNW, asciiSW, asciiSE]

    h.clearScreen()

    for _ in range(repeat):

        for frame in ASCII_FRAMES:

            h.clearScreen()
            frame()
            t.sleep(duration)

    t.sleep(3)
    h.clearScreen()
    exit()


def asciiNE():
    print('''
             /$$$$$$$  /$$$$$$ /$$$$$$$$
            | $$__  $$|_  $$_/|_____ $$
            | $$  \ $$  | $$       /$$/
            | $$$$$$$   | $$      /$$/
            | $$__  $$  | $$     /$$/
            | $$  \ $$  | $$    /$$/
            | $$$$$$$/ /$$$$$$ /$$$$$$$$
            |_______/ |______/|________/
 
 

        /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$ 
       /$$__  $$ /$$__  $$| $$  | $$ /$$__  $$| $$__  $$
      | $$  \__/| $$  \ $$| $$  | $$| $$  \ $$| $$  \ $$
      |  $$$$$$ | $$  | $$| $$  | $$| $$$$$$$$| $$  | $$
       \____  $$| $$  | $$| $$  | $$| $$__  $$| $$  | $$
       /$$  \ $$| $$/$$ $$| $$  | $$| $$  | $$| $$  | $$
      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$| $$$$$$$/
       \______/  \____ $$$ \______/ |__/  |__/|_______/ 
                      \__/  
                                      
''')
    
def asciiNW():
    print('''
            $$$$$$$\  $$$$$$\ $$$$$$$$\                 
            $$  __$$\ \_$$  _|\____$$  |                
            $$ |  $$ |  $$ |      $$  /                 
            $$$$$$$\ |  $$ |     $$  /                  
            $$  __$$\   $$ |    $$  /                   
            $$ |  $$ |  $$ |   $$  /                    
            $$$$$$$  |$$$$$$\ $$$$$$$$\                 
            \_______/ \______|\________|                
                                                        
                                                        
                                                        
       $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\  
      $$  __$$\ $$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\ 
      $$ /  \__|$$ /  $$ |$$ |  $$ |$$ /  $$ |$$ |  $$ |
      \$$$$$$\  $$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |
       \____$$\ $$ |  $$ |$$ |  $$ |$$  __$$ |$$ |  $$ |
      $$\   $$ |$$ $$\$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
      \$$$$$$  |\$$$$$$ / \$$$$$$  |$$ |  $$ |$$$$$$$  |
       \______/  \___$$$\  \______/ \__|  \__|\_______/ 
                     \___|  
                                      
''')
    
def asciiSW():
    print('''
             _______   ______  ________                 
            /       \ /      |/        |                
            $$$$$$$  |$$$$$$/ $$$$$$$$/                 
            $$ |__$$ |  $$ |      /$$/                  
            $$    $$<   $$ |     /$$/                   
            $$$$$$$  |  $$ |    /$$/                    
            $$ |__$$ | _$$ |_  /$$/____                 
            $$    $$/ / $$   |/$$      |                
            $$$$$$$/  $$$$$$/ $$$$$$$$/                 
                                                        
                                                        
                                                        
        ______    ______   __    __   ______   _______  
       /      \  /      \ /  |  /  | /      \ /       \ 
      /$$$$$$  |/$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$$  |
      $$ \__$$/ $$ |  $$ |$$ |  $$ |$$ |__$$ |$$ |  $$ |
      $$      \ $$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$ |
       $$$$$$  |$$ |_ $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |
      /  \__$$ |$$ / \$$ |$$ \__$$ |$$ |  $$ |$$ |__$$ |
      $$    $$/ $$ $$ $$< $$    $$/ $$ |  $$ |$$    $$/ 
       $$$$$$/   $$$$$$  | $$$$$$/  $$/   $$/ $$$$$$$/  
                     $$$/                               
          
''')
    
def asciiSE():
    print('''

             _______   ______  ________                 
            |       \ |      \|        \                
            | $$$$$$$\ \$$$$$$ \$$$$$$$$                
            | $$__/ $$  | $$      /  $$                 
            | $$    $$  | $$     /  $$                  
            | $$$$$$$\  | $$    /  $$                   
            | $$__/ $$ _| $$_  /  $$___                 
            | $$    $$|   $$ \|  $$    \                
             \$$$$$$$  \$$$$$$ \$$$$$$$$                
                                                        
                                                        
                                                        
        ______    ______   __    __   ______   _______  
       /      \  /      \ |  \  |  \ /      \ |       \ 
      |  $$$$$$\|  $$$$$$\| $$  | $$|  $$$$$$\| $$$$$$$|
      | $$___\$$| $$  | $$| $$  | $$| $$__| $$| $$  | $$
       \$$    \ | $$  | $$| $$  | $$| $$    $$| $$  | $$
       _\$$$$$$\| $$ _| $$| $$  | $$| $$$$$$$$| $$  | $$
      |  \__| $$| $$/ \ $$| $$__/ $$| $$  | $$| $$__/ $$
       \$$    $$ \$$ $$ $$ \$$    $$| $$  | $$| $$    $$
        \$$$$$$   \$$$$$$\  \$$$$$$  \$$   \$$ \$$$$$$$ 
                      \$$$                              
                          
''')