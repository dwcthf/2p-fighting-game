import pygame

class Thanh():
    def __init__(self, x ,y):
        self.flip = False
        self.rect = pygame.Rect((x,y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        self.alive = True
        self.defend = False
        self.attack_rect_x_speed = 20
        self.x0 = 0
        self.shoot = False
        self.cooldown = 6000
        self.last = 0
        self.now = 6000

    def move(seft, screen_width, screen_height, surface, target, round_over):
        Speed = 10
        Gravity = 2
        dx = 0
        dy = 0
        delay = 100000
        #get in4 from keyboard
        key = pygame.key.get_pressed()
        
        #jump
        if key[pygame.K_w] and seft.jump == False and seft.defend == False:
            seft.vel_y = -30
            seft.jump = True
        
        #delay skill 
        if seft.shoot == False:
            seft.now = pygame.time.get_ticks()
        if seft.attacking == False and seft.defend == False:
            #attackkkkk
            if key[pygame.K_t] or key[pygame.K_y]:
                while delay > 1:
                    delay = delay-1
                if delay == 1:  
                    if key[pygame.K_t]:
                        seft.attack_type = 1
                    elif key[pygame.K_y]:
                        seft.attack_type = 2
                    seft.attack(surface, target)
                    delay = 10
            elif key[pygame.K_u]:
                seft.now = pygame.time.get_ticks()
                seft.attack_type = 3
                if seft.now - seft.last >= seft.cooldown:
                    seft.shoot = True
                seft.attack(surface, target)
        #defend
        if key[pygame.K_s]:
            seft.defend = True
            seft.attack(surface, target)
        else:
            seft.defend = False
        
        #move
        if key[pygame.K_a] and seft.defend == False:
            dx = -Speed
        if key[pygame.K_d] and seft.defend == False:
            dx = Speed
      
        #gravityyyy
        seft.vel_y += Gravity
        dy += seft.vel_y  

        #dont run from meee
        if seft.rect.left + dx < 0:
            dx = -seft.rect.left
        if seft.rect.right + dx > screen_width :
            dx = screen_width -seft.rect.right
        if seft.rect.bottom + dy > screen_height -110:
            seft.vel_y = 0
            seft.jump = False
            dy = screen_height -110 -seft.rect.bottom
        
        #face to face
        if target.rect.centerx > seft.rect.centerx:
            seft.flip = False
        else:
            seft.flip = True
        #update positon
        seft.rect.x += dx
        seft.rect.y += dy

    def move1(seft, screen_width, screen_height, surface, target, round_over):
        Speed = 10
        Gravity = 2
        dx = 0
        dy = 0
        delay = 100000
        #get in4 from keyboard
        key = pygame.key.get_pressed()

        #jump
        if key[pygame.K_UP] and seft.jump == False and seft.defend == False: 
            seft.vel_y = -30
            seft.jump = True
        
        #delay skill 
        if seft.shoot == False:
            seft.now = pygame.time.get_ticks()
        if seft.attacking == False and seft.defend == False:
            #attackkkkk
            if key[pygame.K_KP_1] or key[pygame.K_KP_2]:
                while delay > 1:
                    delay = delay-1
                if delay == 1:                   
                    if key[pygame.K_KP1]:
                        seft.attack_type = 1
                    elif key[pygame.K_KP2]:
                        seft.attack_type = 2
                    seft.attack(surface, target)
                    delay = 10
            elif key[pygame.K_KP3]:
                seft.now = pygame.time.get_ticks()
                seft.attack_type = 3
                if seft.now - seft.last >= seft.cooldown:
                    seft.shoot = True
                seft.attack(surface, target)
        #defend
        if key[pygame.K_DOWN]:
            seft.defend = True
            seft.attack(surface, target)
        else:
            seft.defend = False
        
        #move
        if key[pygame.K_LEFT] and seft.defend == False:
            dx = -Speed
        if key[pygame.K_RIGHT] and seft.defend == False:
            dx = Speed
      
        #gravityyyy
        seft.vel_y += Gravity
        dy += seft.vel_y  

        #dont run from meee
        if seft.rect.left + dx < 0:
            dx = -seft.rect.left
        if seft.rect.right + dx > screen_width :
            dx = screen_width -seft.rect.right
        if seft.rect.bottom + dy > screen_height -110:
            seft.vel_y = 0
            seft.jump = False
            dy = screen_height -110 -seft.rect.bottom
        
        #face to face
        if target.rect.centerx > seft.rect.centerx:
            seft.flip = False
        else:
            seft.flip = True
        #update positon
        seft.rect.x += dx
        seft.rect.y += dy

    def attack(self, surface, target):
        if self.attack_type == 1 and self.defend == False:
            attack_rect = pygame.Rect(self.rect.centerx - (1.5*self.rect.width * self.flip), self.rect.y, 1.5*self.rect.width, self.rect.height)
            pygame.draw.rect(surface, (0, 255, 0), attack_rect)   
        elif self.attack_type == 2 and self.defend == False:
            attack_rect = pygame.Rect(self.rect.centerx - (2.5*self.rect.width * self.flip), self.rect.y + 0.9*self.rect.height, 2.5*self.rect.width, 0.1*self.rect.height)
            pygame.draw.rect(surface, (0, 255, 0), attack_rect)   
        elif self.shoot == True and self.defend == False:
            attack_rect = pygame.Rect((self.rect.centerx + self.x0)- (1.5*self.rect.width * self.flip), self.rect.y, self.rect.width, 0.3*self.rect.height)
            if self.flip == True:
                self.x0 = self.x0 - self.attack_rect_x_speed
            else:
                self.x0 = self.x0 + self.attack_rect_x_speed
            if attack_rect.x > 1000 or attack_rect.x < 0 or attack_rect.colliderect(target.rect):
                self.x0 = 0
            pygame.draw.rect(surface, (0, 255, 0), attack_rect)  
            if attack_rect.x > 1000 or attack_rect.x < 0:
                self.shoot = False
                self.last = pygame.time.get_ticks()


        if self.defend == True:
            defend_aura = pygame.Rect(self.rect.centerx - 0.65*self.rect.width, self.rect.centery - 0.6*self.rect.height, 1.3*self.rect.width, 1.2*self.rect.height)
            pygame.draw.rect(surface, (222, 165, 164), defend_aura)
        if target.defend == True and self.attack_type > 0 and self.attack_type != 3 and self.defend == False:
            if attack_rect.colliderect(target.rect):
                target.health -= 0.05
        elif target.defend == False and self.attack_type > 0 and self.attack_type != 3 and self.defend == False:
            if attack_rect.colliderect(target.rect):
                target.health -= 0.5
        elif target.defend == True and self.shoot == True and self.attack_type == 3 and self.defend == False:
            if attack_rect.colliderect(target.rect):
                target.health -= 5
                self.shoot = False
                self.last = pygame.time.get_ticks()
        elif target.defend == False and self.shoot == True and self.attack_type == 3 and self.defend == False:
            if attack_rect.colliderect(target.rect):
                target.health -= 20
                self.shoot = False
                self.last = pygame.time.get_ticks()
        self.attacking = False
        

    def update(self):
    #check what action the player is performing
        if self.health <= 0:
            self.health = 0
            self.alive = False

    def draw(seft, surface):
        pygame.draw.rect(surface, (255, 0 ,0), seft.rect)
    def draw1(seft, surface):
        pygame.draw.rect(surface, (0, 0 ,255), seft.rect)

