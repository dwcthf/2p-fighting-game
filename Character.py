import pygame

class Thanh():
    def __init__(self, x ,y):
        self.flip = False
        self.rect = pygame.Rect((x,y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 1
        self.health = 100
        self.alive = True

    def move(seft, screen_width, screen_height, surface, target, round_over):
        Speed = 10
        Gravity = 2
        dx = 0
        dy = 0
        delay = 100000
        #get in4 from keyboard
        key = pygame.key.get_pressed()
        
        #jump
        if key[pygame.K_w] and seft.jump == False:
            seft.vel_y = -30
            seft.jump = True
        
        #delay skill 
        if seft.attacking == False:
            #attackkkkk
            if key[pygame.K_t] or key[pygame.K_y]:
                while delay > 1:
                    delay = delay-1
                if delay == 1:
                    seft.attack(surface, target)
                    if key[pygame.K_t]:
                        seft.attack_type = 1
                    else:
                        seft.attack_type = 2
                    delay = 10

        #move
        if key[pygame.K_a]:
            dx = -Speed
        if key[pygame.K_d]:
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
        if key[pygame.K_UP] and seft.jump == False:
            seft.vel_y = -30
            seft.jump = True
        
        #delay skill 
        if seft.attacking == False:
            #attackkkkk
            if key[pygame.K_KP_1] or key[pygame.K_KP_2]:
                while delay > 1:
                    delay = delay-1
                if delay == 1:
                    seft.attack(surface, target)
                    if key[pygame.K_KP_1]:
                        seft.attack_type = 1
                    else:
                        seft.attack_type = 2
                    delay = 10
        #move
        if key[pygame.K_LEFT]:
            dx = -Speed
        if key[pygame.K_RIGHT]:
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
        if self.attack_type == 1:
            attack_rect = pygame.Rect(self.rect.centerx - (1.5*self.rect.width * self.flip), self.rect.y, 1.5*self.rect.width, self.rect.height)
        elif self.attack_type == 2:
            attack_rect = pygame.Rect(self.rect.centerx - (2.5*self.rect.width * self.flip), self.rect.y + 0.9*self.rect.height, 2.5*self.rect.width, 0.1*self.rect.height)
        pygame.draw.rect(surface, (0, 255, 0), attack_rect)
        if attack_rect.colliderect(target.rect):
            target.health -= 0.5
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

