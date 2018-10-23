import pygame


class MediaPlayer:

    def __init__(self):
        # set up defaults
        self.file_loaded = None
        self.track_title = None
        self.player_is_started, self.player_is_paused, self.player_is_stopped = False

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
            print(f"Music file {music_file} loaded!")
        except pygame.error:
            print(f"File {music_file} not found! ({pygame.get_error()})")
            return

    def player_start(self):
        if not pygame.mixer.music.get_busy():
            self.player_is_started = True
            self.player_is_paused, self.player_is_stopped = False
            pygame.mixer.music.play()

    def player_stop(self):
        if pygame.mixer.music.get_busy():
            self.player_is_paused, self.player_is_started = False
            self.player_is_stopped = True
            self.file_loaded = None
            pygame.mixer.music.stop()

    def player_pause(self):
        if self.player_is_paused:
            self.player_is_paused = False
            pygame.mixer.music.unpause()
        else:
            self.player_is_paused = True
            pygame.mixer.music.pause()

    def status(self):
        return self
