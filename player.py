import pygame


def player_load(music_file, volume=0.8):

    print("player_load")
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pygame.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pygame.mixer.music.set_volume(volume)
    try:
        pygame.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pygame.error:
        print("File {} not found! ({})".format(music_file, pygame.get_error()))
        return


def player_start():
    print("player_start")

    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


def player_stop():
    print("player_stop")
    if pygame.mixer.music.get_busy():
        pygame.mixer.stop()
