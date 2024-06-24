from time import sleep
import pygame
import pygame_menu
from pygame_menu import Theme
import pygame_menu.locals
import os

# custom theme
myTheme = Theme(
    background_color=(60, 60, 60),
    title_background_color=(225, 225, 225),
    title_font=pygame_menu.font.FONT_MUNRO,
    title_font_color=(225, 225, 225),
    title_offset=(400, 0),
    widget_font=pygame_menu.font.FONT_MUNRO,
    widget_font_color=(200, 200, 200),
    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE
)

# screen size
def getHeight():
    return 600
def getWidth():
    return 1200

width = getWidth()
height = getHeight()

# initialization
pygame.init()
surface = pygame.display.set_mode((width, height))

# functions
 
def startGame():
    print("game started")
    pass

def openSettings():
    print("settings opened")
    mainmenu._open(settings_menu)
    pass

def openCharList():
    print("char list opened")
    mainmenu._open(characterList_menu)
    pass

# character list menu
characterList_menu = pygame_menu.Menu(
    'Playable Characters',
    width,
    height,
    theme=myTheme
) 

# setting menu
settings_menu = pygame_menu.Menu(
    'Settings',
    width,
    height,
    theme=myTheme
)

# main menu
mainmenu = pygame_menu.Menu(
    'Honkai Star Rail fangame',
    width,
    height,
    theme=myTheme
)

info_text = mainmenu.add.label(
    "Original game belongs to Hoyoverse, characters belong to their creators (see Character Info), no profit is being made from this project, coded by Catisioo",
    font_size=17,
    align=pygame_menu.locals.ALIGN_CENTER
)
info_text.set_position(width - info_text.get_width() - 20, 20)

# main menu frame
frame = mainmenu.add.frame_v(width-40, height-80, background_color=(50, 50, 50), padding=0)

## character frame
character_frame = mainmenu.add.frame_h(width-40, 460, padding=0)
frame.pack(character_frame)

# enemy frame
enemy_frame = mainmenu.add.frame_v(387, 460, padding=0)
character_frame.pack(enemy_frame)

# enemy image frame
enemy_image_frame = mainmenu.add.frame_h(387, 440, padding=0)
enemy_frame.pack(enemy_image_frame)

# enemy image
enemy_image_path = os.path.join(os.path.dirname(__file__), 'evilguy.png')
enemy_image_frame.pack(
    mainmenu.add.image(
        enemy_image_path, angle=0, scale=(0.95, 0.95)
    )
)

# char 1 frame
char1_frame = mainmenu.add.frame_v(193, 440, padding=0)
character_frame.pack(char1_frame)

# char 1 image
char1_image_path = os.path.join(os.path.dirname(__file__), 'char1.png')
char1_frame.pack(
    mainmenu.add.image(
        char1_image_path, angle=0, scale=(0.90, 0.90)
    )
)

# char 2 frame
char2_frame = mainmenu.add.frame_v(193, 440, padding=0)
character_frame.pack(char2_frame)

# char 2 image
char2_image_path = os.path.join(os.path.dirname(__file__), 'char1.png')
char2_frame.pack(
    mainmenu.add.image(
        char2_image_path, angle=0, scale=(0.90, 0.90)
    )
)

# char 3 frame
char3_frame = mainmenu.add.frame_v(193, 440, padding=0)
character_frame.pack(char3_frame)

# char 3 image
char3_image_path = os.path.join(os.path.dirname(__file__), 'char1.png')
char3_frame.pack(
    mainmenu.add.image(
        char3_image_path, angle=0, scale=(0.90, 0.90)
    )
)

# char 4 frame
char4_frame = mainmenu.add.frame_v(193, 440, padding=0)
character_frame.pack(char4_frame)

# char 2 image
char4_image_path = os.path.join(os.path.dirname(__file__), 'char1.png')
char4_frame.pack(
    mainmenu.add.image(
        char4_image_path, angle=0, scale=(0.90, 0.90)
    )
)

## bottom frame
buttons_frame = mainmenu.add.frame_h(width-40, 60, padding=0)
frame.pack(buttons_frame)

# defines bottom 4 button frames
settingsBtn_frame = mainmenu.add.frame_h((width-40)/4, 60, padding=0)
playBtn_frame = mainmenu.add.frame_h((width-40)/4, 60, padding=0)
charactersBtn_frame = mainmenu.add.frame_h((width-40)/4, 60, padding=0)
quitBtn_frame = mainmenu.add.frame_h((width-40)/4, 60, padding=0)

# packs bottom 4 button frames into bottom frame
buttons_frame.pack(settingsBtn_frame)
buttons_frame.pack(playBtn_frame)
buttons_frame.pack(charactersBtn_frame)
buttons_frame.pack(quitBtn_frame)

# packs bottom 4 buttons
settingsBtn_frame.pack(
    mainmenu.add.button(
        'Settings',
        openSettings,
        padding=10,
        background_color=(200, 200, 200, 50),
    ),
    align=pygame_menu.locals.ALIGN_LEFT, margin=(10, 0)
)
playBtn_frame.pack(
    mainmenu.add.button(
        'PLAY',
        startGame,
        padding=10,
        background_color=(200, 200, 200, 50),
    ),
    align=pygame_menu.locals.ALIGN_RIGHT, margin=(10, 0)
)
charactersBtn_frame.pack(
    mainmenu.add.button(
        'Character Info',
        openCharList,
        padding=10,
        background_color=(200, 200, 200, 50),
    ),
    align=pygame_menu.locals.ALIGN_LEFT, margin=(10, 0)
)
quitBtn_frame.pack(
    mainmenu.add.button(
        'Quit Game',
        pygame_menu.events.EXIT,
        padding=10,
        background_color=(200, 200, 200, 50)
    ),
    align=pygame_menu.locals.ALIGN_RIGHT, margin=(10, 0)
)

## infinite execution loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
 
    pygame.display.update()