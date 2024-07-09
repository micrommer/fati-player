import flet as ft
# define a song class as our model
class Song(object):
 def __init__(self, song_name:str, artist_name: str, audio: str,img: int):
        super(Song, self).__init__()
        self.song_name = song_name
        self.artist_name = artist_name
        self.audio = audio
        self.img = img

    # define a proeprties for this class to access each attribute

 @property
 def name(self):
  return self.song_name
 @property
 def name(self):
  return self.artist_name
 @property
 def name(self):
  return self.audio
 @property
 def name(self):
  return self.img

# next , define a directory class where we store individual songs
class AudioDirectory(object):

# fill out as many songs as you want ...
  playlist : list = [
Song (
song_name="Street Cafe",
artist_name="Blonker",
audio="Blonker - Street Cafe.mp3",
img= "1.jpg",

),
Song (
song_name="Little Flower",
artist_name="Fausto Papetti",
audio="Fausto Papetti - Little Flower.mp3",
img= "2.png",

),
Song (
song_name="Sur Un Air Du Vivaldi",
artist_name="Paul Mauriat",
audio="Paul Mauriat - Sur Un Air Du Vivaldi.mp3",
img= "3.png",

),
Song (
song_name="Moment",
artist_name="Kenny G ",
audio="Kenny G - Moment.mp3",
img= "4.jpg",

),
Song (
song_name="Pop Corn",
artist_name="Eric Simon",
audio="Eric Simon - Pop Corn.mp3",
img= "5.jpg",

),
Song (
song_name="Hotel California",
artist_name="Anthony Ventura",
audio="Anthony Ventura - Hotel California.mp3",
img= "6.jpg",

),
Song (
song_name="Bi Tabi Instrumental",
artist_name="Shadmehr Aghili.mp3",
audio="Bi Tabi Instrumental Shadmehr Aghili.mp3",
img= "7.jpg",

),
Song (
song_name="Unknown",
artist_name="Earth",
audio="Earth.mp3",
img= "8.jpg",

),
Song (
song_name="Emmanuel",
artist_name="Fausto Papetti",
audio="Fausto Papetti - Emmanuel.mp3",
img= "9.jpg",

),
Song (
song_name="(Everything I Do) I do It For You",
artist_name="Francis Goya",
audio="Francis Goya - (Everything I Do) I do It For You.mp3",
img= "10.jpg",

),
Song (
song_name="Gipsy",
artist_name="Francis Goya",
audio="Francis Goya - Gipsy.mp3",
img= "11.jpg",

),
Song (
song_name="Silent Whisper",
artist_name="Kenny G",
audio="Kenny G - Silent Whisper.mp3",
img= "12.jpg",

),
Song (
song_name="Romeo and Juliet",
artist_name="Nino Rota",
audio="Nino Rota - Romeo and Juliet.mp3",
img= "13.jpg",

),
Song (
song_name="La Cumparsita",
artist_name="Richard Clayderman",
audio="Richard Clayderman - La Cumparsita.mp3",
img= "14.jpg",

),
Song (
song_name="Seasons",
artist_name="Richard Klayderman",
audio="Richard Klayderman - Seasons.mp3",
img= "15.jpg",

),
Song (
song_name="Unknown",
artist_name="Water",
audio="Water.mp3",
img= "16.jpg",

),

],

  # our first page/view is the playlist
class playlist(ft.View):
 def __init__(self, page: ft.Page) -> None:
  super(playlist,self).__init__(
  route="/playlist",
  horizontal_alignment="center"
  )

  self.page = page
  self.playlist = list[Song] = AudioDirectory.playlist

  self.controls = [
  ft.Row(
  [
    ft.Text("Play", size=21 , weight="bold"),
  ],
  alignment="center"
),
  ft.Divider(height=10, color="transparent"),
],


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route):
        page.views.clear()

        if page.route == "/playlist":
            playlist= playlist(page)
            page.views.append(playlist)


        page.update()

    page.on_route_change = router
    page.go("/playlist")
ft.app(target=main , assets_dir="assets")
