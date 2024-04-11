import pygame

def get_monitor_refresh_rate():
    pygame.init()
    info = pygame.display.Info()
    refresh_rate = info.current_w
    pygame.quit()
    return refresh_rate

if __name__ == "__main__":
    refresh_rate = get_monitor_refresh_rate()
    print("Monitor refresh rate:", refresh_rate, "Hz")
