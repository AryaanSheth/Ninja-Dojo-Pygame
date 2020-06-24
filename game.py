# Aryaan Sheth
# Pygame Summative - Ninja Dojo: Remastered - Fighting Game

try:
    import pygame   # Imports Pygame Library
    import random   # Imports Random Library
    import playsound    # Imports playsound module
    import Tkinter as tk    # imports tkinter
    import tkMessageBox     # impots tkInter message box
    import time             # imports time module

    pygame.init()
    # Initializes Pygame

    try:
        pygame.mixer.init()
    except:
        pass
    # Try except statement for audio so if no audio output is detected an error doesnt occour

    class var:  # User defined object for player values
        def __init__(self, x, isRight):
            self.x = x
            self.y = 300
            self.width = 100
            self.height = 250
            self.speed = 9
            self.right = False
            self.left = False
            self.walkCount = 0
            self.isJump = False
            self.jumpCount = 10
            self.attack_l = False
            self.attack_l_count = 0
            self.attack_h = False
            self.attack_h_count = 0
            self.isLeft = False
            self.isRight = isRight
            self.hp = 100
            self.isAttack = 1
            self.spAttack = 0
            self.spTrue = False
            self.isBlock = False
            self.blockCount = 0
    # Object above holds values such as player x and y as well as movement and attacking, jumping, special attacks and blocking

    end = False
    fps = 24
    running = False
    menu_screen = True
    musicon = True
    isMenu = False
    power_up = False
    menuLoc = 2
    # Defines all variables that don't require a object to function

    # Defines screen size adds caption and sets game to fullscreen
    width, height = 640, 400   # 640 - 400 screen red
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("Ninja Dojo")

    bkg_choose = random.randint(1, 3)
    if bkg_choose == 1:
        bkg = pygame.image.load("bkg.png")
    elif bkg_choose == 2:
        bkg = pygame.image.load("temple.png")
    elif bkg_choose == 3:
        bkg = pygame.image.load("bkg3.jpg")
    # Selects a random number which correlates to a background to display

    walkLeft = [pygame.image.load("1\RUN LEFT\RUN_LEFT 1.png"), pygame.image.load("1\RUN LEFT\RUN_LEFT 2.png"),
                pygame.image.load("1\RUN LEFT\RUN_LEFT 3.png"), pygame.image.load("1\RUN LEFT\RUN_LEFT 1.png"),
                pygame.image.load("1\RUN LEFT\RUN_LEFT 2.png"), pygame.image.load("1\RUN LEFT\RUN_LEFT 3.png"),
                pygame.image.load("1\RUN LEFT\RUN_LEFT 1.png"), pygame.image.load("1\RUN LEFT\RUN_LEFT 2.png"),
                pygame.image.load("1\RUN LEFT\RUN_LEFT 3.png")]  # Player 1 Move left animations
    walkRight = [pygame.image.load("1\RUN RIGHT\RUN_RIGHT 1.png"), pygame.image.load("1\RUN RIGHT\RUN_RIGHT 2.png"),
                 pygame.image.load("1\RUN RIGHT\RUN_RIGHT 3.png"), pygame.image.load("1\RUN RIGHT\RUN_RIGHT 1.png"),
                 pygame.image.load("1\RUN RIGHT\RUN_RIGHT 2.png"), pygame.image.load("1\RUN RIGHT\RUN_RIGHT 3.png"),
                 pygame.image.load("1\RUN RIGHT\RUN_RIGHT 1.png"), pygame.image.load("1\RUN RIGHT\RUN_RIGHT 2.png"),
                 pygame.image.load("1\RUN RIGHT\RUN_RIGHT 3.png")]  # Player 1 Move Right animations
    punch = [pygame.image.load("1\PUNCH\PUNCH 1.png"), pygame.image.load("1\PUNCH\PUNCH 2.png"),
             pygame.image.load("1\PUNCH\PUNCH 3.png"), pygame.image.load("1\PUNCH\PUNCH 4.png"),
             pygame.image.load("1\PUNCH\PUNCH 5.png"), pygame.image.load("1\PUNCH\PUNCH 6.png"),
             pygame.image.load("1\PUNCH\PUNCH 7.png"), pygame.image.load("1\PUNCH\PUNCH 8.png"),
             pygame.image.load("1\PUNCH\PUNCH 1.png")]  # Player 1 Punch Right animations
    punchr = [pygame.image.load("1\PUNCH R\PUNCH 1.png"), pygame.image.load("1\PUNCH R\PUNCH 2.png"),
              pygame.image.load("1\PUNCH R\PUNCH 3.png"), pygame.image.load("1\PUNCH R\PUNCH 4.png"),
              pygame.image.load("1\PUNCH R\PUNCH 5.png"), pygame.image.load("1\PUNCH R\PUNCH 6.png"),
              pygame.image.load("1\PUNCH R\PUNCH 7.png"), pygame.image.load("1\PUNCH R\PUNCH 8.png"),
              pygame.image.load("1\PUNCH R\PUNCH 1.png")]  # Player 1 Punch left animations
    kick = [pygame.image.load("1\LOW STRIKE\LOW_STRIKE 1.png"), pygame.image.load("1\LOW STRIKE\LOW_STRIKE 2.png"),
            pygame.image.load("1\LOW STRIKE\LOW_STRIKE 3.png"), pygame.image.load("1\LOW STRIKE\LOW_STRIKE 4.png"),
            pygame.image.load("1\LOW STRIKE\LOW_STRIKE 5.png"), pygame.image.load("1\LOW STRIKE\LOW_STRIKE 6.png"),
            pygame.image.load("1\LOW STRIKE\LOW_STRIKE 7.png"), pygame.image.load("1\LOW STRIKE\LOW_STRIKE 8.png"),
            pygame.image.load("1\LOW STRIKE\LOW_STRIKE 1.png")]  # Player 1 Kick Right animations
    kickr = [pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 1r.png"),
             pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 2r.png"),
             pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 3r.png"),
             pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 4r.png"),
             pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 5r.png"),
             pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 6r.png"),
             pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 7r.png"),
             pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 8r.png"),
             pygame.image.load("1\LOW STRIKE R\LOW_STRIKE 1r.png")]  # Player 1 Kick left animations
    stillright = pygame.image.load("1\RUN RIGHT\RUN_RIGHT 1.png")  # Player 1 Still Right animations
    stillleft = pygame.image.load("1\RUN LEFT\RUN_LEFT 1.png")  # Player 1 Still left animations

    walkLeft2 = [pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 1.png"), pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 2.png"),
                 pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 1.png"), pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 2.png"),
                 pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 1.png"), pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 2.png"),
                 pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 1.png"), pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 2.png"),
                 pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 1.png")]  # Player 2 Move left animations
    walkRight2 = [pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 1.png"),
                  pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 2.png"),
                  pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 1.png"),
                  pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 2.png"),
                  pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 1.png"),
                  pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 2.png"),
                  pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 1.png"),
                  pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 2.png"),
                  pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 1.png")]  # Player 2 Move Right animations
    punch2 = [pygame.image.load("2/PUSH/PUSH 1.png"), pygame.image.load("2/PUSH/PUSH 2.png"),
              pygame.image.load("2/PUSH/PUSH 3.png"),
              pygame.image.load("2/PUSH/PUSH 4.png"), ]  # Player 2 Punch Right animations
    punch2r = [pygame.image.load("2/PUSH R/PUSH 1r.png"), pygame.image.load("2/PUSH R/PUSH 2r.png"),
               pygame.image.load("2/PUSH R/PUSH 3r.png"),
               pygame.image.load("2/PUSH R/PUSH 4r.png"), ]  # Player 2 Punch left animations
    kick2 = [pygame.image.load("2/UP_KICK/UP_KICK 1.png"), pygame.image.load("2/UP_KICK/UP_KICK 2.png"),
             pygame.image.load("2/UP_KICK/UP_KICK 3.png"), pygame.image.load("2/UP_KICK/UP_KICK 4.png"),
             pygame.image.load("2/UP_KICK/UP_KICK 5.png"), pygame.image.load("2/UP_KICK/UP_KICK 6.png"),
             pygame.image.load("2/UP_KICK/UP_KICK 7.png"), pygame.image.load("2/UP_KICK/UP_KICK 8.png"),
             pygame.image.load("2/UP_KICK/UP_KICK 9.png")]  # Player 2 Kick Right animations
    kick2r = [pygame.image.load("2/UP_KICK R/UP_KICK 1.png"), pygame.image.load("2/UP_KICK R/UP_KICK 2r.png"),
              pygame.image.load("2/UP_KICK R/UP_KICK 3r.png"), pygame.image.load("2/UP_KICK R/UP_KICK 4r.png"),
              pygame.image.load("2/UP_KICK R/UP_KICK 5r.png"), pygame.image.load("2/UP_KICK R/UP_KICK 6r.png"),
              pygame.image.load("2/UP_KICK R/UP_KICK 7r.png"), pygame.image.load("2/UP_KICK R/UP_KICK 8r.png"),
              pygame.image.load("2/UP_KICK R/UP_KICK 9r.png")]  # Player 2 Kick left animations
    stillleft2 = pygame.image.load("2/MOVE_LEFT/MOVE_LEFT 1.png")  # Player 2 Still left animations
    stillright2 = pygame.image.load("2/MOVE_RIGHT/MOVE_RIGHT 1.png")  # Player 2 Still Right animations

    akko0 = pygame.image.load("akkohp/akko 0.png")
    akko1 = pygame.image.load("akkohp/akko 10.png")
    akko2 = pygame.image.load("akkohp/akko 20.png")
    akko3 = pygame.image.load("akkohp/akko 30.png")
    akko4 = pygame.image.load("akkohp/akko 40.png")
    akko5 = pygame.image.load("akkohp/akko 50.png")
    akko6 = pygame.image.load("akkohp/akko 60.png")
    akko7 = pygame.image.load("akkohp/akko 70.png")
    akko8 = pygame.image.load("akkohp/akko 80.png")
    akko9 = pygame.image.load("akkohp/akko 90.png")
    akko10 = pygame.image.load("akkohp/akko 100.png")
    # Akko/player 2 HP bars

    hiro0 = pygame.image.load("hirohp/hiro 0.png")
    hiro1 = pygame.image.load("hirohp/hiro 10.png")
    hiro2 = pygame.image.load("hirohp/hiro 20.png")
    hiro3 = pygame.image.load("hirohp/hiro 30.png")
    hiro4 = pygame.image.load("hirohp/hiro 40.png")
    hiro5 = pygame.image.load("hirohp/hiro 50.png")
    hiro6 = pygame.image.load("hirohp/hiro 60.png")
    hiro7 = pygame.image.load("hirohp/hiro 70.png")
    hiro8 = pygame.image.load("hirohp/hiro 80.png")
    hiro9 = pygame.image.load("hirohp/hiro 90.png")
    hiro10 = pygame.image.load("hirohp/hiro 100.png")
    # Akhiro/hiro/player 1 hp bars

    leftBlockHiro = [pygame.image.load("1/BLOCK/LEFT_BLOCK.png"),pygame.image.load("1/BLOCK/LEFT_BLOCK.png"), pygame.image.load("1/BLOCK/LEFT_BLOCK.png"),
                     pygame.image.load("1/BLOCK/LEFT_BLOCK.png"), pygame.image.load("1/BLOCK/LEFT_BLOCK.png"), pygame.image.load("1/BLOCK/LEFT_BLOCK.png"),
                     pygame.image.load("1/BLOCK/LEFT_BLOCK.png"), pygame.image.load("1/BLOCK/LEFT_BLOCK.png"), pygame.image.load("1/BLOCK/LEFT_BLOCK.png")]
# player 1/Hiro left block
    rightBlockHiro = [pygame.image.load("1/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("1/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("1/BLOCK/RIGHT_BLOCK.png"),
                      pygame.image.load("1/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("1/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("1/BLOCK/RIGHT_BLOCK.png"),
                      pygame.image.load("1/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("1/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("1/BLOCK/RIGHT_BLOCK.png")]
    # player 1/Hiro Right block
    leftBlockAkko = [pygame.image.load("2/BLOCK/LEFT_BLOCK.png"),pygame.image.load("2/BLOCK/LEFT_BLOCK.png"),pygame.image.load("2/BLOCK/LEFT_BLOCK.png"),
                     pygame.image.load("2/BLOCK/LEFT_BLOCK.png"),pygame.image.load("2/BLOCK/LEFT_BLOCK.png"),pygame.image.load("2/BLOCK/LEFT_BLOCK.png"),
                     pygame.image.load("2/BLOCK/LEFT_BLOCK.png"),pygame.image.load("2/BLOCK/LEFT_BLOCK.png"),pygame.image.load("2/BLOCK/LEFT_BLOCK.png")]
    # player 2/Akko left block
    rightBlockAkko = [pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),
                      pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),
                      pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),pygame.image.load("2/BLOCK/RIGHT_BLOCK.png"),]
    # player 2/Akko left block

    menu = pygame.image.load("titlepage.png")
    # Title screens for game

    ctrls = pygame.image.load("controls.jpg")   # Control screen image

    treeL = pygame.image.load("left side tree.png")
    treeR = pygame.image.load("right side tree.png")
    # Trees on both side of the game

    L_spBar = pygame.image.load("sp bar left.png")
    R_spBar = pygame.image.load("sp bar right.png")
    # bpecial power bars

    hpUp = pygame.image.load("hpUp.png")
    spUp = pygame.image.load("spUp.png")
    # power up sprites

    clock = pygame.time.Clock()  # Define clock var

    player1 = var(100, True)
    player2 = var(500, True)
    # Calls objects with parameters filled in for bot players
    try:
        def main_audio():
            playsound.playsound("music2.mp3", block=False)

        main_audio()
    except playsound.PlaysoundException:
        pass
    # Loads the music and threads it so other music an play simultaneously.

    powerup_hitbox2 = pygame.sprite.Sprite()
    powerup_hitbox2.image = pygame.image.load("spUp.png")
    powerup_hitbox2.rect = powerup_hitbox2.image.get_rect()
# special power up powerup sprite pre info

    powerup_hitbox = pygame.sprite.Sprite()
    powerup_hitbox.image = pygame.image.load("hpUp.png")
    powerup_hitbox.rect = powerup_hitbox.image.get_rect()
# hp powerup sprite pre info

    puX = random.randint(70, 580)
    puY = random.randint(150, 300)
    spOrHp = random.randint(1, 2)
# powerup span areas and deciders for what powerup

    def powerup():
        global power_up, powerup_hitbox, puX, puY, spOrHp   # globals

        if power_up == False:
            puspawn = random.randint(0, 100)
            puX = random.randint(70, 580)
            puY = random.randint(150, 300)
            spOrHp = random.randint(1, 2)
# rolls chords until 10 is accquired for powerup to spawn
            if puspawn == 10:
                power_up = True
            # makes power up true so powerups can spawn

        if power_up == True and spOrHp == 1:
            powerup_hitbox.rect.topleft = (puX, puY)
            screen.blit(powerup_hitbox.image, powerup_hitbox.rect)
        # spawns hp powerup

        if pygame.sprite.collide_rect(powerup_hitbox, p2_hitbox):
            player2.hp += 5
            if player2.hp > 100:
                player2.hp = 100
            power_up = False
            spOrHp = 0
            try:
                pygame.mixer_music.load("powerup_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass

        elif pygame.sprite.collide_rect(powerup_hitbox, p1_hitbox):
            player1.hp += 5
            if player1.hp > 100:
                player1.hp = 100
            power_up = False
            spOrHp = 0
            try:
                pygame.mixer_music.load("powerup_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
        # player hitpox collisions with powerup and sfx for power up


        if power_up == True and spOrHp == 2:
            powerup_hitbox2.rect.topleft = (puX, puY)
            screen.blit(powerup_hitbox2.image, powerup_hitbox2.rect)
        # special power power up adder

        if pygame.sprite.collide_rect(powerup_hitbox2, p2_hitbox):
            player2.spAttack += 15
            if player2.spAttack > 100:
                player2.spAttack = 100
            power_up = False
            spOrHp = 0
            pygame.mixer_music.load("powerup_sfx.wav")
            pygame.mixer_music.play()

        elif pygame.sprite.collide_rect(powerup_hitbox2, p1_hitbox):
            player1.spAttack += 15
            if player1.spAttack > 100:
                player1.spAttack = 100
            power_up = False
            spOrHp = 0
            pygame.mixer_music.load("powerup_sfx.wav")
            pygame.mixer_music.play()
        # player and special power power up collisions

    def special_attack():
        if player1.spAttack >= 135:
            player1.spAttack = 135
            player1.spTrue = True
        if player2.spAttack >= 135:
            player2.spAttack = 135
            player2.spTrue = True
        #   player special attack bar restrains so bar doen't leave image frame.

        pygame.draw.rect(screen, (72,209,204), (78, 89, player1.spAttack, 12))
        pygame.draw.rect(screen, (72,209,204), (433, 89, player2.spAttack, 12))
        # blits empty bars below each playes sp bar

        tester = pygame.transform.scale(L_spBar, (150, 15))
        screen.blit(tester, (70, 88))
        tester = pygame.transform.scale(R_spBar, (150, 15))
        screen.blit(tester, (425, 87))
        # scales the sp bar image to fit the area

    def hp_bars():  # Logic behind hp bars.
        if player2.hp >= 100 and player2.hp >90:
            tester = pygame.transform.scale(akko10, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 90 and player2.hp >80:
            tester = pygame.transform.scale(akko9, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 80 and player2.hp > 70:
            tester = pygame.transform.scale(akko8, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 70 and player2.hp > 60:
            tester = pygame.transform.scale(akko7, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 60 and player2.hp > 50:
            tester = pygame.transform.scale(akko6, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 50 and player2.hp > 40:
            tester = pygame.transform.scale(akko5, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 40 and player2.hp > 30:
            tester = pygame.transform.scale(akko4, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 30 and player2.hp > 20:
            tester = pygame.transform.scale(akko3, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 20 and player2.hp > 10:
            tester = pygame.transform.scale(akko2, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 10 and player2.hp > 0:
            tester = pygame.transform.scale(akko1, (520, 300))
            screen.blit(tester, (100, -50))
            pygame.display.update()
        elif player2.hp <= 0:
            tester = pygame.transform.scale(akko0, (520, 300))
            screen.blit(tester, (100, -50))
    # Player2/Akko hp bars. They change every 10 hp points lost by the player

        if player1.hp >= 100 and player1.hp > 90:
            tester = pygame.transform.scale(hiro10, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 90 and player1.hp > 80:
            tester = pygame.transform.scale(hiro9, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 80 and player1.hp > 70:
            tester = pygame.transform.scale(hiro8, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 70 and player1.hp > 60:
            tester = pygame.transform.scale(hiro7, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 60 and player1.hp > 50:
            tester = pygame.transform.scale(hiro6, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 50 and player1.hp > 40:
            tester = pygame.transform.scale(hiro5, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 40 and player1.hp > 30:
            tester = pygame.transform.scale(hiro4, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 30 and player1.hp > 20:
            tester = pygame.transform.scale(hiro3, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 20 and player1.hp > 10:
            tester = pygame.transform.scale(hiro2, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 10 and player1.hp > 0:
            tester = pygame.transform.scale(hiro1, (520, 300))
            screen.blit(tester, (20, -50))
            pygame.display.update()
        elif player1.hp <= 0:
            tester = pygame.transform.scale(hiro0, (520, 300))
            screen.blit(tester, (20, -50))
    # Akhiro/Hiro/Player 1 hp bar logic. Goes down every time player loses 10 hp

    p1_hitbox = pygame.sprite.Sprite()
    p1_hitbox.image = pygame.image.load("p1 hitbox.png")
    p1_hitbox.rect = p1_hitbox.image.get_rect()
    # player 1 hitbox pre work

    p2_hitbox = pygame.sprite.Sprite()
    p2_hitbox.image = pygame.image.load("p2 hitbox.png")
    p2_hitbox.rect = p2_hitbox.image.get_rect()
    #player 2 hitbox pre work

    def hitboxes():
        global end, running, menu_screen, p1_hitbox, p2_hitbox

        p1_hitbox.rect.topleft = (player1.x, player1.y)
        screen.blit(p1_hitbox.image, p1_hitbox.rect)
        # Player 1 Hitbox

        p2_hitbox.rect.topleft = (player2.x, player2.y)
        screen.blit(p2_hitbox.image, p2_hitbox.rect)
        # Player 2 Hitbox


        if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player1.attack_l == True and player1.isAttack == 1 and end == False and player2.isBlock == False):
            player2.hp -= 2
            if player1.isRight:
                player2.x += 90
            elif player1.isLeft:
                player2.x -= 90
            print(player2.hp)
            player1.spAttack += 5
            try:
                pygame.mixer_music.load("hit_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
        if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player1.attack_h == True and player1.isAttack == 1 and end == False and player2.isBlock == False):
            player2.hp -= 3
            if player1.isRight:
                player2.x += 30
            elif player1.isLeft:
                player2.x -= 30
            print(player2.hp)
            player1.spAttack += 7
            try:
                pygame.mixer_music.load("hit_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
        if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player2.attack_l == True and player2.isAttack == 1 and end == False and player1.isBlock == False):
            player1.hp -= 2
            if player2.isRight:
                player1.x += 30
            elif player2.isLeft:
                player1.x -= 30
            print(player1.hp)
            player2.spAttack += 5
            try:
                pygame.mixer_music.load("hit_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
        if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player2.attack_h == True and player2.isAttack == 1 and end == False and player1.isBlock == False):
            player1.hp -= 3
            if player2.isRight:
                player1.x += 60
            elif player2.isLeft:
                player2.x -= 60
            print(player1.hp)
            player2.spAttack += 7
            try:
                pygame.mixer_music.load("hit_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
    # hitboxes for normal attacks that plays sound each hit

            if (pygame.sprite.collide_rect(p1_hitbox,p2_hitbox) and player1.attack_l == True and player1.isAttack == 1 and end == False and player1.spTrue == True and player2.isBlock == False):
                player2.hp -= 50-(player1.hp/2)
                if player1.isRight:
                    player2.x += 180
                elif player1.isLeft:
                    player2.x -= 180
                print(player2.hp)
                player1.spTrue = False
                player1.spAttack = 0
                try:
                    pygame.mixer_music.load("hit_sfx.wav")
                    pygame.mixer_music.play()
                except:
                    pass
            if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player1.attack_h == True and player1.isAttack == 1 and end == False and player1.spTrue == True and player2.isBlock == False):
                player2.hp -= 50-(player1.hp/2)
                if player1.isRight:
                    player2.x += 30
                elif player1.isLeft:
                    player2.x -= 30
                print(player2.hp)
                player1.spTrue = False
                player1.spAttack = 0
                try:
                    pygame.mixer_music.load("hit_sfx.wav")
                    pygame.mixer_music.play()
                except:
                    pass
            if (pygame.sprite.collide_rect(p1_hitbox,p2_hitbox) and player2.attack_l == True and player2.isAttack == 1 and end == False and player2.spTrue == True and player1.isBlock == False):
                player1.hp -= 50-(player2.hp/2)
                if player2.isRight:
                    player1.x += 180
                elif player2.isLeft:
                    player1.x -= 180
                print(player1.hp)
                player2.spTrue = False
                player2.spAttack = 0
                try:
                    pygame.mixer_music.load("hit_sfx.wav")
                    pygame.mixer_music.play()
                except:
                    pass
            if (pygame.sprite.collide_rect(p1_hitbox,p2_hitbox) and player2.attack_h == True and player2.isAttack == 1 and end == False and player2.spTrue == True and player1.isBlock == False):
                player1.hp -= 50-(player2.hp/2)
                if player2.isRight:
                    player1.x += 30
                elif player2.isLeft:
                    player2.x -= 30
                print(player1.hp)
                player2.spTrue = False
                player2.spAttack = 0
                try:
                    pygame.mixer_music.load("hit_sfx.wav")
                    pygame.mixer_music.play()
                except:
                    pass
        # Attack collisions between the players and damage values and knock-back for SP-Attacks


        if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player1.attack_l == True and player1.isAttack == 1 and end == False and player2.isBlock == True):
            player2.hp -= 0
            if player1.isRight:
                player2.x += 15
            elif player1.isLeft:
                player2.x -= 15
            print(player2.hp)
            player1.spAttack += 0
            try:
                pygame.mixer_music.load("hit_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
        if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player1.attack_h == True and player1.isAttack == 1 and end == False and player2.isBlock == True):
            player2.hp -= 1.5
            if player1.isRight:
                player2.x += 30
            elif player1.isLeft:
                player2.x -= 30
            print(player2.hp)
            player1.spAttack += 0
            try:
                pygame.mixer_music.load("hit_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
        if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player2.attack_l == True and player2.isAttack == 1 and end == False and player1.isBlock == True):
            player1.hp -= 0
            if player2.isRight:
                player1.x += 15
            elif player2.isLeft:
                player1.x -= 15
            print(player1.hp)
            player2.spAttack += 0
            try:
                pygame.mixer_music.load("hit_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
        if (pygame.sprite.collide_rect(p1_hitbox, p2_hitbox) and player2.attack_h == True and player2.isAttack == 1 and end == False and player1.isBlock == True):
            player1.hp -= 1.5
            if player2.isRight:
                player1.x += 30
            elif player2.isLeft:
                player2.x -= 30
            print(player1.hp)
            player2.spAttack += 0
            try:
                pygame.mixer_music.load("hit_sfx.wav")
                pygame.mixer_music.play()
            except:
                pass
        # hitboxes for blocked attacks that plays sound each hit

        if player1.x <= 0:
            player1.x = 0
        elif player2.x <= 0:
            player2.x = 0
        if player1.x >= 570:
            player1.x = 570
        elif player2.x >= 570:
            player2.x = 570
        # player chord restrictions so knock back cant make player fall off screen

        if player1.hp <= 0:
            font1 = pygame.font.Font("LemonMilkbold.otf", 75)
            text = font1.render('AKKO WINS', True, (0, 0, 0), (255, 255, 255))
            screen.blit(text, (100, 150))
            player1.speed = 0
            player2.speed = 0
            end = True
            pygame.display.update()
    # player 2 winning display screen if player 1 hp is 0

        elif player2.hp <= 0:
            font2 = pygame.font.Font("LemonMilkbold.otf", 75)
            text1 = font2.render('AKIHIRO WIN', True,  (0, 0, 0), (255, 255, 255))
            screen.blit(text1, (60, 150))
            player1.speed = 0
            player2.speed = 0
            end = True
            pygame.display.update()
    # player 1 winning display screen if player 2 hp is 0

    def player1_animations():
        if (player1.walkCount + 1) >= fps:
            player1.walkCount = 0

        if (player1.attack_l_count + 1) >= fps:
            player1.attack_l_count = 0

        if (player1.attack_h_count + 1) >= fps:
            player1.attack_h_count = 0

        if (player1.blockCount + 1) >= fps:
            player1.blockCount = 0
            # frame counters for both attack and movement and blocking

        if player1.left and player1.isBlock == False:    # player left animations
            screen.blit(walkLeft[player1.walkCount // 3], (player1.x, player1.y))
            player1.walkCount = player1.walkCount + 1
            player1.isBlock = False

        elif player1.right and player1.isBlock == False: # player right animations
            screen.blit(walkRight[player1.walkCount // 3], (player1.x, player1.y))
            player1.walkCount = player1.walkCount + 1
            player1.isBlock = False

        elif player1.right == False and player1.left == False and player1.attack_l == False and player1.attack_h == False and player1.isLeft == False and player1.isRight == True and player1.isBlock == False:
            screen.blit(stillright, (player1.x, player1.y))

        elif player1.right == False and player1.left == False and player1.attack_l == False and player1.attack_h == False and player1.isLeft == True and player1.isRight == False and player1.isBlock == False:
            screen.blit(stillleft, (player1.x, player1.y))

        elif player1.right == False and player1.left == False and player1.attack_l == False and player1.attack_h == False and player1.isLeft == False and player1.isRight == False and player1.isBlock == False:
            screen.blit(stillright, (player1.x, player1.y))
        # Standing still direction saveing



        if player1.attack_l == False and player1.attack_h == False and player1.isLeft == False and player1.isRight == True and player1.isBlock == True:
            screen.blit(rightBlockHiro[player1.blockCount // 3], (player1.x, player1.y - 25))
            player1.blockCount = player1.blockCount + 1
            player1.left = False
            player1.right = False

            if player1.blockCount >= fps - 1:
                player1.isBlock = False

        if player1.attack_l == False and player1.attack_h == False and player1.isLeft == True and player1.isRight == False and player1.isBlock == True:
            screen.blit(leftBlockHiro[player1.blockCount // 3], (player1.x, player1.y - 25))
            player1.blockCount = player1.blockCount + 1
            player1.left = False
            player1.right = False

            if player1.blockCount >= fps - 1:
                player1.isBlock = False
        #blocking for both directions


        if player1.attack_l == True and player1.isLeft == False and player1.isRight == True:
            screen.blit(punchr[player1.attack_l_count // 3], (player1.x, player1.y - 25))
            player1.attack_l_count = player1.attack_l_count + 1
            player1.left = False
            player1.right = False

            if player1.attack_l_count >= fps - 1:
                player1.attack_l = False

        if player1.attack_l == True and player1.isLeft == True and player1.isRight == False:
            screen.blit(punch[player1.attack_l_count // 3], (player1.x, player1.y - 25))
            player1.attack_l_count = player1.attack_l_count + 1
            player1.left = False
            player1.right = False

            if player1.attack_l_count >= fps - 1:
                player1.attack_l = False
    # light attacks for both directions

        if player1.attack_h and player1.isLeft == True and player1.isRight == False:
            screen.blit(kick[player1.attack_h_count // 3], (player1.x, player1.y + 10))
            player1.attack_h_count = player1.attack_h_count + 1
            player1.left = False
            player1.right = False

            if player1.attack_h_count >= fps - 1:
                player1.attack_h = False

        if player1.attack_h and player1.isLeft == False and player1.isRight == True:
            screen.blit(kickr[player1.attack_h_count // 3], (player1.x, player1.y + 10))
            player1.attack_h_count = player1.attack_h_count + 1

            if player1.attack_h_count >= fps - 1:
                player1.attack_h = False
    # heavy attacks for both directions

    def player2_animations():
        if (player2.walkCount + 1) >= fps:
            player2.walkCount = 0

        if (player2.attack_l_count + 1) >= fps:
            player2.attack_l_count = 0

        if (player2.attack_h_count + 1) >= fps:
            player2.attack_h_count = 0

        if (player2.blockCount + 1) >= fps:
            player2.blockCount = 0
        # animation counters for movement and both attacks and blocking

        if player2.left and player2.isBlock == False:    # Player left animations
            screen.blit(walkLeft2[player2.walkCount // 3], (player2.x, player2.y - 25))
            player2.walkCount = player2.walkCount + 1

        elif player2.right and player2.isBlock == False: # Player right animations
            screen.blit(walkRight2[player2.walkCount // 3], (player2.x, player2.y - 25))
            player2.walkCount = player2.walkCount + 1

        elif player2.right == False and player2.left == False and player2.attack_l == False and player2.attack_h == False and player2.isLeft == False and player2.isRight == True and player2.isBlock == False:
            screen.blit(stillright2, (player2.x, player2.y - 25))

        elif player2.right == False and player2.left == False and player2.attack_l == False and player2.attack_h == False and player2.isLeft == True and player2.isRight == False and player2.isBlock == False:
            screen.blit(stillleft2, (player2.x, player2.y - 25))

        elif player2.right == False and player2.left == False and player2.attack_l == False and player2.attack_h == False and player2.isLeft == False and player2.isRight == False and player2.isBlock == False:
            screen.blit(stillleft2, (player2.x, player2.y - 25))
        # directional standingd


        if player2.attack_l == False and player2.attack_h == False and player2.isLeft == False and player2.isRight == True and player2.isBlock == True:
            screen.blit(rightBlockAkko[player2.blockCount // 3], (player2.x, player2.y-35))
            player2.blockCount = player2.blockCount + 1
            player2.left = False
            player2.right = False

            if player2.blockCount >= fps - 1:
                player2.isBlock = False

        if player2.attack_l == False and player2.attack_h == False and player2.isLeft == True and player2.isRight == False and player2.isBlock == True:
            screen.blit(leftBlockAkko[player2.blockCount // 3], (player2.x, player2.y-35))
            player2.blockCount = player2.blockCount + 1
            player2.left = False
            player2.right = False

            if player2.blockCount >= fps - 1:
                player2.isBlock = False
# player 2 blocking for both directions

        if player2.attack_l == True and player2.isLeft == True and player2.isRight == False:
            screen.blit(punch2[player2.attack_l_count // 6], (player2.x, player2.y - 25))
            player2.attack_l_count = player2.attack_l_count + 1

            if player2.attack_l_count >= fps - 1:
                player2.attack_l = False

        elif player2.attack_l == True and player2.isRight == True and player2.isLeft == False:
            screen.blit(punch2r[player2.attack_l_count // 6], (player2.x, player2.y - 25))
            player2.attack_l_count = player2.attack_l_count + 1


            if player2.attack_l_count >= fps - 1:
                player2.attack_l = False
    # light attacks in both directions

        if player2.attack_h == True and player2.isLeft == True and player2.isRight == False:
            screen.blit(kick2[player2.attack_h_count // 3], (player2.x, player2.y - 35))
            player2.attack_h_count = player2.attack_h_count + 1


            if player2.attack_h_count >= fps - 1:
                player2.attack_h = False

        elif player2.attack_h == True and player2.isLeft == False and player2.isRight == True:
            screen.blit(kick2r[player2.attack_h_count // 3], (player2.x, player2.y - 35))
            player2.attack_h_count = player2.attack_h_count + 1


            if player2.attack_h_count >= fps - 1:
                player2.attack_h = False
    # heavy attacks in both directions

    def player1_movement():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player1.x > player1.speed and end == False:  # player move left
            player1.x -= player1.speed
            player1.left = True
            player1.right = False
            player1.isLeft = True
            player1.isRight = False
            player1.isBlock = False

        elif keys[pygame.K_d] and player1.x < 540 - player1.speed and end == False:  # Player move right
            player1.x += player1.speed
            player1.left = False
            player1.right = True
            player1.isLeft = False
            player1.isRight = True
            player1.isBlock = False
        else:   # If player doest move
            player1.left = False
            player1.right = False

        if not player1.isJump:
            if keys[pygame.K_w] and end == False:   # Player Jumping
                player1.isJump = True
                player1.right = False
                player1.left = False
                player1.isBlock = False
                player1.walkCount = 0
                try:
                    pygame.mixer_music.load("jump_sfx.wav")
                    pygame.mixer_music.play()
                except:
                    pass
# player 1 jumping
        else:
            if player1.jumpCount >= -10 and end == False:
                player1.y -= (player1.jumpCount * abs(player1.jumpCount)) * .5
                player1.jumpCount -= 1
            else:
                player1.jumpCount = 10
                player1.isJump = False

        if keys[pygame.K_c] and end == False:   # player light attack/punch
            player1.attack_l = True
            player1.attack_h = False
            player1.right = False
            player1.left = False
            player1.isBlock = False

        elif keys[pygame.K_s] and end == False: # player heavy attack/kick
            player1.attack_h = True
            player1.attack_l = False
            player1.right = False
            player1.left = False
            player1.isBlock = False

        elif keys[pygame.K_v] and end == False: # player blocks
            player1.attack_l = False
            player1.right = False
            player1.left = False
            player1.isBlock = True

    def player2_movement():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player2.x > player2.speed and end == False:  # left movement
            player2.x -= player2.speed
            player2.left = True
            player2.right = False
            player2.isLeft = True
            player2.isRight = False

        elif keys[pygame.K_RIGHT] and player2.x < 580 - player2.speed and end == False: # Right movement
            player2.x += player2.speed
            player2.right = True
            player2.left = False
            player2.isLeft = False
            player2.isRight = True

        else:   # standing still
            player2.left = False
            player2.right = False

        if not player2.isJump:
            if keys[pygame.K_UP] and end == False:  # jumping
                player2.isJump = True
                player2.right = False
                player2.left = False
                player2.walkCount = 0
                try:
                    pygame.mixer_music.load("jump_sfx.wav") # jump sfx
                    pygame.mixer_music.play()
                except:
                    pass

        else:
            if player2.jumpCount >= -10:
                player2.y -= (player2.jumpCount * abs(player2.jumpCount)) * .5
                player2.jumpCount -= 1
            else:
                player2.jumpCount = 10
                player2.isJump = False

        if keys[pygame.K_k] and end == False:   # light attack/punch
            player2.attack_l = True
            player2.right = False
            player2.left = False
            player2.attack_h = False

        if keys[pygame.K_DOWN] and end == False:    # heavy attack/kick
            player2.attack_l = False
            player2.attack_h = True
            player2.right = False
            player2.left = False

        elif keys[pygame.K_l] and end == False: # player block
            player2.attack_h = False
            player2.attack_l = False
            player2.right = False
            player2.left = False
            player2.isBlock = True

    def screen_scale():
        global screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:   # minimizes screen
            screen = pygame.display.set_mode((width, height))

        elif keys[pygame.K_TAB]:    # makes game full screen
            screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

    def redrawGameWindow():
        screen.blit(bkg, (0, 0))
        screen.blit(treeL, (-20, -240))
        screen.blit(treeR, (480, -240))

        player1_animations()
        player2_animations()
        powerup()
        hp_bars()
        special_attack()
        hitboxes()


        pygame.display.update()
    # contains major parts and combines them in a function to achieve a cleaner main loop

    def menu_screen_controls():
        global menu_screen, running, isMenu
        keys = pygame.key.get_pressed()
        screen.blit(menu, (0, 0))

        if keys[pygame.K_m]:    # music mute
            pygame.mixer_music.load("music2.mp3")
            pygame.mixer_music.stop()

        elif keys[pygame.K_SPACE]:  # game start
            menu_screen = False
            running = True

        if keys[pygame.K_h] and isMenu == False:  # if held shows game controls
            isMenu = True

        elif keys[pygame.K_h] and isMenu == True:  # if held shows game controls
            isMenu = False

        if isMenu == True:
            screen.blit(ctrls, (0, 0))
        elif isMenu == False:
            screen.blit(menu, (0, 0))

    while menu_screen:
        clock.tick(fps)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_screen = False
        screen_scale()
        menu_screen_controls()

        pygame.display.update()
    # Title screen loop that runs till SPACE is pressed

    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.mouse.set_visible(False)
        player1_movement()
        player2_movement()
        screen_scale()
        redrawGameWindow()
        pygame.display.update()
    # Main game loop where the magic happens

except:
    root = tk.Tk()
    root.withdraw()
    tkMessageBox.showerror('ERROR', 'A problem occurred trying to boot Ninja Dojo: Remastered')
