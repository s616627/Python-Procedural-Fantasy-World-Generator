import pygame
import sys

def display_map(world):

    X = 1200
    Y = 1000

    deviceInfo = pygame.display.Info()
    screen_width = deviceInfo.current_w
    screen_height = deviceInfo.current_h

    font_size = int((15 / 1920) * screen_width)

    my_font = pygame.font.SysFont('Merriweather', font_size)

    scrn = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    scrn.fill((237, 237, 208))

    pygame.display.set_caption('fantasy world generation')

    artic_imp = pygame.image.load('worldTiles\\artic.png').convert()
    artic_mountain_imp = pygame.image.load('worldTiles\\artic_mountains.png').convert()
    artic_sea_imp = pygame.image.load('worldTiles\\artic_sea.png').convert()
    desert_imp = pygame.image.load('worldTiles\\desert.png').convert()
    mountain_imp = pygame.image.load('worldTiles\\mountains.png').convert()
    forest_imp = pygame.image.load('worldTiles\\pines.png').convert()
    plains_imp = pygame.image.load('worldTiles\\plains.png').convert()
    rainforest_imp = pygame.image.load('worldTiles\\rainforest.png').convert()
    river_imp = pygame.image.load('worldTiles\\rivers.png').convert()
    savannah_imp = pygame.image.load('worldTiles\\savannah.png').convert()
    sea_imp = pygame.image.load('worldTiles\\sea.png').convert()
    taiga_imp = pygame.image.load('worldTiles\\taiga.png').convert()

    capitol_imp = pygame.image.load('worldTiles\\capitol.png').convert_alpha()
    artic_capitol_imp = pygame.image.load('worldTiles\\artic_capitol.png').convert_alpha()

    tile_width = int((4 / 1920) * screen_width)

    artic_small_imp = pygame.transform.scale(artic_imp, (tile_width, tile_width))
    artic_mountain_small_imp = pygame.transform.scale(artic_mountain_imp, (tile_width, tile_width))
    artic_sea_small_imp = pygame.transform.scale(artic_sea_imp, (tile_width, tile_width))
    desert_small_imp = pygame.transform.scale(desert_imp, (tile_width, tile_width))
    mountain_small_imp = pygame.transform.scale(mountain_imp, (tile_width, tile_width))
    forest_small_imp = pygame.transform.scale(forest_imp, (tile_width, tile_width))
    plains_small_imp = pygame.transform.scale(plains_imp, (tile_width, tile_width))
    rainforest_small_imp = pygame.transform.scale(rainforest_imp, (tile_width, tile_width))
    river_small_imp = pygame.transform.scale(river_imp, (tile_width, tile_width))
    savannah_small_imp = pygame.transform.scale(savannah_imp, (tile_width, tile_width))
    sea_small_imp = pygame.transform.scale(sea_imp, (tile_width, tile_width))
    taiga_small_imp = pygame.transform.scale(taiga_imp, (tile_width, tile_width))

    capitol_small_imp = pygame.transform.scale(capitol_imp, (tile_width, tile_width)).convert_alpha()
    artic_capitol_small_imp = pygame.transform.scale(artic_capitol_imp, (tile_width, tile_width)).convert_alpha()

    border = int((screen_width / 96))

    for y in range(world.height):
        for x in range(world.width):
            if world.biome_map[y][x] == "Artic":
                scrn.blit(artic_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Artic Sea":
                scrn.blit(artic_sea_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Artic Mountains":
                scrn.blit(artic_mountain_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Desert":
                scrn.blit(desert_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Mountains":
                scrn.blit(mountain_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Forest":
                scrn.blit(forest_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Plains":
                scrn.blit(plains_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Rainforest":
                scrn.blit(rainforest_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "River":
                scrn.blit(river_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Savannah":
                scrn.blit(savannah_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Sea":
                scrn.blit(sea_small_imp, (x * tile_width + border, y * tile_width + border))
            elif world.biome_map[y][x] == "Taiga":
                scrn.blit(taiga_small_imp, (x * tile_width + border, y * tile_width + border))
            else:
                scrn.blit(artic_small_imp, (x * tile_width + border, y * tile_width + border))

            if world.location_map[y][x].name != "---":
                if world.biome_map[y][x] != "Artic Sea" and world.biome_map[y][x] != "Sea":
                    if world.biome_map[y][x] == "Artic Mountains" or world.biome_map[y][x] == "Artic":
                        scrn.blit(artic_capitol_small_imp, (x * tile_width + border, y * tile_width + border))
                    else:
                        scrn.blit(capitol_small_imp, (x * tile_width + border, y * tile_width + border))

    directions = my_font.render("Press Any Key to Quit", True, (0, 0, 0))
    scrn.blit(directions, ((world.width) * tile_width + border + 500, border))

    for x in range(len(world.city_names_list) - 1):
        city_name = my_font.render(f"{world.city_names_list[x]}: Capital of the {world.fantasy_races[x].plural_name}",
                                   True, (0, 0, 0))
        scrn.blit(city_name, ((world.width) * tile_width + border + 10, border + x * font_size))

    for x in range(len(world.gods) - 1):
        god_name = my_font.render(
            f"{world.gods[x].name}: Lord of {world.gods[x].god_spheres[0][0]}, {world.gods[x].god_spheres[1][0]} and {world.gods[x].god_spheres[2][0]}",
            True, (0, 0, 0))
        scrn.blit(god_name, (
        (world.width) * tile_width + border + 10, (border + x * font_size) + (font_size) * len(world.city_names_list)))

    pygame.display.flip()

    status = True

    print(f"Screen Width: {screen_width} pixels")
    print(f"Screen Height: {screen_height} pixels")

    while (status):

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                status = False

            if i.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
                status = False


        pygame.display.flip()


