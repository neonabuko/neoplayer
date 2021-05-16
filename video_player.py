import pyglet
vid_path = './assets/Green Day - Walking Contradiction [ Official Music Video].mp4' # Name of the video
window = pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vid_path)

player.queue(MediaLoad)
player.play()

@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(0,0)


pyglet.app.run()
