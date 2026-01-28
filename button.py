import pygame,os

class Button:
    def __init__(self, screen, x, y, img_path, size, bgColor, hover=True):
        self.screen = screen
        self.hover = hover
        self.assets_dir = os.path.join(os.path.dirname(__file__), "assets/images")
        self.img = pygame.image.load(os.path.join(self.assets_dir, img_path)).convert_alpha()
        orig_w, orig_h = self.img.get_size()
        scale = size/orig_w
        new_size = (size ,int(orig_h*scale))
        self.img = pygame.transform.smoothscale(self.img, new_size)
        self.img_rect = self.img.get_rect()
        self.bgColor = pygame.color.Color(bgColor)
        self.bgColor.a = 0
        self.img_bg = self.bgColor
        self.img_rect.centerx = x
        self.img_rect.centery = y

    
    def draw(self):
        self.checkHover()
        surf = pygame.Surface((self.img_rect.w, self.img_rect.h),pygame.SRCALPHA)
        pygame.draw.rect(surf,self.img_bg,surf.get_rect(),border_radius=12)
        self.screen.blit(surf, self.img_rect.topleft)
        self.screen.blit(self.img, self.img_rect.topleft)

        

    def checkHover(self):
        if self.hover:
            if self.img_rect.collidepoint(pygame.mouse.get_pos()):
                self.bgColor.a = 100
                pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND))
                return True
            else:
                self.bgColor.a = 0
                pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW))
                return False
    
