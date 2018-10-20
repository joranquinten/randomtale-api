import pygame


class Mediaplayer():
    
    def __init__(self):
        # set up defaults
        self.file_loaded = None
        self.player_is_started = False
        self.player_is_paused = False
        self.player_is_stopped = False
        self.track_title = None

        # set up the mixer
        self.freq = 44100  # audio CD quality
        self.bitsize = -16  # unsigned 16 bit
        self.channels = 2  # 1 is mono, 2 is stereo
        self.buffer = 2048  # number of samples (experiment to get best sound)
        pygame.mixer.init(self.freq, self.bitsize, self.channels, self.buffer)

    def player_load(self, music_file, volume=0.8):
        pygame.mixer.music.set_volume(volume)
        try:
            pygame.mixer.music.load(music_file)
            self.file_loaded = music_file
            print("Music file {} loaded!".format(music_file))
        except pygame.error:
            print("File {} not found! ({})".format(
                music_file,
                pygame.get_error())
            )
            return

    def player_start(self):
        if not pygame.mixer.music.get_busy():
            self.player_is_paused = False
            self.player_is_started = True
            self.player_is_stopped = False
            pygame.mixer.music.play()
            return

    def player_stop(self):
        if pygame.mixer.music.get_busy():
            self.player_is_paused = False
            self.player_is_started = False
            self.player_is_stopped = True
            self.file_loaded = None
            pygame.mixer.music.stop()

    def player_pause(self):

        if self.player_is_paused:
            self.player_is_paused = False
            pygame.mixer.music.unpause()
            return

        if not self.player_is_paused:
            self.player_is_paused = True
            pygame.mixer.music.pause()
            return

    def status(self):
        return self

