from mutagen.oggvorbis import OggVorbis

file_ = OggVorbis("./track.ogg")

artist = file_.get("artist", [""])[0]
print(artist)
title = file_.get("title", [""])[0]
print(title)
