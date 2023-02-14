init -25:
    define gui.use_side_image = False

    define gallery.enabled = False

    # If true, items in the gallery will be unlocked based on variables and instead of automatically after the player has seen them
    define gallery.variable_mode = False

    define gallery.items = []

    # If true, items in the gallery will only unlock once all items have been seen. Doesn't do anything if variable mode is on.
    define gallery.strict_multiple = False

    define music_room.enabled = False
    # If True, all tracks will be unlocked by default. If false, tracks will appear only once they are heard by the player.
    define music_room.unlocked = False
    define music_room.tracks = []